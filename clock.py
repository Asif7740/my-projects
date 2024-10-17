import tkinter as tk
import time
import math

# Function to update the clock hands
def update_clock():
    # Get the current time
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate angles for the hands (in degrees)
    second_angle = (seconds / 60) * 360
    minute_angle = (minutes / 60) * 360 + (seconds / 60) * 6
    hour_angle = (hours / 12) * 360 + (minutes / 60) * 30

    # Update the clock hands
    update_hand(second_hand, second_angle, hand_length['second'])
    update_hand(minute_hand, minute_angle, hand_length['minute'])
    update_hand(hour_hand, hour_angle, hand_length['hour'])

    # Call the function again after 1000 ms (1 second)
    root.after(1000, update_clock)

# Function to update a hand's position
def update_hand(hand, angle, length):
    angle_radians = math.radians(angle)  # Convert to radians
    x = center_x + length * math.sin(angle_radians)
    y = center_y - length * math.cos(angle_radians)  # Y decreases upwards
    canvas.coords(hand, center_x, center_y, x, y)

# Create the main window
root = tk.Tk()
root.title("Unique Analog Clock")

# Create the canvas for the clock
canvas_size = 400
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white", bd=0, highlightthickness=0)
canvas.pack()

# Center of the clock
center_x = canvas_size // 2
center_y = canvas_size // 2

# Radius of the clock
clock_radius = 150

# Gradient background effect
canvas.create_oval(center_x - clock_radius, center_y - clock_radius, 
                   center_x + clock_radius, center_y + clock_radius, 
                   outline="#DDDDDD", width=4, fill="#D1C4E9")

# Add Roman numerals for hour markers
roman_numerals = ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]
for i in range(12):
    angle = math.radians(i * 30)
    x = center_x + (clock_radius - 35) * math.sin(angle)
    y = center_y - (clock_radius - 35) * math.cos(angle)
    canvas.create_text(x, y, text=roman_numerals[i], font=("Times New Roman", 18, "bold"), fill="#333")

# Markings for hours (12-hour clock) with shadow effect
for i in range(60):
    angle = math.radians(i * 6)
    x1 = center_x + (clock_radius - 10) * math.sin(angle)
    y1 = center_y - (clock_radius - 10) * math.cos(angle)
    x2 = center_x + clock_radius * math.sin(angle)
    y2 = center_y - clock_radius * math.cos(angle)
    
    # Shadow for hour markers
    if i % 5 == 0:
        canvas.create_line(x1 + 2, y1 + 2, x2 + 2, y2 + 2, width=3, fill="#888")
        canvas.create_line(x1, y1, x2, y2, width=3, fill="black")
    else:
        canvas.create_line(x1, y1, x2, y2, width=1, fill="#888")

# Define hand lengths for hour, minute, and second hands
hand_length = {
    'hour': 60,
    'minute': 90,
    'second': 100
}

# Draw the hands with unique styles
hour_hand = canvas.create_line(center_x, center_y, center_x, center_y - hand_length['hour'], width=10, fill="#000", capstyle=tk.ROUND)
minute_hand = canvas.create_line(center_x, center_y, center_x, center_y - hand_length['minute'], width=6, fill="#5C6BC0", capstyle=tk.ROUND)
second_hand = canvas.create_line(center_x, center_y, center_x, center_y - hand_length['second'], width=2, fill="#FF5722", capstyle=tk.ROUND)

# Draw the center of the clock (with shadow effect)
canvas.create_oval(center_x - 12, center_y - 12, center_x + 12, center_y + 12, fill="#333", outline="")
canvas.create_oval(center_x - 8, center_y - 8, center_x + 8, center_y + 8, fill="#FFF", outline="")

# Start updating the clock
update_clock()

# Start the tkinter main loop
root.mainloop()
