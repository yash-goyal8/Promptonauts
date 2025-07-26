import json
from datetime import datetime, timedelta
import time
import schedule

def parse_time(time_str):
    try:
        return datetime.strptime(time_str, "%I %p")
    except ValueError:
        return datetime.strptime(time_str, "%I:%M %p")

def schedule_notifications(profile):
    routines = profile.get("routines", {})
    notifications = []

    for meal in ["breakfast", "lunch", "dinner"]:
        if meal in routines:
            notif_time = parse_time(routines[meal]) - timedelta(minutes=30)
            notifications.append({
                "type": "meal",
                "name": meal,
                "time": notif_time.strftime("%H:%M")
            })

    meds = routines.get("medications", {})
    for med, when in meds.items():
        if when == "before dinner" and "dinner" in routines:
            dinner_time = parse_time(routines["dinner"]) - timedelta(minutes=30)
            notifications.append({
                "type": "medication",
                "name": med,
                "time": dinner_time.strftime("%H:%M")
            })
    return notifications

def send_notification(notification):
    print(f"Reminder: {notification['type'].capitalize()} - {notification['name']} at {notification['time']}")

def job_factory(notification):
    return lambda: send_notification(notification)

def start_notification_scheduler(profile):
    if profile.get("preferences", {}).get("wants_reminders", False):
        notifications = schedule_notifications(profile)
        for note in notifications:
            hour, minute = map(int, note["time"].split(":"))
            schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(job_factory(note))
        while True:
            schedule.run_pending()
            time.sleep(30)

if __name__ == "__main__":
    # Load the user profile from the correct path
    with open("./src/user_profile.json", "r") as f:
        profile = json.load(f)
    print("Starting notification scheduler...")
    start_notification_scheduler(profile)