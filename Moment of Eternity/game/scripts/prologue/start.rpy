label prologue_start:
    # Пролог: Воспоминания о грядущем - Мимолётный сон.
    # Prologue: Memories of the Future - A Fleeting Dream.

    scene black with averagedissolve
    play music deepspace fadeout 0.7

    show screen textmiddle("Пролог - точка отсчёта") with averagedissolve
    $ renpy.pause(1.7)
    hide screen textmiddle with averagedissolve

    # hide screen textmiddle with averagedissolve

    vox "Я помню день, когда изменилось всё."
    vox "Тогда я стоял на холме..."
    vox "В последний раз я видел мир таким, каким я его помнил."

    vox "Я пытался впитать в себя каждое мгновение."
    vox "Ведь я знал, что..."
    vox "время моей жизни стремительно близилось к нулю."

    vox "День, принёсший миру великое бедствие."
    vox "Чтобы мы ни делали, оно рано или поздно наступило бы."
    vox "Даже если бы все встали на колени и молили о спасении..."
    vox "Не было бы никого, кто смог спасти нас."

    vox "\"Ничто мне не поможет.\" "
    vox "\"Никто меня не спасет.\" "

    vox "Большая тень накрыла знакомый город."
    vox "Грохот раскалял уши,"
    vox "когда миллионы голосов вспыхнули в агонии,"
    vox "и внезапно утихли..."

    jump prologue_bg_night_room_light_off
