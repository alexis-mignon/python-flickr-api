"""
Shared test utilities for Flickr API tests.
"""
import json
import os
import xml.etree.ElementTree as ET


def xml_to_flickr_json(xml_string):
    """Convert Flickr XML response to JSON format."""
    xml_string = xml_string.strip()
    root = ET.fromstring(xml_string)

    def convert_value(value):
        """Convert 0/1 strings to integers for boolean fields."""
        # Only convert 0 and 1 (boolean flags), keep other numbers as strings
        # (like photo IDs which should remain strings)
        if value in ("0", "1"):
            return int(value)
        return value

    def element_to_dict(elem):
        result = {}
        for key, value in elem.attrib.items():
            result[key] = convert_value(value)
        if elem.text and elem.text.strip():
            result["_content"] = elem.text.strip()
        children_by_tag = {}
        for child in elem:
            tag = child.tag
            if tag not in children_by_tag:
                children_by_tag[tag] = []
            children_by_tag[tag].append(element_to_dict(child))
        for tag, children in children_by_tag.items():
            if len(children) == 1:
                result[tag] = children[0]
            else:
                result[tag] = children
        return result

    root_dict = element_to_dict(root)
    if root.tag == "rsp":
        return root_dict
    else:
        return {root.tag: root_dict}


def load_api_doc(method_name):
    """Load API documentation JSON file for a method."""
    api_docs_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "api-docs"
    )
    filepath = os.path.join(api_docs_dir, f"{method_name}.json")
    with open(filepath, "r") as f:
        return json.load(f)
