from __future__ import annotations

from typing import TYPE_CHECKING, List, Dict, Set, Tuple

from BaseClasses import Region

import json
import pkgutil
import functools

if TYPE_CHECKING:
    from .world import AceAttorneyWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).

REGIONS_FILE = "json/regions.json"

class RegionData:
    name: str = ""
    case: str = ""

    def __init__(self, name: str, case: str):
        self.name = f"{case}: {name}"
        self.case = case

@functools.cache
def import_regions() -> List[RegionData]:
    data = pkgutil.get_data(__name__, REGIONS_FILE)
    assert data is not None
    return json.loads(data.decode("utf-8"), object_hook=lambda d: RegionData(**d))

@functools.cache
def regions_by_case() -> Tuple[Set[str], Dict[str, List[str]]]:
    region_data = import_regions()
    cases = set([data.case for data in region_data])
    regions = {case: [data.name for data in region_data if data.case == case] for case in cases}
    return cases, regions



def create_and_connect_regions(world: AceAttorneyWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: AceAttorneyWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.

    # Let's put all these regions in a list.
    regions: List[Region] = []

    cases, region_dict = regions_by_case()

    for case in cases:
        if case in world.options.cases.value:
            for region_name in region_dict[case]:
                reg = Region(region_name, world.player, world.multiworld)
                regions.append(reg)
    main_menu = Region("Menu", world.player, world.multiworld)
    regions.append(main_menu)
    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: AceAttorneyWorld) -> None:
    
    cases, region_dict = regions_by_case()

    menu_region = world.get_region("Menu")

    for case in cases:
        if case in world.options.cases.value:
            for i, region_name in enumerate(region_dict[case]):
                reg = world.get_region(region_name)
                if i == 0:
                    menu_region.connect(reg, f"Menu to Case {region_name}",)
                else:
                    prev_reg = world.get_region(region_dict[case][i - 1])
                    prev_reg.connect(reg, f"{prev_reg.name} to {region_name}")
