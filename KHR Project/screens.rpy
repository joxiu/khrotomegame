# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xpos 0.165
        yalign 0.4

        vbox:
            style "menu"
            spacing 6#2

            for caption, action, chosen in items:

                if action:
                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"
                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear
        idle_color "#D7D7D7"
        hover_color "#FFFFFF"
        size 30

    style menu_choice_button is button:
        xminimum int(config.screen_width * 1.07)
        xmaximum int(config.screen_width * 1.07)
        yminimum int(config.screen_height * 0.075)
        ymaximum int(config.screen_height * 0.075)
        top_padding 18
        bottom_padding 18
        #idle_color "#556777"
        #hover_color "#323D47"
        


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text" color "#FFFFFF"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"
    style mm_button_text:
        size 30



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    #hbox:
        #style_group "quick"

        #xalign 1.0
        #yalign 1.0

        #textbutton _("Back") action Rollback()
        #textbutton _("Save") action ShowMenu('save')
        #textbutton _("Q.Save") action QuickSave()
        #textbutton _("Q.Load") action QuickLoad()
        #textbutton _("Skip") action Skip()
        #textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        #textbutton _("Auto") action Preference("auto-forward", "toggle")
        #textbutton _("Prefs") action ShowMenu('preferences')

#init -2:
    #style quick_button:
        #is default
        #background None
        #xpadding 5

    #style quick_button_text:
        #is default
        #size 12
        #idle_color "#8888"
        #hover_color "#ccc"
        #selected_idle_color "#cc08"
        #selected_hover_color "#cc0"
        #insensitive_color "#4448"

    imagebutton idle "ui/savebutton3.png" hover "ui/savebutton3_hover.png" action ShowMenu("save") xpos 1160 ypos 516 focus_mask True
    imagebutton idle "ui/loadbutton3.png" hover "ui/loadbutton3_hover.png" action ShowMenu("load") xpos 1160 ypos 550 focus_mask True
    imagebutton idle "ui/skipbutton3.png" hover "ui/skipbutton3_hover.png"  action Skip() xpos 1160 ypos 592 focus_mask True
    imagebutton idle "ui/autobutton3.png" hover "ui/autobutton3_hover.png" action Preference("auto-forward", "toggle") xpos 1160 ypos 626 focus_mask True
    imagebutton idle "ui/logbutton3.png" hover "ui/logbutton3_hover.png" action ShowMenu("text_history") xpos 1160 ypos 668 focus_mask True
    imagebutton idle "ui/configbutton3.png" hover "ui/configbutton3_hover.png" action ShowMenu("preferences") xpos 1160 ypos 702 focus_mask True
    


##############################################################################
# Affection Level screen
#
# Screen that shows the characters' affection points
screen aff_button: 
    if affTF:    
        vbox xpos 1210 ypos 10:
            imagebutton:
                idle "ui/lpsample1.png"
                hover "ui/lpsample1_hover.png"
                action ui.callsinnewcontext("aff_screen_label")
                
label aff_screen_label:
    play sound "music/sfx/click.mp3"
    with dissolve
    if cc == tsuna:
        call screen aff_screen_Tsuna
        ## TODO Others
    play sound "music/sfx/click.mp3"
    with fade
    return
    
## TODO Need to research: how to simplify this part
screen aff_screen_Tsuna:
    frame:
        has vbox
        if (affPoints < 5):
            add "affstats/Tsuna/lpscreen_0.png"
        elif ((affPoints >= 5)&(affPoints < 10)):
            add "affstats/Tsuna/lpscreen_5.png"
        elif ((affPoints >= 10)&(affPoints < 15)):
            add "affstats/Tsuna/lpscreen_10.png"
        elif ((affPoints >= 15)&(affPoints < 20)):
            add "affstats/Tsuna/lpscreen_15.png"
        elif ((affPoints >= 20)&(affPoints < 25)):
            add "affstats/Tsuna/lpscreen_20.png"
        elif ((affPoints >= 25)&(affPoints < 30)):
            add "affstats/Tsuna/lpscreen_25.png"
        elif ((affPoints >= 30)&(affPoints < 35)):
            add "affstats/Tsuna/lpscreen_30.png"
        elif ((affPoints >= 35)&(affPoints < 40)):
            add "affstats/Tsuna/lpscreen_35.png"
        elif ((affPoints >= 40)&(affPoints < 45)):
            add "affstats/Tsuna/lpscreen_40.png"
        elif ((affPoints >= 45)&(affPoints < 50)):
            add "affstats/Tsuna/lpscreen_45.png"
        elif ((affPoints >= 50)&(affPoints < 55)):
            add "affstats/Tsuna/lpscreen_50.png"
        elif ((affPoints >= 55)&(affPoints < 60)):
            add "affstats/Tsuna/lpscreen_55.png"
        elif ((affPoints >= 60)&(affPoints < 65)):
            add "affstats/Tsuna/lpscreen_60.png"
        elif ((affPoints >= 65)&(affPoints < 70)):
            add "affstats/Tsuna/lpscreen_65.png"
        elif ((affPoints >= 70)&(affPoints < 75)):
            add "affstats/Tsuna/lpscreen_70.png"
        elif ((affPoints >= 75)&(affPoints < 80)):
            add "affstats/Tsuna/lpscreen_75.png"
        elif ((affPoints >= 80)&(affPoints < 85)):
            add "affstats/Tsuna/lpscreen_80.png"
        elif ((affPoints >= 85)&(affPoints < 90)):
            add "affstats/Tsuna/lpscreen_85.png"
        elif ((affPoints >= 90)&(affPoints < 95)):
            add "affstats/Tsuna/lpscreen_90.png"
        elif ((affPoints >= 95)&(affPoints < 100)):
            add "affstats/Tsuna/lpscreen_95.png"
        else:
            add "affstats/Tsuna/lpscreen_100.png"
        
        imagebutton:
            xpos 1204 ypos -756
            idle "ui/lpsample1.png"
            hover "ui/lpsample1_hover.png"
            action Return()
            
##############################################################################
# Phone System Screen
#
# Screen that shows the phone system
screen phone_button: 
    if phoneTF:
        vbox xpos 10 ypos 10:
            imagebutton:
                idle "ui/newmsgbutton.png"
                hover "ui/newmsgbutton_hover.png"
                action ui.callsinnewcontext("phone_screen_label")

label phone_screen_label:
    play sound "music/sfx/rustle.mp3"
    with vpunch
    call screen phone_screen
    play sound "music/sfx/rustle.mp3"
    with fade
    $ phoneTF = False
    return
    
screen phone_screen:
    frame:
        has vbox #xpos 0.5 ypos 0.01
        # Use mailCode to determine which .png is shown
        if mailCode == "27-01":
            add "phone/27-01.png"
        elif mailCode == "27-02":
            add "phone/27-02.png"
            #etc
        imagebutton:
            xpos 606 ypos -116
            idle "phone/homebutton.png"
            hover "phone/homebutton_hover.png"
            action Return()
        # Is the mail a reply-able mail?
        if replyTF:
            imagebutton:
                xpos 539 ypos -227
                idle "phone/replybutton.png"
                hover "phone/replybutton_hover.png"
                action ui.callsinnewcontext("phone_reply_label")

label phone_reply_label:
    with fade
    if mailCode[:2] == "27":
        jump tsuna_mail
    elif mailCode[:2] == "59":
        jump gokudera_mail
    elif mailCode[:2] == "80":
        jump yamamoto_mail
    elif mailCode[:2] == "18":
        jump hibari_mail
    elif mailCode[:2] == "69":
        jump mukuro_mail
    elif mailCode[:2] == "D":
        jump dino_mail
    with fade
    return
