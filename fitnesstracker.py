import datetime

# A dictionary to store activities
activity_log = []

def log_activity():
    print("\n--- Log Fitness Activity ---")
    activity = input("Enter activity (e.g., Running, Cycling): ").strip()
    duration = input("Enter duration (in minutes): ").strip()
    calories = input("Enter calories burned: ").strip()
    
    # Create an entry with current date and time
    activity_entry = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "activity": activity,
        "duration": duration,
        "calories": calories
    }
    activity_log.append(activity_entry)
    print("Activity logged successfully!")

def view_log():
    print("\n--- Activity Log ---")
    if not activity_log:
        print("No activities logged yet.")
    else:
        for i, entry in enumerate(activity_log, 1):
            print(f"\nActivity {i}:")
            print(f"Date: {entry['date']}")
            print(f"Activity: {entry['activity']}")
            print(f"Duration: {entry['duration']} minutes")
            print(f"Calories Burned: {entry['calories']} kcal")

def main():
    while True:
        print("\n=== Fitness Tracker ===")
        print("1. Log Activity")
        print("2. View Activity Log")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            log_activity()
        elif choice == "2":
            view_log()
        elif choice == "3":
            print("Exiting Fitness Tracker. Stay healthy!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
