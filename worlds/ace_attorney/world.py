from collections.abc import Mapping
from typing import Any, Set

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world
from . import options as ace_attorney_options  # rename due to a name conflict with World.options

from .regions import prettify_case_string

# APQuest will go through all the parts of the world api one step at a time,
# with many examples and comments across multiple files.
# If you'd rather read one continuous document, or just like reading multiple sources,
# we also have this document specifying the entire world api:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md


# The world class is the heart and soul of an apworld implementation.
# It holds all the data and functions required to build the world and submit it to the multiworld generator.
# You could have all your world code in just this one class, but for readability and better structure,
# it is common to split up world functionality into multiple files.
# This implementation in particular has the following additional files, each covering one topic:
# regions.py, locations.py, rules.py, items.py, options.py and web_world.py.
# It is recommended that you read these in that specific order, then come back to the world class.
class AceAttorneyWorld(World):
    """
    Ace Attorney is a visual novel series where you find
    contradictions to corner culprits.

    Support for all modern PC ports is planned, but currently only
    the Apollo Justice Trilogy is supported.
    """

    # The docstring should contain a description of the game, to be displayed on the WebHost.

    # You must override the "game" field to say the name of the game.
    game = "Ace Attorney"

    # The WebWorld is a definition class that governs how this world will be displayed on the website.
    web = web_world.AceAttorneyWorld()

    # This is how we associate the options defined in our options.py with our world.
    # (Note: options.py has been imported as "ace_attorney_options" at the top of this file to avoid a name conflict)
    options_dataclass = ace_attorney_options.AceAttorneyOptions
    options: ace_attorney_options.AceAttorneyOptions  # Common mistake: This has to be a colon (:), not an equals sign (=).

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.
    location_name_to_id = locations.location_name_to_id()
    item_name_to_id = items.ITEM_NAME_TO_ID

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    origin_region_name = "Menu"

    cases: Set[str] = set()
    start_case: str = ""
    victory_case: str = ""

    def generate_early(self) -> None:
        if "all" in self.options.cases.value:
            self.options.cases.value.update(self.options.cases.valid_keys)
            self.options.cases.value.discard("all")
        self.cases = set(case.split(" ", 1)[1] for case in self.options.cases.value)
        self.start_case = prettify_case_string(self.options.start_case.current_key).upper()
        self.victory_case = prettify_case_string(self.options.victory_case.current_key).upper()
        if self.start_case not in self.cases:
            self.cases.add(self.start_case)
            self.options.cases.value.add(f"Case {self.start_case}")
        if self.victory_case not in self.cases:
            self.cases.add(self.victory_case)
            self.options.cases.value.add(f"Case {self.victory_case}")

    # Our world class must have certain functions ("steps") that get called during generation.
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    # Our world class must also have a create_item function that can create any one of our items by name at any time.
    # We also put this in a different file, the same one that create_items is in.
    def create_item(self, name: str) -> items.AceAttorneyItem:
        return items.create_item_with_correct_classification(self, name)

    # For features such as item links and panic-method start inventory, AP may ask your world to create extra filler.
    # The way it does this is by calling get_filler_item_name.
    # For this purpose, your world *must* have at least one infinitely repeatable item (usually filler).
    # You must override this function and return this infinitely repeatable item's name.
    # In our case, we defined a function called get_random_filler_item_name for this purpose in our items.py.
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "lock_locations", "profile_sanity", "cases", "start_case"
        )
