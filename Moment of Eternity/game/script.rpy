define gigodissolve = Dissolve(3.3)
define normdissolve = Dissolve(1.1)
define slowdissolve = Dissolve(0.8)
define averagedissolve = Dissolve(0.5)
define fastdissolve = Dissolve(0.3)
define superfastdissolve = Dissolve(0.1)


# Начало здесь:
init:

    # character points
    $ enji_points = 0
    $ phil_points = 0
    $ key_points = 0

    # flagues
    $ flag_phil_proposition: bool = False
    $ flag_roof = 0
    $ flag_prologue_office_retard: bool = False


label start:
    jump prologue_start
