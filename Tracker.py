import json
try:
    with open("workouts.json", "r") as file:
        workouts=json.load(file)
except:
    workouts=[]
while True:
    print("\n-----Gym Tracker-----")
    print("1. Add Workout")
    print("2. View Workouts")
    print("3. Exit")
    choice=int(input('Enter choice: '))
    
    if choice==1:
        exercise=input('Enter Exercise: ')
        date=input("Date (DD-MM-YYYY): ")
        muscle_group=input("Enter Muscle Group: ")
        sets=[]
        num_sets=int(input("How many sets? "))
        for i in range(num_sets):
            weight=input(f"Set {i+1} Weight: ")
            rep=input(f"Set {i+1} Reps: ")
            set_data={'Weight': weight, 'Reps': rep}
            sets.append(set_data)
        workout={"Exercise": exercise, "Date": date, "Muscle_Group": muscle_group, "Sets": sets}
        workouts.append(workout)
        with open("workouts.json", "w") as file:
            json.dump(workouts, file, indent=4)
        print('Workout Added Successfully!')
        
    elif choice==2:
        print('\nWorkout History: ')
        if workouts==[]:
            print('No Workouts Found. ')
        else:
            for workout in workouts:
                print(f"\n{workout["Date"]} | "
                          f"{workout["Muscle_Group"]} | "
                          f"{workout["Exercise"]}  ")
                if "Sets" in workout:
                    for i, set_data in enumerate(workout["Sets"]):
                        print (f"Set {i+1}: "
                                   f"{set_data["Weight"]} kg x "
                                   f"{set_data["Reps"]} reps ")
                else:
                    print(f"{workout["Weight"]} kg x {workout["Reps"]} reps")
                print()
        
    elif choice==3:
        print('Goodbye!')
        break
    else:
        print('Invalid Choice')
    
