label chapter_1_start:

    scene black with averagedissolve

    show screen textmiddle("Глава I") with averagedissolve
    $ renpy.pause(1.7)
    hide screen textmiddle with averagedissolve

    if flag_phil_proposition:
        jump phil_home_start

    else:
        jump chapter_1_hotel_start
