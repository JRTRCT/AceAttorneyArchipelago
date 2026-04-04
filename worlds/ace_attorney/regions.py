from __future__ import annotations

from typing import TYPE_CHECKING, List

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import AceAttorneyWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).

CASES = [
    "case_4_1",
    "case_4_2",
    "case_4_3",
    "case_4_4",
    "case_5_1",
    "case_5_2",
    "case_5_3",
    "case_5_4",
    "case_5_5",
    "case_5_SP",
    "case_6_1",
    "case_6_2",
    "case_6_3",
    "case_6_4",
    "case_6_5",
    "case_6_SP"
]

def prettify_case_string(case_name: str) -> str:
    if case_name.count('_') != 2:
        return case_name
    split = case_name.split('_')
    return f"{split[1]}-{split[2]}"

def unprettify_case_string(case_name: str) -> str:
    if case_name.count('-') != 1:
        return case_name
    split = case_name.split('-')
    return f"case_{split[0]}_{split[1]}"


def create_and_connect_regions(world: AceAttorneyWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: AceAttorneyWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.

    # Let's put all these regions in a list.
    regions: List[Region] = []

    for region_name in CASES:
        if region_name in world.options.cases.value:
            reg = Region(prettify_case_string(region_name), world.player, world.multiworld)
            regions.append(reg)
    main_menu = Region("Menu", world.player, world.multiworld)
    regions.append(main_menu)
    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: AceAttorneyWorld) -> None:

    menu_region = world.get_region("Menu")

    for region_name in CASES:
        if region_name in world.options.cases.value:
            region_name = prettify_case_string(region_name)
            reg = world.get_region(region_name)
            menu_region.connect(reg, f"Menu to Case {region_name}",)
