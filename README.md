# Gym Tracker
A desktop-based workout tracking application built using Python, JSON, and CustomTkinter.

Gym Tracker helps users log workouts, track progress, monitor personal records, and manage their fitness journey through both a command-line interface and a graphical user interface.

## Features

### Workout Management
- Add workouts with date, exercise, muscle group, weight, and reps
- View complete workout history
- Delete existing workouts
- Edit existing workouts

### Strength Tracking
- Support for multiple sets
- Track weight and reps for each set
- Personal Records (PRs) tracking

### Analytics
- Total workout statistics
- Workout summaries

### Desktop GUI
- View workouts through a graphical interface
- Add workouts without using the terminal
- Support for up to 3 sets directly through the GUI
- Automatic JSON saving
- Backward compatibility with older workout data formats

### Reliability
- JSON-based persistent storage
- Error handling using try-except blocks
- Refactored using functions for better code organization
 
## Version History
- V1 – Add and store workouts using JSON
- V2 – View workout history
- V3 – Workout statistics
- V4 – Personal Records (PR) tracking
- V5 – Search workouts by exercise
- V6 – Search workouts by muscle group
- V7 – Delete workouts
- V8 – Edit workouts and update set details
- V9 – Error handling and validation
- V10 – Refactored code using functions
- V11 – JSON persistence improvements
- V12 – GUI workout viewer using CustomTkinter
- V13 – GUI workout entry with multi-set support

## Technologies Used
- Python
- JSON
- Git & GitHub
- CustomTkinter

## Project Structure
 Gym Tracker/

- ├── gym_tracker.py # CLI version

- ├── gym_tracker_gui.py # GUI version

- ├── workouts.json # Workout database

- ├── README.md

## How To Run

### Clone the repository
- git clone <your-repository-url> cd Gym-Tracker
### Install dependencies
- pip install customtkinter
### Run the CLI version
- python3 gym_tracker.py
### Run the GUI version
- python3 gym_tracker_gui.py

## Screenshots
### Main Window

![Main Window](screenshots/main_window.png)

### Add Workout Form

![Add Workout Form](screenshots/add_workout.png)

### View Workouts

![View Workouts](screenshots/view_workouts.png)

## Future Improvements
- Dynamic "Add Set" button
- Search functionality in GUI
- Statistics dashboard
- PR dashboard
- Export workouts to CSV
- Data visualizations and charts

## About This Project
I built Gym Tracker as a personal project to strengthen my Python programming skills before starting college. Through this project, I learned:

- File handling with JSON
- Functions and code refactoring
- Error handling
- CRUD operations
- GUI development using CustomTkinter
- Debugging and problem-solving
- Git and GitHub workflows

This project reflects my journey from writing simple Python scripts to building a functional desktop application.

## Author
Ayaan Mahajan


