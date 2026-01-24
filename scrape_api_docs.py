#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "requests",
#     "beautifulsoup4",
# ]
# ///
"""
Scrape Flickr API documentation and store method details locally.

This script fetches all API method documentation from the Flickr website
and saves them as JSON files in the api-docs/ directory for later use
in creating test cases.
"""

import json
import os
import re
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.flickr.com/services/api/"
OUTPUT_DIR = "api-docs"
DELAY_BETWEEN_REQUESTS = 0.5  # Be polite to the server


def get_soup(url, session):
    """Fetch a URL and return a BeautifulSoup object."""
    response = session.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def get_all_method_links(session):
    """Get all API method links from the main API page."""
    soup = get_soup(BASE_URL, session)
    methods = []

    # Find all links that match the pattern flickr.*.html
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if re.match(r".*flickr\.[a-z]+\.[a-zA-Z.]+\.html$", href):
            method_name = link.get_text(strip=True)
            if method_name.startswith("flickr."):
                full_url = urljoin(BASE_URL, href)
                methods.append({"name": method_name, "url": full_url})

    return methods


def sanitize_xml_response(xml_text):
    """
    Fix malformed XML in API response examples.

    Flickr's documentation sometimes contains XML with unescaped quotes
    inside attribute values (e.g., title=""quoted text""). This function
    detects and escapes these nested quotes.
    """
    if not xml_text:
        return xml_text

    # Pattern to find attribute values with nested unescaped quotes
    # Matches: attr="..."..." where there are quotes inside the value
    # We look for patterns like: ="text""more text""
    # which should become: ="text&quot;more text&quot;"
    def fix_attr_value(match):
        attr_name = match.group(1)
        full_value = match.group(2)

        # Check if there are unescaped quotes inside (not at boundaries)
        # A valid attribute value shouldn't have " inside unless escaped
        if '""' in full_value:
            # Pattern like ""text"" - the outer quotes are the attr delimiters
            # and inner quotes should be escaped
            # Replace "" at start/end with &quot;
            fixed = full_value
            # Handle opening quote-quote: ="" followed by quote
            if fixed.startswith('"'):
                fixed = '&quot;' + fixed[1:]
            # Handle closing quote-quote: quote followed by ""
            if fixed.endswith('"'):
                fixed = fixed[:-1] + '&quot;'
            return f'{attr_name}="{fixed}"'
        return match.group(0)

    # Match attribute="value" patterns - capture the whole attribute
    # This regex finds attr="..." and we process each match
    result = re.sub(
        r'(\w+)="([^"]*""[^"]*)"',
        fix_attr_value,
        xml_text
    )

    return result


def parse_method_page(soup, method_name):
    """Parse a method documentation page and extract structured data."""
    data = {
        "name": method_name,
        "description": "",
        "authentication": "",
        "arguments": [],
        "response": "",
        "errors": [],
    }

    # Content is in div.InfoCase (old table-based layout)
    info_case = soup.find("div", class_="InfoCase")
    if not info_case:
        return data

    # Get description - text after h1 but before first h3
    h1 = info_case.find("h1")
    if h1:
        description_parts = []
        for sibling in h1.next_siblings:
            if sibling.name == "h3":
                break
            if hasattr(sibling, "get_text"):
                text = sibling.get_text(strip=True)
                if text:
                    description_parts.append(text)
            elif isinstance(sibling, str) and sibling.strip():
                description_parts.append(sibling.strip())
        data["description"] = " ".join(description_parts)

    # Find all h3 sections
    sections = {}
    current_section = None
    current_content = []

    for elem in info_case.children:
        if hasattr(elem, "name") and elem.name == "h3":
            if current_section:
                sections[current_section] = current_content
            current_section = elem.get_text(strip=True).lower()
            current_content = []
        elif current_section:
            current_content.append(elem)

    if current_section:
        sections[current_section] = current_content

    # Parse authentication
    if "authentication" in sections:
        auth_text = []
        for elem in sections["authentication"]:
            if hasattr(elem, "get_text"):
                auth_text.append(elem.get_text(strip=True))
            elif isinstance(elem, str) and elem.strip():
                auth_text.append(elem.strip())
        data["authentication"] = " ".join(auth_text)

    # Parse arguments - they're in a DL (definition list)
    if "arguments" in sections:
        data["arguments"] = parse_arguments_dl(sections["arguments"])

    # Parse example response - preserve XML formatting
    if "example response" in sections:
        for elem in sections["example response"]:
            # Skip NavigableString elements (whitespace, etc.)
            if not hasattr(elem, "name") or elem.name is None:
                continue
            # Look for pre or code tags that contain the XML
            response_text = None
            if elem.name == "pre":
                response_text = elem.get_text()
            elif elem.name == "code":
                response_text = elem.get_text()
            else:
                # Check if pre/code is nested inside this element
                pre = elem.find("pre")
                if pre:
                    response_text = pre.get_text()
                else:
                    code = elem.find("code")
                    if code:
                        response_text = code.get_text()

            if response_text:
                # Sanitize any malformed XML (e.g., unescaped quotes)
                data["response"] = sanitize_xml_response(response_text)
                break

    # Parse error codes
    if "error codes" in sections:
        data["errors"] = parse_errors(sections["error codes"])

    return data


def parse_arguments_dl(content):
    """Parse arguments from DL (definition list) elements."""
    arguments = []

    for elem in content:
        if not hasattr(elem, "name") or elem.name != "dl":
            continue

        # DL contains DT (term) and DD (definition) pairs
        current_arg = None
        for child in elem.children:
            if not hasattr(child, "name"):
                continue

            if child.name == "dt":
                # New argument - DT contains name and (Required)/(Optional)
                if current_arg:
                    arguments.append(current_arg)

                text = child.get_text(strip=True)
                # Parse "arg_name (Required)" or "arg_name (Optional)"
                match = re.match(r"([a-z_]+)\s*\((Required|Optional)\)", text)
                if match:
                    current_arg = {
                        "name": match.group(1),
                        "required": match.group(2) == "Required",
                        "description": "",
                    }
                else:
                    # Fallback: just use the text as name
                    current_arg = {
                        "name": text.split()[0] if text else "",
                        "required": "Required" in text,
                        "description": "",
                    }

            elif child.name == "dd" and current_arg:
                # Description for the current argument
                current_arg["description"] = child.get_text(strip=True)

        if current_arg:
            arguments.append(current_arg)

    return arguments


def parse_errors(content):
    """Parse the error codes section into a structured list."""
    errors = []
    text_parts = []

    for elem in content:
        if hasattr(elem, "get_text"):
            text_parts.append(elem.get_text(strip=True))
        elif isinstance(elem, str) and elem.strip():
            text_parts.append(elem.strip())

    full_text = " ".join(text_parts)

    # Errors are formatted like "1: Too many tags in ALL query Description here"
    # Split on the pattern "number: error title"
    error_pattern = re.compile(r"(\d+):\s*([^\d]+?)(?=\d+:|$)")
    matches = error_pattern.findall(full_text)

    for code, text in matches:
        # The text contains both the title and description
        # Try to split on sentence boundaries
        parts = text.strip().split(". ", 1)
        if len(parts) == 2:
            title = parts[0].strip()
            description = parts[1].strip()
        else:
            # If no clear split, use the first line as title
            lines = text.strip().split("\n", 1)
            title = lines[0].strip()
            description = lines[1].strip() if len(lines) > 1 else ""

        errors.append(
            {"code": int(code), "title": title, "description": description}
        )

    return errors


def scrape_method(method_info, session):
    """Scrape a single method's documentation."""
    print(f"  Fetching {method_info['name']}...")
    soup = get_soup(method_info["url"], session)
    return parse_method_page(soup, method_info["name"])


def save_method(method_data, output_dir):
    """Save method data to a JSON file."""
    # Create filename from method name: flickr.photos.search -> flickr.photos.search.json
    filename = f"{method_data['name']}.json"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(method_data, f, indent=2, ensure_ascii=False)

    return filepath


def main():
    """Main entry point."""
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Create a session for connection reuse
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "FlickrAPIScraper/1.0 (python-flickr-api test helper)"
        }
    )

    print("Fetching API method list...")
    methods = get_all_method_links(session)
    print(f"Found {len(methods)} API methods")

    # Also save an index file
    index = {"methods": [m["name"] for m in methods], "count": len(methods)}

    with open(os.path.join(OUTPUT_DIR, "_index.json"), "w") as f:
        json.dump(index, f, indent=2)

    print(f"\nScraping method documentation to {OUTPUT_DIR}/")
    for i, method in enumerate(methods, 1):
        try:
            data = scrape_method(method, session)
            filepath = save_method(data, OUTPUT_DIR)
            print(f"  [{i}/{len(methods)}] Saved {filepath}")
        except Exception as e:
            print(f"  [{i}/{len(methods)}] ERROR scraping {method['name']}: {e}")

        # Be polite
        time.sleep(DELAY_BETWEEN_REQUESTS)

    print(f"\nDone! Scraped {len(methods)} methods to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
