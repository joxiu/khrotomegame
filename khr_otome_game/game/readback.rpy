# readback.rpy
# drop in readback module for Ren'Py (v.6.7.1 and higher)
# by delta
# this file is licensed under the terms of the WTFPL
# see http://sam.zoy.org/wtfpl/COPYING for details

init -2 python:

    # Two custom characters that store what they said
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            return

    # this enables us to show the current line in readback without having to bother the buffer with raw shows
    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)


    adv = ReadbackADVCharacter(show_function=say_wrapper)
    nvl = ReadbackNVLCharacter()
    config.locked = False
    config.readback_buffer_length = 100 # number of lines stored
    config.readback_full = True # True = completely replaces rollback, False = readback accessible from game menu only (dev mode)
    config.readback_disallowed_tags = ["size"] # a list of tags that will be removed in the text history
    config.readback_choice_prefix = ">> " # this is prefixed to the choices the user makes in readback
    config.locked = True
    
    readback_buffer = []
    entered_from_game = False
    
    
    
    layout.provides("text_history")
    
    config.game_menu.insert(1,( "text_history", u"Text History", ui.jumps("text_history_screen"), 'not main_menu'))
    config.nvl_show_display_say = say_wrapper

    style.create("readback_text", "say_dialogue")
    style.readback_text.size= 16
    style.readback_text.color = "#333333"
    style.create("readback_label", "readback_text")
    style.readback_label.bold = True
    style.create("readback_window", "file_picker_frame")
    style.create("readback_window_box", "file_picker_frame_box")
    style.create("readback_content", "default")
    style.readback_content.background = None
    style.readback_content.xpadding = 10
    style.readback_content.xmargin = 8
    style.readback_content.ymargin = 8
    style.readback_content.background = Solid("#eeeeee")
    style.create("readback_viewport", "default")
    style.readback_viewport.xmaximum = 900
    style.readback_viewport.clipping = True


init 2 python:

    def menu(items, **add_input): #overwriting standard menu handler
        newitems = []
        for label, val in items:
            if val == None:
                narrator(label, interact=False)
            else:
                newitems.append((label, val))
        rv = renpy.display_menu(newitems, **add_input)
        for label, val in items:
            if rv == val:
                store_say(None, config.readback_choice_prefix + label)
        return rv

    ## readback
    def store_say(who, what):
        global readback_buffer
        new_line = (preparse_say_for_store(who),preparse_say_for_store(what))
        readback_buffer.append(new_line)
        readback_prune()

    current_line = None
    def store_current_line(who, what):
        global current_line
        current_line = (preparse_say_for_store(who), preparse_say_for_store(what))

    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"
    
    import re
    remove_tags_expr = re.compile(disallowed_tags_regexp) # remove tags undesirable in readback
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return re.sub(remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]

    def readback_catcher():
        ui.add(renpy.Keymap(rollback=ui.callsinnewcontext("_game_menu", "text_history_screen")))
        ui.add(renpy.Keymap(rollforward=ui.returns(None)))

    if config.readback_full:
        config.rollback_enabled = False
        config.overlay_functions.append(readback_catcher)


label text_history_screen:
    python:
        layout.navigation("text_history")

        yadj = ui.adjustment()
        
        if not current_line and len(readback_buffer) == 0:
            lines_to_show = []
        elif current_line and len(readback_buffer) == 0:
            lines_to_show = [current_line]
        elif current_line and current_line != readback_buffer[-1]:  # current line may not yet be in rb buffer, but has the same format
            lines_to_show = readback_buffer + [current_line]
        else:
            lines_to_show = readback_buffer

        ui.window(style="readback_window")
        ui.vbox(style="readback_window_box")
        #ui.text("Text History", style="prefs_label")


        ui.side(('c', 'r'), spacing=5)
        ui.window(style="readback_content")
        vp = ui.viewport(draggable=True, offsets=(0.0,1.0), mousewheel=True, style="readback_viewport")
        ui.vbox()
        ui.null(height=10)
        for line in lines_to_show:
            if line[0] and line[0] != " ":
                ui.text(line[0], style="readback_label")
            ui.text(line[1], style="readback_text")
            ui.null(height=10)
        ui.close()
        ui.bar(adjustment=vp.yadjustment, style='vscrollbar')

        ui.close()

        ui.close()
        ui.interact()
        
        renpy.jump("text_history_screen")

