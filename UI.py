import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.title("Sports Match Analyzer")
root.geometry("1200x750")
root.configure(bg="#0F172A")

section_style = {"bg": "#1E293B", "fg": "white", "font": ("Segoe UI", 11, "bold")}
text_style = {"bg": "#1E293B", "fg": "white"}

def label_frame(parent, title, **options):
    layout = {key: options.pop(key) for key in ["fill", "expand", "padx", "pady"] if key in options}
    frame = tk.LabelFrame(parent, text=title, **section_style, **options)
    frame.pack(fill=layout.get("fill", "both"), expand=layout.get("expand", False), padx=layout.get("padx", 0), pady=layout.get("pady", 0))
    return frame

header = tk.Frame(root, bg=section_style["bg"], height=70)
header.pack(fill="x")

tk.Label(header, text="⚽ Sports Match Analyzer", font=("Segoe UI", 24, "bold"), **text_style).pack(pady=15)

main_frame = tk.Frame(root, bg="#0F172A")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_panel = tk.Frame(main_frame, bg=section_style["bg"], width=300)
left_panel.pack(side="left", fill="y", padx=(0, 10))

tk.Label(left_panel, text="🏠 Home Page", font=("Segoe UI", 16, "bold"), **text_style).pack(pady=10)

search_frame = label_frame(left_panel, "Team Search", fill="x", padx=10, pady=10)
team_entry = tk.Entry(search_frame, font=("Segoe UI", 11))
team_entry.pack(fill="x", padx=10, pady=10)

tk.Button(search_frame, text="Search Team", bg="#3B82F6", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=5)

fav_frame = label_frame(left_panel, "Favourite Teams", fill="both", expand=True, padx=10, pady=10)
tk.Listbox(fav_frame, bg="#334155", fg="white", font=("Segoe UI", 10)).pack(fill="both", expand=True, padx=5, pady=5)

right_panel = tk.Frame(main_frame, bg="#0F172A")
right_panel.pack(side="right", fill="both", expand=True)

info_frame = label_frame(right_panel, "Team Information", fill="x", pady=5)
tk.Label(info_frame, text="Team details will appear here...", anchor="w", justify="left", padx=10, pady=10, **text_style).pack(fill="x")

for label, height in [
    ("Upcoming Fixtures", 8),
    ("Previous Results", 8),
    ("AI Summary", 6),
    ("Match Notes", 6),
]:
    frame = label_frame(right_panel, label, fill="both", expand=True, pady=5)
    ScrolledText(frame, height=height).pack(fill="both", expand=True, padx=5, pady=5)

root.mainloop()
