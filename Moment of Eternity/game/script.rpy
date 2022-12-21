define gigodissolve = Dissolve(3.3)
define normdissolve = Dissolve(1.1)
define slowdissolve = Dissolve(0.8)
define averagedissolve = Dissolve(0.5)
define fastdissolve = Dissolve(0.3)
define superfastdissolve = Dissolve(0.1)


# Начало здесь:
init:

    # character points
    $ enji_p = 0
    $ phil_p = 0
    $ key_p = 0

    # flagues
    $ flague_phil_proposition = 0
    $ flague_roof = 0
    $ flag_prologue_office_retard = 0


label start:
    jump prologue_start
