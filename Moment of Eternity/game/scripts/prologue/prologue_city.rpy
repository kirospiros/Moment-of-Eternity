label prologue_city_train_station:
    # Пролог: Утро - Город - Станция
    # Prologue: Morning - City - Station.

    scene bg_city_train_station
    with slowdissolve
    pause 0.3

    "Наконец я прибыл в FYTLu#324."
    "Вьезжая в город, поезд уже нигде не останавливался и помчался к центральной станции, петляя по всяким тоннелям и мостам."
    "Время - пол десятого, но я уже давно смирился с тем, что опоздал, ведь официально мой рабочий день начинается в девять..."

    me "\"Мне следует искрене извиниться, когда его увижу...\" "

    "Был бы у меня телефон, я мог бы позвонить и предупредить, что снова опоздаю."
    "И в очередной раз я страдаю от собственной глупости."
    "Я чувствую себя подавленным, но для меня это уже давно не в новинку."

    jump prologue_city_main_station


label prologue_city_main_station:

    scene bg_city_main_station
    with slowdissolve
    pause 0.2

    "Я вышел из вагона и какое-то время просто рассеяно смотрел по сторонам, думая, как мне отсюда добраться в центр."
    "Не знаю точно, сколько я стоял, но через небольшой промежуток времени поезд отбыл."
    "И в этот момент, я увидел лицо знакомого человека, которого не ожидал здесь встретить."

    jump prologue_city_main_station_norm


label prologue_city_main_station_norm:

    scene bg_city_main_station_norm
    with fastdissolve
    pause 0.1

    show key_usual at center

    $ unknown.who_args["color"] = "#8B008B"
    unknown "..."

    hide key_usual

    "Уже при беглом взгляде я понял, кто это был."
    "Что ж, мне в любом случае придеться сегодня извиняться..."
    "Но причина опущенной головы и моего молчания была в том, что я просто уже не мог выдержать угрызения совести..."
    "А всё потому, что в этот день, этот парень самолично приехал забрать меня на работу."
    "Мне уже стало плохо от того, что я подумал, сколько это хлопот ему принесло."
    "Я глубоко вздохнул, повернулся к нему лицом, пристально посмотрел в глаза, и со всем виноватым видом, который я мог изобразить, искренне произнес:"

    show key_usual at center

    me "\"Пожалуйста, простите, что снова вас подвел!\""

    "Я сделал поклон, выразив как и уважение, так и признав свою вину."
    "Не то, чтобы сейчас подобные знаки и жесты были популярны в обществе, но я действительно хотел по-особому извиниться..."
    "Знакомьтесь, один из моих немногих друзей, а также по совместительству мой босс, Кей Константин Корнельевич..."

    jump prologue_city_main_station_key_meeting


label prologue_city_main_station_key_meeting:

    play music lounge fadeout 6
    show key_usual_worried at center
    hide key_usual

    key "Эх..."
    key "Боже..."

    show key_usual_speaking
    hide key_usual_worried

    key "Не часто увидишь такое."
    key "Видимо тебе действительно жаль, раз уж ты прибегнул к формальной форме общения со мной."
    key "Видеть тебя таким немного необычно, поэтому, я думаю, что не зря прождал столько времени, находясь здесь."
    key "Поэтому я уже не сильно сержусь."

    show key_usual at center
    hide key_usual_speaking

    "Весьма ожидаемо. Этот человек может с легкостью понимать, что происходит у тебя в голове. Поэтому скрыть что-то от него будет нелегкой задачей."
    "Я не так давно знаком с Константином, но что точно я знаю, он весьма наблюдателен..."
    "В общении с друзьями, становится расслабленным, но часто уходит в себя. Правда, не всегда приятно слушать его мысли."
    "Может Кей сейчас и выглядит немного серьёзным, но он всегда такой, независимо от того, что делает."

    show key_usual_speaking at center
    hide key_usual

    key "Так, что-то мы долго тут стоим."

    "Его мягкий и задумчивый тон изменился."
    "Вместо этого голос стал более монотонным и деловым."

    key "Доброе утро. Как всегда, надеюсь на твою хорошую работу."

    "Вместе со своим стандартным приветствием, он протянул мне руку, а я, как всегда, крепко пожал её."
    "Сейчас на его лице уже не было того дружелюбия, а всё потому, что пришло время заняться делом."
    "А когда речь идёт о работе, он становится особенно внимательным и ответственным."

    me "\"Что ж, я уже готов на что угодно, Кей.\""

    hide key_usual_speaking

    "Несмотря на то, что он - мой босс, я обращаюсь к нему просто по фамилии, и не использую каких-либо формальных предложений."
    "Когда-то давно, а точнее еще при нашей первой встрече, он сам попросил называть себя просто Кей..."
    "На собеседовании его удивило, что я не выказываю ему никаких признаков уважения, а обращаюсь к нему, как к себе."
    "Затем он слегка посмеялся, сказав, что я первый, кто запросто может с ним так разговаривать."
    "Честно говоря, был бы это кто-другой, меня бы скорее всего выгнали из кабинета."
    "Но тогда, впервые заговорив с этим парнем, я понял, что лучше быть перед ним честным."
    "И это на удивление сработало."
    "..."

    stop music fadeout 3

    jump prologue_city_main_station_left


label prologue_city_main_station_left:

    "Мы покинули место встречи и направились к его машине. Кей шел впереди, а я плелся рядом..."

    me "\"Что-нибудь особенное сегодня?\""

    show key_usual_speaking at center

    key "И да, и нет. Однако учитывая, что ты опоздал, то трудиться будешь допоздна."
    key "Без обид, считай это своим наказанием."

    show key_usual

    hide key_usual_speaking

    me "\"Хех...\""

    "Горько выдавил я из себя."
    "Сейчас Кей звучал так, будто упрекает меня как друг и как начальник одновременно."
    "А он всего-то на четыре года старше меня."
    "Если я, конечно, не запамятовал..."

    hide key_usual with fastdissolve

    # TODO: <НУЖНО 2 CG: 1 - УЛИЦА, ПО КОТОРОЙ ИДУТ ПЕРСОНАЖИ, 2 - ВИД С ОКНА МАШИНЫ>
    # TODO: Пролог: Утро - Город - Поездка в офис | Prologue: Morning - City - Going to the office.

    scene bg_city_streets with averagedissolve

    play music coolride fadeout 3

    jump prologue_city_streets


label prologue_city_streets:

    "Выйдя со станции с западной стороны, мы вышли на широкий тротуар и пошли вверх по улице."

    # TODO: "По левую руку была проезжая часть, бок о бок с ней стояли высокие здания, а еще дальше за ними растянулся парк."
    # TODO: "Справа от нас возвышался аккуратный забор с клумбами, а вскоре этот пейзаж сменился на променад с квадратной плиткой, а по сторонам стали возвышаться стройные деревья."
    # TODO: "Сбоку от дороги изредка можно было увидеть небольшие скверы, обустроенные лавочками."

    "Людей на улице было немного."
    "Так как шли мы быстро, я не мог постоянно отвлекаться и рассматривать всё подряд, но, судя по всему, это был самый обычный городской день."
    "..."
    "И вскоре достигли места - парковочной зоны, - где Кей оставил свою машину."

    jump prologue_city_about_key_car


label prologue_city_about_key_car:

    "С виду это был чёрный городской джип, как всегда выглядевший ухоженным."
    "Но и была у него важная особенность, отличающая его от девяноста процентов машин нынешнего мира."
    "Поначалу и не скажешь, но эта машина также использовала новую энергомеханическую систему с элементом XiJ."
    "..."

    # TODO:
    # "Но, в отличие от электричек LDET-334, которая преобразовывала элемент в некое подобие электро энергии, в автомобилях элемент подвергался термо излучению."
    # "Эффективность этого заключалась в огромном количестве взрывной силы, что позволяла набирать скорость в 250 км/ч за полторы секунды, и развивать максимальную скорость до 600 км/ч ."
    # "Также плюсом являлось то, что сами по себе жидкокристаллические образцы XiJ давали много запасов энергии, а после их плавления автомобиль мог держать ту же скорость."
    # "То есть дополнительная подача энергии за счёт последующей термообработки элемента не была необходимой еще на долгий промежуток времени."
    # "Мало того, была разработана новая универсальная система экстра торможения."
    # "Те же самые частицы элемента XiJ резко подвергались криогенной обработке, и благодаря этому активная затрачиваемая энергия на движение моментально исчезала."
    # "Часть из которой возращалась в специальное stack хранилище, откуда могла быть извлечена и возвращена в эксплуатацию."
    # "..."
    # "Такие технологии, возможно, уже скоро станут частью повседневной жизни среднестатистического человека, но они ещё долго будут удивлять даже такого серого парня, как я..."

    "Мелкими приятными деталями, пожалуй, являются: новейшая система автовождения, улучшенная система безопаности, гибкое и аеродинамическое построение корпуса авто."
    "В таких машинах слова \"уют и спокойствие\" становились банальной повседневностью."
    "А называлась конкретно эта модель - ReZL_a0."
    "Обладать таким - действительно редкость. Не то, чтобы дорого, а пока не всем дозволено."
    "И неудивительно, что такую роскошь могут позволить себе только люди, как \"мистер\" Кэй."
    "..."

    "Во время поездки в офис, я равнодушно глядел в окно и лишь изредка обращал внимание на очередные проносившиеся мимо объекты."
    "Здания, люди, машины..."
    "Не поймите меня неправильно, на самом деле мне нравилось то, что я вижу, даже несмотря на то, что я уже привык часто приезжать в город."
    "На первый взгляд, казалось, всё было одинаково - обычные дни в современном мегаполисе..."
    "Но если быть чуточку внимательнее, то каждый день покажется тебе совершенно иным."
    "Эта повседневная рутина могла раздражать, на даже в ней можно было найти нечто особенное."
    "Или..."
    "Мне просто хотелось, чтобы так и было."
    "Каждый раз проезжая мимо знакомых мест, я невольно бросал взгляд в надежде увидеть что-то новое и необычное."
    "Но даже если какие-то небольшие детали и менялись."
    "То для меня общая картина оставалась одной и той же."

    jump prologue_office_entry
