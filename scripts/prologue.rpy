## The game starts here.
label prologue:
    ## PROLOGUE
    $ reporter = Character("Reporter",color="#F3F781")
    $ boy = Character("Boy",color="#BCF5A9")
    
    scene bg tutoringCenter_breakRoom with fade
    play music "music/ProbablyNoTime.mp3" loop
    
    "Inside the break room, the television is on and broadcasting the latest news. 
    Every person occupying the room watches it silently."
    "I am no exception as I stare at the news in horror."
    reporter "\"Another member of the Ashworth family has been murdered. 
              There are still no clues as to who the culprit is.\""
    reporter "\"The question now is: Who is their next target?\""
    h "\"That’s terrible…\""
    
    play sound "music/sfx/doorOpen.mp3"
    aiko "\"Hey, [h_fname]. Your kid is waiting outside, and there's also a guy wanting to speak to you.\""
    
    "I tear my eyes away from the screen to see my best friend, Aiko, at the door."
    "She works at the Tutoring Center just like me, even though she hates kids. 
     The only reason why she’s here is because I’m here too."
    "We started working here together when we were sixteen. 
     Three years later and I’m still here, even though I have enough on my plate 
     with my university classes."
    "With a dragged out sigh, I peel myself out of my chair and follow Aiko out the breakroom."
    
    play sound "music/sfx/footsteps_playmat.mp3"
    h "\"Coming!\""

    stop sound
    scene bg tutoringCenter_frontDesk with fade
    play music "music/Carosello.mp3" loop
    
    "At the counter, I spot a man standing still. 
     He smiles watching several children playing in the distance." 
    "He doesn’t seem to be the father of any child here at the tutoring center with his young looks."
    h "(I wonder why he would need my assistance.)"
    
    h "\"Hello. Can I help you?\""
    "The man flashes me a kind smile, and I can't help but smile back."
    h "(He’s certainly easy on the eyes.)"
    uc "\"Ah, yes. Are you [h_fullname]?\""
    
    "I blink slowly as I try to remember if I know him from somewhere."
    h "(He doesn’t look familiar at all. Why would he know my name?)"
    
    menu:
        "Yes, that’s me.":
            h "\"Yes, I'm [h_fullname]. Do I know you?\""
            uc "\"No, you probably don’t. I came because someone recommended you.\""
            "I give him an apologetic smile."
            h "\"Are you a college student then? I’m sorry, but we don’t teach advanced classes.\""
            uc "\"I’m not a student. 
                Actually, I have a cousin who needs help with their high school math homework, 
                and I was hoping you could help them.\""
            h "\"Of course. Haha, sorry for the confusion. 
               It's the first time somebody has recommended me.\""

        "Silence.":
            h "I stay silent with a hesitant expression on my face."
            "The man notices my apprehensiveness and gasps sharply."
            uc "\"O-OH! I’m not a stalker or anything!\""
            "I don’t believe his explanation and continue my silence."
            uc "\"People just recommended you, and I just assumed that you were her…\""
            h "\"Why didn’t you say so sooner?! You need the application form, right?\""

                  
        "No, but I could be her.":
            h "\"I don’t know who you’re talking about, but I could be her if you want me to.\""
            uc "\"Y-Y-You… I-I’m… E-Excuse me?”\""
            "I try to hold in my laughter as the man’s face flushes with embarrassment."
            uc "\"I--... I was l-l-looking for [h_fullname], p-please.\""
            "Being merciful, I decide to change the subject."
            h "\"So what are you here for?\""
            uc "\"I’m here because of a recommendation for a tutor.\""
            h "\"Oh! Well, I’m your girl. My name is [h_fullname]!\""
            uc "\"R-Right…\""

    "I turn to grab some forms and hand it to the man."
    h "\"If you could fill out these forms, I'll be more than happy to help you out, sir.\""
    uc "\"Please call me Tsuna.\""
          
    boy "\"Ms. [h_lname], don't forget about me!\""
    "I send Tsuna an apologetic smile. 
     The child I needed to tutor stands in the background with an impatient expression on his face."
    tsuna "\"It seems that I'm bothering you...\""
    h "\"You're not.\""
         
    "I send the boy a small glare, silently telling him to zip his mouth. 
     He notices my gesture and sticks out his tongue in defiance."
    "Tsuna catches the mini-war going on between us and laughs quietly."
    
    tsuna "\"Since I'm not my cousin’s guardian, I have to take these forms and bring them back another day. 
           And you need to tend to your student, no?\""
    boy "\"She does! I was here before you, mister.\""
    "I sigh and shake my head with disbelief."
    h "\"Hey! Stop being embarrassing and leave him alone.\""
    tsuna "\"It's fine. The boy was here first. I should leave.\""
    "He bows his head slightly and leaves."
    "I watch his receding figure but catch myself when I feel the boy's smug smile."
    
    h "\"Now I'm making you do extra work!\""
    boy "\"H-Hey! That’s evil!\""

    scene bg tutoringCenter_outside with fade
    play music "music/ForestAndTrees.mp3" loop

    play sound "music/sfx/birdChirping.mp3"
    "Walking out of the tutoring center, I stretch my arms into the air. 
     I let out a long sigh of relief as I air out my exhaustion."
    h "\"Maaaan, it's been a long day.\""
    stop sound
    
    with vpunch
    "Suddenly, I feel something freezing press against my cheek."
    "It catches me by surprise, and I let out a small gasp as I twirl my body around."
    h "\"AIKO!\""
    aiko "\"Here.\""
    "In her hand is a canned beverage, one that was unceremoniously placed against my cheek."
    
    h "(She could have warned me that she was here!)"
    "Writing it off as Aiko’s usual, wordless antics, I accept her gift."
    h "\"So what are you going to do now?\""
    aiko "\"Sleep.\""
    h "\"That’s right, you have a nap schedule to keep!\""
    "A small smile forms on her lips, though she catches herself and replaces it with her habitual frown."
                                                                                                          
    aiko "\"Do you need me to walk you to your class?\""
    h "\"No, no. The campus isn’t that creepy at night.\""
    aiko "\"...You shouldn’t have taken night classes.\""
    h "\"I know, but it was the only way I could work and study.\""
    "I notice the worry on Aiko’s face and let out a long sigh."
    h "\"I’ll be fine. I have the pepper spray you got me, as well as the whistle.\""
    "She gives me a satisfactory nod."
    aiko "\"I’ll be off then… Don’t get into any trouble on your way there.\""
    h "\"We’ve been friends for ten years. You know nothing exciting happens to me.\""
    "Aiko shrugs with a blank expression on her face."
    "I wave goodbye to her and watch her leave. 
     Once she is gone, I start to head in the opposite direction and towards my university."
    
    play sound "music/sfx/footsteps_gravel.mp3"                                                                      
    "As I step forward, I feel something under my foot."
    stop sound
    "Glancing down, I spot several cigarettes lying on the ground. 
     The culprit is only a few feet away as he enjoys a new cigarette."
    h "\"Excuse me.\""
    "The man looks up at me with a surprised expression."
    man1 "\"What do you want?\""
    "I press my lips together, holding in my reprimand."
    h "(He looks like he'll hurt me if I say anything.)"
    
    h "\"Umm, did you throw these on the ground?\""
    "He stares down at the ground, and his eyes widen."
    man1 "\"What about it?\""
    h "\"You shouldn't be littering around this place. 
       There are lots of kids coming and going from here.\""
    man1 "\"Oh, that's right. You're a tutor...\""
    h "\"W-What?\""
    h "(He acts as if he knows me.)"
    
    man2 "\"Hey, Gokudera! We're moving---\""
    "Another man enters the conversation, but he stops talking the minute he sees me."
    man2 "\"Oh, who do we have here?! Hello!\""
    "He waves his hand enthusiastically, and I hesitantly wave back."
    h "(He looks way too happy and carefree to be friends with that smoking man.)"
    gokudera "\"She's just telling me to pick up some stuff.\""
    "As rough as he looks, he appears to be pretty obedient. 
     He begins picking up the used up cigarettes and throws them into the nearest trashcan."
    h "\"Thank you.\""
    
    gokudera "\"Che, you look surprised that I threw them away.\""
    man2 "\"I was too!\""
    gokudera "\"S-Shut it, loser.\""
    man2 "\"Hahahaha!\""
    h "\"Hahahaha!\""
    gokudera "\"A-AM I SURROUNDED BY IDIOTS?\""
    man2 "\"Don't call her that!\""
    "Gokudera flinches at the man's sudden aggressiveness. When he glances at me, he flushes."
    gokudera "\"My deepest apologies.\""
    man2 "\"That's the proper way to treat a princess.\""
    h "(Princess? I hardly know them! They can’t be giving me a nickname like that.)"
    
    h "\"It's weird having you call me that.\""
    man2 "\"Oh, that's right. You don't know.\""
    "Gokudera elbows the man, causing him to change the subject."
    man2 "\"I mean, you don't know my name. I'm Yamamoto Takeshi.\""
    "He keeps laughing, but it only confuses me even more."
    h "\"I have to get going… Bye!\""
    h "(Best to separate myself from these weirdos.)"
    play sound "music/sfx/footsteps_gravel.mp3" loop
    "Before they could say another word, I speed away from the two men. "
    
    "I continue walking down the usual path I take to the university. 
     Each step is quicker than the next as I hurry to make up for lost time. "
    h "(Those guys seriously distracted me! I hope I’m not late!)"
    
    uc "\"Excuse me, miss?\""
    stop sound
    h "(What now?)"
    "I stop in my tracks, my head instinctively turning to whoever the voice belongs to."
    "My eyes land on a rather tall man with blonde hair. There is a map in his
      hands, and he points to a location on it."
    uc "\"I need help getting here.\""
    h "\"Oh, that’s my university. Are you a professor there?\""
    uc "\"Do you think I look that old?\""
    "He flashes me a bright smile, and I freeze for a moment."

    menu:
        "Sorry.":
            h "\"Sorry. I just speculated.\""
            uc "\"No worries. I would probably think the same thing if I were you.\""
            h "\"I’m not quite sure...\""
            "He continues to smile as his attention refocuses on the map."
            uc "\"Well, I certainly am too old to understand this map.\""
            "I let out a giggle and stare down at the map."
            h "\"I’m actually headed there right now. I can walk with you there
              if you’d like.\""

        "Yes, you do.":
            h "\"Yeah, you look super old.\""
            uc "\"W-WHAT?!\""
            "He panics slightly as he presses his hand to his face."
            h "\"Look at those wrinkles!\""
            "His spirit appears to be crushed as dark clouds surround him."
            h "\"I’m just joking. The opportunity to tease you was too good to pass up.\""
            "The man laughs nervously as he scratches his neck."
            "I glance back at the map."
            h "\"So, anyways. I can take you the university if you want.\""
            
        "Stutter":
            "His smile is too bright and I can’t think straight."
            h "\"I- I- I… N-Noo?\""
            uc "\"Are you okay? You’re turning a little red.\""
            "He reaches forward to touch my cheek."
            "However, I dodge his touch and step away from him."
            h "\"Uh-uh! Nope. Nope! Too close!\""
            uc "\"Oh, sorry!\""
            "Refusing to speak about my almost heart attack, I direct my
              attention back to the map."
            h "\"I..I think I can take you to the university.\""

    "The man crumbles the map, stashing it in his back pocket."
    uc "\"Thank you! You are so kind. I’m Dino Cavallone, by the way.\""
    h "\"[h_fullname]\""
    "(How many times have I introduced myself today?)"
    dino "\"A beautiful name as I thought.\""
    h "\"T-Thank you.\""
    "(‘As I thought’? What does he mean?)"
    
    play sound "music/sfx/footsteps_gravel.mp3" loop
    "As we head towards our destination, he begins to ask me an unusual amount of questions 
     about my safety precautions--"
    "How do I safely make it from school to home, do I keep any protective
     measurements in my bag, has anybody weird approached me, and so on."
    "It’s odd how he seems so worried about me after we just met, and I can’t
      help but feel suspicious."
    stop sound
    stop music

    scene bg university_outside_night with fade
    play music "music/StrangeLs.mp3" loop

    "When we finally make it to the university, the man named Dino tenses."
    h "\"Is something wrong?\""
    "Dino scans the area as he pushes me behind him."
    dino "\"Someone is following us.\""

    play sound "music/sfx/explosion.mp3"
    "{b}{size=+6}BOOM!!{/b}{/size}"
    
    "An explosion that is not too far from us grabs our attention."
    "I freeze with fear while Dino springs into action."
    dino "\"Stay here!\""
    "Without thinking, I follow his instructions and hide behind one of the pillars."
    "Dino rushes towards the explosion, but a mysterious pebble appears under
      his shoe and he falls."
    h "\"......... Are you okay?\""
    "He jumps back onto his feet and scratches his head in embarrassment."
    dino "\"Yeah, I just tripped, that’s all!\""
    h "(Yeah right. He fell right on his face!)"
    play sound "music/sfx/footsteps_gravel.mp3"
    "Once he collects himself, he heads towards the explosion once more."
    
    stop sound
    h "(What in the world is happening?!)"
    man1 "\"Stay crouched.\""
    with vpunch
    "I whip my head around to see a tall, menacing looking man behind me. 
     He didn’t look approachable at all with his slanted eyes and deep frown."
    "Instinctively, I try jumping to my feet as my hand dives into my bag 
     to grab a hold of the pepper spray."
    "He doesn’t give me a chance as he places his hand on the crown of my head
      and pushes me down."
    man1 "\"Stay. Crouched.\""
    h "\"W-Who are you?”\""
    "He doesn’t bother replying as he stays by my side."
    uc "\"Kufufufu, Hibari. You sure need to learn your manners if you plan on
      staying in the team.\""
    with vpunch
    "I let out a startled scream as a man appears out of thin air."
    h "\"H-How did you do that? And what the hell is going on?\""
    "The man named Hibari sends the other male a death glare, ignoring my confusion."
    hibari "\"I don’t need manners to do my job, herbivore.\""
    "Herbivore?" "\"My, my. Someone should show you that people have names.
      It’s Mukuro— \""
    h "\"Seriously! What’s going on?\""

    play sound "music/sfx/explosion.mp3"
    "{b}{size=+6}BOOM!!{/b}{/size}"
    h "(Another explosion! And it’s right next to me?)"

    scene bg white with fade
    
    "I hear commotion around me as gusts of wind surround me. 
     Then my whole vision blurs as a white light engulfs my surroundings."
    "I feel an immense amount of energy surge within me, empowered by my
      raging adrenaline."
    h "(Am I dead?)"
    
    scene bg university_outside_night with fade

    "The white light lingers for a few seconds, and everything returns to how it is."
    "Although the explosion was only a few feet away from us, the area around
      me looks unscathed."
    "I notice that the group of men that I have met throughout the day are now surrounding me."
    "My confusion only worsens as I try to understand what’s happening."
    tsuna "\"Don’t get close to her. She’ll nullify your powers.\""
    yama "\"Woah. She really is the heir!\""
    hibari "\"Then our search is finally done…\""
    dino "\"She looks terrified. I don’t think she has any clue of what’s going on.\""
    h "\"Why are you all here?\""
    tsuna "\"It’s best to discuss this somewhere safe. 
           The Varia now know about her, so we need to move quickly.\""
    h "\"The Varia?\""
    yama "\"They’re the group that’s killing the Ashworth family.\""
    h "\"What? Then why are they after me?\""
    dino "\"Let’s go somewhere safe first. How about your house?\""
    "Although I didn’t know whether or not to trust them, fear consumes my judgment 
     and I lead them to my house."

    scene bg house_familyRoom with fade
    play music "music/ProbablyNoTime.mp3" loop
    
    play sound "music/sfx/doorOpen.mp3"
    h "\"Daaaaaad!\""
    "Loud footsteps echo down the hallway as a man furiously runs towards the family room."
    neron "\"What happened?! What’s--- Woah.\""
    "He stops in front of me and the six other men surrounding me."
    h "(Crap, he hates it when I bring a guy to the house. Bringing six of them is even worse.)"
    "At first, he wore a look of concern, but then a skeptical expression takes over."
    
    dino "\"Good evening, Mr. [h_lname]. Sorry for intruding so late at night.\""
    neron "\"What’s going on here?\""
    h "\"Dad, these guys saved me.\""
    neron "\"From what exactly?\""
    h "\"Some men that are murdering the Ashworth family apparently. 
       It looks like they got me confused for somebody else.\""
    
    "I laugh nervously. I’m hoping these guys will tell me it’s all one big mistake, but they don’t. 
     They stare at me in silence."
    "Their reactions only make me more confused."
    h "\"W-What's with those looks?\""
    neron "\"Weeeeeeell...\""
    tsuna "\"I think it's best you told her, sir.\""
    h "\"Tell me what? Dad, do you know something? Are the Ashworth's my 
       distant family members or something?\""
    neron "\"Weeeeeell...\""
    gokudera "\"STOP DANCING AROUND THE QUESTION OLD MAN!\""
    neron "\"You might be the legitimate heir to the Ashworth family or something.\""
    h "\"Or something?!\""
    yama "\"Isn't that exciting?\""
    "Gokudera rolls his eyes at the tan male's enthusiasm."
    h "\"What?! How?\""
    dino "\"Well, you're currently the only heir left, so that makes you the crowned heir.\""
    h "\"Crowned?\""
    
    "My father's face darkens with worry as he turns to the group of men."
    neron "\"Is Cordelia… Is the Queen alive?\""
    h "\"Did you just call mom the Queen?!\""
    tsuna "\"Yes, your mother is the reigning queen, and she is alive..\""
    "I glance back and forth as everyone starts to talk, a million questions springing up in my mind."
    h "(Am I really a princess?)"
    mukuro "\"Kufufu. This is certainly interesting.\""
    hibari "\"This is a mess...\""
    "Hibari begins to leave but the sound of Dino's voice cements him on the spot." 
    dino "\"Hey! You can't leave, Kyoya! We need to discuss this as a group.\""
    "I can't tell the actual reason for his stay, but Hibari relents and continues to remain with the group."
    h "(This can’t be happening to me!)"
    
    neron "\"So my Cordelia is okay?\""
    tsuna "\"Yes, sir.\""
    neron "\"That's a relief.\""
    "I inhale deeply before letting out a yell."
    h "\"EVERYONE STOP TALKING!\""
    "The room becomes eerily quiet as all the attention lands on me."
    
    h "\"Ehh...um... Let me get things straight.\""
    "I point at my father."
    h "\"Mom, who supposedly abandoned me when I was four, is actually the queen of Belmark? 
       One of the last countries with powerful royalty?\""
    h "\"And people are killing her lineage with me being next?\""
    "The group of guys nod their heads, acting as if this is all yesterday’s news."
    h "\"I'm going to bed. This is all just a dream. There’s absolutely no way this is real.\""
    "Dino extends his arm to hold me back."
    dino "\"This isn't a dream, [h_fname].\""
    "Seeing his heartthrob smile, I narrow my eyes."
    h "(This is definitely a dream.)"
    tsuna "\"I can assure you that today's events are real.\""
    
    gokudera "\"We don't have time for you to be doubting. These guys are seriously going to kill you.\""
    "I glance at my dad, who seems to be worried. When he catches my stare, he sends me a sad smile."
    neron "\"I'm sorry for not telling you sooner. 
           I never thought something this awful would happen and that you would be the last heir.\""
    yama "\"Haha no one would have expected that.\""
    mukuro "\"I would have.\""
    h "\"But how is this possible?\""
    neron "\"I made love to your---\""
    gokudera "\"I think she meant something else, old man...\""
    "My dad coughs awkwardly into his hand."
    neron "\"Right... Well, I met your mom when I was in college. 
           We married young and had you. At the beginning, we were so happy.\""
    neron "\"But her kingdom needed her. We had to split up. 
           As much as she loved us, she had an obligation to her people.\""
    neron "\"She chose her kingdom over us, but it was understandable.\""
    
    h "\"S-So why me?\""
    tsuna "\"Because it appears that you have the same power as her.\""
    "I remember the bright light that appeared when I was consumed by the explosion."
    h "\"That's a power?\""
    
    hibari "\"She needs to choose soon, or things will get complicated.\""
    yama "\"He's right, Tsuna.\""
    tsuna "\"[h_fname], I need you to choose who will guard you.\""
    h "\"Huh? Guard me?\""
    gokudera "\"Someone needs to be guarding you at all times until you succeed your mother 
              or until those assholes get caught.\""
    h "\"What if I don't want to succeed?\""
    mukuro "\"Unfortunately, you don't have a choice until those men are captured.\""
    
    "I stand there in a daze."
    "So much has happened within the hour, and I have no idea what to think about it."
    h "(I'm a princess. I have powers. I need to choose a guy to be with me at all times?!)"
    
    neron "\"Please choose somebody even if you don't want this. 
           I'll feel better knowing that you're safe.\""
    tsuna "\"We are all at your service, Princess.\""
    "All of them bow in unison, showing their utmost respect for me."
    
    h "\"Oh no…\""
    h "(This really is happening. I really am a princess. I really am in trouble.)"
    "I scan the group of men. Who do I choose?"

    ## Character Selection
    play music "music/ComicallyRomantic.mp3" loop
    
    menu:
        "Who should I choose as my bodyguard?"
    
        "Sawada Tsunayoshi":
            jump tsunaChapter1
        
        "Gokudera Hayato":
            jump gokuderaChapter1
        
        "Yamamoto Takeshi":
            jump yamamotoChapter1
        
        "Hibari Kyoya":
            jump hibariChapter1
        
        "Mukuro Rokudo":
            jump mukuroChapter1
        
        "Dino Cavallone":
            jump dinoChapter1
