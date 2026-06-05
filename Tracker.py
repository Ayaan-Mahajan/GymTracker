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
        ex=input('Enter Exercise: ')
        weight=(input('Enter Weight(kg): '))
        rep=int(input('Enter Reps: '))
        date=input("Date (DD-MM-YYYY): ")
        workout={"Exercise": ex, "Weight": weight, "Reps": rep, "Date": date}
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
                print(f"{workout["Date"]} | "
                          f"{workout["Exercise"]} - "
                          f"{workout["Weight"]} x "
                          f"{workout["Reps"]} reps")
        
    elif choice==3:
        print('Goodbye!')
        break
    else:
        print('Invalid Choice')
    
