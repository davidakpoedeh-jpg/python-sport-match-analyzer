import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as messagebox
 
from Sports_api import SportsAPIClient
from Validation import validate_team_name, clean_team_name
from Storage import (
    save_favourite_team,
    load_favourite_teams,
    save_match_note,
    save_generated_summary,
)
from Ai_features import MatchAnalyzer as AIFeatures
from MatchAnalyzer import MatchAnalyzer as PredictionEngine
 

GEMINI_API_KEY = "AQ.Ab8RN6I4JMzJGJVSZ1z81pIh_r0QKMUJLt8AVSwNVhG_kT1BIg"
api_client = SportsAPIClient()
ai = AIFeatures(api_key=GEMINI_API_KEY)
predictor = PredictionEngine()
current_team = {"data": None}
def search_team():
    raw_name = team_entry.get()
    if not validate_team_name(raw_name):
        messagebox.showerror(
            "Invalid name", "Team name must contain only letters and spaces."
        )
        return
    team_name = clean_team_name(raw_name)
    team = api_client.get_team(team_name)
    if team is None:
        messagebox.showinfo("Not found", f"Could not find team '{team_name}'.")
        return
    current_team["data"] = team
    team_id = team["idTeam"]
    info_text = (
        f"Name: {team.get('strTeam', 'N/A')}\n"
        f"Country: {team.get('strCountry', 'N/A')}\n"
        f"Stadium: {team.get('strStadium', 'N/A')}\n"
        f"League: {team.get('strLeague', 'N/A')}"
    )
    info_label.config(text=info_text)
    upcoming = api_client.get_upcoming_matches(team_id)
    fixtures_box.delete("1.0", tk.END)
    if upcoming:
        for match in upcoming:
            fixtures_box.insert(
                tk.END,
                f"{match.get('strHomeTeam')} vs {match.get('strAwayTeam')} "
                f"on {match.get('dateEvent')}\n",
            )
    else:
        fixtures_box.insert(tk.END, "No upcoming matches found.\n")
    previous = api_client.get_previous_matches(team_id)
    results_box.delete("1.0", tk.END)
    if previous:
        for match in previous:
            results_box.insert(
                tk.END,
                f"{match.get('strHomeTeam')} {match.get('intHomeScore')} - "
                f"{match.get('intAwayScore')} {match.get('strAwayTeam')}\n",
            )
    else:
        results_box.insert(tk.END, "No previous matches found.\n")
    prediction = predictor.predict_match(previous if previous else [])
    ai_box.delete("1.0", tk.END)
    ai_box.insert(tk.END, f"Prediction: {prediction}\n\n")
    trivia = ai.generate_team_trivia(team_name)
    ai_box.insert(tk.END, f"Trivia:\n{trivia}\n")
    save_favourite_team(team_name)
    refresh_favourites()
def generate_preview():
    team = current_team["data"]
    if team is None:
        messagebox.showinfo("No team selected", "Search for a team first.")
        return
    upcoming = api_client.get_upcoming_matches(team["idTeam"])
    if not upcoming:
        messagebox.showinfo("No fixtures", "No upcoming match to preview.")
        return
    match = upcoming[0]
    preview = ai.generate_pre_match_preview(
        match.get("strHomeTeam"), match.get("strAwayTeam"), match.get("strVenue", "TBD")
    )
    ai_box.delete("1.0", tk.END)
    ai_box.insert(tk.END, preview)
    save_generated_summary(preview)
def generate_summary():
    team = current_team["data"]
    if team is None:
        messagebox.showinfo("No team selected", "Search for a team first.")
        return
    previous = api_client.get_previous_matches(team["idTeam"])
    if not previous:
        messagebox.showinfo("No results", "No previous match to summarise.")
        return
    match = previous[0]
    score = f"{match.get('intHomeScore')}-{match.get('intAwayScore')}"
    summary = ai.generate_post_match_summary(
        match.get("strHomeTeam"), match.get("strAwayTeam"), score
    )
    ai_box.delete("1.0", tk.END)
    ai_box.insert(tk.END, summary)
    save_generated_summary(summary)
def add_note():
    note = notes_entry.get()
    if note.strip():
        save_match_note(note)
        notes_box.insert(tk.END, f"- {note}\n")
        notes_entry.delete(0, tk.END)
def refresh_favourites():
    favourites_list.delete(0, tk.END)
    for fav in load_favourite_teams():
        favourites_list.insert(tk.END, fav)
root = tk.Tk()
root.title("Sports Match Analyzer")
root.geometry("1200x750")
root.configure(bg="#0F172A")
section_style = {"bg": "#1E293B", "fg": "white", "font": ("Segoe UI", 11, "bold")}
text_style = {"bg": "#1E293B", "fg": "white"}
def label_frame(parent, title, **options):
    layout = {key: options.pop(key) for key in ["fill", "expand", "padx", "pady"] if key in options}
    frame = tk.LabelFrame(parent, text=title, **section_style, **options)
    frame.pack(
        fill=layout.get("fill", "both"),
        expand=layout.get("expand", False),
        padx=layout.get("padx", 0),
        pady=layout.get("pady", 0),
    )
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
tk.Button(
    search_frame, text="Search Team", bg="#3B82F6", fg="white",
    font=("Segoe UI", 10, "bold"), command=search_team
).pack(pady=5)
 
ai_buttons_frame = label_frame(left_panel, "AI Tools", fill="x", padx=10, pady=10)
tk.Button(
    ai_buttons_frame, text="Pre-Match Preview", bg="#10B981", fg="white",
    font=("Segoe UI", 10, "bold"), command=generate_preview
).pack(fill="x", pady=3)
tk.Button(
    ai_buttons_frame, text="Post-Match Summary", bg="#10B981", fg="white",
    font=("Segoe UI", 10, "bold"), command=generate_summary
).pack(fill="x", pady=3)
fav_frame = label_frame(left_panel, "Favourite Teams", fill="both", expand=True, padx=10, pady=10)
favourites_list = tk.Listbox(fav_frame, bg="#334155", fg="white", font=("Segoe UI", 10))
favourites_list.pack(fill="both", expand=True, padx=5, pady=5)
right_panel = tk.Frame(main_frame, bg="#0F172A")
right_panel.pack(side="right", fill="both", expand=True)
info_frame = label_frame(right_panel, "Team Information", fill="x", pady=5)
info_label = tk.Label(
    info_frame, text="Team details will appear here...",
    anchor="w", justify="left", padx=10, pady=10, **text_style
)
info_label.pack(fill="x")
fixtures_frame = label_frame(right_panel, "Upcoming Fixtures", fill="both", expand=True, pady=5)
fixtures_box = ScrolledText(fixtures_frame, height=6)
fixtures_box.pack(fill="both", expand=True, padx=5, pady=5)
results_frame = label_frame(right_panel, "Previous Results", fill="both", expand=True, pady=5)
results_box = ScrolledText(results_frame, height=6)
results_box.pack(fill="both", expand=True, padx=5, pady=5)
ai_frame = label_frame(right_panel, "AI Summary", fill="both", expand=True, pady=5)
ai_box = ScrolledText(ai_frame, height=8)
ai_box.pack(fill="both", expand=True, padx=5, pady=5)
notes_frame = label_frame(right_panel, "Match Notes", fill="both", expand=True, pady=5)
notes_entry_frame = tk.Frame(notes_frame, bg=section_style["bg"])
notes_entry_frame.pack(fill="x", padx=5, pady=(5, 0))
notes_entry = tk.Entry(notes_entry_frame, font=("Segoe UI", 10))
notes_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
tk.Button(notes_entry_frame, text="Add Note", command=add_note).pack(side="left")
notes_box = ScrolledText(notes_frame, height=4)
notes_box.pack(fill="both", expand=True, padx=5, pady=5)
refresh_favourites()
 
root.mainloop()