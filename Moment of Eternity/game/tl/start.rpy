define gigodissolve = Dissolve(3.3)
define normdissolve = Dissolve(1.1)
define slowdissolve = Dissolve(0.8)
define averagedissolve = Dissolve(0.5)
define fastdissolve = Dissolve(0.3)

label splashscreen:
    #image warning = Text("Hello, World", size=40)

    scene black
    with Pause(1)

    show text "This game may contain NSFW content." with slowdissolve
    with Pause(2)

    hide text with slowdissolve
    with Pause(1)

    show text "Project of" with slowdissolve
    with Pause(2)

    hide text with slowdissolve
    with Pause(1)

    scene bg_full_solo_evade with normdissolve
    with Pause(2)

    scene bg_nothing with dissolve
    with Pause(2)

    return
