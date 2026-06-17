import customtkinter as ctk
import json
from tkinter import messagebox

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

def search_workouts():
    window = ctk.CTkToplevel(app)

    window.title("Search Workouts")
    window.geometry("400x300")

    ctk.CTkLabel(
        window,
        text="Search Workouts",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    ctk.CTkLabel(
    window,
    text="Search By"
    ).pack(pady=5)

    search_type = ctk.StringVar(value="Exercise")

    search_menu = ctk.CTkOptionMenu(
    window,
    values=["Exercise", "Muscle Group"],
    variable=search_type
    )

    search_menu.pack(pady=5)

    ctk.CTkLabel(
    window,
    text="Enter Search Term"
    ).pack(pady=5)

    search_entry = ctk.CTkEntry(window)

    search_entry.pack(pady=5)

    def perform_search():
        results_box.delete("1.0", "end")

        try:
            with open("workouts.json", "r") as file:
                workouts = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            results_box.insert(
            "end",
            "No workouts found."
            )
            return

        query = search_entry.get().lower()

        search_by = search_type.get()

        matches = []

        for workout in workouts:
            if (search_by == "Exercise" and query in workout["Exercise"].lower()):
                matches.append(workout)
            elif (search_by == "Muscle Group" and query in workout["Muscle_Group"].lower()):
                matches.append(workout)

        if len(matches) == 0:
            results_box.insert(
                "end",
                "No matching workouts found."
           )

            return

        for workout in matches:
            results_box.insert(
                "end",
                f"Date: {workout['Date']}\n"
            )

            results_box.insert(
                "end",
                f"Exercise: {workout['Exercise']}\n"
            )

            results_box.insert(
                "end",
                f"Muscle Group: {workout['Muscle_Group']}\n"
            )

            results_box.insert(
                "end",
                "Sets:\n"
            )

            if "Sets" in workout:
                for index, workout_set in enumerate(workout["Sets"], start=1):
                    results_box.insert(
                        "end",
                        f"  Set {index}: "
                        f"{workout_set['Weight']} kg × "
                        f"{workout_set['Reps']} reps\n"
                   )

            else:
                results_box.insert(
                    "end",
                    f"Weight: {workout['Weight']} kg\n"
                )

                results_box.insert(
                    "end",
                    f"Reps: {workout['Reps']}\n"
               )

            results_box.insert(
                "end",
                "\n" + "-" * 35 + "\n\n"
            )
    search_btn = ctk.CTkButton(
        window,
        text="Search",
        command=perform_search
    )

    search_btn.pack(pady=10)

    results_box = ctk.CTkTextbox(
    window,
    width=350,
    height=150
    )

    results_box.pack(pady=15)

def view_prs():
    window = ctk.CTkToplevel(app)

    window.title("Personal Records")
    window.geometry("450x500")

    ctk.CTkLabel(
        window,
        text="🏆 Personal Records",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    scroll_frame = ctk.CTkScrollableFrame(
    window,
    width=400,
    height=350
    )

    scroll_frame.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
    )

    try:
        with open("workouts.json", "r") as file:
            workouts = json.load(file)
        print("Workouts loaded:", len(workouts))

    except (FileNotFoundError, json.JSONDecodeError):
        ctk.CTkLabel(
            window,
        text="No workouts found."
    ).pack(pady=20)
        return
    prs = {}
    for workout in workouts:
        exercise = workout["Exercise"]
        highest_weight = 0
        if "Sets" in workout:
            for workout_set in workout["Sets"]:
                weight = float(workout_set["Weight"])

                highest_weight = max(
                highest_weight,
                weight
                )

        else:
            weight = float(
                    str(workout["Weight"]).replace("kg", "")
            )

            highest_weight = weight

        if (exercise not in prs or highest_weight > prs[exercise]):
            prs[exercise] = highest_weight 

    for exercise in sorted(prs):
        pr=prs[exercise]
        ctk.CTkLabel(
           scroll_frame,
           text=f"🥇 {exercise}: {pr:g} kg",
           font=("Arial", 16)
        ).pack(pady=5)

def workout_stats():

    window = ctk.CTkToplevel(app)

    window.title("Workout Statistics")
    window.geometry("450x400")

    ctk.CTkLabel(
        window,
        text="📊 Workout Statistics",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    try:
        with open("workouts.json", "r") as file:
            workouts = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):

        ctk.CTkLabel(
            window,
            text="No workouts found."
        ).pack(pady=20)

        return
    workout_dates = set()

    for workout in workouts:

        workout_dates.add(workout["Date"])

    total_workouts = len(workout_dates)
    total_sets = 0
    total_volume = 0
    muscle_counts = {}
    exercise_counts = {}
    for workout in workouts:
        muscle = workout["Muscle_Group"]
        if muscle not in muscle_counts:
            muscle_counts[muscle] = 0
        muscle_counts[muscle] += 1

        exercise = workout["Exercise"]
        if exercise not in exercise_counts:
            exercise_counts[exercise] = 0
        exercise_counts[exercise] += 1

        if "Sets" in workout:
            total_sets += len(workout["Sets"])
            for workout_set in workout["Sets"]:
                weight = float(workout_set["Weight"])
                reps = int(workout_set["Reps"])
                total_volume += weight * reps
            
        else:
            total_sets += 1
            weight = float(str(workout["Weight"]).replace("kg", ""))
            reps = int(workout["Reps"])
            total_volume += weight * reps
    most_trained_muscle = max(
    muscle_counts,
    key=muscle_counts.get
)

    most_performed_exercise = max(
    exercise_counts,
    key=exercise_counts.get
)

    ctk.CTkLabel(
        window,
        text=f"📅 Total Workout Days: {total_workouts}",
        font=("Arial", 18)
    ).pack(pady=15)

    ctk.CTkLabel(
    window,
    text=f"💪 Total Sets: {total_sets}",
    font=("Arial", 18)
    ).pack(pady=15)

    ctk.CTkLabel(
    window,
    text=f"🏋️ Total Volume: {total_volume:,.0f} kg",
    font=("Arial", 18)
    ).pack(pady=15)

    ctk.CTkLabel(
    window,
    text=f"🔥 Most Trained Muscle: {most_trained_muscle}",
    font=("Arial", 18)
    ).pack(pady=15)

    ctk.CTkLabel(
    window,
    text=(
        f"🥇 Most Performed Exercise: "
        f"{most_performed_exercise}"
    ),
    font=("Arial", 18)
).pack(pady=15)

def edit_workout():
    
    window = ctk.CTkToplevel(app)

    window.title("Edit Workout")

    window.geometry("500x500")


    ctk.CTkLabel(
        window,
        text="Edit Workout",
        font=("Arial",20,"bold")
    ).pack(pady=20)

    scroll_frame = ctk.CTkScrollableFrame(
    window,
    width=430,
    height=350)
    scroll_frame.pack(
    pady=10,
    padx=20,
    fill="both",
    expand=True)

    try:
        with open("workouts.json", "r") as file:
             workouts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        workouts = []

    def open_editor(workout):
        editor = ctk.CTkToplevel(app)
        editor.title(
        "Edit Workout")
        editor.geometry(
        "400x500")
        ctk.CTkLabel(

        editor,

        text="Edit Workout",

        font=("Arial",20,"bold")

        ).pack(
        pady=20
        )

        ctk.CTkLabel(editor,text="Date").pack()
        date_entry=ctk.CTkEntry(editor)
        date_entry.pack()

        ctk.CTkLabel(editor,text="Exercise").pack()
        exercise_entry=ctk.CTkEntry(editor)
        exercise_entry.pack()
         
        ctk.CTkLabel(editor,text="Muscle Group").pack()
        muscle_entry=ctk.CTkEntry(editor)
        muscle_entry.pack()

        date_entry.insert(0,workout["Date"])
        exercise_entry.insert(0,workout["Exercise"])
        muscle_entry.insert(0,workout["Muscle_Group"])

        sets_frame = ctk.CTkScrollableFrame(
        editor,
        width=300,
        height=250
)
        sets_frame.pack(pady=10,fill="both",expand=True)
        
        set_entries=[]
        def add_set(weight_val="", reps_val=""):
            set_frame = ctk.CTkFrame(sets_frame)
            set_frame.pack(pady=5)
            weight = ctk.CTkEntry(set_frame, width=80)
            reps = ctk.CTkEntry(set_frame, width=80)
            weight.grid(row=0,column=0,padx=5)
            reps.grid(row=0,column=1,padx=5)
            weight.insert(0, weight_val)
            reps.insert(0, reps_val)
            set_entries.append((weight, reps))

        for s in workout["Sets"]:
             add_set(s["Weight"],s["Reps"])

        ctk.CTkButton(

           editor,

           text="➕ Add Set",

           command=add_set

        ).pack(

            pady=10

        )

        
        def save_changes():
            idx = workouts.index(workout)
            updated_sets=[]
            for weight,reps in set_entries:
                updated_sets.append({ "Weight":weight.get(),  "Reps":reps.get() })
            workouts[idx]={ "Date":date_entry.get(), "Exercise":exercise_entry.get(), "Muscle_Group":muscle_entry.get(), "Sets":updated_sets}
            with open( "workouts.json", "w") as file:
                json.dump(workouts,file,indent=4)
            messagebox.showinfo("Success", "Workout Updated Successfully! 🔥")
            editor.destroy()
            window.destroy()
            edit_workout()

        save_button = ctk.CTkButton(

        editor,

        text="Save Changes",

        command=save_changes)
        
        save_button.pack(

        pady=20)
         

    for workout in workouts:
        button_text = (
        f"{workout['Date']} | "
        f"{workout['Exercise']}"
    )
        ctk.CTkButton(

           scroll_frame,

           text=button_text,

           command=lambda w=workout:
           open_editor(w)

        ).pack(

           pady=5,

           fill="x"

        )

def delete_workout():

    window=ctk.CTkToplevel(app)

    window.title(

            "Delete Workout"

    )

    window.geometry(

            "500x500"

    )
    scroll_frame=ctk.CTkScrollableFrame(

        window,

        width=430,

        height=350

    )
    scroll_frame.pack(

        pady=10,

        padx=20,

        fill="both",

        expand=True

    ) 
    try:
        with open( "workouts.json", "r") as file:
            workouts=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        workouts=[]

    if len(workouts)==0:
        ctk.CTkLabel(

            window,

            text="No workouts found.",

            font=("Arial",18)

        ).pack(

            pady=30

        )
        return
        
    def remove_workout(workout):
        confirm = messagebox.askyesno(

           "Delete Workout",

           f"Delete {workout['Exercise']} ?")
        if not confirm:
            return
        workouts.remove(workout)
        with open("workouts.json",  "w") as file:
            json.dump(workouts,  file,  indent=4)

        messagebox.showinfo(

        "Success",

        "Workout Deleted Successfully! 🗑️")

        window.destroy()
        

    for workout in workouts:
        button_text=(
                    f"{workout['Date']} | "

                    f"{workout['Exercise']}")


        ctk.CTkButton(

            scroll_frame,


            text=button_text,


            command=lambda w=workout:


            remove_workout(w)


        ).pack(


            pady=5,


            fill="x")

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
    text="Search",
    command=search_workouts
)
search_button.pack(pady=10)


stats_button = ctk.CTkButton(
    app,
    text="PR Dashboard",
    command=view_prs
)
stats_button.pack(pady=10)

workout_stats_button = ctk.CTkButton(
    app,
    text="Workout Statistics",
    command=workout_stats
)

workout_stats_button.pack(pady=10)

edit_button = ctk.CTkButton(
    app,
    text="Edit Workout",
    command=edit_workout
)

edit_button.pack(pady=10)

delete_button = ctk.CTkButton(

        app,

        text="Delete Workout",

        command=delete_workout

)

delete_button.pack(
        pady=10
)

exit_button = ctk.CTkButton(
    app,
    text="Exit",
    command=app.destroy
)
exit_button.pack(pady=30)


    
app.mainloop()