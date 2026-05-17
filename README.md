# Project Overview
 This Python Application serves as a complete Hotel Reservation System. I prefer the system to be organized, reliable, and easy to use for managing hotel rooms and bookings. This CLI based application follows a modular design and Object Oriented Programming (OOP) principles with clean separation of data, logic and user interface.
 Users can easily add unlimited rooms, book rooms for guests, view all rooms and reservations, and keep all data safe. The system automatically saves all data to a JSON file and never crashes due to invalid input.
 # KEY FEATURES OF THE CLI-based Hotel Reservation System
 * Add new rooms
 * View all rooms with availability status
 * Book available rooms
 * View all reservations
 * Cancel existing reservations
 * Auto‑calculate total booking amount
 * Data persistence: Auto‑save / auto‑load from JSON
 * Full error handling (never crashes on invalid input)
 # Error Handling
 Built‑in protection ensures the app never crashes:
 - Empty input → Clear message
 - Duplicate room numbers → Blocked
 - Invalid menu choices → Guided correction
 - Corrupted/missing JSON → Auto‑reset safely
 - Wrong data type → Rejected with instruction
 # Advanced Python Concepts Used
 1. List Comprehension – Filter/search data in one line (main.py Line 32, 54)
 2. Context Manager – Safe file handling (utils.py Line 18, 36)
 3. @classmethod – Create objects from saved JSON (models.py Line 12, 28)
 4. Magic/Dunder Methods – _str_, _eq_ for clean object behavior
 5. Type Hints – Clear data types for readability & error prevention
 6. Error Handling (try…except) → Handles missing files, corrupted data, invalid input
 # Installation & How to Run
 1. Requirements
    - Python 3.7 or higher
    - No external packages needed (uses only built‑in modules)
 2. Run the App
    - Open terminal / command prompt
    - Navigate to the project folder
 3. Run
    - Add Room: Register new hotel rooms
    - View Rooms: See all rooms and their status
    - Book Room: Reserve a room for guests
    - View Reservations: Check all bookings
    - Cancel Reservation: Remove bookings and free rooms
    - Save & Exit: Saves everything automatically
 # Author
 STUDENT: MAOMAY, ZALDY L.
 Section: BSCS 1B
 Instructor: ALLAN IBO JR.
 Course: INTERMEDIATE PROGRAMMING (Final Project)
 Instructor: ALLAN IBO JR.
 FINAL PROJECT# Maomay_Zaldy_FinalProject
My digital space to display my talents and works

https://youtu.be/ldlPoBhThRA?si=3P8jKEwoirVxl5xl
