troubleshooting_data = {
    "power": {
        "title": "Power Troubleshooting",
        "steps": [
            "Check that the computer is plugged into a working outlet.",
            "Make sure the power cable is securely connected.",
            "Try a different power cable if available.",
            "Check the power supply and internal power connections."
        ]
    },

    "internet": {
        "title": "Internet Troubleshooting",
        "steps": [
            "Make sure Wi-Fi is enabled.",
            "Restart the router.",
            "Check if other devices can connect to the internet.",
            "Restart the computer.",
            "Forget and reconnect to the Wi-Fi network."
        ]
    },

    "performance": {
        "title": "Performance Troubleshooting",
        "steps": [
            "Check how much storage space is available.",
            "Close unnecessary programs.",
            "Open Task Manager and check CPU, Memory, and GPU usage.",
            "Look for unnecessary background processes."
        ]
    },

    "overheating": {
        "title": "Overheating Troubleshooting",
        "steps": [
            "Make sure the computer fans are spinning properly.",
            "Check for dust buildup around fans and vents.",
            "Check CPU temperatures.",
            "Make sure the computer has proper airflow.",
            "Check that thermal paste is applied correctly."
        ]
    }
}


def show_troubleshooting(category):
    problem = troubleshooting_data[category]

    print(f"\n--- {problem['title']} ---")

    print("\nRecommended steps:")

    for number, step in enumerate(problem["steps"], start=1):
        print(f"{number}. {step}")

def main():
    while True:
        print("\n=================================")
        print("  PC Troubleshooting Assistant") 
        print("=================================")

        print("\nWhat problem are you experiencing?")
        print("1. Computer won't turn on")
        print("2. No internet")
        print("3. Computer is running slowly")
        print("4. Computer is overheating")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        categories = {
            "1": "power",
            "2": "internet",
            "3": "performance",
            "4": "overheating",

        }

        if choice in categories:
            show_troubleshooting(categories[choice])

            input("\nPress Enter to return to the main menu...")

        elif choice == "5":
            print("\nThank you for using Mekhi's PC Troubleshooting Assistant. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1-5.")

main()