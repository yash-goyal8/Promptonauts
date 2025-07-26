import threading
from tools import send_custom_email
from onboarding import collect_user_info
from memory import load_user_profile, save_user_profile, get_contact_email
from executor import generate_response

# Import the notification scheduler
from notify_user import start_notification_scheduler

def main():
    # Step 1: Load profile from root directory
    user_profile = load_user_profile()

    # Step 2: If no profile found, onboard new user
    if user_profile is None:
        print("No user profile found. Starting onboarding...\n")
        user_profile = collect_user_info()
        save_user_profile(user_profile)
        print(f"\nOnboarding complete. Welcome, {user_profile['name']}!\n")
    else:
        print(f"Welcome back, {user_profile['name']}!")


    # Step 3: Start conversation loop
    waiting_for_email_message = None  # state flag

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        if waiting_for_email_message:
            contact_name, email = waiting_for_email_message
            send_custom_email(email, f"A message from {user_profile['name']}", user_input)
            print(f"Email sent to {contact_name}.")
            waiting_for_email_message = None
            continue

        if user_input.lower().startswith("email "):
            parts = user_input.split()
            if len(parts) >= 2:
                contact_name = parts[1].capitalize()
                email = get_contact_email(contact_name)

                if not email:
                    print(f"I don’t have {contact_name}’s email.")
                    continue

                message = user_input.partition(contact_name)[2].strip()

                if not message:
                    print(f"What would you like me to tell {contact_name}?")
                    waiting_for_email_message = (contact_name, email)
                else:
                    send_custom_email(email, f"A message from {user_profile['name']}", message)
                    print(f"Email sent to {contact_name}.")
                continue

        response = generate_response(user_input)
        print("Assistant:", response)

if __name__ == "__main__":
    main()