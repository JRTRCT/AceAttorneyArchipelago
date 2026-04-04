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
    "case_4_1": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 0,
            "Starting Evidence: Smith's Autopsy Report": 1,
            "Starting Evidence: Crime Photo 1": 2,
            "Obtain Evidence: Deadly Bottle": 3,
            "Obtain Evidence: Wright's Cell Phone": 8,
            "Obtain Evidence: Olga's Photo": 9,
            "Contradiction: The Competition": 10,
            "Obtain Evidence: Chips Photo": 12,
            "Obtain Evidence: Crime Photo 2": 13,
            "Contradiction: That Fateful Night (Olga)": 14,
            "Contradiction: That Fateful Night (Olga) 2": 15,
            "Contradiction: Serious Competition": 16,
            "Obtain Evidence: Victim's Hand": 17,
            "Contradiction: The Final Hand": 18,
            "Percieve: The Best Laid Traps": 19,
            "Obtain Evidence: Bloody Ace": 20,
            "Contradiction: Appetite Before Murder": 21,
            "Contradiction: That Fateful Night (Kristoph)": 22,
            "Present Evidence: Bloody Ace": 23,
            "Finish Case: 4-1": 24
        },
        "profile_locations": {
            "Starting Profile: Kristoph Gavin": 4,
            "Starting Profile: Phoenix Wright": 5,
            "Starting Profile: Shadi Smith": 6,
            "Obtain Profile: Winston Payne": 7,
            "Obtain Profile: Olga Orly": 11
        }
    },
    "case_4_2": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 25,
            "Obtain Evidence: Map": 27,
            "Obtain Evidence: Bowl": 31,
            "Obtain Evidence: Trucy's Evidence": 32,
            "Obtain Evidence: Cell Phone": 33,
            "Obtain Evidence: Mirror": 34,
            "Obtain Evidence: Fingerprint Powder": 38,
            "Obtain Evidence: Meraktis's Autopsy Report": 39,
            "Obtain Evidence: Knife": 40,
            "Obtain Evidence: Noodle Stand": 41,
            "Obtain Evidence: Plum's Evidence": 42,
            "Obtain Evidence: Wocky's Check-Up Report": 47,
            "Obtain Evidence: Pistol": 49,
            "Contradiction: A Night in the Park": 50,
            "Contradiction: A Night in the Park 2": 51,
            "Percieve: From Shot to Call": 52,
            "Contradiction: Stickler's \"Truth\"": 53,
            "Obtain Evidence: Slippers": 54,
            "Obtain Evidence: Detective Skye's Orders": 55,
            "Obtain Evidence: Alita's Sandles": 56,
            "Obtain Evidence: Lamp": 57,
            "Obtain Evidence: Wocky's Chart": 58,
            "Obtain Evidence: Bullet": 59,
            "Contradiction: Wocky's Plan": 60,
            "Contradiction: The Meraktis Clinic": 61,
            "Contradiction: The Meraktis Clinic 2": 62,
            "Percieve: Tiala's Explanation": 63,
            "Present: Wocky's Check-Up Report": 64,
            "Finish Case: 4-2": 65
        },
        "profile_locations": {
            "Starting Profile: Phoenix Wright": 26,
            "Obtain Profile: Trucy Wright": 28,
            "Obtain Profile: Dr. Hickfield": 29,
            "Obtain Profile: Guy Eldoon": 30,
            "Obtain Profile: Plum Kitaki": 35,
            "Obtain Profile: Alita Tiala": 36,
            "Obtain Profile: Ema Skye": 37,
            "Obtain Profile: Klavier Gavin": 43,
            "Obtain Profile: Winfred Kitaki": 44,
            "Obtain Profile: Wocky Kitaki": 45,
            "Obtain Profile: Pal Meraktis": 46,
            "Obtain Profile: Wesley Stickler": 48
        }
    },
    "case_4_3": {
        "locations": {
            "Starting Evidence: Attorney's Badge (Justice)": 66,
            "Obtain Evidence: Lyrics Sheet": 67,
            "Obtain Evidence: Investigation Request": 74,
            "Obtain Evidence: Revolver": 75,
            "Obtain Evidence: Brooch": 76,
            "Obtain Evidence: Key Ring": 77,
            "Obtain Evidence: Mixing Board": 78,
            "Obtain Evidence: LeTouse's Autopsy Report": 81,
            "Obtain Evidence: Crime Photo": 82,
            "Obtain Evidence: Diagram": 83,
            "Contradiction: Murderous Circumstances": 84,
            "Percieve: What I Saw": 85,
            "Contradiction: What I Saw 2": 86,
            "Contradiction: The Missing Body": 87,
            "Obtain Evidence: Video Tape": 88,
            "Obtain Evidence: Headset": 90,
            "Obtain Evidence: igniter": 91,
            "Obtain Evidence: Remote Trigger": 92,
            "Obtain Evidence: Forum Diagram": 93,
            "Obtain Evidence: Borginian Newspaper": 94,
            "Obtain Evidence: Replica": 95,
            "Obtain Evidence: Prosecutor Gavin's Guitar": 96,
            "Obtain Evidence: Newspaper Article": 97,
            "Percieve: Proof of Innocence": 98,
            "Contradiction: What I Heard": 99,
            "Contradiction: Above the Ceiling": 100,
            "Contradiction: The Big Illusion": 101,
            "Obtain Evidence: Burnt Fragments": 102,
            "Contradiction: Daryan's Rebuttal": 103,
            "Contradiction: Proof of Innocence": 104,
            "Contradiction: Cocoon Smuggling": 105,
            "Finish Case: 4-3": 106
        },
        "profile_locations": {
            "Starting Profile: Phoenix Wright": 68,
            "Starting Profile: Trucy Wright": 69,
            "Starting Profile: Klavier Gavin": 70,
            "Obtain Profile: LeTouse": 71,
            "Obtain Profile: Lamiroir": 72,
            "Obtain Profile: Machi Tobaye": 73,
            "Obtain Profile: Ema Skye": 79,
            "Obtain Profile: Daryan Crescend": 80,
            "Obtain Profile: Valant Gramarye": 89
        }
    },
    "case_4_4": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 107,
            "Obtain Evidence: Magic Show Ticket": 110,
            "Obtain Evidence: Gramarye Envelope": 111,
            "Obtain Evidence: Vera's Card": 112,
            "Obtain Evidence: Coffee Cup": 113,
            "Obtain Evidence: Hidden Painting": 114,
            "Obtain Evidence: Red Envelope": 115,
            "Obtain Evidence: Letter Box": 116,
            "Obtain Evidence: Tiny Frame": 117,
            "Obtain Evidence: Portrait": 118,
            "Obtain Evidence: Acrylic": 119,
            "Obtain Evidence: Landscape": 120,
            "Obtain Evidence: Drew's Autopsy Report": 126,
            "Contradiction: The Journalist's Story": 128,
            "Contradiction: What Brushel Noticed": 129,
            "Percieve: The Scent of A Story": 130,
            "Contradiction: The Interview: A Recap": 131,
            "Contradiction: The Red Envelope": 132,
            "Starting Evidence: Attorney's Badge (Wright)": 133,
            "Starting Evidence: Crime Scene Photo": 134,
            "Starting Evidence: Magnifi's Autopsy Report": 135,
            "Obtain Evidence: Notebook Page": 136,
            "Obtain Evidence: Magnifi's Chart": 137,
            "Obtain Evidence: Small Syringe": 138,
            "Obtain Evidence: Magnifi's First Letter": 144,
            "Obtain Evidence: Stage Profile": 145,
            "Contradiction: The Circumstances": 146,
            "Obtain Evidence: Magnifi's Second Letter": 147,
            "Contradiction: The Night of the Crime": 149,
            "Obtain Evidence: IV Report": 150,
            "Obtain Evidence: Magnifi's Diary": 151,
            "Contradiction: Who Shot What": 152,
            "Obtain Evidence: The Amazing Mr. Hat": 153,
            "Obtain Evidence: Transferral of Rights": 154,
            "Obtain Evidence: Nail Polish": 155,
            "Obtain Evidence: Commemorative Stamp": 156,
            "Obtain Evidence: Portrait of Thalassa": 157,
            "Obtain Evidence: Zak's Confession": 164,
            "Obtain Evidence: Letter from Misham": 165,
            "Percieve: Poisoning Vera": 166,
            "Finish Case: 4-4": 167
        },
        "profile_locations": {
            "Starting Profile: Phoenix Wright": 108,
            "Starting Profile: Trucy Wright": 109,
            "Obtain Profile: Vera Misham": 163,
            "Obtain Profile: Ema Skye": 122,
            "Obtain Profile: Drew Misham": 123,
            "Obtain Profile: Valant Gramarye": 124,
            "Obtain Profile: Spark Brushel": 162,
            "Obtain Profile: Klavier Gavin": 127,
            "Starting Profile: Shadi Enigmar": 139,
            "Starting Profile: Magnifi Gramarye": 140,
            "Obtain Profile: Trucy Enigmar": 141,
            "Obtain Profile: Klavier Gavin (7 Years Ago)": 142,
            "Obtain Profile: Dick Gumshoe": 143,
            "Obtain Profile: Valant Gramarye (7 Years Ago)": 148,
            "Starting Profile: Apollo": 158,
            "Starting Profile: Kristoph Gavin": 159,
            "Obtain Profile: Thalassa Gramarye": 160,
            "Obtain Profile: Mike Meekens": 161
        }
    },
    "case_5_1": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 168,
            "Obtain Evidence: Arme's Autopsy Report": 169,
            "Obtain Evidence: Stuffed Animal Bomb": 170,
            "Obtain Evidence: Phony Phanty Tail": 171,
            "Obtain Evidence: Bomb Transport Case": 177,
            "Obtain Evidence: Missing Remote Switch": 178,
            "Contradiction: When the Bomb Went Off (Tonate)": 179,
            "Pinpoint: When the Bomb Went Off": 181,
            "Contradiction: When the Bomb Went Off (Woods)": 182,
            "Obtain Evidence: Courtroom No. 4 Diagram": 183,
            "Obtain Evidence: Apollo's Assault Photo": 184,
            "Contradiction: Alone with Apollo": 185,
            "Obtain Evidence: Courtroom Bombing Photo": 186,
            "Obtain Evidence: Bloody Writing Analysis": 187,
            "Contradiction: After the Explosion": 188,
            "Contradiction: The Truth": 189,
            "Present: Missing Remote Switch": 190,
            "Finish Case: 5-1": 191
        },
        "profile_locations": {
            "Starting Profile: Apollo Justice": 172,
            "Starting Profile: Juniper Woods": 173,
            "Starting Profile: Gaspen Payne": 174,
            "Starting Profile: Candice Arme": 175,
            "Obtain Profile: Athena Cykes": 176,
            "Obtain Profile: Ted Tonate": 180
        }
    },
    "case_5_2": {
        "locations": {
            "Starting Evidence: Attorney's Badge": 192,
            "Obtain Evidence: Yokai Legend Scroll": 193,
            "Obtain Evidence: Tenma Taro Warding Charm": 196,
            "Obtain Evidence: Nine-Tails Flower": 197,
            "Obtain Evidence: Special Edition Paper": 201,
            "Obtain Evidence: Crime Scene Diagram": 202,
            "Obtain Evidence: Foyer Diagram": 203,
            "Obtain Evidence: Fox and Demon Statue": 206,
            "Obtain Evidence: Golden Fur": 207,
            "Obtain Evidence: Crime Photo": 209,
            "Obtain Evidence: Amazing Nine-Tails Mask": 210,
            "Obtain Evidence: Amazing Nine-Tails Glossy": 211,
            "Obtain Evidence: Jinxie's Statement": 213,
            "Obtain Evidence: TV Listings": 214,
            "Obtain Evidence: Kyubi's Autopsy Report": 217,
            "Obtain Evidence: Blckmail Letter": 218,
            "Contradiction: About the Murder": 219,
            "Contradiction: Feathers and Tracks": 220,
            "Obtain Evidence: Villiage Superstitions": 221,
            "Contradiction: Guarding the Foyer": 222,
            "Contradiction: Ears Working Overtime": 223,
            "Pinpoint: What Jinxie Saw": 224,
            "Obtain Evidence: Forbidden Chamber Key": 225,
            "Obtain Evidence: Couleur Me L'Belle": 226,
            "Obtain Evidence: Azuki Kozo Statue": 227,
            "Obtain Evidence: Hand Cream": 228,
            "Contradiction: The Yokai Is Jinxie": 229,
            "Contradiction: What L'Belle Saw": 230,
            "Contradiction: In the Fox Chamber": 231,
            "Pinpoint: The Ruler of Demonkind": 232,
            "Contradiction: The Ruler of Demonkind": 233,
            "Contradiction: The Amazing Nine-Tails's True Identity": 234,
            "Present: Amazing Nine-Tails Mask": 235,
            "Finish Case: 5-2": 236
        },
        "profile_locations": {
            "Starting Profile: Trucy Wright": 194,
            "Obtain Profile: Jinxie Tenma": 195,
            "Obtain Profile: The Amazing Nine-Tails": 198,
            "Obtain Profile: Damian Tenma": 199,
            "Obtain Profile: Rex Kyubi": 200,
            "Obtain Profile: Athena Cykes": 204,
            "Obtain Profile: Phineas Filch": 205,
            "Obtain Profile: Bobby Fulbright": 208,
            "Obtain Profile: Florent L'Belle": 212,
            "Obtain Profile: Phoenix Wright": 215,
            "Obtain Profile: Simon Blackquill": 216
        }
    },
    "case_5_3": {
        "locations": {},
        "profile_locations": {}
    },
    "case_5_4": {
        "locations": {},
        "profile_locations": {}
    },
    "case_5_5": {
        "locations": {},
        "profile_locations": {}
    },
    "case_5_SP": {
        "locations": {},
        "profile_locations": {}
    },
    "case_6_1": {
        "locations": {},
        "profile_locations": {}
    },
    "case_6_2": {
        "locations": {},
        "profile_locations": {}
    },
    "case_6_3": {
        "locations": {},
        "profile_locations": {}
    },
    "case_6_4": {
        "locations": {},
        "profile_locations": {}
    },
    "case_6_5": {
        "locations": {},
        "profile_locations": {}
    },
    "case_6_SP": {
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
