import flickr_api
from flickr_api.objects import Contact

flickr_api.set_keys(
    api_key="cab11b0586f1d59792c54308de486f72", api_secret="3fde806ba11d3f2f"
)

# 1. Testing the "Static" Call (What this change enables/fixes)
try:
    # This usually fails if 'self' is present but no instance is provided
    args, formatter = Contact.getList(page=1)
    print("✅ Static call successful: Contact.getList() works without an instance.")
except TypeError as e:
    print(f"❌ Static call failed: {e}")

# 2. Testing the "Instance" Call (Checking for breaking changes)
try:
    c = Contact()
    args, formatter = c.getList(page=1)
    print("✅ Instance call successful: my_contact.getList() still works.")
except TypeError as e:
    print(f"⚠️ Instance call failed: {e}")
    print("   Note: This confirms the change is 'Breaking' for instance-based calls.")
