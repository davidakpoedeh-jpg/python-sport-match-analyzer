from google import genai
class MatchAnalyzer:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def _safe(self, text, default="Unknown"):
        return text if text else default

    def generate_team_trivia(self, team_name):
        team_name = self._safe(team_name)
        return (
            f"{team_name} is known for its passionate fanbase and strong team spirit. "
            "Historically, teams with a similar style have performed well in close contests, "
            "so watch for disciplined defending and fast transitions."
        )

    def generate_pre_match_preview(self, home_team, away_team, venue):
        home_team = self._safe(home_team)
        away_team = self._safe(away_team)
        venue = self._safe(venue, "the scheduled venue")
        return (
            f"Pre-match preview for {home_team} vs {away_team} at {venue}:\n\n"
            "Expect a competitive match where both sides will try to control possession early. "
            "If the home side uses the crowd advantage effectively, they may press high and create more chances. "
            "Defending teams should stay compact and look for quick counterattacks.")

    def generate_post_match_summary(self, home_team, away_team, score):
        home_team = self._safe(home_team)
        away_team = self._safe(away_team)
        score = self._safe(score, "0-0")
        return (
            f"Post-match summary: {home_team} faced {away_team} and the final score was {score}.\n\n"
            "The match showed strong moments from both sides. Key takeaways include solid defensive organization, "
            "important attacking combinations, and a result that may influence confidence going into the next fixture.")
