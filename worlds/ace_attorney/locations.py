from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import AceAttorneyWorld

from .regions import CASES

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
            "Obtain Evidence: Postcard": 68,
            "Obtain Evidence: Lyrics Sheet": 69,
            "Obtain Evidence: Investigation Request": 76,
            "Obtain Evidence: Revolver": 77,
            "Obtain Evidence: Brooch": 78,
            "Obtain Evidence: Key Ring": 79,
            "Obtain Evidence: Mixing Board": 80,
            "Obtain Evidence: LeTouse's Autopsy Report": 83,
            "Obtain Evidence: Crime Photo": 84,
            "Obtain Evidence: Diagram": 85,
            "Contradiction: Murderous Circumstances": 86,
            "Percieve: What I Saw": 87,
            "Contradiction: What I Saw 2": 88,
            "Contradiction: The Missing Body": 89,
            "Obtain Evidence: Video Tape": 90,
            "Obtain Evidence: Headset": 92,
            "Obtain Evidence: igniter": 93,
            "Obtain Evidence: Remote Trigger": 94,
            "Obtain Evidence: Forum Diagram": 95,
            "Obtain Evidence: Borginian Newspaper": 96,
            "Obtain Evidence: Replica": 97,
            "Obtain Evidence: Prosecutor Gavin's Guitar": 98,
            "Obtain Evidence: Newspaper Article": 99,
            "Percieve: Proof of Innocence": 100,
            "Contradiction: What I Heard": 101,
            "Contradiction: Above the Ceiling": 102,
            "Contradiction: The Big Illusion": 103,
            "Obtain Evidence: Burnt Fragments": 104,
            "Contradiction: Daryan's Rebuttal": 105,
            "Contradiction: Proof of Innocence": 106,
            "Contradiction: Cocoon Smuggling": 107,
            "Finish Case: 4-3": 108
        },
        "profile_locations": {
            "Starting Profile: Phoenix Wright": 70,
            "Starting Profile: Trucy Wright": 71,
            "Starting Profile: Klavier Gavin": 72,
            "Obtain Profile: LeTouse": 73,
            "Obtain Profile: Lamiroir": 74,
            "Obtain Profile: Machi Tobaye": 75,
            "Obtain Profile: Ema Skye": 81,
            "Obtain Profile: Daryan Crescend": 82,
            "Obtain Profile: Valant Gramarye": 91
        }
    },
    "4-4": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 109,
            "Obtain Evidence: Magic Show Ticket": 112,
            "Obtain Evidence: Gramarye Envelope": 113,
            "Obtain Evidence: Vera's Card": 114,
            "Obtain Evidence: Coffee Cup": 115,
            "Obtain Evidence: Hidden Painting": 116,
            "Obtain Evidence: Red Envelope": 117,
            "Obtain Evidence: Letter Box": 118,
            "Obtain Evidence: Tiny Frame": 119,
            "Obtain Evidence: Portrait": 120,
            "Obtain Evidence: Acrylic": 121,
            "Obtain Evidence: Landscape": 122,
            "Obtain Evidence: Drew's Autopsy Report": 128,
            "Contradiction: The Journalist's Story": 130,
            "Contradiction: What Brushel Noticed": 131,
            "Percieve: The Scent of A Story": 132,
            "Contradiction: The Interview: A Recap": 133,
            "Contradiction: The Red Envelope": 134,
            "Starting Evidence: Attorney's Badge (Wright)": 135,
            "Starting Evidence: Crime Scene Photo": 136,
            "Starting Evidence: Magnifi's Autopsy Report": 137,
            "Obtain Evidence: Notebook Page": 138,
            "Obtain Evidence: Magnifi's Chart": 139,
            "Obtain Evidence: Small Syringe": 140,
            "Obtain Evidence: Magnifi's First Letter": 146,
            "Obtain Evidence: Stage Profile": 147,
            "Contradiction: The Circumstances": 148,
            "Obtain Evidence: Magnifi's Second Letter": 149,
            "Contradiction: The Night of the Crime": 151,
            "Obtain Evidence: IV Report": 152,
            "Obtain Evidence: Magnifi's Diary": 153,
            "Contradiction: Who Shot What": 154,
            "Obtain Evidence: The Amazing Mr. Hat": 155,
            "Obtain Evidence: Transferral of Rights": 156,
            "Obtain Evidence: Nail Polish": 157,
            "Obtain Evidence: Commemorative Stamp": 158,
            "Obtain Evidence: Portrait of Thalassa": 159,
            "Obtain Evidence: Zak's Confession": 166,
            "Obtain Evidence: Letter from Misham": 167,
            "Percieve: Poisoning Vera": 168,
            "Finish Case: 4-4": 169
        },
        "profile_locations": {
            "Starting Profile: Phoenix Wright": 110,
            "Starting Profile: Trucy Wright": 111,
            "Obtain Profile: Vera Misham": 165,
            "Obtain Profile: Ema Skye": 124,
            "Obtain Profile: Drew Misham": 125,
            "Obtain Profile: Valant Gramarye": 126,
            "Obtain Profile: Spark Brushel": 164,
            "Obtain Profile: Klavier Gavin": 129,
            "Starting Profile: Shadi Enigmar": 141,
            "Starting Profile: Magnifi Gramarye": 142,
            "Obtain Profile: Trucy Enigmar": 143,
            "Obtain Profile: Klavier Gavin (7 Years Ago)": 144,
            "Obtain Profile: Dick Gumshoe": 145,
            "Obtain Profile: Valant Gramarye (7 Years Ago)": 150,
            "Starting Profile: Apollo": 160,
            "Starting Profile: Kristoph Gavin": 161,
            "Obtain Profile: Thalassa Gramarye": 162,
            "Obtain Profile: Mike Meekens": 163
        }
    },
    "5-1": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 170,
            "Obtain Evidence: Arme's Autopsy Report": 171,
            "Obtain Evidence: Stuffed Animal Bomb": 172,
            "Obtain Evidence: Phony Phanty Tail": 173,
            "Obtain Evidence: Bomb Transport Case": 179,
            "Obtain Evidence: Missing Remote Switch": 180,
            "Contradiction: When the Bomb Went Off (Tonate)": 181,
            "Pinpoint: When the Bomb Went Off": 183,
            "Contradiction: When the Bomb Went Off (Woods)": 184,
            "Obtain Evidence: Courtroom No. 4 Diagram": 185,
            "Obtain Evidence: Apollo's Assault Photo": 186,
            "Contradiction: Alone with Apollo": 187,
            "Obtain Evidence: Courtroom Bombing Photo": 188,
            "Obtain Evidence: Bloody Writing Analysis": 189,
            "Contradiction: After the Explosion": 190,
            "Contradiction: The Truth": 191,
            "Present: Missing Remote Switch": 192,
            "Finish Case: 5-1": 193
        },
        "profile_locations": {
            "Starting Profile: Apollo Justice": 174,
            "Starting Profile: Juniper Woods": 175,
            "Starting Profile: Gaspen Payne": 176,
            "Starting Profile: Candice Arme": 177,
            "Obtain Profile: Athena Cykes": 178,
            "Obtain Profile: Ted Tonate": 182
        }
    },
    "5-2": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 194,
            "Obtain Evidence: Yokai Legend Scroll": 195,
            "Obtain Evidence: Tenma Taro Warding Charm": 198,
            "Obtain Evidence: Nine-Tails Flower": 199,
            "Obtain Evidence: Special Edition Paper": 203,
            "Obtain Evidence: Crime Scene Diagram": 204,
            "Obtain Evidence: Foyer Diagram": 205,
            "Obtain Evidence: Fox and Demon Statue": 208,
            "Obtain Evidence: Golden Fur": 209,
            "Obtain Evidence: Crime Photo": 211,
            "Obtain Evidence: Amazing Nine-Tails Mask": 212,
            "Obtain Evidence: Amazing Nine-Tails Glossy": 213,
            "Obtain Evidence: Jinxie's Statement": 215,
            "Obtain Evidence: TV Listings": 216,
            "Obtain Evidence: Kyubi's Autopsy Report": 219,
            "Obtain Evidence: Blckmail Letter": 220,
            "Contradiction: About the Murder": 221,
            "Contradiction: Feathers and Tracks": 222,
            "Obtain Evidence: Villiage Superstitions": 223,
            "Contradiction: Guarding the Foyer": 224,
            "Contradiction: Ears Working Overtime": 225,
            "Pinpoint: What Jinxie Saw": 226,
            "Obtain Evidence: Forbidden Chamber Key": 227,
            "Obtain Evidence: Couleur Me L'Belle": 228,
            "Obtain Evidence: Azuki Kozo Statue": 229,
            "Obtain Evidence: Hand Cream": 230,
            "Contradiction: The Yokai Is Jinxie": 231,
            "Contradiction: What L'Belle Saw": 232,
            "Contradiction: In the Fox Chamber": 233,
            "Pinpoint: The Ruler of Demonkind": 234,
            "Contradiction: The Ruler of Demonkind": 235,
            "Contradiction: The Amazing Nine-Tails's True Identity": 236,
            "Present: Amazing Nine-Tails Mask": 237,
            "Finish Case: 5-2": 238
        },
        "profile_locations": {
            "Starting Profile: Trucy Wright": 196,
            "Obtain Profile: Jinxie Tenma": 197,
            "Obtain Profile: The Amazing Nine-Tails": 200,
            "Obtain Profile: Damian Tenma": 201,
            "Obtain Profile: Rex Kyubi": 202,
            "Obtain Profile: Athena Cykes": 206,
            "Obtain Profile: Phineas Filch": 207,
            "Obtain Profile: Bobby Fulbright": 210,
            "Obtain Profile: Florent L'Belle": 214,
            "Obtain Profile: Phoenix Wright": 217,
            "Obtain Profile: Simon Blackquill": 218
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
        res.update({f"{region}: {loc}":id for loc, id in LOCATION_NAME_TO_ID[region]["locations"].items()})
        res.update({f"{region}: {loc}":id for loc, id in LOCATION_NAME_TO_ID[region]["profile_locations"].items()})
    return res

def create_all_locations(world: AceAttorneyWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: AceAttorneyWorld) -> None:

    final_case: str = world.victory_case

    for region in CASES:
        if region in world.cases:
            
            world.get_region(region).add_locations({f"{region}: {loc}":id if loc != f"Finish Case: {final_case}" else None for loc, id in LOCATION_NAME_TO_ID[region]["locations"].items()}, AceAttorneyLocation)
            if world.options.profile_sanity:
                world.get_region(region).add_locations({f"{region}: {loc}":id for loc, id in LOCATION_NAME_TO_ID[region]["profile_locations"].items()}, AceAttorneyLocation)
    



def create_events(world: AceAttorneyWorld) -> None:

    final_case: str = world.victory_case
    victory_location = world.get_location(f"{final_case}: Finish Case: {final_case}")
    victory_item = items.AceAttorneyItem("Victory", ItemClassification.progression, None, world.player)
    victory_location.place_locked_item(victory_item)
