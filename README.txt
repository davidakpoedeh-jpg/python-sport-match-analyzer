This is our project of a Sports Match Analyzer

A Python application for analyzing sports matches and displaying statistics. It runs a simple rule-based prediction (based on recent win/loss history) for a quick, non-AI estimate. The project fetches live data from TheSportsDB API — team info, upcoming fixtures, and past results.

It uses Google's Gemini AI to generate:
A pre-match preview for the next fixture
A post-match summary of the last result
Trivia facts about the team
A fan-friendly analysis of current form

The files cantained are:
- main.py - Program entry point
- MatchAnalyzer.py - Match analysis logic
- Sports_api.py - API integration
- TeamMatches.py - Team match handling
- Validation.py - Input validation
- Storage.py - Data storage
- sports_data.json - Stored data

Technologies Used:

- Python
- Tkinter
- Requests
- JSON
- Regular Expressions (Regex)
- Google Gemini AI
- TheSportsDB API

To run the code, you have to replace "Enter you gemini API key" on main.py line 17 with an actual API key

