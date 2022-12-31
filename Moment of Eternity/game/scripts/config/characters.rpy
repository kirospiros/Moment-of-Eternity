##Определяем персонажей через подобие классов.
# image main_character = "sprites/main_character/main_character.png"
image side main_character = Transform(
    "sprites/main_character/side main_character.png", yalign = 1.0, xalign = -0.1
)

define me = Character(
    _("Я"), image="main_character", color="#2E8B57"
)


# define me = Character(_("Я"), color="#2E8B57")
define enji = Character(_("Энджи"), color="#7B68EE")
define phil = Character(_("Фил"), color="#F0FFFF")
define key = Character(_("Кей"), color="#8B008B")

define natali = Character(_("Натали"), color="#B0E0E6")

define vox = Character(_("Голос"), color="#ffffff")

define speaker = Character(_("Диктор"), color="#c8ffc8")
define waiter = Character(_("Официант"), color="#c8ffc8")

define character_name = "?"
define current_color = "#ffffff"

define unknown = Character(_(character_name), color=current_color)
define system = Character(_("system"), color="#B0E0E6")
