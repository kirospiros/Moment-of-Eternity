define me = Character('Я', color="#2E8B57")
define enj = Character('Энджи', color="#7B68EE")
define phil = Character('Фил', color="#F0FFFF")
define key = Character('Кей', color="#8B008B")
define nat = Character('Натали', color="#B0E0E6")
define v = Character('Голос', color="#ffffff")
define sp = Character('Диктор', color="#c8ffc8")
define wa = Character('Официант', color="#c8ffc8")

define un = Character('?', color="#8B008B")
define un_e = Character('?', color="#7B68EE")
define un_p = Character('?', color="#F0FFFF")
define un_n = Character('?', color="#B0E0E6")
define un_s = Character('?', color="#FFE4E1")
define syst = Character('system', color="#B0E0E6")

define gigodissolve = Dissolve(3.3)
define normdissolve = Dissolve(1.1)
define slowdissolve = Dissolve(0.8)
define averagedissolve = Dissolve(0.5)
define fastdissolve = Dissolve(0.3)
define superfastdissolve = Dissolve(0.1)

# music
define audio.deepspace = "music/DeepSpace.mp3"
define audio.solace = "music/Solace.mp3"
define audio.november = "music/November.mp3"
define audio.whales = "music/Whales.mp3"
define audio.lounge = "music/The_Lounge.mp3"
define audio.coolride = "music/CoolRide.mp3"
define audio.corporationmotivation = "music/CorporationMotivation.mp3"
define audio.different = "music/Different.mp3"
define audio.goodvibes = "music/GoodVibes.mp3"
define audio.interconnected = "music/Interconnected.mp3"
define audio.drifting2 = "music/Drifting2.mp3"


# Начало здесь:
init:
    # character points
    $ enj_p = 0
    $ phil_p = 0
    $ key_p = 0

    # flagues
    $ flague_phil_proposition = 0
    $ flague_roof = 0
    $ flague_choice1_retard = 0
