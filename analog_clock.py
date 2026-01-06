import tkinter as tk
import time
import math

# Constants
R = 140
CX = CY = R
NUM_RADIUS = 110

# Create window
root = tk.Tk()
root.title("Analog Clock")

# Canvas
canvas = tk.Canvas(root, width=2 * R, height=2 * R, bg="white")
canvas.pack()

# Clock face
canvas.create_oval(10, 10, 2 * R - 10, 2 * R - 10, outline="black", width=2)

# Numbers
for i in range(1, 13):
    ang = math.radians(i * 30 - 90)
    x = CX + NUM_RADIUS * math.cos(ang)
    y = CY + NUM_RADIUS * math.sin(ang)
    canvas.create_text(
        x, y,
        text=str(i),
        font=("Helvetica", 14, "bold"),
        fill="black"
    )

def update_clock():
    now = time.localtime()
    sec = now.tm_sec
    minute = now.tm_min
    hour = now.tm_hour % 12

    canvas.delete("hands")

    # Second hand
    a = math.radians(sec * 6 - 90)
    canvas.create_line(
        CX, CY,
        CX + 90 * math.cos(a),
        CY + 90 * math.sin(a),
        fill="red",
        width=1,
        tags="hands"
    )

    # Minute hand
    a = math.radians(minute * 6 - 90)
    canvas.create_line(
        CX, CY,
        CX + 70 * math.cos(a),
        CY + 70 * math.sin(a),
        fill="black",
        width=3,
        tags="hands"
    )

    # Hour hand
    a = math.radians(hour * 30 + minute * 0.5 - 90)
    canvas.create_line(
        CX, CY,
        CX + 50 * math.cos(a),
        CY + 50 * math.sin(a),
        fill="black",
        width=5,
        tags="hands"
    )

    # Center dot
    canvas.create_oval(
        CX - 4, CY - 4,
        CX + 4, CY + 4,
        fill="black",
        tags="hands"
    )

    root.after(200, update_clock)

# Start clock
update_clock()
root.mainloop()
