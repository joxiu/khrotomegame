## END CREDIT ==================================================== ##
label endCredit:
    # reset states?
    $ cc = Character("cc",color="#c8ffc8")
    $ affPoints = 0
    $ affTF = False
    $ phoneTF = False
    $ replyTF = False
    $ mailCode = "0"

    scene black with fade
    show text "The end" with fade
    $ renpy.pause(3.0)
    hide text with fade
return

label tbc:
  scene black with fade
  show text "To be continued..." with fade
  $ renpy.pause(3.0)
  hide text with fade
return