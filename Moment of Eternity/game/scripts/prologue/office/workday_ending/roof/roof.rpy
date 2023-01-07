label prologue_went_to_roof:

    $ flag_roof = True

    "..."
    "Желание вновь оказаться на крыше оказалось сильнее."
    "Я сел в лифт и поехал на верхний этаж."

    scene bg office stairs
    with fade

    "Меня встретила та же лестница и похожий узкий коридор..."
    "Дело в том, что лифт не шел непосредственно на крышу."
    "Чтобы туда попасть, нужно было подняться по ступеням последнего этажа."
    "..."
    "Я медленно шел вверх."
    "Выход на крышу закрывала массивная дверь."
    "Странным было то, что она ни разу на моей памяти не была заперта."
    "Поэтому любой мог спокойно там проводить время."
    "Но самым интересным было то, что кроме меня этой возможностью никто не пользовался."
    "Я поднимался всё выше..."
    "..!"
    "Внезапно услышал нежданный звук."
    "И как только я открыл дверь..."

    scene bg office rooftop sunset
    with slowdissolve

    jump prologue_met_natali


label prologue_met_natali:

    "..?"

    show natali concerned
    with fastdissolve

    "..."

    me "\"А-а?\""

    "Невольно вырвалось у меня..."

    show natali concerned closed_eyes
    with fastdissolve

    "Я немного удивился."
    "Но не стоило это так показывать."
    "Женщина, которую я видел сегодня утром, чуть ли не на секунду остановила на мне свой слегка недовольный и обеспокоенный взгляд."

    hide natali

    "А затем с завидной скоростью, в то же время излучая спокойствие, спустилась по лестнице позади меня и ретировалась."
    "Спустя минуту, лишь стук её каблуков едва доносился до моих ушей."
    "А вскоре и вовсе стих."
    "Я какое-то время торчал на месте и лишь смотрел на происходящее через левое плечо."
    "Хмм...."

    scene bg office stairs gray
    with fade

    "\"Поэтому любой мог спокойно там проводить время.\""
    "\"Но самым интересным было то, что кроме меня этой возможностью никто не пользовался.\""

    scene bg office rooftop sunset
    with fade

    jump prologue_roof_met_enji


label prologue_roof_met_enji:

    me "\"Как иронично то вышло.\""

    "Похоже, мои ожидания не совсем оправдались."
    "И это уедининое место, где раньше, как предполагалось, я мог спокойно проводить время в одиночестве, уже не смотрелось настолько перспективно..."
    "На крыше не было ничего интересного."
    "Поэтому поначалу меня заинтересовало, что могла здесь делать эта незнакомка."
    "..."

    me "\"Вот оно что...\""

    "Теперь мне всё стало понятно."

    show enji sorried
    with fastdissolve

    with Pause(1.5)

    hide enji
    with fastdissolve

    "Я сделал вид, будто не заметил её."
    "Я стоял поодаль, устремив свой взгляд в небо."
    "Не думаю, что она не увидела меня."
    "Но по крайней мере, Энджи делала вид, будто её не интересует ничего, кроме одиночества."
    "Я еще раз тайком взглянул на неё."

    show enji upset
    with averagedissolve

    "Она точно смотрела куда-то вниз."
    "До этого у неё был виноватый вид, сейчас же она выглядела немного подавленной."
    "Впервые вижу её такой..."

    hide enji upset
    with fastdissolve

    "Не думаю, что Энджи пришла бы на крышу просто так."
    "Между ними явно что-то произошло."
    "Это уже не говоря о том, что я вообще никак не могу трактовать действия той незнакомки..."
    "..."
    "Не то, чтобы мне было сильно любопытно."
    "Я с самого начала не собирался ввязываться в разборки, если таковые действительно имели место."
    "К тому же, разговаривать сейчас с Энджи в такой неловкой для неё ситуации было бы глупо."
    "Мало ли, чего можно от неё ожидать..."
    "Я, кстати, был немного удивлен, что она не припомнила мне тот утренний случай в общем зале."
    "Наверное, она не злопамятная."
    "Может, у нее нет настроения."
    "Независимо от причины, мне это на руку."
    "..."

    show enji thinking
    with fastdissolve

    "Тишина..."
    "Лишь ветер иногда пролетал, встряхивая её короткие волосы."
    "На секунду мне показалось, что Энджи тут нет, а вижу я призрака или галлюцинацию."
    "Да, настолько было безмятежним это зрелище."
    "Возможно, Энджи, как и я, сейчас приводила мысли в порядок."
    "А ведь если подумать, ей было тяжелее, чем мне."

    hide enji
    with slowdissolve

    "Чтобы меня не заклеймили извращенцем, я больше не смотрел в ее сторону."
    "Опершись на перила забора, что окружал всю крышу многоэтажки, я закрыл глаза и решил насладиться свободой еще какое-то время."

    scene black
    with normdissolve

    "..."
    "..."
    "..."

    jump prologue_office_roof_start_dialogue


label prologue_office_roof_start_dialogue:

    enji "Скажи..."

    scene bg office rooftop sunset
    with slowdissolve

    show enji speaking down
    with averagedissolve

    play music interconnected fadeout 3

    "..?"

    show enji speaking
    with averagedissolve

    enji "c чем у тебя ассоциируется высота?"

    show enji siding
    with averagedissolve

    "В её речи и жестах не было ни ноток гордости, ни надменности, ни презрения."
    "Я чувствовал лишь любопытство."
    "И я не мог промолчать:"

    me "\"Никогда об этом не думал, но...\""

    jump prologue_office_roof_enji_question


label prologue_office_roof_enji_question:

    menu:
        "Наверное, это просто красиво.":
            jump prologue_office_roof_enji_answer_false

        "Мне кажется, вид с большой высоты безграничен. Вызывает и тревогу, и безмятежность.":
            jump prologue_office_roof_enji_answer_true


label prologue_office_roof_after_answer:

    show enji usual
    with fastdissolve

    me "\"Честно, повторюсь, никогда особо об этом не думал. У меня раньше никогда не возникало четких ассоциаций по этому поводу.\""

    show enji speaking down
    with fastdissolve

    enji "Когда смотришь на мир, в котором живешь, возникают и другие мысли..."
    enji "Вид с высоты также может вызвать и противоречивые чувства."

    "Энджи продолжала мыслить вслух, не обращая на меня внимания."

    enji "Можно почувствовать величие, находясь в роли наблюдателя, но и чувство небезопасности."
    enji "Слишком обширный вид поставит тебя в деликатное положение: являясь наблюдателем, ты будешь видеть барьер между собой и миром, но в то же время ты будешь осознавать, что ты всё ещё его часть."

    "?"
    "Чувствуя мое недопонимание, она взглянула на меня."

    show enji speaking
    with fastdissolve

    enji "Мир - лишь то, что мы можем ощутить. Ведь у нас нет других способов его воспринимать."
    enji "Разум подсознательно отделяет то, что мы чувствуем, и то, что мы знаем."
    enji "Сейчас реальным для тебя является эта площадка на крыше небоскреба, а всё, что ты видишь далеко внизу, воспринимается как нечто иное."
    enji "Тем более, если речь идет о каком-нибудь другом городе или даже стране."
    enji "То, и другое - мир, в котором ты живешь, но ведь эта площадка кажется тебе более реальной, чем далекий вид с высоты?"
    enji "На самом деле, между ними никакой разницы нет, ведь правильнее осознавать бо́льший, видимый тобой мир, а не только пространство рядом с тобой."
    enji "Но последнее ощущается тебе более реальным. Забавно получается..."
    enji "Вот такие мысли в твоей голове вызывет вид с высоты, замечаешь ты это или нет."

    show enji siding
    with fastdissolve

    "..."
    "Ни с того ни с сего, Энджи поделилась со мной такими ... понятными мыслями."
    "После её слов, я кое-что осознал."
    "Я делал это для того, чтобы понять такое знакомое странное чувство."
    "Каждый раз, стоя здесь и наблюдая за всем с высоты, я невольно сталкивал свой разум, руководствующийся логикой, и опыт, задетый чувствами..."
    "В отличии от повседневной жизни, где подобный процесс протекает размеренно, здесь, высоко над землей, всё это начинает резко обостряться."

    hide enji siding
    with averagedissolve

    "Странно выходит."
    "Я ощущал некоего рода дискомфорт, слушая Энджи."
    "Ибо она говорила о довольно очевидных вещах."
    "Которые можно понять, не прилагая никаких усилий."
    "Но порой..."
    "такие простые вещи трудно заметить."
    "Осознание этого раньше часто приходило ко мне, но в то же время не задерживалось..."
    "Останется ли {i}это{/i} чувство у меня надолго?"

    enji "..."

    stop music fadeout 3

    "Похоже, мой обеспокоенный вид слегка позабавил Энджи."

    show enji smiling evil
    with fastdissolve

    pause 0.8

    hide enji
    with averagedissolve

    "Оставляя меня в недоумении, она тихо ушла."
    "Я какое-то время стоял и размышлял о кое-чем более важном:"

    me "\"Был ли это своеобразный способ Энджи отомстить мне за случившееся утром?\""

    jump prologue_went_to_key
