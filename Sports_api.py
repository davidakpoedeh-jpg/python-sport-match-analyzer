import requests
import re
API_KEY = "3"
BASE_URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}"
class SportsAPIClient:
    def __init__(self):
        self.base_url = BASE_URL
    def clean_team_name(self, team_name):
        pattern = r"[^A-Za-z0-9 ]"
        return re.sub(pattern, "", team_name)
    def get_team(self, team_name):
        team_name = self.clean_team_name(team_name)
        url = f"{self.base_url}/searchteams.php?t={team_name}"
        try:
            response = requests.get(url)
            data = response.json()
            if data["teams"] is None:
                print("Team not found.")
                return None
            return data["teams"][0]
        except Exception:
            print("Unable to connect to the Sports API.")
            return None
    def get_upcoming_matches(self, team_id):
        url = f"{self.base_url}/eventsnext.php?id={team_id}"
        try:
            response = requests.get(url)
            data = response.json()
            return data["events"]
        except Exception:
            print("No upcoming matches.")
            return []
    def get_previous_matches(self, team_id):
        url = f"{self.base_url}/eventslast.php?id={team_id}"
        try:
            response = requests.get(url)
            data = response.json()
            return data["results"]
        except Exception:
            print("No previous matches.")
            return []
    def get_match_details(self, match_id):
        url = f"{self.base_url}/lookupevent.php?id={match_id}"
        try:
            response = requests.get(url)
            data = response.json()
            return data["events"][0]
        except Exception:
            print("Match details unavailable.")
            return None