from test.bases import WorldTestBase

from ..world import AceAttorneyWorld

class AceAttorneyTestBase(WorldTestBase):
    game = "Ace Attorney"
    world: AceAttorneyWorld