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
    tony "The P C (*whispering* 'for short') was a great gift and I have looked up several log videos!"
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
    scene tonys
    show tony n
    "(Tony's apartment is very cluttered)"
    "(As a beaver he has the uncontrollable instinct to stop the flow of running water)"
    "(Sound proofing the walls of the apartment... putting piles of papers and sticks up every wall surface and into every conceivable orifice and corner...)"
    "(Water wouldn't dare flow through these rooms!)"
    "(Or at least that's what Tony tells himself)"
    scene tonys
    show tony sad at right
    tony "How do I thank Nairda for the Personal Computer?"
    tony "(*whispering to himself*) P C for short"
    scene tonys
    show tony shy at right
    tony "What if I USE it?!?"
    "(Tony turns on the PC and asks the ever so popular 'Waterfowl Waterfowl Stay' search engine for advice)"
    pcresult "Thanking a friend for a present is easy! Read '300 Ways to thank your friend' now!"
    "(Tony opens the link, overwhelmed with the amount of advice he chooses to only read the first suggestion and just do that.)"
    pcresult "Number 1: Write your friend a letter! A letter can show how you really fee..."
    tony "OK that's enough reading! I'll write a letter to Nairda!"
    "(Tony asks the 'Waterfowl Waterfowl Stay' search engine how to write a letter with a Personal Computer (PC for short))"
    pcresult "There's plenty of free open-source writing programs on the interweb."
    "(There's so many options Tony once again chooses the first one)"

# QUESTION: Do you want a lore refresher?
    pcresult "Download?"
    menu:
        "Download Open Workplace":
            jump downloadopenworkplace

        "Don't Download Open Workplace":
            jump dontdownloadopenworkplace



label downloadopenworkplace:
    $ onpc = onpc +5  # Writing it on the Personal Computer (PC for short)
    play sound "audio/yes.mp3"
    pcresult "Boop Beep Boop Boop Beep Boop"
    pcresult "Download Complete. Opening program now."
    "(A new page opens on Open Workplace, all ready for Tony to write his letter.)"
    jump letterwrite

label dontdownloadopenworkplace:
    $ onpc = onpc -1  # Writing it by hand for some reason
    play sound "audio/no.mp3"
    tony "I'll hand write it instead!"
    "(Tony gets the bright idea to write the letter by hand instead)"
    "(Grabbing some paper from the crevices of his walls and pulling out a pen he had stuffed into the floorboards, Tony is all ready to write his letter.)"
    jump letterwrite


label letterwrite:
    "(Stretching his fingers out in front of him, he prepares to write a thank you note to Nairda)"
    "(A thank you note for the Personal Computer (PC for short))"

    "(What should it say?)"
menu:
    "My dearest friend,":
        $ write1 = "w1a"

    "To Nairda,":
        $ write1 = "w1b"

    "To my BEST friend, Nairda!":
        $ write1 = "w1c"


"(Good start, good start...)"
menu:
    "Thank you for the Personal Computer (P C for short)":
        $ write2 = "w2a"

    "The Personal Computer (P C for short) really is something":
        $ write2 = "w2b"

    "Did you know the Personal Computer is known as P C for short?":
        $ write2 = "w2c"

"(Looking at the Personal Computer (PC for short) for inspiration, Tony continues...)"
menu:
    "The P C (for short) was a great gift and I have already looked up several log videos!":
        $ write3 = "w3a"

    "There is a searching engine that answers all of my questions with some accuracy!":
        $ write3 = "w3b"

    "There are so many single otters and bears in my area wishing to meet me!":
        $ write3 = "w3c"

"(Looking at the Personal Computer (PC for short) for inspiration, Tony continues...)"
menu:
    "How many words does it take to fill up one interweb? I must be getting close to it now":
        $ write3 = "w3a"

    "Have you seen the interweb? It is like a phone for your hands!":
        $ write3 = "w3b"

    "So many news articles say conflicting things, my favourite part is the fighting in the comments":
        $ write3 = "w3c"

menu:
    "Do not search up toilet logs... it does not show you logs you can use to stop the flow of water in the toilet.":
        $ write4 = "w4a"

    "And what is the video on the about people just doing normal things like stretching or cleaning themselves? So many likes for such mundane content!":
        $ write4 = "w4b"

    "If there was a better gift to recieve, I have yet to receive it!":
        $ write4 = "w4c"

"(Looking at the Personal Computer (PC for short) for inspiration, Tony continues...)"
menu:
    "Yours Sincerely, tony.":
        $ write5 = "w5a"

    "With Regards, Tony.":
        $ write5 = "w5b"

    "ok bye bye":
        $ write5 = "w5c"

"(Tony is happy with his letter)"
jump which_end

# SCENE XX - ENDINGS ENDINGS ENDINGS ENDINGS
# This checks which ending Nairda gets:
# Letter written on Personal Computer (PC for short)
label which_end:
    "(It was time to send it! Well, to post it under the door of Nairda's apartment)"
    if onpc >= 5:
        jump bypc_end
# Letter written by hand
    elif onpc <= 1:
        jump byhand_end


label bypc_end:
    "(Nairda gets a neatly typed letter in the post, opening it and having a read)"
    jump endings

label byhand_end:
    "(Nairda gets a weirdly shaped, slightly moist, envelope in the post.)"
    "(Opening it up, there's scribblings only a madman could decipher)"
    "(Putting on his reading glasses, he does his best...)"
    jump endings


label endings:

if write1 == "w1a":
    l "My dearest friend,"
if write1 == "w1b":
    l "To Nairda,"
if write1 == "w1c":
    l "To my BEST friend, Nairda!"


"It continues"
if write2 == "w2a":
    l "Thank you for the Personal Computer (P C for short)"
if write2 == "w2b":
    l "The Personal Computer (P C for short) really is something"
if write2 == "w2c":
    l "Did you know the Personal Computer is known as P C for short?"


if write3 == "w3a":
    l "The P C (for short) was a great gift and I have already looked up several log videos!"
if write3 == "w3b":
    l "There is a searching engine that answers all of my questions with some accuracy!"
if write3 == "w3c":
    l "There are so many single otters and bears in my area wishing to meet me!"


if write4 == "w4a":
    l "Do not search up toilet logs... it does not show you logs you can use to stop the flow of water in the toilet."
    l "I have seen terrible things."
if write4 == "w4b":
    l "And what is the video on the about people just doing normal things like stretching or cleaning themselves? So many likes for such mundane content!"
if write4 == "w4c":
    l "If there was a better gift to recieve, I have yet to receive it!"

if write5 == "w5a":
    l "Yours sincerely, Tony."
if write5 == "w5b":
    l "With Regards, Tony."
if write5 == "w5c":
    l "Ok bye bye"
    "(The letter is not signed by anyone, but Nairda has an inkling it was from his neighbour, Tony.)"


    # This ends the game.
    return
