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

    sets_frame = ctk.CTkFrame(window)
    sets_frame.pack(pady=10, fill="x")


    set_entries = []

    def add_set():
        set_number = len(set_entries) + 1

        ctk.CTkLabel(
           sets_frame,
           text=f"Set {set_number} Weight (kg)"
        ).pack(pady=5)

        weight_entry = ctk.CTkEntry(sets_frame)
        weight_entry.pack()

        ctk.CTkLabel(
            sets_frame,
            text=f"Set {set_number} Reps"
        ).pack(pady=5)

        reps_entry = ctk.CTkEntry(sets_frame)
        reps_entry.pack()

        set_entries.append(
            (weight_entry, reps_entry))
        
    
    add_set()

    add_set_button = ctk.CTkButton(
       window,
       text="➕ Add Set",
       command=add_set
)

    add_set_button.pack(pady=10)

    
    def save_workout():

        sets = []

        for weight_entry, reps_entry in set_entries:
            if (
                weight_entry.get() != ""
                and reps_entry.get() != ""
    ):

                sets.append(
                   {
                        "Weight": weight_entry.get(),
                        "Reps": reps_entry.get()
                  }
        )
            

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
        
        window.destroy()
        

    save_button = ctk.CTkButton(
        window,
        text="Save Workout",
        command=save_workout
    )

    save_button.pack(pady=20)

    success_label = ctk.CTkLabel(
    window,
    text=""
)
    success_label.pack()
    
    
  

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