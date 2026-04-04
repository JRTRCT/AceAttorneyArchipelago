from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import AceAttorneyWorld

import functools

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
FILLER_NAME_TO_ID = {
    "Objection!": 1,
    "Hold It!": 2,
    "Take That!": 3,
    "Gotcha!": 4,
    "Eureka!": 5,
    "'Scuse Me!": 6,
    "Got It!": 7,
    "Not So Fast!": 8,
    "Overruled!": 9,
    "Silence!": 10,
    "Yes!": 11,
    "Shut Up!": 12,
    "That's Enough!": 13,
    "Satorha!": 14,
    "Such Insolence!": 15
}

ITEM_NAME_TO_ID = {
    "Deadly Bottle": 16,
    "Smith's Autopsy Report": 17,
    "Crime Photo": 18,
    "Crime Photo 2": 19
}

PROFILE_NAME_TO_ID = {
    "Phoneix Wright": 20
}


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class AceAttorneyItem(Item):
    game = "APQuest"

@functools.cache
def item_name_to_id() -> Dict[str, int]:
    name_to_id = {}
    name_to_id.update(FILLER_NAME_TO_ID)
    name_to_id.update(ITEM_NAME_TO_ID)
    name_to_id.update(PROFILE_NAME_TO_ID)
    return name_to_id


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
    return [key for key in FILLER_NAME_TO_ID.keys()][world.random.randint(0, len(FILLER_NAME_TO_ID))]


def create_item_with_correct_classification(world: AceAttorneyWorld, name: str) -> AceAttorneyItem:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = ItemClassification.filler

    if name in ITEM_NAME_TO_ID.keys() or (name in PROFILE_NAME_TO_ID.keys() and world.options.profile_sanity):
        classification = ItemClassification.progression

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

    itempool: list[Item] = [world.create_item(name) for name in ITEM_NAME_TO_ID.keys()]
    if world.options.profile_sanity:
        itempool.extend(world.create_item(name) for name in PROFILE_NAME_TO_ID.keys())

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
