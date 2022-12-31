## Определяем персонажей вместе с их изображениями.

define me = Character(
    _("Я"), image="main_character", color="#2E8B57"
)


define enji = Character(_("Энджи"), color="#7B68EE")
define phil = Character(_("Фил"), color="#F0FFFF")
define key = Character(_("Кей"), color="#8B008B")

define natali = Character(_("Натали"), color="#B0E0E6")

define vox = Character(_("Голос"), color="#ffffff")

define speaker = Character(
    _("Диктор"), image="speaker", color="#c8ffc8"
)

define waiter = Character(_("Официант"), color="#c8ffc8")

define character_name = "?"
define current_color = "#ffffff"

define unknown = Character(_(character_name), color=current_color)
define system = Character(_("system"), color="#B0E0E6")


## Определяет плавное появление и исчезновение новых side-изображений.
## Dissolve работает некорректно, без плавного перехода
transform change_transform(old, new):
    ## При исчезновении со сцены
    contains:
        old
        yalign 1.0
        alpha 1.0
        linear 0.25 alpha 0.0
    ## При появлении на сцене
    contains:
        new
        yalign 1.0
        alpha 0.0
        linear 0.25 alpha 1.0

define config.side_image_change_transform = change_transform

## По мере необходимости: отвечает за переход между side-изображениями одного и
## того же персонажа. В `same_transform` нужно будет расписать `old` и `new`.
# define config.side_image_same_transform = same_transform
