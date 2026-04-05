from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import AceAttorneyWorld

from .regions import CASES, prettify_case_string

import functools

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID: Dict[str, Dict[str, Dict[str, int]]] = {
    "4-1": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 1,
            "Starting Evidence: Smith's Autopsy Report": 2,
            "Starting Evidence: Crime Photo 1": 3,
            "Obtain Evidence: Deadly Bottle": 4,
            "Obtain Evidence: Wright's Cell Phone": 9,
            "Obtain Evidence: Olga's Photo": 10,
            "Contradiction: The Competition": 11,
            "Obtain Evidence: Chips Photo": 13,
            "Obtain Evidence: Crime Photo 2": 14,
            "Contradiction: That Fateful Night (Olga)": 15,
            "Contradiction: That Fateful Night (Olga) 2": 16,
            "Contradiction: Serious Competition": 17,
            "Obtain Evidence: Victim's Hand": 18,
            "Contradiction: The Final Hand": 19,
            "Percieve: The Best Laid Traps": 20,
            "Obtain Evidence: Bloody Ace": 21,
            "Contradiction: Appetite Before Murder": 22,
            "Contradiction: That Fateful Night (Kristoph)": 23,
            "Present Evidence: Bloody Ace": 24,
            "Finish Case: 4-1": 25
        },
        "profile_locations": {
            "Starting Profile: Kristoph Gavin": 5,
            "Starting Profile: Phoenix Wright": 6,
            "Starting Profile: Shadi Smith": 7,
            "Obtain Profile: Winston Payne": 8,
            "Obtain Profile: Olga Orly": 12
        }
    },
    "4-2": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 26,
            "Obtain Evidence: Map": 28,
            "Obtain Evidence: Bowl": 32,
            "Obtain Evidence: Trucy's Evidence": 33,
            "Obtain Evidence: Cell Phone": 34,
            "Obtain Evidence: Mirror": 35,
            "Obtain Evidence: Fingerprint Powder": 39,
            "Obtain Evidence: Meraktis's Autopsy Report": 40,
            "Obtain Evidence: Knife": 41,
            "Obtain Evidence: Noodle Stand": 42,
            "Obtain Evidence: Plum's Evidence": 43,
            "Obtain Evidence: Wocky's Check-Up Report": 48,
            "Obtain Evidence: Pistol": 50,
            "Contradiction: A Night in the Park": 51,
            "Contradiction: A Night in the Park 2": 52,
            "Percieve: From Shot to Call": 53,
            "Contradiction: Stickler's \"Truth\"": 54,
            "Obtain Evidence: Slippers": 55,
            "Obtain Evidence: Detective Skye's Orders": 56,
            "Obtain Evidence: Alita's Sandles": 57,
            "Obtain Evidence: Lamp": 58,
            "Obtain Evidence: Wocky's Chart": 59,
            "Obtain Evidence: Bullet": 60,
            "Contradiction: Wocky's Plan": 61,
            "Contradiction: The Meraktis Clinic": 62,
            "Contradiction: The Meraktis Clinic 2": 63,
            "Percieve: Tiala's Explanation": 64,
            "Present: Wocky's Check-Up Report": 65,
            "Finish Case: 4-2": 66
        },
        "profile_locations": {
            "Starting Profile: Phoenix Wright": 27,
            "Obtain Profile: Trucy Wright": 29,
            "Obtain Profile: Dr. Hickfield": 30,
            "Obtain Profile: Guy Eldoon": 31,
            "Obtain Profile: Plum Kitaki": 36,
            "Obtain Profile: Alita Tiala": 37,
            "Obtain Profile: Ema Skye": 38,
            "Obtain Profile: Klavier Gavin": 44,
            "Obtain Profile: Winfred Kitaki": 45,
            "Obtain Profile: Wocky Kitaki": 46,
            "Obtain Profile: Pal Meraktis": 47,
            "Obtain Profile: Wesley Stickler": 49
        }
    },
    "4-3": {
        "locations": {
            "Starting Evidence: Attorney's Badge (Justice)": 67,
            "Obtain Evidence: Lyrics Sheet": 68,
            "Obtain Evidence: Investigation Request": 75,
            "Obtain Evidence: Revolver": 76,
            "Obtain Evidence: Brooch": 77,
            "Obtain Evidence: Key Ring": 78,
            "Obtain Evidence: Mixing Board": 79,
            "Obtain Evidence: LeTouse's Autopsy Report": 82,
            "Obtain Evidence: Crime Photo": 83,
            "Obtain Evidence: Diagram": 84,
            "Contradiction: Murderous Circumstances": 85,
            "Percieve: What I Saw": 86,
            "Contradiction: What I Saw 2": 87,
            "Contradiction: The Missing Body": 88,
            "Obtain Evidence: Video Tape": 89,
            "Obtain Evidence: Headset": 91,
            "Obtain Evidence: igniter": 92,
            "Obtain Evidence: Remote Trigger": 93,
            "Obtain Evidence: Forum Diagram": 94,
            "Obtain Evidence: Borginian Newspaper": 95,
            "Obtain Evidence: Replica": 96,
            "Obtain Evidence: Prosecutor Gavin's Guitar": 97,
            "Obtain Evidence: Newspaper Article": 98,
            "Percieve: Proof of Innocence": 99,
            "Contradiction: What I Heard": 100,
            "Contradiction: Above the Ceiling": 101,
            "Contradiction: The Big Illusion": 102,
            "Obtain Evidence: Burnt Fragments": 103,
            "Contradiction: Daryan's Rebuttal": 104,
            "Contradiction: Proof of Innocence": 105,
            "Contradiction: Cocoon Smuggling": 106,
            "Finish Case: 4-3": 107
        },
        "profile_locations": {
            "Starting Profile: Phoenix Wright": 69,
            "Starting Profile: Trucy Wright": 70,
            "Starting Profile: Klavier Gavin": 71,
            "Obtain Profile: LeTouse": 72,
            "Obtain Profile: Lamiroir": 73,
            "Obtain Profile: Machi Tobaye": 74,
            "Obtain Profile: Ema Skye": 80,
            "Obtain Profile: Daryan Crescend": 81,
            "Obtain Profile: Valant Gramarye": 90
        }
    },
    "4-4": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 108,
            "Obtain Evidence: Magic Show Ticket": 111,
            "Obtain Evidence: Gramarye Envelope": 112,
            "Obtain Evidence: Vera's Card": 113,
            "Obtain Evidence: Coffee Cup": 114,
            "Obtain Evidence: Hidden Painting": 115,
            "Obtain Evidence: Red Envelope": 116,
            "Obtain Evidence: Letter Box": 117,
            "Obtain Evidence: Tiny Frame": 118,
            "Obtain Evidence: Portrait": 119,
            "Obtain Evidence: Acrylic": 120,
            "Obtain Evidence: Landscape": 121,
            "Obtain Evidence: Drew's Autopsy Report": 127,
            "Contradiction: The Journalist's Story": 129,
            "Contradiction: What Brushel Noticed": 130,
            "Percieve: The Scent of A Story": 131,
            "Contradiction: The Interview: A Recap": 132,
            "Contradiction: The Red Envelope": 133,
            "Starting Evidence: Attorney's Badge (Wright)": 134,
            "Starting Evidence: Crime Scene Photo": 135,
            "Starting Evidence: Magnifi's Autopsy Report": 136,
            "Obtain Evidence: Notebook Page": 137,
            "Obtain Evidence: Magnifi's Chart": 138,
            "Obtain Evidence: Small Syringe": 139,
            "Obtain Evidence: Magnifi's First Letter": 145,
            "Obtain Evidence: Stage Profile": 146,
            "Contradiction: The Circumstances": 147,
            "Obtain Evidence: Magnifi's Second Letter": 148,
            "Contradiction: The Night of the Crime": 150,
            "Obtain Evidence: IV Report": 151,
            "Obtain Evidence: Magnifi's Diary": 152,
            "Contradiction: Who Shot What": 153,
            "Obtain Evidence: The Amazing Mr. Hat": 154,
            "Obtain Evidence: Transferral of Rights": 155,
            "Obtain Evidence: Nail Polish": 156,
            "Obtain Evidence: Commemorative Stamp": 157,
            "Obtain Evidence: Portrait of Thalassa": 158,
            "Obtain Evidence: Zak's Confession": 165,
            "Obtain Evidence: Letter from Misham": 166,
            "Percieve: Poisoning Vera": 167,
            "Finish Case: 4-4": 168
        },
        "profile_locations": {
            "Starting Profile: Phoenix Wright": 109,
            "Starting Profile: Trucy Wright": 110,
            "Obtain Profile: Vera Misham": 164,
            "Obtain Profile: Ema Skye": 123,
            "Obtain Profile: Drew Misham": 124,
            "Obtain Profile: Valant Gramarye": 125,
            "Obtain Profile: Spark Brushel": 163,
            "Obtain Profile: Klavier Gavin": 128,
            "Starting Profile: Shadi Enigmar": 140,
            "Starting Profile: Magnifi Gramarye": 141,
            "Obtain Profile: Trucy Enigmar": 142,
            "Obtain Profile: Klavier Gavin (7 Years Ago)": 143,
            "Obtain Profile: Dick Gumshoe": 144,
            "Obtain Profile: Valant Gramarye (7 Years Ago)": 149,
            "Starting Profile: Apollo": 159,
            "Starting Profile: Kristoph Gavin": 160,
            "Obtain Profile: Thalassa Gramarye": 161,
            "Obtain Profile: Mike Meekens": 162
        }
    },
    "5-1": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 169,
            "Obtain Evidence: Arme's Autopsy Report": 170,
            "Obtain Evidence: Stuffed Animal Bomb": 171,
            "Obtain Evidence: Phony Phanty Tail": 172,
            "Obtain Evidence: Bomb Transport Case": 178,
            "Obtain Evidence: Missing Remote Switch": 179,
            "Contradiction: When the Bomb Went Off (Tonate)": 180,
            "Pinpoint: When the Bomb Went Off": 182,
            "Contradiction: When the Bomb Went Off (Woods)": 183,
            "Obtain Evidence: Courtroom No. 4 Diagram": 184,
            "Obtain Evidence: Apollo's Assault Photo": 185,
            "Contradiction: Alone with Apollo": 186,
            "Obtain Evidence: Courtroom Bombing Photo": 187,
            "Obtain Evidence: Bloody Writing Analysis": 188,
            "Contradiction: After the Explosion": 189,
            "Contradiction: The Truth": 190,
            "Present: Missing Remote Switch": 191,
            "Finish Case: 5-1": 192
        },
        "profile_locations": {
            "Starting Profile: Apollo Justice": 173,
            "Starting Profile: Juniper Woods": 174,
            "Starting Profile: Gaspen Payne": 175,
            "Starting Profile: Candice Arme": 176,
            "Obtain Profile: Athena Cykes": 177,
            "Obtain Profile: Ted Tonate": 181
        }
    },
    "5-2": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 193,
            "Obtain Evidence: Yokai Legend Scroll": 194,
            "Obtain Evidence: Tenma Taro Warding Charm": 197,
            "Obtain Evidence: Nine-Tails Flower": 198,
            "Obtain Evidence: Special Edition Paper": 202,
            "Obtain Evidence: Crime Scene Diagram": 203,
            "Obtain Evidence: Foyer Diagram": 204,
            "Obtain Evidence: Fox and Demon Statue": 207,
            "Obtain Evidence: Golden Fur": 208,
            "Obtain Evidence: Crime Photo": 210,
            "Obtain Evidence: Amazing Nine-Tails Mask": 211,
            "Obtain Evidence: Amazing Nine-Tails Glossy": 212,
            "Obtain Evidence: Jinxie's Statement": 214,
            "Obtain Evidence: TV Listings": 215,
            "Obtain Evidence: Kyubi's Autopsy Report": 218,
            "Obtain Evidence: Blckmail Letter": 219,
            "Contradiction: About the Murder": 220,
            "Contradiction: Feathers and Tracks": 221,
            "Obtain Evidence: Villiage Superstitions": 222,
            "Contradiction: Guarding the Foyer": 223,
            "Contradiction: Ears Working Overtime": 224,
            "Pinpoint: What Jinxie Saw": 225,
            "Obtain Evidence: Forbidden Chamber Key": 226,
            "Obtain Evidence: Couleur Me L'Belle": 227,
            "Obtain Evidence: Azuki Kozo Statue": 228,
            "Obtain Evidence: Hand Cream": 229,
            "Contradiction: The Yokai Is Jinxie": 230,
            "Contradiction: What L'Belle Saw": 231,
            "Contradiction: In the Fox Chamber": 232,
            "Pinpoint: The Ruler of Demonkind": 233,
            "Contradiction: The Ruler of Demonkind": 234,
            "Contradiction: The Amazing Nine-Tails's True Identity": 235,
            "Present: Amazing Nine-Tails Mask": 236,
            "Finish Case: 5-2": 237
        },
        "profile_locations": {
            "Starting Profile: Trucy Wright": 195,
            "Obtain Profile: Jinxie Tenma": 196,
            "Obtain Profile: The Amazing Nine-Tails": 199,
            "Obtain Profile: Damian Tenma": 200,
            "Obtain Profile: Rex Kyubi": 201,
            "Obtain Profile: Athena Cykes": 205,
            "Obtain Profile: Phineas Filch": 206,
            "Obtain Profile: Bobby Fulbright": 209,
            "Obtain Profile: Florent L'Belle": 213,
            "Obtain Profile: Phoenix Wright": 216,
            "Obtain Profile: Simon Blackquill": 217
        }
    },
    "5-3": {
        "locations": {},
        "profile_locations": {}
    },
    "5-4": {
        "locations": {},
        "profile_locations": {}
    },
    "5-5": {
        "locations": {},
        "profile_locations": {}
    },
    "5-SP": {
        "locations": {},
        "profile_locations": {}
    },
    "6-1": {
        "locations": {},
        "profile_locations": {}
    },
    "6-2": {
        "locations": {},
        "profile_locations": {}
    },
    "6-3": {
        "locations": {},
        "profile_locations": {}
    },
    "6-4": {
        "locations": {},
        "profile_locations": {}
    },
    "6-5": {
        "locations": {},
        "profile_locations": {}
    },
    "6-SP": {
        "locations": {},
        "profile_locations": {}
    }
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class AceAttorneyLocation(Location):
    game = "Ace Attorney"

@functools.cache
def location_name_to_id() -> Dict[str, int]:
    res = {}
    for region in CASES:
        res.update({f"{prettify_case_string(region)}: {loc}":id for loc, id in LOCATION_NAME_TO_ID[region]["locations"].items()})
        res.update({f"{prettify_case_string(region)}: {loc}":id for loc, id in LOCATION_NAME_TO_ID[region]["profile_locations"].items()})
    return res

def create_all_locations(world: AceAttorneyWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: AceAttorneyWorld) -> None:

    for region in CASES:
        if region in world.options.cases.value:
            world.get_region(region).add_locations({f"{prettify_case_string(region)}: {loc}":id for loc, id in LOCATION_NAME_TO_ID[region]["locations"].items()}, AceAttorneyLocation)
            if world.options.profile_sanity:
                world.get_region(region).add_locations({f"{prettify_case_string(region)}: {loc}":id for loc, id in LOCATION_NAME_TO_ID[region]["profile_locations"].items()}, AceAttorneyLocation)
    



def create_events(world: AceAttorneyWorld) -> None:

    final_case: str = prettify_case_string(world.options.victory_case.current_key)
    victory_location = world.get_location(f"{final_case}: Finish Case: {final_case}")
    victory_item = items.AceAttorneyItem("Victory", ItemClassification.progression, None, world.player)
    victory_location.place_locked_item(victory_item)
