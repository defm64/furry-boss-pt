init offset = 999
screen main_menu():
    tag menu
    add gui.main_menu_background
    frame:
        style "main_menu_frame"
    use navigation
    if gui.show_name:
        vbox:
            style "main_menu_vbox"
            text "[config.name!t]":
                style "main_menu_title"
            text "[config.version]":
                style "main_menu_version"
    imagebutton auto "defm64/defm64_%s.png" xpos 10 ypos 974 action OpenURL("https://allmylinks.com/defm64")
screen about():
    tag menu
    use game_menu(_("Credits"), scroll="viewport"):
        style_prefix "about"
        vbox:
            text _("Made by")
            text "{color=#9933ff}Dirty Fox Games{/color}\n"
            text _("Art")
            text "{color=#9933ff}Xsissa{/color}\n"
            text _("Music")
            text "{color=#9933ff}Antti Luode{/color}\n"
            text _("Additional help")
            text "{color=#9933ff}Zyrilix{/color}\n"
            text _("Portuguese translation")
            text "{a=https://allmylinks.com/defm64}defm64{/a}"
screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton "English" action Language(None)
                    textbutton "Português" action Language("portuguese")
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
default persistent.language_selected = False
label splashscreen:
    if not persistent.language_selected:
        scene bg cabinet blur with fade
        menu:
            "English":
                $ renpy.change_language(None)
                $ persistent.language_selected = True
            "Português":
                $ renpy.change_language("portuguese")
                $ persistent.language_selected = True
