## Tsuna's Route ================================================= ##
label sampletsunaChapter1:
    ## Show aff_button & init chosen character
    $ affTF = True
    $ cc = tsuna
    $ affPoints = 0

    ## Show phone
    ". . Phone System Test 1 . ."
    play sound "music/sfx/phoneRingtone.mp3"
    $ phoneTF = True            # Show phone button
    $ replyTF = True            # Message is reply-able
    $ mailCode = "27-01"        # Specify which mail is shown
    "You have a New Message! (Click the Phone button)\n
     - Home button: back\n
     - Reply (Text Message bar thing): reply to message.\n\n
     
     PS. Will hide button if message not clicked at this time or 
     message is already clicked.\n
     Click it now before it's gone!"
    $ phoneTF = False
    $ replyTF = False
    "End of test 1"
    
    ". . Phone System Test 2 . ."
    play sound "music/sfx/phoneRingtone.mp3"
    $ phoneTF = True            # Show phone button
    $ replyTF = True            # Message is reply-able
    $ mailCode = "27-02"        # Specify which mail is shown
    "You have a New Message (again)!"
    $ phoneTF = False
    $ replyTF = False
    
    "You have chosen [cc]'s route"
    
    ## Route start
    cc "\"Hi, [h_fname]-chan!\""
    cc "\"I'm Sawada Tsunayoshi, and I'm your new personal bodyguard.\""
    cc "\"Nice to meet you!\""
    
    ". . Answer Selection . ."
    ## Answer selection Sample
    menu:
        "Sample of answer selection. Pick your answer. 
         Current affection point: [affPoints]"
    
        "Affection +10":
            $ affPoints += 10
            "Good answer event here"
        "Affection +0":
            "Bad answer event here"
    
    "Continue story"
    "Affection point: [affPoints]"
    
    ". . Ending . ."
    "Let's say max affection point is 100.\n 
     Minimum affection point required for Good End is 80."
    ## Ending Sample
    $ affPoints = 70
    menu:
        "Current affection point: [affPoints]. \n
         Let's say this is the last answer player need to decide."
    
        "Affection +10":
            $ affPoints += 10
            "Good answer event here"
        "Affection +0":
            "Bad answer event here"
    
    "Affection point now: [affPoints]"
    if affPoints >= 80:
        jump tsunaGoodEnd
    else:
        jump tsunaBadEnd

## Endings Sample    
label sampletsunaGoodEnd:
    "You've entered Tsuna's good end, congrats!"
    jump endCredit
    return
    
label sampletsunaBadEnd:
    "You've entered Tsuna's bad end, please try again!"
    jump endCredit
    return

## Mails
label tsuna_mail:
    if mailCode[3:] == "01":
        jump tsuna_mail_1
    elif mailCode[3:] == "02":
        jump tsuna_mail_2

    return

label tsuna_mail_1:
    menu:
        "Aff Pts = 100":
            # Do something probably
            $ affPoints = 100
            
        "Aff Pts = 95":
            # Do something probably
            $ affPoints = 95
        
        "Aff Pts = 90":
            # Do something probably
            $ affPoints = 90
            
    $ replyTF = False
    show mail sending at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ renpy.pause(2.5)
    play sound "music/sfx/messageSent.mp3"
    show mail sent at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ renpy.pause(1.0)
    
    return
            
label tsuna_mail_2:
    menu:
        "Aff Pts = 10":
            # Do something probably
            $ affPoints = 10
    
        "Aff Pts = 15":
            # Do something probably
            $ affPoints = 15
    
        "Aff Pts = 20":
            # Do something probably
            $ affPoints = 20
            
    $ replyTF = False
    show mail sending at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ renpy.pause(2.5)
    play sound "music/sfx/messageSent.mp3"
    show mail sent at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ renpy.pause(1.0)
    
    return
    
## Tsuna's Route End ============================================= ##
