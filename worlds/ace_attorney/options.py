from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, OptionSet, Toggle

from .regions import prettify_case_string

import typing

# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  APQuest doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md

class AAChoice(Choice):
    @classmethod
    def get_option_name(cls, value: int) -> str:
        return "Case " + prettify_case_string(cls.name_lookup[value]).upper()


# The first type of Option we'll discuss is the Toggle.
# A toggle is an option that can either be on or off. This will be represented by a checkbox on the website.
# The default for a toggle is "off".
# If you want a toggle to be on by default, you can use the "DefaultOnToggle" class instead of the "Toggle" class.
class Profilesanity(Toggle):
    """
    When Profilesanity is turned on, both evidence and profiles will be randomized.
    When Profilesanity is turned off, only evidence will be randomized.
    """

    # The docstring of an option is used as the description on the website and in the template yaml.

    # You'll also want to set a display name, which will determine what the option is called on the website.
    display_name = "Profilesanity"


class LockLocations(Toggle):
    """
    When Lock Cases is turned on, cases will be locked until the correct item is obtained.
    When Lock Cases is turned off, all enabled cases will be unlocked at all times,
    and Starting Case is treated like any other case.
    """

    display_name = "Lock Cases"


# A Choice is an option with multiple discrete choices. This will be represented by a dropdown on the website.
class StartCase(AAChoice):
    """
    The case which is unlocked from the beginning.
    """

    display_name = "Starting Case"

    option_case_4_1 = 0
    option_case_4_2 = 1
    option_case_4_3 = 2
    option_case_4_4 = 3
    option_case_5_1 = 4
    option_case_5_2 = 5
    option_case_5_3 = 6
    option_case_5_4 = 7
    option_case_5_5 = 8
    option_case_5_SP = 9
    option_case_6_1 = 10
    option_case_6_2 = 11
    option_case_6_3 = 12
    option_case_6_4 = 13
    option_case_6_5 = 14
    option_case_6_SP = 15

    # Choice options must define an explicit default value.
    default = option_case_4_1

class VictoryCase(AAChoice):
    """
    Finishing this case is the completion condition for this APWorld.
    """

    display_name = "Victory Case"

    option_case_4_1 = 0
    option_case_4_2 = 1
    option_case_4_3 = 2
    option_case_4_4 = 3
    option_case_5_1 = 4
    option_case_5_2 = 5
    option_case_5_3 = 6
    option_case_5_4 = 7
    option_case_5_5 = 8
    option_case_5_SP = 9
    option_case_6_1 = 10
    option_case_6_2 = 11
    option_case_6_3 = 12
    option_case_6_4 = 13
    option_case_6_5 = 14
    option_case_6_SP = 15

    # Choice options must define an explicit default value.
    default = option_case_4_1

class Cases(OptionSet):
    """
    All cases enabled for this APWorld. Starting Case and Victory Case will be added if they are not included.
    """

    display_name = "Enabled Cases"

    valid_keys_casefold = False

    valid_keys = [
        "all",
        "Case 4-1",
        "Case 4-2",
        "Case 4-3",
        "Case 4-4",
        "Case 5-1",
        "Case 5-2",
        "Case 5-3",
        "Case 5-4",
        "Case 5-5",
        "Case 5-SP",
        "Case 6-1",
        "Case 6-2",
        "Case 6-3",
        "Case 6-4",
        "Case 6-5",
        "Case 6-SP"
    ]

    default = ["all"]


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class AceAttorneyOptions(PerGameCommonOptions):
    profile_sanity: Profilesanity
    start_case: StartCase
    victory_case: VictoryCase
    lock_locations: LockLocations
    cases: Cases


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Case Options",
        [StartCase, VictoryCase, Cases],
    ),
    OptionGroup(
        "Item Options",
        [LockLocations, Profilesanity],
    ),
]
