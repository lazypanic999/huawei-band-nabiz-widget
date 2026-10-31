"""Small always-on-top heart-rate display for Huawei HR Overlay."""

import json
import tkinter as tk
from urllib.error import URLError
from urllib.request import urlopen


STATUS_URL = "http://localhost:8764/status"
BG = "#121827"

root = tk.Tk()
root.title("Canlı nabız")
root.geometry("190x90+0+0")
root.resizable(False, False)
root.attributes("-topmost", True)
root.configure(bg=BG)
root.after(200, root.lift)

frame = tk.Frame(root, bg=BG, highlightbackground="#ef476f", highlightthickness=1)
frame.pack(fill="both", expand=True)

heart = tk.Label(frame, text="♥", font=("Segoe UI Symbol", 25), fg="#ef476f", bg=BG)
heart.pack(side="left", padx=(10, 5))

value = tk.Label(frame, text="--", font=("Segoe UI", 29, "bold"), fg="white", bg=BG)
value.pack(side="left")

unit = tk.Label(frame, text="BPM", font=("Segoe UI", 9), fg="#aeb7cc", bg=BG)
unit.pack(side="left", padx=(4, 0), pady=(22, 0))

drag_start = None


def start_drag(event):
    global drag_start
    drag_start = (event.x_root - root.winfo_x(), event.y_root - root.winfo_y())


def drag(event):
    if drag_start:
        root.geometry(f"+{event.x_root - drag_start[0]}+{event.y_root - drag_start[1]}")


def update():
    try:
        with urlopen(STATUS_URL, timeout=0.7) as response:
            data = json.load(response)
        bpm = data.get("bpm")
        connected = data.get("connected")
        value.configure(text=str(bpm) if connected and isinstance(bpm, int) and bpm > 0 else "--")
    except (OSError, URLError, ValueError, json.JSONDecodeError):
        value.configure(text="--")
    root.after(1000, update)


for widget in (frame, heart, value, unit):
    widget.bind("<ButtonPress-1>", start_drag)
    widget.bind("<B1-Motion>", drag)
    widget.bind("<Button-3>", lambda _event: root.destroy())

update()
root.mainloop()
