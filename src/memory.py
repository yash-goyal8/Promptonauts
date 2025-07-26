# src/memory.py

import json
import os

# Get the path to the root directory (one level above src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE_FILE = os.path.join(BASE_DIR, "user_profile.json")

def save_user_profile(profile):
    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f, indent=4)
    print("💾 Profile saved.")

def load_user_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)
    return None

def get_contact_email(contact_name):
    profile = load_user_profile()
    if not profile:
        return None
    contacts = profile.get("emergency_contacts", {})
    contact = contacts.get(contact_name.capitalize())
    if contact and "email" in contact:
        return contact["email"]
    return None
