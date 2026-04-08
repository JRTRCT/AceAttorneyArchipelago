from .bases import AceAttorneyTestBase

class TestAllCases(AceAttorneyTestBase):
    options = {
        "profile_sanity": False,
        "start_case": "case_4_1",
        "victory_case": "case_4_1",
        "lock_locations": False,
        "cases": ["all"]
    }