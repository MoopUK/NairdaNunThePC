# The script of the game goes in this file.

# Game Story Draft points:

# SCENE 00: Intro
# Intro to game, explaining it is a mouse only mechanic as it is a Ren'py novel, click to continue story along.

# SCENE 01: Pizza Time
# 2. Nairda and Strudle both get a pizza and head home for some TV

# SCENE 03: Tony starts the letter
# Wake up, Tony has to write a letter to Nairda to thank HIM for buying Tony a PC, but it becomes a jumbled mess of recursion as Tony
# doesn't know how to use a PC very well.

# SCENE 04: Nairda tries to read it at the end, it's very confusing.

# Side plot: Nairda and Strudle doing normal frog things, Tony is avoiding them until the letter is complete


# The game starts here.
label start:
    # SCENE 00: Introduction
    scene apartmentdoor
    show tony n
    tony "The theme is... Recursion! And the limitation is... Mouse Only! Click on the page to move the... story along?"
    "(Tony is mumbling words to himself)"
    scene apartmentdoor
    show tony confused
    tony "Wait? So I just...?"
    gamedev "Yes, you just need to read the teleprompter like you were literally just doing..."
    tony "Ok! I can do that!"
    gamedev "..."
    "(Tony has never made it through an entire introduction without some form of distraction)"
    "(The game developer smiles as genuinely as they can)"
    gamedev "I believe in you, Tony!"
    scene apartmentdoor
    show tony shy
    tony "This is for the game jam, Mini Jam 197: Recursion"
    scene apartmentdoor
    show tony happy
    tony "A story where my BEST FRIEND..."
    "(The teleprompter does not specify their relationship)"
    tony "...Nairda the frog detective, solves ALL THE CRIMES!"
    "(Tony isn't reading the teleprompter. The game developer is putting their hands over their face.)"
    "(At this point the introduction is already a lost cause...)"
    gamedev "Thank you, Tony! You did great."
    show tony shy
    tony "T-thank you! I've never been great at anything before..."
    scene apartmentdoor
    "(And with that, welcome to)"
    "(Nairda Nun... and the PC?)"

    # SCENE 01: Pizza Time
    scene pizza
    show nun n at right
    show snun n at left
    "(The famous Peckish Pizza Shop is reopened and offering 50 percent off!)"
    "(Who could say no to that? Nairda couldn't that's for sure!)"
    nun "One large veggie pizza please, Fry the pizza guy!"
    snun "Could you add some flies to it? If you caught any in the zapper of course"
    "(Fry stops in his tracks and thinks for a moment)"
    scene pizza
    show fry n
    fry "I don't think I'm legally allowed to due to health and safety... I could look up if there's any store bought flies I could buy for
    next time though?"
    scene pizza
    show nun n at right
    show snun sad at left
    snun "Ah... I guess it could be an issue with health and safety. They are delicious though! For frogs at least..."
    show fry happy
    fry "I've never tried them personally, I have a bit of a phobia for foods I can't fillet"
    fry "I'm pretty sure there aren't hands or knives small or sharp enough to do that to most bugs so I skip them altogether"
    scene pizza
    show nun n at right
    show snun sad at left
    show fry sad
    fry "My father always said there's nothing wrong with eatin' bugs but I've alwayss been picky with my food"
    scene pizza
    show fry shy
    fry "I've never been picky with pizza though"
    "(Fry whispers under his breath)"
    fry "G'damn I love pizza..."
    "(He recomposes himself)"
    fry "Anyhow! Here's your pizza!"
    "(Fry hands the pizza over the counter)"
    scene pizza
    show nun happy at right
    show snun happy at left
    nun "Thanks, Fry the pizza guy!"
    "(Leaving the pizza shop Nairda whispers to himself)"
    nun "G'damn I love pizza so much..."
    show snun confused at left
    snun "Hm? Did you say something?"
    nun "Oh nothing, the pizza smells good is all"

    scene pizza
    "(Nairda and Strudle head on home to eat their large veggie pizza without a side of flies)"
    "(And snuggle up onto the sofa to watch their favourite guilty pleasure show on the TV)"

# Maybe a choice for which to watch and a silly sentence about each depending on choice
    "('Pie or die' The guessing game about 'is it pie? or an explosive?' | 'Desperate Frog Lives' | 'The Capybara Royals' | )"

    # SCENE 03: Tony starts the letter
    scene apartmentdoor
    "(Tony stands outside of the apartment doors thinking of how to thank Nairda for their recent write of a computer)"
    show tony confused
    tony "Uh-hmm... T-thank you for the PeeCee"
    tony "Personal cee?"
    show tony shy
    tony "Personal Computer!"
    tony "Or P C for short!"
    "(Tony fumbles)"
    show tony happy
    tony "The P C (*whispering* 'for short') was a great write and I have looked up several log videos!"
    show tony n
    tony "They are videos of water being blocked by tree logs"
    show tony happy
    tony "Spruce is wonferful this time of year!"
    "(He tidies up his shirt)"
    show tony n
    tony "Perfect! I'll just say that!"
    "(His neighbour's door starts to unlock and someone is turning the door handle)"
    show tony sad
    tony "OR I'LL SAY IT LATER!!!"
    scene apartmentdoor
    "(Tony runs back into his apartment, slamming the door shut, hiding from Nairda Nun)"
    show nun n at right
    nun "What was all of that ruckus?"
    "(They look around and see the empty apartment hallway, so still and quiet you could hear a pin drop a mile away)"
    nun "Guess it was nothing..."
    scene apartmentdoor
    "(He closes the door again)"

    scene tonys
    show tony sad
    tony "That was close!"

# QUESTION: Tony writes
    "Help Tony write his letter"
    menu:
        "To Nairda,":
            jump LL1
        "Dearest BEST friend,":
            jump LL2

label L1:
# The letter will add on to each other so that in the end it's your letter you wrote
    pc "To Nairda,"

    jump LL1

label L2:
    pc "Dearest BEST friend,"

    jump LL2

label LL1:
    "Yo LL1"
    jump testtest

label LL2:
    "Yo LL2"
    jump testtest

label testtest:
"(Next line tester)"
menu:
    "Test A":
        $ write = "testa"
        pc "AAAAAAAAAAAAAAAAA!"
    "Test B":
        $ write = "testb"
        pc "BBBBBBBBBBBBBBBBBB!"
    "Test C":
        $ write = "testc"
        pc "CCCCCCCCCCCCCCCCCC!"

"(Next NEXT line tester)"
menu:
    "Test D":
        $ write2 = "testd"
        pc "DDDDDDDDDDDDDDD!"
    "Test B":
        $ write2 = "teste"
        pc "EEEEEEEEE!"
    "Test F":
        $ write2 = "testf"
        pc "FFFFFFFFFFFFFF!"



"Nairda opens the letter"
if write == "testa":
    nun "A test A!"
if write == "testb":
    nun "Ah Test B!"
if write == "testc":
    nun "Ah Test C!"


"It continues"
if write2 == "testd":
    nun "A test D!"
if write2 == "teste":
    nun "Ah Test E!"
if write2 == "testf":
    nun "Ah Test F!"





    # This ends the game.
    return
