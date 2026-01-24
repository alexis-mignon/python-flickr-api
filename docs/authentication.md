# Flickr API Keys and Authentication

This guide covers obtaining API credentials and setting up authentication for the python-flickr-api library.

## Requirements

To use the Flickr API, you need:

1. A Flickr account
2. An API key
3. An API secret

You can obtain API credentials at: https://www.flickr.com/services/apps/create/

## Setting API Keys

### Method 1: Direct Assignment (Recommended)

```python
import flickr_api

flickr_api.set_keys(api_key="your_api_key", api_secret="your_api_secret")
```

### Method 2: Configuration File

Create a file named `flickr_keys.py` in your project or Python path:

```python
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
```

The library will automatically detect and use these values.

## Authentication Levels

### Read-Only Access (No Authentication)

With just API keys, you can access public data:

```python
flickr_api.set_keys(api_key="...", api_secret="...")

# These work without authentication
user = flickr_api.Person.findByUserName("username")
photos = user.getPublicPhotos()
results = flickr_api.Photo.search(tags="nature")
```

### Write Access (OAuth Required)

For operations that modify data (upload, delete, add comments, etc.), you need OAuth authentication.

## OAuth Authentication Flow

The library uses OAuth 1.0a for user authentication. Here's the complete flow:

### Step 1: Create an AuthHandler

```python
import flickr_api

flickr_api.set_keys(api_key="your_api_key", api_secret="your_api_secret")

# Create auth handler
auth = flickr_api.auth.AuthHandler()
```

### Step 2: Get Authorization URL

```python
# Get URL for user to authorize your app
# Permission levels: "read", "write", or "delete"
url = auth.get_authorization_url("write")
print(f"Please visit: {url}")
```

### Step 3: User Authorizes Your App

Direct the user to the URL. After they authorize, Flickr will:
- Display a verifier code (for desktop apps), or
- Redirect to your callback URL with the verifier (for web apps)

### Step 4: Set the Verifier

```python
# Get verifier from user or callback
verifier = input("Enter the verifier code: ")
auth.set_verifier(verifier)
```

### Step 5: Set the Auth Handler

```python
flickr_api.set_auth_handler(auth)
```

### Complete Example

```python
import flickr_api

# Set API keys
flickr_api.set_keys(api_key="your_api_key", api_secret="your_api_secret")

# Create auth handler and get authorization URL
auth = flickr_api.auth.AuthHandler()
url = auth.get_authorization_url("write")

print(f"Please visit this URL and authorize the app:\n{url}")
verifier = input("\nEnter the verifier code from Flickr: ")

# Complete authentication
auth.set_verifier(verifier)
flickr_api.set_auth_handler(auth)

# Now you can perform write operations
user = flickr_api.test.login()
print(f"Authenticated as: {user.username}")
```

## Web Application Callback

For web applications, specify a callback URL to receive the verifier automatically:

```python
auth = flickr_api.auth.AuthHandler(callback="https://yourapp.com/flickr/callback")
url = auth.get_authorization_url("write")

# After user authorizes, Flickr redirects to:
# https://yourapp.com/flickr/callback?oauth_token=...&oauth_verifier=...

# In your callback handler:
verifier = request.args.get("oauth_verifier")
auth.set_verifier(verifier)
```

## Saving and Loading Credentials

### Save to File

```python
# Save authentication (without API keys)
auth.save("flickr_token.txt")

# Save authentication (with API keys included)
auth.save("flickr_credentials.txt", include_api_keys=True)
```

### Load from File

```python
# Load and set auth handler
flickr_api.set_auth_handler("flickr_token.txt")

# Or load with API keys
flickr_api.set_auth_handler("flickr_credentials.txt", set_api_keys=True)
```

### Save/Load as Dictionary

```python
# Save to dict (useful for database storage)
credentials = auth.todict(include_api_keys=True)

# Load from dict
auth = flickr_api.auth.AuthHandler.fromdict(credentials)
flickr_api.set_auth_handler(auth)
```

## Creating AuthHandler from Existing Tokens

If you already have access tokens:

```python
# From token strings
auth = flickr_api.auth.AuthHandler.create(
    access_key="your_access_token_key",
    access_secret="your_access_token_secret"
)
flickr_api.set_auth_handler(auth)

# Or via constructor
auth = flickr_api.auth.AuthHandler(
    access_token_key="your_access_token_key",
    access_token_secret="your_access_token_secret"
)
```

## Getting the Authenticated User

After authentication, get the current user:

```python
# Using test.login()
user = flickr_api.test.login()
print(f"Logged in as: {user.username}")

# Or using Person.getFromToken()
user = flickr_api.Person.getFromToken()
```

## Token File Format

The token file format (when saved without API keys):

```
ACCESS_TOKEN_KEY
ACCESS_TOKEN_SECRET
```

With API keys included:

```
oauth_token=ACCESS_TOKEN_KEY
oauth_token_secret=ACCESS_TOKEN_SECRET
api_key=YOUR_API_KEY
api_secret=YOUR_API_SECRET
```

## Troubleshooting

### "Invalid API Key" Error

- Verify your API key and secret are correct
- Ensure you've called `set_keys()` before any API calls

### "Invalid OAuth Token" Error

- The access token may have expired or been revoked
- Re-authenticate to get a new token

### "Insufficient Permissions" Error

- Request the appropriate permission level ("read", "write", or "delete")
- "delete" permission includes all write permissions
- "write" permission includes read permissions
