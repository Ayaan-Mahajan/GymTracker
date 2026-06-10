import customtkinter as ctk

app = ctk.CTk()

app.title("Gym Tracker")
app.geometry("400x300")

label = ctk.CTkLabel(
    app,
    text="BRO THE GUI WORKS 😭🔥"
)
label.pack(pady=40)

app.mainloop()