import re
def validate_team_name(team_name): 
    "Returns True if the team name contains only letters and spaces."
    pattern = r"^[A-Za-z ]+$"
    if re.match(pattern, team_name):
        return True
    else:
        return False
def clean_team_name(team_name):
    team_name = re.sub(r"[^A-Za-z ]", "", team_name)
    team_name = team_name.strip()
    team_name = team_name.title()
    return team_name
def validate_date(date):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(pattern, date):
        return True
    else:
        return False
def extract_scores(text):
    pattern = r"\d+-\d+"
    scores = re.findall(pattern, text)
    return scores
def score_positions(text):
    pattern = r"\d+-\d+"
    matches = re.finditer(pattern, text)
    for match in matches:
        print("Score:", match.group())
        print("Starts at:", match.start())
        print("Ends at:", match.end())
        print()
def contains_score(text):
    pattern = r"\d+-\d+"
    if re.search(pattern, text):
      return True
      return False
