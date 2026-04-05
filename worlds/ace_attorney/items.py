from __future__ import annotations

from typing import TYPE_CHECKING, Dict, NamedTuple

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import AceAttorneyWorld

import functools

class ItemData(NamedTuple):
    id: int
    group: str
    case: str = ""
    classification: ItemClassification = ItemClassification.progression

ITEM_DICT: Dict[str, ItemData] = {
    "Objection!": ItemData(1, "filler", classification=ItemClassification.filler),
    "Hold It!": ItemData(2, "filler", classification=ItemClassification.filler),
    "Take That!": ItemData(3, "filler", classification=ItemClassification.filler),
    "Gotcha!": ItemData(4, "filler", classification=ItemClassification.filler),
    "Eureka!": ItemData(5, "filler", classification=ItemClassification.filler),
    "'Scuse Me!": ItemData(6, "filler", classification=ItemClassification.filler),
    "Got It!": ItemData(7, "filler", classification=ItemClassification.filler),
    "Not So Fast!": ItemData(8, "filler", classification=ItemClassification.filler),
    "Overruled!": ItemData(9, "filler", classification=ItemClassification.filler),
    "Silence!": ItemData(10, "filler", classification=ItemClassification.filler),
    "Yes!": ItemData(11, "filler", classification=ItemClassification.filler),
    "Shut Up!": ItemData(12, "filler", classification=ItemClassification.filler),
    "That's Enough!": ItemData(13, "filler", classification=ItemClassification.filler),
    "Satorha!": ItemData(14, "filler", classification=ItemClassification.filler),
    "Such Insolence!": ItemData(15, "filler", classification=ItemClassification.filler),
    "Deadly Bottle": ItemData(16, "evidence", "4-1"),
    "Smith's Autopsy Report": ItemData(16, "evidence", "4-1"),
    "Crime Photo 1": ItemData(18, "evidence", "4-1"),
    "Crime Photo 2": ItemData(19, "evidence", "4-1"),
    "Phoneix Wright": ItemData(20, "profile", "4-1"),
    "Kristoph Gavin": ItemData(21, "profile", "4-1"),
    "Chip Photo": ItemData(22, "evidence", "4-1"),
    "Winston Payne": ItemData(23, "profile", "4-1"),
    "Olga Orly": ItemData(24, "profile", "4-1")
}

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.

ITEM_NAME_TO_ID = {f"{data.case}: {name}": data.id for name, data in ITEM_DICT.items()}

FILLER_ITEM_NAMES = [name for name, data in ITEM_DICT.items() if data.group == "filler"]


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
    return FILLER_ITEM_NAMES[world.random.randint(0, len(FILLER_ITEM_NAMES))]


def create_item_with_correct_classification(world: AceAttorneyWorld, name: str) -> AceAttorneyItem:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = ItemClassification.filler

    if name in ITEM_DICT.keys() and (ITEM_DICT[name].group == "evidence" or (ITEM_DICT[name].group == "profile" and world.options.profile_sanity)):
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

    itempool: list[Item] = [world.create_item(name) for name, data in ITEM_DICT.items() if data.group == "evidence"]
    if world.options.profile_sanity:
        itempool.extend(world.create_item(name) for name, data in ITEM_DICT.items() if data.group == "profile")

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
