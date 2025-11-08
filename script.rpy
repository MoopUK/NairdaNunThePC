# GAME INFO ___________________________________________________________________
# TITLE: Nairda Nun and the PC
# AUTHOR: Kouda_Ha

# This game was made for the Mini Jam 197: Recursion.
# Game Jam theme: Recursion
# Game Jam limitation: Mouse only

# How these themes/limitations were used:
# Ren'py is already mouse only for controls, and I tried to think of how to do *recursion* but
# not based on computing, went for "Linguistic Recursion", got a bit confused by it,
# I think it kind of worked out...

# Game Story Contents:

# SCENE 00: Intro
# Intro to game, explaining it is a mouse only mechanic as it is a Ren'py novel, click to continue story along.

# SCENE 01: Pizza Time
# Nairda and Strudle both get a pizza and head home for some TV

# SCENE 02: Tony starts the letter
# Tony has to write a letter to Nairda to thank HIM for buying Tony a PC, but it becomes a jumbled mess of recursion as Tony
# doesn't know how to use a PC very well.

# SCENE 03: Nairda gets his letter and Endings
# Nairda tries to read it at the end, it's very confusing.
#______________________________________________________________________________

# The game starts here.
label start:
    # SCENE 00: Introduction
    play music "audio/openingbgm.wav"
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
    gamedev "And you remember what 'Linguistic Recursion' is, right? For the game?"
    scene apartmentdoor
    show tony confused
    tony "O-o"
    tony "O-of course!"
    gamedev "Ok, great! Let's get started!"
    scene apartmentdoor
    "(And with that, welcome to)"
    "(Nairda Nun... and the PC?)"

    # SCENE 01: Pizza Time
    scene pizza
    play music "audio/cafe.mp3"
    "(The famous Peckish Pizza Shop is reopened and offering 50 percent off!)"
    "(Who could say no to that? Nairda couldn't that's for sure!)"
    show nun n at right
    show snun n at left
    nun "One large veggie pizza please, Fry the pizza guy!"
    snun "Could you add some flies to it? If you caught any in the zapper of course"
    "(Fry stops in his tracks and thinks for a moment)"
    scene pizza
    show fry confused
    fry "I don't think I'm legally allowed to due to health and safety... I could look up if there's any store bought flies I could buy for
    next time though?"
    scene pizza
    show nun confused at right
    show snun sad at left
    snun "Ah... I guess it could be an issue with health and safety. They are delicious though! For frogs at least..."
    scene pizza
    show nun n at right
    show snun n at left
    show fry happy
    fry "I've never tried them personally, I have a bit of a phobia for foods I can't fillet"
    fry "I'm pretty sure there aren't hands or knives small or sharp enough to do that to most bugs so I skip them altogether"
    scene pizza
    show nun n at right
    show snun n at left
    show fry sad
    fry "My father always said there's nothing wrong with eatin' bugs but I've always been picky with my food"
    scene pizza
    show fry shy
    fry "I've never been picky with pizza though!"
    "(Fry whispers under his breath)"
    scene pizza
    show fry happy
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
    scene pizza
    show nun shy at right
    show snun confused at left
    nun "Oh nothing, the pizza smells good is all"

    scene apartmentdoor
    "(Nairda and Strudle head on home to eat their large veggie pizza without a side of flies)"
    scene nuninterior
    show nun happy at right
    show snun happy at left
    "(And snuggle up onto the sofa to watch their favourite guilty pleasure show on the TV)"

# QUESTION: Donwload the program or no?
    "What do they watch?"
    menu:
        "Pie or die":
            "(The guessing gameshow about pies)"
            "(Is it pie?)"
            "(Or an explosive?)"
            "(Contestants better guess correctly...)"
            "(Or they might lose more than just a TV Show competition!)"
            "(Kind of a dark show... people wonder why it'd been greenlit in the first place)"

        "Desperate Frog Lives":
            "(Nothing to do with housewives, it is literally about the desperate attempts of survival
            by frogs in weird social situations.)"
            "(The winners of the show get a prize of at least 12)"
            "(That's a lot.)"
        "The Capybara Royals":
            "(A stupid program about the excessively rich doing stupid things with their money thinking
            people watch this show to admire their beautiful and lavish lifestyle.)"
            "(People watch to rage bait themselves and have a rant about how the money could be used to
            save millions of lives instead of stupid table lamps and extended swimming pools...)"
            "(Ironically making the royals even richer and making the show seem popular for the wrong reasons.)"

    # SCENE 02: Tony starts the letter
    scene apartmentdoor
    play music "audio/openingbgm.wav"
    "(Tony stands outside of the apartment doors thinking of how to thank Nairda for their recent gift of a second-hand computer)"
    "(Welcoming him to the new age of... online!)"
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
    tony "Spruce is wonderful this time of year!"
    "(He tidies up his suspenders)"
    show tony n
    tony "Perfect! I'll just say that!"
    play sound "audio/doorunlock.mp3"
    "(His neighbour's door starts to unlock and someone is turning the door handle)"
    show tony sad
    tony "OR I'LL SAY IT LATER!!!"
    scene apartmentdoor
    stop music
    play sound "audio/doorslam.mp3"
    "(Tony runs back into his apartment, slamming the door shut, hiding from Nairda Nun)"
    show nun confused at right
    nun "What was all of that ruckus?"
    "(They look around and see the empty apartment hallway, so still and quiet you could hear a pin drop a mile away)"
    show nun n at right
    nun "Guess it was nothing..."
    scene apartmentdoor
    "(He closes the door again)"

    scene tonyinterior
    play music "audio/tonybgm.wav"
    show tony sad
    tony "That was close!"
    scene tonyinterior
    show tony n
    "(Tony's apartment is very cluttered)"
    "(As a beaver he has the uncontrollable instinct to stop the flow of running water)"
    "(Sound proofing the walls of the apartment... putting piles of papers and sticks up every wall surface and into every conceivable orifice and corner...)"
    "(Water wouldn't dare flow through these rooms!)"
    "(Or at least that's what Tony tells himself)"
    scene tonyinterior
    show tony sad at right
    tony "How do I thank Nairda for the Personal Computer?"
    tony "(*whispering to himself*) P C for short"
    scene tonyinterior
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

# QUESTION: Donwload the program or no?
    pcresult "Download?"
    menu:
        "Download Open Workplace":
            jump downloadopenworkplace

        "Don't Download Open Workplace":
            jump dontdownloadopenworkplace

label downloadopenworkplace:
    $ onpc = onpc +5  # Writing it on the Personal Computer (PC for short)
    pcresult "Boop Beep Boop Boop Beep Boop"
    pcresult "Download Complete. Opening program now."
    "(A new page opens on Open Workplace, all ready for Tony to write his letter.)"
    jump letterwrite

label dontdownloadopenworkplace:
    $ onpc = onpc -1  # Writing it by hand for some reason
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
    "Thank you for the Personal Computer (P C for short),":
        $ write2 = "w2a"

    "The Personal Computer (P C for short) really is something,":
        $ write2 = "w2b"

    "Did you know the Personal Computer is known as P C for short,":
        $ write2 = "w2c"

"(Looking at the Personal Computer (PC for short) for inspiration, Tony continues...)"
menu:
    "the P C (for short) was a great gift and I have already looked up several log videos…":
        $ write3 = "w3a"

    "there is also this thing called a searching engine that answers all of my questions with some accuracy,":
        $ write3 = "w3b"

    "and why are there so many single otters and bears in my area wishing to meet me,":
        $ write3 = "w3c"

"(The sentence just keeps on growing…)"
menu:
    "how many words does it take to fill up one interweb as I must be getting close to it now,":
        $ write3 = "w3a"

    "have you seen the interweb, it is like a phone for your hands,":
        $ write3 = "w3b"

    "so many news articles say conflicting things, my favourite part is the fighting in the comments,":
        $ write3 = "w3c"

menu:
    "also do not search up toilet logs on the Personal Computer (P C for short)... it does not show you logs you can use to stop the flow of water in the toilet… I have seen terrible things…":
        $ write4 = "w4a"

    "and what is the video on the about people just doing normal things like stretching or cleaning themselves, so many likes for such mundane content,":
        $ write4 = "w4b"

    "if there was a better gift to receive, I have yet to receive it, unless I did receive it but I have since forgotten as that is something I do sometimes,":
        $ write4 = "w4c"

"(He takes a deep breath and thinks of how to end his masterpiece)"
menu:
    "Yours Sincerely, Tony.":
        $ write5 = "w5a"

    "how do I end this it’s Tony?":
        $ write5 = "w5b"

    "ok bye bye then":
        $ write5 = "w5c"


# SCENE 03: Nairda gets his letter and Endings
"(Tony is happy with his letter and scrunches it into an envelope)"
"(It was time to send it! Well, to post it under the door of Nairda's apartment)"
tony "No need to pay postage when it's your next door neighbour!"
tony "Or should I post it officially?"
menu:
    "Shove it under the door?":
        jump underdoor

    "Go to a post box and post it personally yourself?":
        jump postit


label underdoor:
    tony "Posting it would be silly... And the door method is fun and it's free!"
    tony "like pouring river water in your socks!"
    scene apartmentdoor
    "(Tony posts the letter under the front door to Nairda and Strudle's apartment)"
    play sound "audio/doorslam.mp3"
    "(Then runs back inside of his own apartment with glee.)"
    jump which_end

label postit:
    tony "I would prefer it looked official..."
    "(Tony holds the letter in his hands)"
    "(Staring into it like his life depended on this decision!)"
    tony "I'M POSTING IT!"
    "(Tony finds some old, unused stamps and places one on the top corner, along with writing Nairda's address on the front)"
    play sound "audio/doorslam.mp3"
    "(He then shuffles out of the door to make his way to a post box)"
    scene postoffice
    "(The closest post box is several miles away)"
    "(But it is worth it for his BEST FRIEND, Nairda.)"
    jump which_end


# SCENE XX - ENDINGS ENDINGS ENDINGS ENDINGS
# This checks which ending Nairda gets:
label which_end:
# Letter written on Personal Computer (PC for short)
    if onpc >= 5:
        jump bypc_end
# Letter written by hand
    elif onpc <= 1:
        jump byhand_end


label bypc_end:
    scene nuninterior
    play music "audio/cafe.mp3"
    show nun n
    "(Nairda gets a neatly typed letter, opening it and having a read...)"
    jump endings

label byhand_end:
    scene nuninterior
    play music "audio/cafe.mp3"
    show nun confused
    "(Nairda gets a weirdly shaped, slightly moist, letter.)"
    "(Opening it up, there's scribblings only a madman could decipher,)"
    "(Could it be related to his most recent case?)"
    scene nuninterior
    show nun n
    "(Putting on his reading glasses, he does his best...)"
    jump endings


label endings:
scene nuninterior
if write1 == "w1a":
    l "My dearest friend,"
if write1 == "w1b":
    l "To Nairda,"
if write1 == "w1c":
    l "To my BEST friend, Nairda!"


"It continues"
if write2 == "w2a":
    l "Thank you for the Personal Computer (P C for short),"
if write2 == "w2b":
    l "The Personal Computer (P C for short) really is something,"
if write2 == "w2c":
    l "Did you know the Personal Computer is known as P C for short,"

if write3 == "w3a":
    l "The P C (for short) was a great gift and I have already looked up several log videos..."
if write3 == "w3b":
    l "There is a searching engine that answers all of my questions with some accuracy,"
if write3 == "w3c":
    l "and why are there so many single otters and bears in my area wishing to meet me,"


if write4 == "w4a":
    l "do not search up toilet logs... it does not show you logs you can use to stop the flow of water in the toilet..."
    l "I have seen terrible things..."

if write4 == "w4b":
    l "and what is the video on the about people just doing normal things like stretching or cleaning themselves, so many likes for such mundane content,"

if write4 == "w4c":
    l "if there was a better gift to receive, I have yet to receive it, unless I did receive it but I have since forgotten as that is something I do sometimes,"

if write5 == "w5a":
    l "Yours sincerely, Tony."
    "(Nairda didn't expect a letter from Tony, he's always so introverted that Nairda's surprised he'd write one)"
    "(It's not overly clear but Nairda thinks it's a thank you for the computer.)"
    "(The End.)"
    jump end
if write5 == "w5b":
    l "how do I end this it's Tony?"
    "(Nairda didn't expect a letter of thanks from Tony, if this was a thank you letter that is...)"
    "(It's not overly clear but Nairda thinks it's a thank you?)"
    "(The End.)"
    jump end
if write5 == "w5c":
    l "Ok bye bye then"
    "(The letter is not signed by anyone, but Nairda has an inkling it was from his neighbour, Tony.)"
    "(The End.)"
    jump end

label end:
    scene tonyinterior
    play music "audio/tonybgm.wav"
    gamedev "Tony has a way to go with writing letters, I asked him to do a letter using 'Linguistic Recursion',"
    gamedev "But he was confused and said something about having 48 hours left to finish something..."
    gamedev "And that new things are confusing so the best he can do is one long, run-on sentence that seems like it's never ending."
    show tony n
    tony "Did I do good?"
    menu:
        "You did good, Tony!":
            play sound "audio/yes.mp3"
            jump goodtony
        "No.":
            play sound "audio/no.mp3"
            jump badtony

label goodtony:
    scene tonyinterior
    show tony happy
    tony "YESS! Now Tony has done TWO things right!"
    "(The End... for real this time)"
    return

label badtony:
    scene tonyinterior
    show tony sad
    tony "Oh... I did try my best..."
    "(You feel eyes like daggers eminating towards you from behind the screen)"
    gamedev "You're a monster..."
    "(The End... for real this time)"
    return

    # This ends the game.
    return
