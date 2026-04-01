from __future__ import annotations

from typing import TYPE_CHECKING, List, Dict

from BaseClasses import ItemClassification, Location

from . import items

import functools
import pkgutil
import json

if TYPE_CHECKING:
    from .world import AceAttorneyWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "Top Left Room Chest": 1,
    "Top Middle Chest": 2,
    "Bottom Left Chest": 3,
    "Bottom Left Extra Chest": 4,
    "Bottom Right Room Left Chest": 5,
    "Bottom Right Room Right Chest": 6,
    # Location IDs don't need to be sequential, as long as they're unique and greater than 0.
    "Right Room Enemy Drop": 10,
}

LOCATIONS_FILE = "json/locations.json"


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class AceAttorneyLocation(Location):
    game = "Ace Attorney"

class RegionData:
    region_name: str = ""
    case: str = ""
    id: int
    locations: Dict[str, int]

    def __init__(self, region_name: str, case: str, id: int, locations: List[Dict[str, str | int]]):
        self.region_name = f"{case}: {region_name}"
        self.case= case
        self.id = id
        self.locations = {f"{case}: {location["name"]}": int(location["id"]) for location in locations}


@functools.cache
def import_location_regions() -> List[RegionData]:
    data = pkgutil.get_data(__name__, LOCATIONS_FILE)
    assert data is not None
    return json.loads(data.decode("utf-8"), object_hook=lambda d: RegionData(**d))

@functools.cache
def location_name_to_id() -> Dict[str, int]:
    regions = import_location_regions()
    locations: Dict[str, int] = {}
    for region in regions:
        locations.update(region.locations)
    return locations


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: location_name_to_id()[location_name] for location_name in location_names}


def create_all_locations(world: AceAttorneyWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: AceAttorneyWorld) -> None:
    regions = import_location_regions()

    for region in regions:
        if region.case in world.options.cases.value:
            world.get_region(region.region_name).add_locations(region.locations, AceAttorneyLocation)
    



def create_events(world: AceAttorneyWorld) -> None:

    final_case: str = world.options.victory_case.value
    victory_location = world.get_location(f"{final_case}: Finish Case: {final_case}")
    victory_item = items.AceAttorneyItem("Victory", ItemClassification.progression, None, world.player)
    victory_location.place_locked_item(victory_item)
