# Script for all characters.

# Kouda_Ha's premade Character sprites for all Nairda Nun games.

# Defaulting answers to 0 at start of game, choices matter for good and/or bad endings.
default correct = 0

# Character List

# Narrator / The Game Developer (fourth-wall breaking character)
define gamedev = Character("Game Dev")

# Main Character, Nairda Nun
define nun = Character("Nairda Nun", color="#99C68E") #nun, frog green

# Main Character, Husband of Nun
define snun = Character("Strudle", color="#FF0000")#Red

# Apartment neighbour/s, Next door neighbour
define tony = Character("Tony", color="#FF0000")#Red

# Side Character, Fry the Pizza Guy
define fry = Character("Fry", color="#DBA87F") #Pizza crust colour

# images for characters and facial expressions
# General expressions:
# - neutral face
# - sad/crying
# - happy
# - angry
# - confused
# - embarrassed/shy

# Nun (Main Character)
image nun n:
    "nunneutral"
    zoom 0.5
image nun sad:
    "nunsad"
    zoom 0.5
image nun happy:
    "nunhappy"
    zoom 0.5
image nun angry:
    "nunangry"
    zoom 0.5
image nun confused:
    "nunconfused"
    zoom 0.5
image nun shy:
    "nunshy"
    zoom 0.5

# Strudle Nun (Nairda's husband)
image snun n:
    "snunneutral"
    zoom 0.5
image snun sad:
    "snunsad"
    zoom 0.5
image snun happy:
    "snunhappy"
    zoom 0.5
image snun angry:
    "snunangry"
    zoom 0.5
image snun confused:
    "snunconfused"
    zoom 0.5
image snun shy:
    "snunshy"
    zoom 0.5

# Tony (apartment neighbour)
image tony n:
    "tonyneutral"
    zoom 0.5
image tony sad:
    "tonysad"
    zoom 0.5
image tony happy:
    "tonyhappy"
    zoom 0.5
image tony angry:
    "tonyangry"
    zoom 0.5
image tony confused:
    "tonyconfused"
    zoom 0.5
image tony shy:
    "tonyshy"
    zoom 0.5

# Fry (Pizza guy)
image fry n:
    "fryn"
    zoom 0.5
image fry sad:
    "frysad"
    zoom 0.5
image fry happy:
    "fryhappy"
    zoom 0.5
image fry angry:
    "fryangry"
    zoom 0.5
image fry confused:
    "fryconfused"
    zoom 0.5
image fry shy:
    "fryshy"
    zoom 0.5

# MISC ITEMS - All game scenes are in 1280 x 720, resize accordingly
image PC PC:
    "pc"
    zoom 0.5
