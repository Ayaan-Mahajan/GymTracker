import customtkinter as ctk
import json

def add_workout():

    window = ctk.CTkToplevel(app)

    window.title("Add Workout")
    window.geometry("400x500")

    ctk.CTkLabel(window, text="Date").pack(pady=5)
    date_entry = ctk.CTkEntry(window)
    date_entry.pack()

    ctk.CTkLabel(window, text="Exercise").pack(pady=5)
    exercise_entry = ctk.CTkEntry(window)
    exercise_entry.pack()

    ctk.CTkLabel(window, text="Muscle Group").pack(pady=5)
    muscle_entry = ctk.CTkEntry(window)
    muscle_entry.pack()

    ctk.CTkLabel(window, text="Set 1 Weight (kg)").pack(pady=5)
    set1_weight = ctk.CTkEntry(window)
    set1_weight.pack()

    ctk.CTkLabel(window, text="Set 1 Reps").pack(pady=5)
    set1_reps = ctk.CTkEntry(window)
    set1_reps.pack()


    ctk.CTkLabel(window, text="Set 2 Weight (kg)").pack(pady=5)
    set2_weight = ctk.CTkEntry(window)
    set2_weight.pack()

    ctk.CTkLabel(window, text="Set 2 Reps").pack(pady=5)
    set2_reps = ctk.CTkEntry(window)
    set2_reps.pack()


    ctk.CTkLabel(window, text="Set 3 Weight (kg)").pack(pady=5)
    set3_weight = ctk.CTkEntry(window)
    set3_weight.pack()

    ctk.CTkLabel(window, text="Set 3 Reps").pack(pady=5)
    set3_reps = ctk.CTkEntry(window)
    set3_reps.pack()

    
    success_label = ctk.CTkLabel(
        window,
        text=""
    )
    success_label.pack()

    
    def save_workout():

        sets = []

        if set1_weight.get() != "" and set1_reps.get() != "":
           sets.append({
               "Weight": set1_weight.get(),
                "Reps": set1_reps.get()
            })

        if set2_weight.get() != "" and set2_reps.get() !="":
            sets.append({
                "Weight": set2_weight.get(),
                "Reps": set2_reps.get()
           })

        if set3_weight.get() != "" and set3_reps.get() != "":
            sets.append({
                "Weight": set3_weight.get(),
                "Reps": set3_reps.get()
           })

        new_workout = {
            "Date": date_entry.get(),
            "Exercise": exercise_entry.get(),
            "Muscle_Group": muscle_entry.get(),
            "Sets": sets
        }

        try:
            with open("workouts.json", "r") as file:
                workouts = json.load(file)

        except FileNotFoundError:
            workouts = []

        workouts.append(new_workout)

        with open("workouts.json", "w") as file:
            json.dump(workouts, file, indent=4)

        success_label.configure(
            text="Workout Saved! 😭🔥"
        )
        print("Before destroy")
        window.destroy()
        print("After destroy")

    save_button = ctk.CTkButton(
        window,
        text="Save Workout",
        command=save_workout
    )

    save_button.pack(pady=20)
    
    
  

def view_workouts():
    print("BRO THE BUTTON WORKS 😭🔥")

    window = ctk.CTkToplevel(app)

    window.title("View Workouts")
    window.geometry("500x400")

    textbox = ctk.CTkTextbox(
        window,
        width=450,
        height=320
    )

    textbox.pack(padx=20, pady=20)

    try:
        with open("workouts.json", "r") as file:
            workouts = json.load(file)

        for workout in workouts:
            
            textbox.insert(
                "end",
                f"Date: {workout['Date']}\n"
    )

            textbox.insert(
                "end",
                f"Exercise: {workout['Exercise']}\n"
    )

            textbox.insert(
                "end",
                f"Muscle Group: {workout['Muscle_Group']}\n"
    )

            if "Sets" in workout:
                
                for i, current_set in enumerate(workout["Sets"]):
                    textbox.insert(
                        "end",
                        f"Set {i+1}: "
                        f"{current_set['Weight']}kg × "
                        f"{current_set['Reps']} reps\n"
        )

            else:
                
                textbox.insert(
                    "end",
                    f"Weight: {workout['Weight']}kg\n"
    )

                textbox.insert(
                    "end",
                    f"Reps: {workout['Reps']}\n"
    )

            textbox.insert(
                "end",
                "\n------------------------\n\n"
    )
    except FileNotFoundError:
        textbox.insert("end", "workouts.json not found 😭")
    
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Gym Tracker")
app.geometry("500x500")


title = ctk.CTkLabel(
    app,
    text="🏋️ Gym Tracker",
    font=("Arial", 28, "bold")
)

title.pack(pady=30)


add_button = ctk.CTkButton(
    app,
    text="Add Workout",
    command=add_workout
)
add_button.pack(pady=10)


view_button = ctk.CTkButton(
    app,
    text="View Workouts",
    command=view_workouts
)
view_button.pack(pady=10)


search_button = ctk.CTkButton(
    app,
    text="Search"
)
search_button.pack(pady=10)


stats_button = ctk.CTkButton(
    app,
    text="Statistics"
)
stats_button.pack(pady=10)


exit_button = ctk.CTkButton(
    app,
    text="Exit",
    command=app.destroy
)
exit_button.pack(pady=30)


    
app.mainloop()