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

case_counts = {
    "1": 5,
    "2": 4,
    "3": 5,
    "4": 4,
    "5": 6,
    "6": 6,
    "I": 5,
    "I2": 5,
    "G": 5,
    "G2": 5
    }
    
games = [
    "4",
    "5",
    "6"
    ]


def create_and_connect_regions(world: AceAttorneyWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: AceAttorneyWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.

    # Let's put all these regions in a list.
    regions: List[Region] = []

    for game in games:
        for case in range(1, case_counts[game] + 1):
            region_name = f"{game}-{case}"
            if region_name in world.options.cases.value:
                reg = Region(f"Case {region_name}", world.player, world.multiworld)
                regions.append(reg)
    main_menu = Region("Menu", world.player, world.multiworld)
    regions.append(main_menu)
    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: AceAttorneyWorld) -> None:
    
    menu_region = world.get_region("Menu")

    for game in games:
        for case in range(1, case_counts[game] + 1):
            region_name = f"{game}-{case}"
            if region_name in world.options.cases.value:
                reg = world.get_region(f"Case {region_name}")
                menu_region.connect(reg, f"Menu to Case {region_name}")
