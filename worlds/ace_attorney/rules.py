from __future__ import annotations

from typing import TYPE_CHECKING, Iterable, List, Dict

from BaseClasses import Entrance, Location
from rule_builder import rules

from .options import StartCase, Profilesanity

import functools

if TYPE_CHECKING:
    from .world import AceAttorneyWorld

from .regions import CASES, unprettify_case_string

RULES: List[Dict[str, List[int | List[str]]]] = [
    {
        "access_id": [],
        "location_id": [9, 10, 11, 12, 13],
        "req_items": [["4-1: Deadly Bottle"]],
        "req_profiles": []
    },
    {
        "access_id": [9],
        "location_id": [14, 15],
        "req_items": [["4-1: Smith's Autopsy Report"]],
        "req_profiles": []
    },
    {
        "access_id": [9],
        "location_id": [16],
        "req_items": [["4-1: Crime Photo 2"]],
        "req_profiles": []
    },
    {
        "access_id": [16],
        "location_id": [17, 18, 19],
        "req_items": [["4-1: Chip Photo"]],
        "req_profiles": []
    },
    {
        "access_id": [19],
        "location_id": [20],
        "req_items": [["4-1: Wright's Cell Phone"]],
        "req_profiles": [["4-1: Kristoph Gavin"]]
    },
    {
        "access_id": [20],
        "location_id": [21, 22],
        "req_items": [["4-1: Crime Photo 1"]],
        "req_profiles": []
    },
    {
        "access_id": [22],
        "location_id": [23, 24, 25],
        "req_items": [["4-1: Bloody Ace"]],
        "req_profiles": []
    }
]


def set_all_rules(world: AceAttorneyWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: AceAttorneyWorld) -> None:
    if not world.options.lock_locations:
        return

    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    entrances: Iterable[Entrance] = world.get_entrances()

    for entrance in entrances:
        if entrance.connected_region != None and unprettify_case_string(entrance.connected_region.name) in CASES:
            world.set_rule(entrance, rules.Has(f"Unlock {entrance.connected_region.name}", options=[rules.OptionFilter(StartCase, unprettify_case_string(entrance.connected_region.name), "ne")], filtered_resolution=True))

@functools.cache
def get_id_to_loc(world: AceAttorneyWorld) -> Dict[int | None, Location]:
    return {loc.address: loc for loc in world.get_locations()}




def set_all_location_rules(world: AceAttorneyWorld) -> None:

    def get_loc_by_id(id: int) -> Location | None:
        if id in get_id_to_loc(world).keys():
            return get_id_to_loc(world)[id]
        return None

    for rule in RULES:
        access_locs = [get_loc_by_id(id) for id in rule["access_id"] if isinstance(id, int)]
        locations = [get_loc_by_id(id) for id in rule["location_id"] if isinstance(id, int)]
        req_items = rule["req_items"]
        req_profiles = rule["req_profiles"]
        assert access_locs is not None
        assert None not in access_locs
        assert locations is not None
        assert None not in locations
        assert req_items is not None
        assert req_profiles is not None

        for loc in locations:
            assert loc is not None
            item_rules = [rules.HasAll(*items) for items in req_items if isinstance(items, list)]
            loc_rules = [rules.CanReachLocation(acc_loc.name) for acc_loc in access_locs if acc_loc is not None]
            profile_rules = [rules.HasAll(*profiles) for profiles in req_profiles if isinstance(profiles, list)]
            if len(item_rules) == 0:
                item_rules = [rules.True_()]
            if len(loc_rules) == 0:
                loc_rules = [rules.True_()]
            if len(profile_rules) == 0:
                profile_rules = [rules.True_()]
            world.set_rule(
                loc,
                rules.Or(*item_rules) &
                rules.And(*loc_rules) &
                rules.Or(*profile_rules, options=[rules.OptionFilter(Profilesanity, True)], filtered_resolution=True),
            )



def set_completion_condition(world: AceAttorneyWorld) -> None:

    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.set_completion_rule(rules.Has("Victory"))
