
define m = Character("Marth")
define j = Character("Jezebeth")
define s = Character("Satan")
define d = Character("Dylan")
define h = Character("Human")

transform trueleft:
    xalign 0.01
    yalign 0.50
transform left:
    xalign 0.20
    yalign 0.50
transform trueright:
    xalign 0.99
    yalign 0.50
transform right:
    xalign 0.80
    yalign 0.50
transform center:
    xalign 0.50
    yalign 0.50
transform lowcenter:
    xalign 0.50
    yalign 0.70
transform mleft:
    xalign 0.20
    yalign 0.70
transform mright:
    xalign 0.80
    yalign 0.70


default humans = 0
default dylan=False
default puppy=False
default monster=False

#  play sound "audio/
#  play music "audio/

# game start ---------------------------------------------------------------------------------------------------------
label start:
    play music "audio/arguing.mp3"
    scene bg black
    show j neutral at right
    show m neutral at mleft
    j "Are you ready Marth?"
    "I nod my head and mentally prepare myself for what is about to go down."
    hide j neutral
    show m neutral at center
    "My name is Marth, I am a lower level demon to Jezebeth, my master."
    "We live in Hell with Satan and other demons."
    "Our days are spent overseeing human torture and taking care of Satan's many monsters."
    "Recently my master, Jezebeth, asked about Satan's plan to conquer Earth."
    "He told her that he had given up on doing so, and that made her angry."
    "So today, we are leaving Hell and going to conquer Earth ourselves."
    j "COME ON MARTH LET'S GO!"
    scene bg hell
    show j angry at trueleft
    show m angry at mleft
    show satan at trueright
    #show satan at left
    "There's a large flash of light as my master spits flames at Satan."
    "She laughs as the flames hit him, but then frowns when he shows no pain."
    s "You are really going to make me do this?"
    j "Screw you Satan! You are too much of a chicken to even try! And if you won't I will."
    "He sighs and shakes his head."
    s "I can't let you do that."
    j "Just try and stop me!"
    show satan powers at trueright
    "Satan raises his hands and a orange light appears and starts to grow."
    s "Don't make me do this Jezebeth, you can still stay and work for me!"
    j "I would never, NOW MARTH!"
    show ball small at mleft
    "At my masters call I raise the little blue ball that she had given me."
    m "Da mihi transitum ad terram, beati nostri itineribus in nomine mali!"
    show ball medium at trueleft
    "The ball starts to grow and I run to my master and cling to her tail. My master starts to laugh as the ball starts to envelope us."
    "Satan curses loudly."
    show ball large at trueleft
    s "Where did you get that Jezebeth!?"
    "He fires at us but it's too late, the blue ball had fully covered us and we disapearred."
    jump earth

label earth:
    play music "audio/tense.mp3"
    scene bg desert
    show m nervous at mright
    show j neutral at left
    "It's really bright, and my eyes hurt before I even open them."
    j "Wake up dummy, we are here."
    "My master shakes me violently and I get up and look around."
    "As far as I can see there was a strange dry tan substance, like tiny rocks everywhere."
    "I wiggle my toes and my feet sink deeper into it."
    "This is not the earth I was expecting."
    menu:
        "What the heck is this?":
            $rude=True
            m "This is not the Earth I was expecting."
            show j angry at left
            "SLAP"
            j "You doubt me, you ignorant beast! We are on earth! We are just in a 'rural' area."
        "Oh no! I did the incantation wrong!":
            $rude=False
            show m nervous at mright
            m "We are not on Earth, I am so sorry!"
            j "Relax Marth, we are just in a rural area."
    j "I should be able to fly us to the nearest city and then our world domination can begin!"
    m "Yes Master, of course, my apologies."
    show m neutral at mright
    "My master spread her large wings."
    if rude==True:
        "You should be grateful Marth, I am finally going to accomplish what Satan never could!"
    if rude==False:
        show j blushing at left
        j "Aren't you excited Marth? We are finally going to accomplish what Satan never could!"
    m "Of course Master, thank you for allowing me to accompany you."
    play sound "audio/eflying.mp3"
    "My master flapped her wings and rose steadily into the air. I ran and grabbed onto her tail and held on for dear life."
    "We flew higher and higher towards our destiny."
    jump alley

    
label alley:
    play music "audio/main music.mp3"
    play sound "audio/eflying.mp3"
    scene bg welcome
    "We fly over a big city, and a sign that says 'Welcome to SeaSide'."
    "My master flies lower and we land in an alley way off a busy street."
    stop sound 
    scene bg street
    show m neutral at mright
    show j smirking at left
    j "Get off Marth, lets take over this trash planet."
    j "With my amazing powers of mind control and fire and your lightning, this should be a piece of cake."
    "She dances a flame on her fingers and smiles."
    menu:
        "Let's do it!":
            play music "audio/fight.mp3"
            scene bg roof
            show j smirking at left
            show m angry at mleft
            $monster=True
            "We fly towards a large building and my Master lands on top of it."
            j "Lets go Marth, make it storm."
            play sound "audio/estorm.mp3"
            "I use my powers to create lighting and a storm appears in the sky and grows larger and larger and larger until it consumes the whole sky."
            jump captured
        "Maybe we should study them first Master":
            m "It could be good to study them and learn how to best overthrow their governments."
    j "Thats a good point."
    j "Do you think we can study them in this form?"
    menu:
        "We should disguise ourselves":
            m "The humans might not be so accepting of us in this form, which could make it hard to study them."
        "Of course we can":
            jump run
    "Master nods and suddenly turns away."
    "Theres a flash of light as she enters her human form."
    show j neutral human at left
    j "Hurry up Marth and do the same."
    show m neutral human at mright
    j "Good, now lets go!"
    "My master steps out of the alley and onto the busy street."
    jump morning

label morning:
    play music "audio/main music.mp3"
    scene bg street
    show j neutral human at trueleft
    show m neutral human at mleft
    m "So how exactly are we supposed to study the humans anyway Master?"
    j "Simple... umm... we should..... we should go about the day as a normal human would of course!"
    j "Yes, it is morning on Earth so we should eat breakfast like humans."
    j "Lets see, where around here could we have breakfast? Any ideas Marth?"
    "You look around and spot a McDonalds, a popular fast food chain that offers breakfast foods,"
    "and you see a small coffee shop. Through the window you can see humans sitting and chatting."
    "Where should you go eat?"
    menu:
        "McDonalds":
            j "Hmm ok, looks colorful?"
            jump mcdonalds
        "Coffee Shop":
            j "Ok, the humans there look rather happy."
            jump coffeeshop
    
label mcdonalds:
    play music "audio/tense.mp3"
    scene bg mcdonalds
    show j neutral human at trueleft
    show m neutral human at mleft
    "You walk inside and the smell of grease hits your nose."
    "You look over at your master and already she doesn't look happy."
    show human at right
    "The human behind the front counter turns to us and scowls."
    h "What do you want?"
    menu:
        "How dare you speak to my master this way!":
            show m angry human at mleft
            "The human's bored look turns to quizzical."
            h "Master? Listen dude, I don't care what kind of freaky stuff you and your mom have going on."
            show j angry human at trueleft
            j "Mother!? He is not my child! How dare you!"
            "Master starts to turn red and fire appears in her eyes."
            show m nervous human at center
            "Master's eyes glaze over, and I recognize this as her beginning to use her powers."
            j "YOU WILL APOLOGIZE AND GIVE US FOOD"
            "The human's eyes glaze over and their expression droops."
            h "My apologies, allow me to get you some food."
            show j smirking human at trueleft
            j "Good, I would like whatever a McGriddle is and a large coffee."
            j "Marth?"
            m "Ahh yes thank you Master, may I have an order of hashbrowns and a milk?"
            j "Did u get that?"
            "The human nods and returns shortly after with the food."
            "They place it on the counter, their face still void of any expression and bow."
            h "My apologies for the wait, please come again."
            $humans-=2
        "This is normal human speech":
            m "Allow me to order for you Master."
            m "My master would like a McGriddle and a large coffee, and I will have hashbrowns and a milk. Thank you."
            h "Master?"
            m "Sorry?"
            h "Nevermind, your total will be $15.60."
            j "Ugh ridiculous, the concept of money is so stupid."
            m "No worries Master I prepared for this."
            "I hand some money over to the human. I had prepped a 'wallet' in advance to the trip."
            h "Here's your change, your order will be out shortly."
            "After waiting a while we finally get our food."
            $humans-=1
    hide human
    "I grab our food and walk to a table and set the food down."
    m "Here Master, please sit."
    "She sits down and opens the McGriddle. After taking a bite her face turns sour."
    show j neutral human at trueleft
    j "Why is this sandwich so sweet?"
    "She takes a sip of her coffee."
    j "Blehh this is disgusting!"
    show j angry human at trueleft
    show m nervous human at center
    j "Ugh breakfast is terrible, why do humans eat this garbage!?"
    m "My apologies Master! I will get rid of this garbage for you."
    j "Forget it, lets just go."
    j "Once I take over this planet, I can get rid of it for good."
    jump meetdylan

label coffeeshop:
    play music "audio/coffee shop.mp3"
    scene bg cafe
    show j neutral human at trueleft
    show m neutral human at mleft
    "You walk inside and the smell of fresh coffee and bread hits your nose."
    show j blushing human at trueleft
    show m happy human at mleft
    m "Oh Master it smells lovely."
    j "Yeah, it does."
    "The coffee shop is filled with chattering and light pop music."
    "We walk up to the counter and theres a big display case full of colorful pastries."
    j "Ohh those look amazing."
    show human at right
    "A human pops out from the back room and greets us."
    h "Hi there, welcome to Donny's, I'll be right with you."
    m "Thank you!"
    hide human at right
    m "Master I can't wait, I'm gonna get a latte, I have heard they are delicious and very popular among humans."
    j "Hmm good idea."
    show human at right
    "The human comes back and smiles."
    h "Sorry about that, what can I get you?"
    show j neutral human at trueleft
    j "Umm can I get two cafe lattes and umm what pastries would you recommend?"
    m "They all look so good!"
    h "Sure thing, two cafe lattes, and I would recommend the croissants or cinnamon rolls, those are very popular here."
    h "Though my personal favorite is the cheese danish."
    j "Ummm idk, Marth?"
    "What should we get?"
    menu:
        "Two cheese danishes":
            $yum=("cheese danish")
            m "Can we get two cheese danishes please?"
        "One crossaint and one cinnamonroll":
            $yum=("crossaint and cinnamonroll")
            m "Can we get one of each?"
    h "Sure no problem!"
    "The human turns around and starts prepping our food."
    h "You guys can have a seat if you would like and I'll bring the food to you."
    j "Oh... thank you."
    m "Yes thank you!"
    hide human at right
    show j neutral human at left with moveinleft
    show m happy human at mright with moveinright
    "I find an empty table and pull the chair out."
    m "Please sit Master."
    "Shortly our food is brought to our table."
    show human with moveinright
    h "Enjoy!"
    "The food smells amazing and the lattes have some pretty design on top."
    hide human
    "Me and my master both quickly grab our cups and take a sip."
    show j blushing human at left
    j "Oh my gosh, it's so creamy."
    m "Yum, Earth breakfast is so good."
    "I look over at the [yum] and grab a piece, Master does the same."
    j "Oh my..."
    m "Mhmm..."
    j "This is delicious!"
    $humans+=1
    if yum==("cheese danish"):
        show human 
        m "Miss, thank you so much!"
        j "Yes the danishes were incredible!"
        h "Oh goodness I am glad you liked them so much!"
        "The human beems at us and then turns and grabs something behind the counter."
        h "Since you liked them so much, here's another one on the house!"
        m "Oh my!"
        j "Oh umm thanks."
        m "Thank you so much!"
        hide human
        $humans+=2
    "Me and Master greedily finish our drinks and pastries."
    show j smirking human at left
    j "That was so good, maybe humans are alright."
    m "Yeah who knows?"
    j "We better keep going, breakfast is only the first part of the day."
    show m neutral human at mright
    m "Right lets go."
    jump meetdylan

label meetdylan:
    play music "audio/main music.mp3"
    scene bg street
    show j neutral human at trueleft
    show m neutral human at mleft
    show d neutral at trueright
    "We walk outside and look both ways."
    m "Which way should we go Master?"
    j "Umm, Im not sure... how about"
    show d neutral at center
    play sound "audio/ebump into.mp3"
    "Thunk"
    "A man bumps into my Master and spills his coffee."
    "A little splashes on her and the rest splatters across the ground."
    menu:
        "Oh my god what is wrong with you! How dare you hurt my master!":
            play music "audio/tense.mp3"
            show j angry human at trueleft
            show m angry human at lowcenter
            show d angry at right
            m "How dare you spill coffee on my master!"
            m "Oh no there is coffee on your shirt!"
            "My master's face starts to turn red."
            j "You IMBECILE, you ruined my shirt!"
            h "Whatever lady, it was an accident. I'm sorry ok?"
            "He scoffs and walks away."
            hide d angry
            m "How rude!"
            j "Ugh humans are so stupid."
            m "I am so sorry Master."
            m "Let's find something fun to do so you can relax!"
            j "Fine, where will we go?"
            "You look around and see a sign on the cafe."
            m "Master, that sign says that they have an amusement park and festival food down by the pier."
            j "Amusement.. hmm lets do it."
            $humans-=1
            jump travel
        "My goodness, sir are you alright?":
            play music "audio/main music.mp3"
            show j neutral human at trueleft
            show m neutral human at mleft
            show d neutral at center
            m "Are you both ok? Goodness look at the mess."
            h "Yeah I am ok, are you ok ma'am? Oh no I spilled on you, I'm so sorry."
            j "Oh... no worries, your people clothes are no matter of importance."
            h "Still, I'm so sorry, can I pay for your dry cleaning?"
            j "Dry.. cleaning?"
            m "It's an process to clean clothes Master."
            h "Haha you don't know what dry cleaning is?"
            m "Yes apologies we are not from here."
            h "No worries, are you guys lost? Can I help you out at all?"
            m "We are looking for a classic thing that people do here during the day."
            m "Maybe something fun?"
            h "Oh I can help with that, people travel from all over to visit our amusement park. You should go."
            show j smirking human at trueleft
            j "Hmm sounds interesting. Amusement.. yes, lets go."
            d "I can show you the way, I'm Dylan by the way."
            m "Thank you Dylan."
            j "Hmm Dylan, I'm Jezebeth and this is Marth."
            show d laugh at right
            "He smiled at us, and to my suprise my Master returned it."
            $humans+=1
            $dylan=True
            jump travel

label travel:
    play music "audio/main music.mp3"
    scene bg street
    show j neutral human at trueleft
    show m neutral human at mleft
    if dylan==True:
        show d neutral at trueright
    m "How should we get there?"
    j "I believe I heard people in the coffee shop discussing taking a train or a bus."
    if dylan==True:
        d "Yes, those are the easiest way to get around, the bus can be a little crowded but can get you typically closer to your destination."
        d "The train is a little nicer but you might have to walk a little to and from the train station."
        d "Either one will get you there."
    menu:
        "Lets take the train!":
            if dylan==True:
                d "Ok, sounds good, it's this way!"
            else:
                m "I think it's this way, let's go."
            jump train
        "Lets try the bus!":
            if dylan==True:
                d "Ok, sounds good, it's this way!"
            else:
                m "I think it's this way, let's go."
            jump bus

label train:
    play music "audio/main music.mp3"
    play sound "audio/etrain.mp3"
    scene bg train
    show j neutral human at trueleft
    show m happy human at mleft
    if dylan==True:
        show d neutral at trueright
    m "Oh wow, this thing moves fast"
    $humans+=1
    "[humans] is how much you like humans"
    #this is to check the code is running correctly, delete when done
    if dylan==True:
        d "Yeah, thats the best part! Hold on tight to the pole though, it can jerk you around"
        show j smirking human at trueleft
        j "I don't need any help, I can handle myself without some pole."
    "The train jerks around a corner and my master stumbles and bumps into some large man."
    if dylan==True:
        show d laugh at right
        d "Hah what did I tell you! You ok Jez?"
        show j blushing human with moveinleft
        j "Hah! Hahaha! Yes I'm fine, you did warn me."
        "I can't believe my eyes, my master is smiling and laughing, with a human!"
        "She blushed as she grabbed onto one of the poles."
        $humans+=1
    else:
        play music "audio/arguing.mp3"
        show m nervous human at mleft
        m "Oh my master are you ok?"
        show j angry human with moveinleft
        j "Agh watch it!"
        "I could see the flames in my Master's eyes ignite."
        "She did not like making a fool of herself, especially infront of humans."
        "She grunted and grabbed one of the poles in the train."
        $humans-=1
    "The rest of the ride went relatively smooth and soon we were standing at the entrance to the amusement park."
    jump fun

label bus: 
    play music "audio/main music.mp3"
    play sound "audio/ebus.mp3"
    scene bg bus
    show j neutral human at trueleft
    show m neutral human at mleft
    if dylan==True:
        show d neutral at trueright
    m "It's kinda crowded on the bus."
    "We were jam packed with a person on either side of us."
    $humans-=1
    if dylan==True:
        d "Yeah, thats the worst part! Hold on tight to something though, buses stop pretty frequently."
        show j smirking human at trueleft
        j "I don't need any help, I can handle myself without any assistance."
    "The bus jerks to a stop and my master stumbles and bumps into some large man."
    if dylan==True:
        show d laugh at right
        d "Hah what did I tell you! You ok Jez?"
        show j blushing human with moveinleft
        j "Hah! Hahaha! Yes I'm fine, you did warn me."
        "I can't believe my eyes, my master is smiling and laughing, with a human!"
        "She blushed as she grabbed onto one of the poles."
        $humans+=1
    else:
        play music "audio/arguing.mp3"
        show m nervous human at mleft
        m "Oh my master are you ok?"
        show j angry human 
        show m nervous human at lowcenter
        j "Agh watch it!"
        "I could see the flames in my Master's eyes ignite."
        "She did not like making a fool of herself, especially infront of humans."
        "She grunted and grabbed one of the poles in the train."
        $humans-=1
    "The rest of the ride went relatively smooth and soon we were standing at the entrance to the amusement park."
    jump fun

label fun:
    play sound "audio/egame noises.mp3"
    play music "audio/main music.mp3"
    scene bg entrance
    show j neutral human at trueleft
    show m neutral human at mleft
    if dylan==True:
        show d neutral at trueright
    "We walk up to a big colorful archway with the words WonderWay across the top in big bright letters."
    m "This must be the Amusement park!"
    if humans>=2:
        j "It does look rather... amusing."
    else:
        j "The bright colors are hurting my eyes."
    m "I can't wait!"
    if dylan==True:
        d "Yeah, dont worry Jez, we will have tons of fun!"
        d "I used to come here all the time as a kid."
    "We walk inside and our ears are filled with the sound of childrens laughter and cheerful songs."
    "There are machines with what look like animals stabbed through their center, running in circles. And children riding on them."
    m "Oh my god, how.. peculiar..."
    j "That is horrifying, is that how they treat their monsters here!"
    if dylan==True:
        d "No! No definetly not, those are just plastic replicas of horses. So kids can ride them without actually making the animals work. Its a classic carnival ride."
        d "It's called a Merry-Go-Round."
        m "Oh, well, thats better than riding real ones."
        j "Still it creates a very disturbing image."
        d "Its supposed to be fun! See look they are painted bright colors!"
        m "If you say so sir."
    else:
        $humans-=1
    m "Let's keep walking."
    m "Wow there's a ton of stuff to do!"
    "Towering over us were giant tracks of metal."
    "All around were tents and giant colorful fluffy pillows."
    "According to my earth research, I believe they were called stuff-ded animals."
    j "What are those large metal things in the sky?"
    if dylan==True:
        d "Those are rollercoasters. You sit in them and they whip you around really fast, with like loops and stuff."
    else:
        m "If I am recalling correctly it is called a roller coaster."
        m "Humans ride it for a thrill, apparently to feel like they have escaped death."
    j "Ooh lets do it!"
    m "But Master, what about those fluffy things everywhere. People seem to be playing games. Games are the most human thing out there."
    m "Plus I want one of those animals of fluff."
    j "We aren't here for you Marth, don't be so selfish."
    m "Sorry Master."
    j "It's fine, both look fun."
    "Which one should we try?"
    menu:
        "Games and animal pillows!":
            stop sound
            jump games
        "Rollercoaster!":
            stop sound
            jump coaster

label games:
    play music "audio/fight.mp3"
    scene bg games
    show m neutral human at mleft
    "I run towards a stall with big pink plush things hanging in it."
    if dylan==True:
        "Master and Dylan are a ways behind chatting, slowly making their way over."
    else:
        "My master slowly walks over, obviously upset that we are playing games."
    show human 
    "The human at the stall smiles creepily at me."
    h "Why hello there little boy."
    "Little Boy!? Why does everyone here think I am a child?"
    menu:
        "Be angry":
            show m angry human at mleft
            m "How dare you! I am 5000 years old! I serve the one of the 8 Great Demons of Hell!"
            "The human gives a puzzled look and shrugs."
            h "Whatever kid."
            $humans-=1
        "Be chill":
            m "Haha, I'm actually older than you, human."
            "I snarl a little but maintain my composure."
    "Master finally appears behind me."
    show j neutral human at trueleft
    if dylan==True:
        show d neutral at trueright
    j "Are you ok little demon? You look upset."
    h "Ahh hello ma'am. I believe your child wanted to play the game."
    j "Child?"
    "The human ignored the interruption and continued talking."
    "He gestured behing him to some bottles stacked in a pyramid."
    h "The game is simple, knock the bottles down and you win a prize, knock them all down you win a bigger prize."
    h "It's 5 dollars a ball."
    if dylan==True:
        show d angry at trueright
        d "Five dollars! That's ridiculous!"
        d "Come on guys, lets go somewhere else."
    "Master shrugs at the mention of money, it doesn't matter to her."
    "The human smiles creepily down at me"
    h "You want the big prize huh buddy?"
    h "Might not be easy."
    "He turns back to my master and hold out his hand for the money."
    "I reach in my pocket and pull out the human wallet I prepared and take out 5 dollars."
    "I slap them down on the counter."
    m "One please."
    "The human looks down suprised and then grins."
    h "Oh you've got your own money huh?"
    "He turns to get the balls and whispers something under his breath, but I hear it anyway."
    h"It's so easy with kids, I'll take all the money he has."
    "I grit my teeth and when the balls are placed in front of me I grab them."
    "This should be easy. I have demon strength, and while it is nothing compared to my master, I am way stronger than a human."
    "I grab a ball and throw it hitting the pile of bottles right at center of it's base."
    "Plink"
    "The ball bounces right off."
    show j angry human at trueleft
    show m angry human at center
    show human at right
    j "WHAT THE HELL!"
    m "That's not fair! It hit it!"
    h "Heh sorry kid too bad. Don't worry you can buy another ball and try again."
    if dylan==True:
        d"Hey man, give us our money back!"
        d "You are obviously cheating!"
        "Dylan grabs the man by his shirt, but the human isn't fazed."
        h "Sorry dude, all sales are final."
    "He grins and I can feel my face heating up."
    "I look at my master and I know we are both thinking the same thing."
    "Lets take the human down."
    $humans-=1
    menu:
        "Blow up the stand.":
            play music "audio/arguing.mp3"
            "The heat in my face gets hotter and sparks appear in my vision."
            "Little black sparks of lightning appear over my head and start to grow."
            "I look at my master for approval and she smiles back."
            "I let the sparks grow larger and larger until each one is the size of a baseball."
            m "I have a new game to play."
            m "I aim and you run."
            "I look pointedly at the human and smile wickedly."
            "He looks stunned and then starts sprinting away."
            hide human
            play sound "audio/eexplosion.mp3"
            "I fire and the stand explodes with black sparks."
            "Glass shards and stuffing fall from the sky."
            j "Nice shot Marth."
            if dylan==True:
                show d scream at trueright
                "Dylan stands silent in shock."
                d "What.. what was that.."
                d "What the hell are you!?"
                "My master and I look at him and see the terror in his face."
                "Dylan starts to back away"
                j "Wait Dylan it's not what you think!"
                "He whips around and starts sprinting away."
                hide d scream
                m "No Dylan wait!"
                "Neither me nor my Master turn to follow him."
                "It's better if he doesn't get involved with this."
            jump captured

        "Use Master's powers to win":
            show m happy human at mleft
            "I look at my master and smile."
            "I take another 5 out of my wallet and place it on the stand."
            show j smirking human at trueleft
            "My master smirks and takes the ball when the human places it down."
            "She takes a step back and a small flame appears in her hand around the ball."
            "She winds up and throws."
            play sound "audio/ebottle smash.mp3"
            "The baseball, and now a ball of fire smashes into the bottles, shattering the supports behind them and the entire tower collapses."
            h "What the... how did you do that!?"
            "My master just smiles and shrugs."
            "I grab one of the giant prizes and grin."
            m "Thanks!"
            play music "audio/main music.mp3"
            "My master and I turn and walk away, grinning from ear to ear."
            hide human
            if dylan==True:
                "Dylan jogs to catch up to us."
                d "Uh guys?"
                d "Guys! What the hell was that?"
                "My master turns to him with the most innocent look on her face and smiles."
                j "I don't know, beginner's luck maybe?"
                show d laugh at right
                "Dylan mouth hangs open, and then he breaks out laughing."
                d "Hahahahahaaa"
                d "That's some beginners luck!"
                d "Damn Jez! Have you played baseball before?"
                "He goes on and on and my master and I laugh."
            "We continue to walk around the amusment park until it starts to get dark."
            $humans+=1
            jump beach

label coaster:
    play music "audio/main music.mp3"
    scene bg rollercoaster
    show j neutral human at trueleft
    show m neutral human at mleft
    if dylan==True:
        show d neutral at trueright
    j "Alright! Lets go, I wanna see what you humans do for 'thrills'."
    m "Ok...."
    if dylan==True:
        d "Don't worry Marth, it will be fun!"
        m "Hmmm, I don't know..."
    j "Oh chill out Marth, don't ruin this for me."
    "My master runs off in the direction of the towering coaster."
    "I feel a lump in my throat as I get closer."
    "Oh well, how bad could it be?"
    scene bg black
    play sound "<from 30 to 45>audio/ecoaster.mp3" 
    m "AGHHHHHHHHHH"
    j "WOOHOOOOOOOOO"
    if dylan==True:
        d "WEEEEEEEEEEEEEEHEEEEE"
    $humans+=1
    stop sound
    scene bg rollercoaster
    show j blushing human at trueleft
    show m nervous human at mleft
    if dylan==True:
        show d laugh at trueright
    "I wobble away from the exit towards my master."
    if dylan==True:
        "She is chatting exitedly with Dylan."
        "A huge smile lights up her face."
    j "HURRY UP MARTH!"
    j "I wanna go again!"
    m "UGHHHH"
    menu:
        "Okkkkk lets go...":
            "I walk towards the entrance again and the lump returns to my stomach."
            "Ughh this isn't gonna be fun."
            play sound "<from 30 to 45>audio/ecoaster.mp3" 
            scene bg black
            m "BLEGHHHHH"
            $humans+=1
            stop sound
            jump beach
        "I'm good, I'll stay here":
            j"Aww come on Marth... fine."
            if dylan==True:
                j "Dylan will you come?"
                d "Hell yeah! Wait for me!"
                "They sprint off towards the entrance."
            else:
                "She sprints off towards the entrance."
            j "Have fun here being lonely!"
            "My master giggles as she runs."
            hide j blushing human
            if dylan==True:
                show d laugh at trueright
            "Its been such a long time since I have seen my master so happy."
            "Maybe Earth isn't such a bad place after all."
            "I watch the cars on the coaster rush by as I wait patiently for my master to return."
            jump beach

label beach:
    play music "audio/beach.mp3"
    scene bg street 
    show j neutral human at trueleft
    show m neutral human at mleft
    if dylan==True:
        show d neutral at trueright
    "Eventually we wandered out of the amusement park."
    "The bright lights and crowds had gotten tiring."
    j "Ugh I need to relax, is there someplace quiet we can go?"
    m "Oh look! Over there!"
    m "Master look!"
    "I turned my master towards the most gorgeous view I had ever seen."
    scene bg beach
    show j neutral human at trueleft
    show m neutral human at mleft
    if dylan==True:
        show d neutral at trueright
    "The sun was setting and bright colors filled the sky and reflected across the ocean."
    j "Wow it's beautiful."
    if dylan==True:
        d "Yeah, I love the views here."
        d "It's so nice and peaceful."
    m "It's lovely."
    m "Lets stay here!"
    j "WHAT!? Marth you are crazy we can't stay on Earth!"
    "My master turns to me in shock."
    m "I meant near the beach Master, relax."
    if dylan==True:
        show d laugh at trueright
        d "You guys are funny."
        d "Yeah we can stay near the beach. We can walk along the boardwalk or we can walk on the beach."
        d "What do you think?"
    m "Master lets walk on the beach!"
    j "I don't know Marth, lets stay on the platform."
    j "The beach looks... sandy."
    menu:
        "Walk on the beach":
            jump sand
        "Walk on the boardwalk":
            jump boardwalk

label sand:
    play music "audio/beach.mp3"
    scene bg beach
    show j neutral human at trueleft
    show m neutral human at mleft
    if dylan==True:
        show d neutral at trueright
    j "Ugh fine Marth! You win."
    m "Thank you!"
    "We turn down a path that leads to the beach."
    "We start to walk in the sand and my master's face quickly turns sour."
    j "It's in my shoes."
    m "Yes, it is uncomfortable."
    if dylan==True:
        d "Oh well, its popular to take your shoes off and walk barefoot in the sand, it's much more confortable."
    else:
        m "Master when we first landed in the desert, I liked my bare feet in the sand."
        m "Maybe we can take our shoes off."
    "Me and my master nod to each other and we take off our shoes."
    "I wiggle my toes in the cool sand and we walk down the beach near the water."
    "I splash my feet in the water and run along the sand."
    "Behind me, my master looks angry."
    j "This is worse."
    j "I'm done lets go."
    "My master turns and starts walking up and off the beach."
    $humans-=1
    menu:
        "Follow her":
            "I drag my feet in the sand and follow my master, leaving the gorgeous view behind me."
            jump night
        "Ask to stay longer":
            m "Please Master just a little longer!"
            m "The view is so beautiful"
            "My master turns back to me and sighs."
            j "Fine, lets keep walking."
    "We keep walking down the beach in comfortable silence."
    play sound "<from 1 to 7>audio/edog bark.mp3"
    "In the distance a shadow appears and we hear a distant noise."
    show puppy at lowcenter
    "As we get closer, the figure turns into a dog."
    "The shaggy dog runs up to my master, their tail wagging and tongue out."
    j "Awww hello!"
    "My master has always loved monsters, and human animals are no different."
    "She pets the dog and sweet talks to them."
    "The dog is loving the attention and rubs up against my master."
    j "Oh its very nice to meet you, Mr....?"
    j "Oh ok thank you, thats a lovely name."
    if dylan==True:
        d "Sorry, the dog told you their name?"
        j "Yes, his name is Buddy."
        j "At least that is what his previous owners named him."
        j "But they disappeared and left him on this beach."
        d "Oh thats awful!"
        d "Not suprising though, many people want pets, but can't afford them."
        d "After the get them, they realize it's expensive and abandon them."
    else:
        m "What's his name Master?"
        j "Yes, his name is Buddy."
        j "At least that is what his previous owners named him."
        j "But they disappeared and left him on this beach."
    m "That's so terrible."
    m "Lets keep him then!"
    j "Yes, he will have a home with us!"
    j "Come on buddy!"
    "The dog barks and follows behind us and we make our way off the beach."
    $puppy=True
    $humans-=1
    jump night

label boardwalk:
    play music "audio/beach.mp3"
    scene bg boardwalk
    show j neutral human at trueleft
    show m neutral human at mleft
    if dylan==True:
        show d neutral at trueright
    "I frown as we keep walking forward on the boardwalk."
    "At least it looks interesting."
    "To one side you can see the ocean and on the other are a long row of businesses and restaurants and shops."
    "The smell of fried food fills the air and I greedily breathe in." 
    m "Mhmmm lets get some food at least!" 
    j "Yes, what is that amazing smell?"
    $humans+=1
    "Some humans walk by with a bucket of something I recognize as french fries."
    m "That's it! That's what smells so good!"
    if dylan==True:
        show d laugh at trueright
        d"Oh my god its Thrashers!"
        m "Thrashers?"
        d "They're the best french fries in the world!"
        d "They are so good! They make them with vinegar and salt."
        d "And they get mad if you put ketchup on them because it's an insult to their flavor."
        "Master and I both stare at him in silence."
        "Vinegar? Salt? Ketchup?"
        j "Those words mean nothing to us." 
        d "Ugh never mind, I can't explain how good they are! You will just have to try them."  
        "He grabs our hands and pulls us forward."   
    "We start walking in the direction the other humans were coming from."
    "Shop after shop passes."
    "Some selling surfboards and others selling clothes."
    "Until we pass a brightly colored stall."
    m "Wait!"
    "I run towards it."
    "The words, SeaSide's Best Ice Cream, are brightly painted at the top."
    "A giant board displays pictures of colorful blobs."
    m "Oh my gosh! Is this Ice Cream?"
    m "Master we have to try some! Its a delicacy!"
    j "But the fries Marth, they smell so good!"
    m "Please master please."
    "I look at her face and I can tell she really wants those fries."
    menu:
        "Insist on ice cream":
            m "Please master! This is my only chance, and humans rave about it back home!"
            j "Ugh fine."
            show m happy human at mleft
            m "Thank you, thank you!"
            "We walk to the ice cream shop."
            show human at center
            "A human smiles as we apprach."
            h "Hi, how can I help you today?"
            m "Hi! Can I get a....."
            "The list of ice cream flavors overwhelms me."
            "What should I get?"
            menu:
                "Motor Oil: Coffee ice cream with fudge chunks and green caramel swirls":
                    $icecream=("Motor Oil")
                "Dirt: Chocolate ice cream with crushed oreo cookies and gummi worms":
                    $icecream=("Dirt")
            m "I'll take one small [icecream] in a cone."
            h "Good choice, be right up"
            "The human turns around and preps the ice cream."
            "My master glares at my back, still angry at the loss of french fries."
            h "Here you go!"
            m "Thank you!"
            hide human
            "I take my [icecream] ice cream and take a big bite."
            show m angry human at mleft
            m "Aghhhhhh!"
            j "What!? You got your icecream, whats wrong?"
            m "It hurts! My teeth, oww!"
            if dylan==True:
                show d laugh at trueright
                d "Ha! You are supposed to lick it Marth, not bite it!"
                m "Oh..."
                show m happy at mleft
                "I lick the icecream and the sweet flavor sits on my tongue."
                "It's so good!"
                j "Well I'm glad you got what you wanted. Come on lets go."
                "My master leads the way off the boardwalk and I follow, shamelessly licking my ice cream."
                jump night
            else:
                j "Thats what you get for being selfish."
                j "Come on lets get out of here."
                "I follow sadly behind my master as she leads the way off the boardwalk."
                $humans-=1
                jump night
        "Get french fries":
            m "Ok, lets get fries."
            "We keep walking until we reach Thrashers, a run down looking shop with peeling blue paint."
            "There's a line infront of the shop and we wait patiently for our turn."
            if dylan==True:
                "Dylan is practicly bouncing up and down as we wait in line, and he keeps chattering on about how famous these fries are."
                d "They are a delicacy here! Everyone on the boardwalk gets them because they are so delicious."
                d "I have been eating them all my life."
                "My master just laughed at him and finally it was our turn."
            "After paying we were handed a giant steaming bucket of fries that was overflowing."
            "My master took one and sniffed it and popped it in her mouth."
            show j blushing human at trueleft
            j "Oh my gosh!"
            j "They are so good!"
            j "Whatever vinegar is, I like it!"
            show m happy human at mleft
            "I laughed and grabbed one for myself."
            "The flavor filled my mouth and the vinegar tingled my nose. It tasted great."
            m "Mhmm so good."
            "Before we knew it the sun had set and the bucket was empty."
            j "Come on, lets get out of here."
            $humans+=1
            jump night

label night:
    play music "audio/coffee shop.mp3"
    scene bg room
    show j neutral human at trueleft
    show m neutral human at mleft
    if puppy==True:
        show puppy at lowcenter
    "We sit in a motel room that I got for us."
    "Master wanted time to sit and relax before taking over the Earth, so we stopped and rented a room."
    if puppy==True:
        "The dog sits at our feet and me and master sit on the creaky bed."
        m "I had fun today."
        j "Yeah, it wasn't all bad."
        if dylan==True:
            m "It was nice meeting Dylan."
            j "Yeah he was cool."
            "Dylan had parted ways with us after the beach and had gone home."
            "We thanked him for the great day we had and he gave us his phone number."
            "After meeting him I was feeling conflicted about our purpose on earth."
        j "Buddy, come here!"
        "Buddy hops up on the bed and lies down, resting his head on my masters lap."
        m "Maybe earth isn't so bad?"
        j "Yeah I don't know about that.."
        j "But earth animals are something else."
        "She smiles down at Buddy."
        j "Lets deal with this in the morning."
        m "Ok Master, good night."
        j "Night."
        jump decide
    else:
        m "I had fun today Master."
        j "I guess.. I had some."
        "We sit in silence on the motel bed."
        if dylan==True:
            m "It was nice meeting Dylan."
            j "Yeah he was cool."
            "Dylan had parted ways with us after the beach and had gone home."
            "We thanked him for the great day we had and he gave us his phone number."
            "After meeting him I was feeling conflicted about our purpose on earth."
        m "Maybe, we could stay?"
        j "I don't know anymore."
        "Her face scrunches."
        j "I'm confused... lets just figure it out in the morning."
        m "Ok master, good night."
        j "Night."
        jump decide

label decide:
    play music "audio/beach.mp3"
    scene bg room
    show j neutral human at trueleft
    show m neutral human at mleft
    if puppy==True:
        show puppy at lowcenter
    "When I woke up my master was already awake."
    "She was pacing back and forth."
    m "Master?"
    j "Silence Marth! I'm thinking!"
    if humans>=5:
        j "I think.. maybe"
        j "We should, stay?"
        j "I mean I had so much fun and the food is so good here, and it's so much prettier and way less hot and I feel like w.."
        m "Master calm down!"
        m "I agree, please, let's stay."
        show j blushing human at trueleft
        show m happy human at mleft
        "My master beams at me and for the first time in my 5000 years of living, gives me a hug."
        scene bg black with fade
        jump stay
    elif humans<=4 and humans>=0:
        j "I think... maybe"
        j "We should stay"
        j "I still think this world needs improvement."
        j "So maybe I should rule it, but keep it mostly the same?"
        "I nod my head vigorously."
        m "Fantastic idea master!"
        show j smirking human at trueleft
        "My master turns to me and smiles"
        j "Thank you Marth."
        scene bg black with fade
        jump peace
    else:
        j "This world is terrible."
        m "I agree Master, the humans of this world are despicable."
        if dylan==True:
            m "But.. what about Dylan?"
            j "He can rule with us!"
            j "Yes, we can have him by our side as we conquer Earth."
            "My master gives me a small smile, but I can tell that it's fake."
            scene bg black with fade
            jump giveup
        else:
            j "Lets show this garbage dump of a planet just who they are dealing with."
            show j smirking human at trueleft
            "My master gives an evil smirk and I know the best is about to come."
            scene bg black with fade
            jump conquer

label stay:
    play music "audio/good ending.mp3"
    scene bg black
    "ONE YEAR LATER...."
    scene bg cafe 
    show j smirking human at trueleft
    show m happy human at mleft
    if puppy==True:
        show puppy at right
    if dylan==True:
        show d laugh at trueright
    "We stayed on Earth."
    "Over time we got used to all the new rules and settled in quite nicely."
    if puppy==True:
        "My master had gotten a job working at an animal shelter."
        "And of course Buddy stayed with us."
    else:
        "My master had gotten a job in marketing."
        "With her powers to control people's minds, the job was a breeze for her."
    "It was a little hard for me to find work, most people thought I was a kid, so I spent my time at home."
    "I would keep it clean and cook dinner for my master every night."
    "We had gotten a little apartment in SeaSide near the amusement park"
    "Of course Master went every weekend to ride the roller coasters, which were her favorite."
    if dylan==True:
        "We stayed friends with Dylan too!"
        "He would visit often and was great in helping us adapt to human life."
        "We eventually showed him our true demon forms and he was freaked out at first."
        "But he eventually came around."
    "My Master never used to laugh, and now she did every day."
    "We were finally happy."
    scene bg end
    "THE BEST ENDING"
    return

label peace:
    play music "audio/good ending.mp3"
    scene bg black
    "ONE YEAR LATER...."
    scene bg room
    show m neutral at mleft
    if puppy==True:
        show puppy at center
    "We stayed on Earth."
    "Of course it needed lots of improvements, so my master ruled it all behind the scenes."
    "Using her powers of mind control, she controlled all the world leaders."
    "For once in Earth history, it was peaceful."
    "She stopped wars, solved world hunger, solved homelessness."
    "Earth had never been better."
    "Of course it kept my Master very busy."
    "She was flying every week back and forth to different countries."
    if puppy==True:
        "Buddy stayed with us and would keep me company."
        "We would wait together for Master to return each week."
    "We bought an apartment in SeaSide."
    "I would keep it clean for when my Master would return."
    "And when she did we would go explore."
    if dylan==True:
        "And Dylan would occasionally accompany us!"
        "He would visit every once and a while and was great in helping us adapt to human life."
        "We never told him the truth about us."
        "It just seemed safer that way."
    "Everything was good."    
    "My master would also tell me stories of the other countries she had seen."
    "And while she hardly had any time to herself,"
    "She looked happy."
    scene bg end
    "THE GOOD ENDING"
    return

label conquer:
    play music "audio/good ending.mp3"
    scene bg street #bg black
    "ONE YEAR LATER...."
    scene bg beach
    show j smirking human at trueleft
    show m angry human at mleft
    if puppy==True:
        show puppy at right
    "We stayed on Earth."
    "My master quickly destroyed all forms of government and became sole leader of the world."
    "All cities were destroyed and the Earth was turned into a beautiful wilderness."
    "All humans were forced to fend for themselves in a now animal controlled Earth."
    "Wildlife was booming and it made my master happy."
    if puppy==True:
        "Buddy stayed with us and was well taken care of."
        "We got lots of more dogs to keep him company."
    "Besides the occasionally issue with humans to solve, my Master spent most of her time playing with animals and relaxing at home with me and our new pets."
    "We had a nice home on top of a mountain that was filled with animal noises and my master's laughter."
    "With humans being eternally tortured to survive, and animals at the top of the world,"
    "Everything was good."    
    #scene bg end
    "THE EVIL ENDING"
    return                                                              

label giveup:
    play music "audio/giveup.mp3"
    scene bg black
    "ONE YEAR LATER...."
    scene bg hell 
    show j angry at trueleft
    show m nervous at mright
    if puppy==True:
        show puppy at lowcenter
    "We left Earth."
    "My master had tried to convince Dylan to join us when we conquered the world, but he was horrified."
    "He cried to us about how this was his entire life, and he couldn't believe that we thought he would join us in destroying it."
    "After his reaction, my master felt so guilty."
    "The look on Dylan's face broke her heart."
    "So we went back to hell."
    "Satan was forgiving."
    "He listening to our story of what happened and explained that he couldn't take over Earth for the same reason."
    "He said while most humans are terrible, there are some that are so good, they make the rest of the humans worthy of life."
    if puppy==True:
        "We took Buddy with us back to Hell and he got along with all other monsters."
    "For the most part, life went back to normal for us."
    "My master again spent her days surveying demons and torturing humans."
    "And we would continue like this... forever."
    scene bg end
    "THE SAD ENDING"
    return  
       
label run: 
    play music "audio/arguing.mp3"
    scene bg street
    show j smirking at trueleft
    show m neutral at mleft
    show human at right
    "We walk out onto the street and are given weird and scared looks the second we walk out of the alley."
    m "Master are those humans staring at us?"
    j "Pay them no mind Marth."
    "We continue walking down the street and watching the humans around us."
    "All of a sudden a few cop cars pull up."
    "Some cops jump out and point their guns at us."
    show human at trueright
    h "Put your hands up demons!"
    m "Master what do we do."
    "My master looks startled. I don't think she expected the humans to react so quickly."
    j "Marth get the device ready."
    show ball small at mleft
    "I grab the transportation device we used to get to Earth and turn it on."
    show ball medium at trueleft
    h "PUT YOUR HANDS UP DEMONS AND SURRENDER YOURSELVES NOW!"
    "The device starts to grow and envelope us."
    show ball large at trueleft
    "I hear the sounds of guns firing but it's too late, because we are back in hell."
    scene bg hell
    show m nervous at mright
    show j angry at trueright
    j "Marth are you ok?"
    show m nervous at mright
    m "Yes Master."
    show satan powers at trueleft with moveinleft
    s "Back so soon?"
    "He laughs and blasts us with his powers."
    s "I am going to make you pay for this."
    play music "audio/captured.mp3"
    scene bg dungeon
    show m neutral at mright
    show j neutral at left
    "Satn threw us in the dungeon."
    "We were now no better than the humans we used to torture."
    "Satan was very angry, so there was no telling how long he would keep us trapped."
    "So there we stayed, wrapped up in chains for hours upon hours on end."
    scene bg end
    "THE BAD ENDING"
    return 


label captured:
    play music "audio/captured.mp3"
    if monster==True:
        scene bg roof
        show j neutral at trueleft
        show m neutral at mleft
    else:
        scene bg games
        show j neutral human at trueleft
        show m neutral human at mleft
    "All of a sudden the ground starts to shake."
    "A bright light illuminates us from the sky."
    j "What the hell!?"
    show human at trueright
    show human1 at right
    "Large groups of men dressed head to toe with black surround us creating a wall with their shields."
    m "Ummm Master?"
    h "GRAB THEM!"
    scene bg black
    "We were captured by the US military."
    "We tried our best to fight them off, but we didn't have much knowledge about their forces and they overpowered us."
    scene bg lab
    show j neutral at left
    show m neutral at center
    "So now, here we were in an underground laboratory."
    "We were left down here for days to weeks on end."
    m "Do you think we will ever be able to leave?"
    "My master looked defeated. When we first got here she was angry, and used her powers constantly to try and escape."
    "But now she just sat in her chains."
    j "No, we will be here forever, or until they eventually kill us."
    j "I'm sorry Marth."
    j "It's my fault you are in here."
    m "Please don't apologize Master."
    m "It is my duty to follow you and serve you."
    m "And I will gladly do it, even in here."
    scene bg end
    "THE WORST ENDING"
    return 