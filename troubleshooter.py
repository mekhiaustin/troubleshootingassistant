def main():
    print("=================================")
    print("  PC Troubleshooting Assistant")
    print("=================================")

    print("\nWhat problem are you experiencing?")
    print("1. Computer won't turn on")
    print("2. No interent")
    print("3. Computer is running slowly")
    print("4. Computer is overheating")

    while True:
        choice=input("\nEnter your choice (1-4): ")

        if choice == "1":
            power_problem()
            break

        elif choice == "2":
            internet_problem()
            break

        elif choice == "3":
            performance_problem()
            break

        elif choice == "4":
            overheating_problem()
            break

        else:
            print("\nInvalid choice. Please select a number from 1-4.")

def power_problem():
    print("\n---Power Troubleshooting ---")

    power_light = input("Does the computer show any power lights? (yes/no): ").lower()

    if power_light == "no":
        outlet = input("Have you tried a different power outlet? (yes/no): ").lower()

        if outlet == "no":
            print("\nRecommendation: Try a different power outlet.")
        else:
            cable = input("Is the power cable securely connected? (yes/no): ").lower()

            if cable == "no":
                print("\nRecommendation: Test a different power cable.")
            else:
                print("\nPossible causes:")
                print("1. Faulty power supply")
                print("2. Motherboard issue")
                print("3. Internal power connection issue")

    else:
        print("The computer is receiving power.")
        print("Check the display, HDMI/DP cables, and graphics card connections.")

def internet_problem():
    print("\n---Internet Troublessshooting ---")

    wifi = input("Is Wi-Fi enabled? (yes/no): ").lower()

    if wifi == "no":
        print("\nRecommendation: Enable Wi-Fi and try connecting again.")
    else:
        router = input("Have you restarted your router? (yes/no): ").lower()

        if router == "no":
            print('\nRecommendation: Restart your router and try connecting again.')
        else:
            print("\nRecommendation")
            print("- Check other devices to see if they can connect to the internet.")
            print("- Restart your computer and try connecting again.")
            print("- Forget and reconnect to the Wi-Fi network.")

def performance_problem():
    print("\n---Performance Troubleshooting ---")

    storage = input("Is your storage nearly full? (yes/no): ").lower()

    if storage == "yes":
        print("\nRecommendation: Free up some space by deleting unnecessary files.")
    else:
        programs = input("Are there alot of programs running in the background? (yes/no):").lower() 

        if programs == "yes":
            print("\nRecommendation: Close unnecessary programs.")
        else:
            print("\nRecommendation:")
            print("- Check Task Manager")
            print("- Look for high usage of CPU, Memory, or GPU by any program.")
            print("- Check for unnecessary background processes.")

def overheating_problem():
    print("\n--- Overheating Troubleshooting ---")

    fans = input ("Are the computer fans spinning properly? (yes/no): ").lower()

    if fans == "no":
        print("\nPossible fan failure.")
        print("Recommendation: Inspect the fans and replace if necessary.")
    else:
        dust = input("Is there significant dust buildup inside the computer? (yes/no): ").lower()

        if dust == "yes":
            print("\nRecommendation: Clean the dust around the fans and vents.")
        else:
            print("\nRecommendation")
            print("- Check CPU temperatures in BIOS or with monitoring software.")
            print("- Check airflow")
            print("- Ensure thermal paste is applied correctly on the CPU.")

main()