print("=================================")
print("  PC Troubleshooting Assistant")
print("=================================")

print("\nWhat problem are you experiencing?")
print("1. Computer won't turn on")
print("2. No interent")
print("3. Computer is running slowly")
print("4. Computer is overheating")

choice=input("\nEnter your choice (1-4): ")

if choice == "1":
    print("\nTroubleshooting: Power Problem")
    print("1. Check that the power cable is connected.")
    print("2. Try a different power outlet.")
    print("3. Check the power supply connections.")

elif choice == "2":
    print("\nTroubleshooting: Internet Problem")
    print("1. Check that Wi-Fi is enabled.")
    print("2. Restart your router.")
    print("3. Restart your computer")

elif choice == "3":
    print("\nTroubleshooting: Performance Problem")
    print("1. Check Task Manager for program using high resources.")
    print("2. Close unnecessary programs.")
    print("3. Check availible storage space.")

elif choice == "4":
    print("\nTroubleshooting: Overheating Problem")
    print("1. Check that the fans are working.")
    print("2. Clean dust from the computer.")
    print("3. Make sure the computer has proper airflow.")

else:
    print("\nInvalid choice. Please select a number from 1-4.")