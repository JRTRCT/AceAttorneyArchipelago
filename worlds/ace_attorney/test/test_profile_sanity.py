from .bases import AceAttorneyTestBase

class TestProfilesanity(AceAttorneyTestBase):
    options = {
        "profile_sanity": True,
        "start_case": "case_4_1",
        "victory_case": "case_4_1",
        "lock_locations": False,
        "cases": ["bleh"]
    }