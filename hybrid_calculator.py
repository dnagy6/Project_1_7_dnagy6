"""
Program name: Hybrid Training & pace Calculator
Author: Dakota Nagy
Date: June 8, 2026
Purpose: A terminal-based utility to calculate barbell percentages
        for strength training and endurance pacing splits.
Chapters: 1-7 - Python Basics, Control Flow, Functions, Data Structures, OOP, Modules, File I/O
"""

# 'running' flag to control the main loop.
# This allows the user to perform multiple calculations without restarting the program.

running = True

# Creating a simplee dictionary to store the users PRs.
user_maxes = {}

while running:
    print("\nWelcome to the Hybrid Training & Pace Calculator!")
    print("Please select an option:")
    print("1. Lifting Calculator (Barbell Percentage)")
    print("2. Pace Split Calculator (Running)")
    print("3. Exit")
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == '1':
        # Barbell Percentage Calculator
        try:
            lift_name = input("Enter the name of the lift (e.g., Squat, Bench Press, Deadlift): ")
            max_weight = float(input("Enter your one-rep max weight (in pounds): "))
            
            # Saving the lift and max weight to the user_maxes dictionary
            user_maxes[lift_name] = max_weight

            # Dictionary with Tuples to store percentages AND rep ranges
            training_block = {
                "Week 1 (65%)": (0.65, "8-10 reps"),
                "Week 2 (75%)": (0.75, "5-7 reps"),
                "Week 3 (85%)": (0.85, "3-5 reps"),
                "Week 4 (Deload)": (0.50, "10-12 reps")
            }
            
            print(f"\n--- 4-Week Training Block for {max_weight} lbs ---")
            
            # Iteration and unpacking (dictionary items and tuple unpacking)
            for week, block_data in training_block.items():
                percent_decimal = block_data[0]
                rep_range = block_data[1]
                
                calculated_weight = max_weight * percent_decimal
                print(f"{week}: {calculated_weight:.2f} lbs | Target: {rep_range}")
        
                print(f"\n[Session maxes stored: {user_maxes}]")  # Displaying the stored maxes for reference
                
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            
    elif choice == '2':
        # Running Pace Split Calculator
        try:
            total_distance = float(input("Enter the total distance of your run (in miles): "))
            total_time = float(input("Enter your total time for the run (in minutes): "))
            
            pace_per_mile = total_time / total_distance
            print(f"\nYour baseline pace per mile is: {pace_per_mile:.2f} minutes/mile")
            
            print("\n--- Estimated Race Finish Times at this Pace ---")
            
            # Common race distances and their mile equivalents (list of tuples)
            race_distances = [
                ("5K", 3.1),
                ("10K", 6.2),
                ("Half Marathon", 13.1),
                ("Marathon", 26.2)
            ]
            
            # Iteration and unpacking (list items and tuple unpacking)
            for race_name, miles in race_distances:
                estimated_time = pace_per_mile * miles
                print(f"{race_name} ({miles} mi): {estimated_time:.2f} minutes")
                
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            
    elif choice == '3':
        print("Thank you for using the Hybrid Training & Pace Calculator. Goodbye!")
        running = False
        
    else:
        print("Invalid choice. Please select option 1, 2, or 3.")