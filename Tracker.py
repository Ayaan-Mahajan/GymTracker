import json

def load_workouts():
    try:
        with open("workouts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_workouts():
    with open("workouts.json", "w") as file:
        json.dump(workouts, file, indent=4)

def add_workout():
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
    save_workouts()
    print('Workout Added Successfully!')
        
def view_workouts():
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
        
def workout_statistics():
    print("\n===== WORKOUT STATISTICS =====")
    total_workouts=len(workouts)
    print(f"Total Workouts: {total_workouts}")
    total_sets=0
    muscle_counts={}
    for workout in workouts:
        muscle=workout["Muscle_Group"]
        if muscle in muscle_counts:
            muscle_counts[muscle]+=1
        else:
            muscle_counts[muscle]=1
        
        if "Sets" in workout:
            total_sets += len(workout["Sets"])
            
    print("\nWorkouts By Muscle Group: ")
    print()
        
    for muscle, count in muscle_counts.items():
        print(f"{muscle}: {count}")
            
    print()
    print(f"Total Sets Performed: {total_sets} ")

def personal_records():
    print("\n===== PERSONAL RECORDS =====")
    prs={}
    for workout in workouts:
        exercise=workout["Exercise"]
        if "Sets" in workout:
            for set_data in workout["Sets"]:
                weight=float(set_data["Weight"])
                if exercise not in prs:
                    prs[exercise]=weight
                elif weight>prs[exercise]:
                    prs[exercise]=weight
        else:
            weight=float(workout["Weight"].replace("kg", " "))
            if exercise not in prs:
                prs[exercise]=weight
            elif weight>prs[exercise]:
                prs[exercise]=weight
    for exercise, pr in prs.items():
        if pr.is_integer():
            print(f"{exercise}: {int(pr)} kg")
        else:
            print(f"{exercise}: {pr} kg")

def search_by_exercise():
    search_exercise=input("Enter exercise name: ")
    print("\n===== SEARCH RESULTS =====")
    found=False
    for workout in workouts:
        if workout["Exercise"].lower() == search_exercise.lower():
            found=True
            print(f"\n{workout['Date']} | "
                    f"{workout['Muscle_Group']} | "
                    f"{workout['Exercise']}")
            if "Sets" in workout:
                for i, set_data in enumerate(workout["Sets"]):
                    print(f"Set {i+1}: {set_data['Weight']} kg x {set_data['Reps']} reps")
            else:
                print(f"{workout['Weight']} x {workout['Reps']} reps")
    if not found:
        print('No Workouts Found. ')

def search_by_muscle_group():
    search_muscle=input("Enter Muscle Group: ")
    print("\n===== SEARCH RESULTS =====")
    found=False
    for workout in workouts:
        if workout["Muscle_Group"].lower() == search_muscle.lower():
            found=True
            print(f"\n{workout['Date']} | "
                    f"{workout['Muscle_Group']} | "
                    f"{workout['Exercise']}")
        if "Sets" in workout:
            for i, set_data in enumerate(workout["Sets"]):
                print(f"Set {i+1}: {set_data['Weight']} kg x {set_data['Reps']} reps")
        else:
            print(f"{workout['Weight']} x {workout['Reps']} reps")
    if not found:
        print('No Workouts Found. ')

def delete_workout():
    print("\n===== DELETE WORKOUT =====")
    for i, workout in enumerate(workouts):
        print(f"{i+1}. {workout['Date']} | {workout['Exercise']} ({workout['Muscle_Group']})")
    try:
        delete_number=int(input('Enter workout number to delete: '))
        if 1 <= delete_number <= len(workouts):
            workouts.pop(delete_number - 1)
            save_workouts()
            print("Workout deleted successfully!")
        else:
            print("Invalid workout number!")
    except ValueError:
        print("Please enter a valid number!")
            
def edit_workout():
    print("\n===== EDIT WORKOUT =====")
    for i, workout in enumerate(workouts):
        print(f"{i+1}. {workout['Date']} | {workout['Exercise']} ({workout['Muscle_Group']})")
    try:
        edit_number=int(input("Enter workout number to edit: "))
        if 1 <= edit_number <= len(workouts):
            index=edit_number-1
            print('Current Date: ', workouts[index]['Date'])
            print('Current Exercise: ', workouts[index]['Exercise'])
            print('Current Muscle Group: ', workouts[index]['Muscle_Group'])
            new_date=input('Enter New Date (press enter to keep same): ')
            new_exercise=input('Enter new exercise (press enter to keep same): ')
            new_muscle=input('Enter new muscle group (press enter to keep same): ')
            if new_date != "":
                workouts[index]["Date"]=new_date
            if new_exercise != "":
                workouts[index]["Exercise"]=new_exercise
            if new_muscle !="":
                workouts[index]["Muscle_Group"]=new_muscle
                
        else:
            print('Invalid Workout Number')
        edit_sets=input("Do you want to edit sets? (y/n): ")
        if edit_sets.lower()=="y":
            for i, current_set in enumerate(workouts[index]['Sets']):
                print(f"{i+1}. {current_set['Weight']}kg x {current_set['Reps']} reps")
       
            set_number=int(input('Enter set number to edit: '))
            set_index=set_number-1
            if 1<=set_number<=len(workouts[index]['Sets']):
                selected_set=workouts[index]['Sets'][set_index]
                print("Current Weight:", selected_set["Weight"])
                print("Current Reps:", selected_set["Reps"])
                new_weight = input("Enter new weight (press enter to keep same): ")
                new_reps = input("Enter new reps (press enter to keep same): ")
                if new_weight != "":
                    selected_set["Weight"] = new_weight
                if new_reps != "":
                    selected_set["Reps"] = new_reps
            else:
                print("Invalid Set Number!")
        save_workouts()
        print("Workout updated successfully!")
            
    except ValueError:
            print("Please enter a valid number!")
            
workouts=load_workouts()
while True:
    print("\n-----Gym Tracker-----")
    print("1. Add Workout")
    print("2. View Workouts")
    print("3. Workout Statistics")
    print("4. Personal Records")
    print("5. Search by Exercise")
    print("6. Search by Muscle Group")
    print("7. Delete Workout")
    print("8. Edit Workout")
    print("9. Exit")
    choice=int(input('Enter choice: '))

    if choice==1:
        add_workout()
        
    elif choice==2:
        view_workouts()

    elif choice==3:
        workout_statistics()

    elif choice==4:
        personal_records()

    elif choice==5:
        search_by_exercise()

    elif choice==6:
        search_by_muscle_group()

    elif choice==7:
        delete_workout()

    elif choice==8:
        edit_workout()

    elif choice==9:
        print('Goodbye!')
        break
    
    else:
        print('Invalid Choice')
    



    
