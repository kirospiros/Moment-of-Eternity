image splash = "gui/game_intro.png"

label splashscreen:
    scene black
    with Pause(0.5)

    show text "This game may contain NSFW content." with slowdissolve
    with Pause(0.7)
    hide text with slowdissolve

    show text "Project of" with slowdissolve
    with Pause(0.7)
    hide text with slowdissolve

    show splash with normdissolve
    with Pause(0.5)
    scene black with dissolve
    with Pause(0.5)

    return
