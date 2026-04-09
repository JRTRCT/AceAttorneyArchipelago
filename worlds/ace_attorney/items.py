from __future__ import annotations

from typing import TYPE_CHECKING, Dict, NamedTuple, List

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import AceAttorneyWorld

import functools

class ItemData(NamedTuple):
    name:str
    id: int
    group: str
    case: str = ""
    classification: ItemClassification = ItemClassification.progression

ITEM_LIST: List[ItemData] = [
    ItemData("Objection!", 1, "filler", classification=ItemClassification.filler),
    ItemData("Hold It!", 2, "filler", classification=ItemClassification.filler),
    ItemData("Take That!", 3, "filler", classification=ItemClassification.filler),
    ItemData("Gotcha!", 4, "filler", classification=ItemClassification.filler),
    ItemData("Eureka!", 5, "filler", classification=ItemClassification.filler),
    ItemData("'Scuse Me!", 6, "filler", classification=ItemClassification.filler),
    ItemData("Got It!", 7, "filler", classification=ItemClassification.filler),
    ItemData("Not So Fast!", 8, "filler", classification=ItemClassification.filler),
    ItemData("Overruled!", 9, "filler", classification=ItemClassification.filler),
    ItemData("Silence!", 10, "filler", classification=ItemClassification.filler),
    ItemData("Yes!", 11, "filler", classification=ItemClassification.filler),
    ItemData("Shut Up!", 12, "filler", classification=ItemClassification.filler),
    ItemData("That's Enough!", 13, "filler", classification=ItemClassification.filler),
    ItemData("Satorha!", 14, "filler", classification=ItemClassification.filler),
    ItemData("Such Insolence!", 15, "filler", classification=ItemClassification.filler),
    ItemData("Deadly Bottle", 16, "evidence", "4-1"),
    ItemData("Smith's Autopsy Report", 17, "evidence", "4-1"),
    ItemData("Crime Photo 1", 18, "evidence", "4-1"),
    ItemData("Crime Photo 2", 19, "evidence", "4-1"),
    ItemData("Phoneix Wright", 20, "profile", "4-1"),
    ItemData("Kristoph Gavin", 21, "profile", "4-1"),
    ItemData("Chips Photo", 22, "evidence", "4-1"),
    ItemData("Winston Payne", 23, "profile", "4-1"),
    ItemData("Olga Orly", 24, "profile", "4-1"),
    ItemData("Wright's Cell Phone", 25, "evidence", "4-1"),
    ItemData("Bloody Ace", 26, "evidence", "4-1"),
    ItemData("Attorney's Badge", 27, "evidence", "4-1"),
    ItemData("Olga's Photo", 28, "evidence", "4-1"),
    ItemData("Attorney's Badge", 29, "evidence", "4-2"),
    ItemData("Map", 30, "evidence", "4-2"),
    ItemData("Bowl", 31, "evidence", "4-2"),
    ItemData("Trucy's Evidence", 32, "evidence", "4-2"),
    ItemData("Cell Phone", 33, "evidence", "4-2"),
    ItemData("Mirror", 34, "evidence", "4-2"),
    ItemData("Fingerprint Powder", 35, "evidence", "4-2"),
    ItemData("Meraktis's Autopsy report", 36, "evidence", "4-2"),
    ItemData("Knife", 37, "evidence", "4-2"),
    ItemData("Noodle Stand", 38, "evidence", "4-2"),
    ItemData("Plum's Evidence", 39, "evidence", "4-2"),
    ItemData("Wocky's Check-Up Report", 40, "evidence", "4-2"),
    ItemData("Pistol", 41, "evidence", "4-2"),
    ItemData("Slippers", 42, "evidence", "4-2"),
    ItemData("Detective Skye's Orders", 43, "evidence", "4-2"),
    ItemData("Alita's Sandles", 44, "evidence", "4-2"),
    ItemData("Lamp", 45, "evidence", "4-2"),
    ItemData("Wocky's Chart", 46, "evidence", "4-2"),
    ItemData("Bullet", 47, "evidence", "4-2"),
    ItemData("Phoenix Wright", 48, "profile", "4-2"),
    ItemData("Trucy Wright", 49, "profile", "4-2"),
    ItemData("Dr. Hickfield", 50, "profile", "4-2"),
    ItemData("Guy Eldoon", 51, "profile", "4-2"),
    ItemData("Plum Kitaki", 52, "profile", "4-2"),
    ItemData("Alita Talia", 53, "profile", "4-2"),
    ItemData("Ema Skye", 54, "profile", "4-2"),
    ItemData("Klavier Gavin", 55, "profile", "4-2"),
    ItemData("Wocky Kitaki", 56, "profile", "4-2"),
    ItemData("Winfred Kitaki", 57, "profile", "4-2"),
    ItemData("Pal Meraktis", 58, "profile", "4-2"),
    ItemData("Wesley Stickler", 59, "profile", "4-2"),
    ItemData("Unlock 4-1", 60, "unlock", "4-1"),
    ItemData("Unlock 4-2", 61, "unlock", "4-2"),
    ItemData("Unlock 4-3", 62, "unlock", "4-3"),
    ItemData("Unlock 4-4", 63, "unlock", "4-4"),
    ItemData("Unlock 5-1", 64, "unlock", "5-1"),
    ItemData("Unlock 5-2", 65, "unlock", "5-2"),
    ItemData("Unlock 5-3", 66, "unlock", "5-3"),
    ItemData("Unlock 5-4", 67, "unlock", "5-4"),
    ItemData("Unlock 5-5", 68, "unlock", "5-5"),
    ItemData("Unlock 5-SP", 69, "unlock", "5-SP"),
    ItemData("Unlock 6-1", 70, "unlock", "6-1"),
    ItemData("Unlock 6-2", 71, "unlock", "6-2"),
    ItemData("Unlock 6-3", 72, "unlock", "6-3"),
    ItemData("Unlock 6-4", 73, "unlock", "6-4"),
    ItemData("Unlock 6-5", 74, "unlock", "6-5"),
    ItemData("Unlock 6-SP", 75, "unlock", "6-SP"),
    ItemData("Attorney's Badge", 76, "evidence", "4-3")
]

ITEM_DICT: Dict[str, ItemData] = {data.name if data.case == "" or data.group == "unlock" else f"{data.case}: {data.name}": data for data in ITEM_LIST}

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.

ITEM_NAME_TO_ID = {name: data.id for name, data in ITEM_DICT.items()}

FILLER_ITEM_NAMES = [data.name for data in ITEM_LIST if data.group == "filler"]


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class AceAttorneyItem(Item):
    game = "Ace Attorney"


# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: AceAttorneyWorld) -> str:
    # APQuest has an option called "trap_chance".
    # This is the percentage chance that each filler item is a Math Trap instead of a Confetti Cannon.
    # For this purpose, we need to use a random generator.

    # IMPORTANT: Whenever you need to use a random generator, you must use world.random.
    # This ensures that generating with the same generator seed twice yields the same output.
    # DO NOT use a bare random object from Python's built-in random module.
    return FILLER_ITEM_NAMES[world.random.randint(0, len(FILLER_ITEM_NAMES) - 1)]


def create_item_with_correct_classification(world: AceAttorneyWorld, name: str) -> AceAttorneyItem:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = ItemClassification.filler

    if name in ITEM_DICT.keys():
        classification = ITEM_DICT[name].classification

    return AceAttorneyItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: AceAttorneyWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

    itempool: list[Item] = [world.create_item(name) for name, data in ITEM_DICT.items() if data.group == "evidence" and data.case in world.cases]
    if world.options.profile_sanity:
        itempool.extend(world.create_item(name) for name, data in ITEM_DICT.items() if data.group == "profile" and data.case in world.cases)
    if world.options.lock_locations:
        itempool.extend(world.create_item(name) for name, data in ITEM_DICT.items() if data.group == "unlock" and data.case in world.cases and data.case != world.start_case)

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool
