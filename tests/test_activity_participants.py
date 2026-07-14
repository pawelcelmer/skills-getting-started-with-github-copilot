from urllib.parse import quote

from fastapi.testclient import TestClient

import src.app as app_module
from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email():
    activity_name = "Chess Club"
    participant_email = "michael@mergington.edu"
    original_participants = list(app_module.activities[activity_name]["participants"])

    try:
        response = client.delete(
            f"/activities/{quote(activity_name)}/participants/{quote(participant_email)}"
        )

        assert response.status_code == 200
        assert participant_email not in app_module.activities[activity_name]["participants"]
    finally:
        app_module.activities[activity_name]["participants"] = original_participants
