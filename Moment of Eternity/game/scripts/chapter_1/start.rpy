label chapter_1_start:

    scene bg_chapter1_ru with averagedissolve

    $ renpy.pause(2.5)

    if flag_phil_proposition:
        jump phil_home_start

    else:
        jump chapter_1_hotel_start
