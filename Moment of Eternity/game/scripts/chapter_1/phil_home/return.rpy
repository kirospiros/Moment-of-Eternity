label chapter_1_return_home:

    # Глава 1: Вечер. Снова обычный вечер.
    # Chapter 1: Evening. Another usual evening.

    "Да, лучше вернуться домой."
    "К тому же, наверняка уйдет еще некоторое время, чтобы найти дорогу обратно."
    "А бегать за кем-то по всему району мне особо-то и хочется."

    scene bg phil_home room evening
    with averagedissolve

    pause(0.5)

    "Когда я вернулся к Филу, солнце уже почти село."
    "Я тихо открыл входную дверь, разбулся, пересек кухню и вошел в его комнату."

    show phil casual
    with averagedissolve

    phil "Добрый вечер!"

    "Как только я задумался о том, почему Фил не запирает входную дверь в свой дом, он появился у меня за спиной и выдал бодрое приветствие."
    "Меня такое появление вовсе не смутило, ведь я собирался ответить ему словами, подобранными заранее."

    me "Прости за мое поведение этим утром. Не следовало так мне поступать."

    show phil casual smiling
    with averagedissolve

    phil "Всё в порядке. Если честно, ко мне мало кто приходил ночевать, поэтому я не расстроился, когда ты ушел. И развлеклись мы неплохо."

    "В качестве изивинения я хотел помочь ему с уборкой, но, кажется, Фил недавно закончил: вид у него был усталый."

    show phil casual
    with fastdissolve

    "Тем не менее он счастливо улыбался."

    hide phil casual
    with fastdissolve

    "Комната выглядела так, словно в ней ничего не произошло, а воздухе витал несколько приятный аромат хлора... {w=1.2} и каких-то эфирных масел."
    "Не по-девчачьи ли это?"
    "Правда, немного пробежавшись взглядом по полу комнаты, я увидел знакомые открытые книжки и несколько скомканных бумажек."
    "Прошлая мысль быстро улетучилась."
    "Наверное, таков был творческий беспорядок Фила. Не убрал привычный для себя вид."

    show phil casual speaking
    with averagedissolve

    phil "Аэрозоли давно признаны вредными для здоровья."

    "Высказался Фил."

    hide phil
    with fastdissolve

    scene bg phil_home room evening
    with fade

    pause(0.5)

    jump chapter_1_watching_tv


label chapter_1_watching_tv:

    # <Нужен полностью ночной фон комнаты Фила>

    "Остаток вечера мы провели за просмотром какого-то фильма, заодно наслаждаясь лимонной газировочкой, что ловко состряпал Фил."
    "Кстати, у него здорово получается!"
    "..."
    "Про что был фильм?"
    "На самом деле, Фил любезно предоставил выбор мне, но я отказался, намекнув, что переварю что угодно."
    "Как вспомню себя беззаботного несколько лет назад, аж больно становится..."

    scene black
    with slowdissolve

    "Не считая выходных, у меня почти не было свободного времени, и, казалось, я должен использовать его для себя без остатка."
    "Наслаждаться каждой секундой..."
    "Но сравнивая, сколько было времени на увлечения раньше, чем сейчас ... Мне хотелось всё бросить, чтобы лишний раз не сосредотачиваться на прошлом \"я\"."
    "И жить сегодняшним днем."
    "Мой максимализм давно исчез, лишь ностальгией пробиваясь из прошлого."
    "Под натиском безжалостного времени мне пришлось изменить себя."
    "В итоге, на выходных я занимаюсь чем попало, под настроение, а стиль моей жизни не сильно отличается от образа бытия ленивца."
    "Добро пожаловать во взрослую жизнь..?"

    scene bg phil_home room evening
    with fastdissolve

    show phil casual
    with fastdissolve

    phil "Эй, ты как? Чего приуныл?"

    me "Смотри! Сейчас этот парень решиться и побежит в клубную комнату!"

    show phil casual relief
    with fastdissolve

    pause(0.2)

    show phil casual relief closed_eyes
    with fastdissolve

    hide phil casual relief closed_eyes
    with slowdissolve

    "Я сделал вид, будто внимательно смотрю фильм, который выбрал Фил."
    "По сюжету вокруг невзрачного паренька внезапно начала крутиться однокурсница."
    "На первый взгляд порядочная и замкнутая, а позже выяснилось, что очень энергичная, упрямая и по-глупому ребяческая."
    "Кажется, весь мир крутится вокруг нее ... {w=1} и это оказалось правдой. {w=1} В прямом смысле."
    "Парень поневоле вступил в её клуб, где проводили время еще несколько неординарных личностей."
    "В какой-то момент они вместе начали решать её сверхъестественные проблемы, как говорится, \"главный герой натерпелся по полной\"."
    "Но самое интересное случилось вконце: парень, отказавшись от всех будущих невзгод, завязал с клубом."
    "И так вышло, что как только он понял, что всё это время с ней он {i}по-настоящему жил{/i}..."
    "В конце концов, он потерял как и её, так и всех знакомых из клуба."
    "Все они исчезли из его жизни, как будто ничего не было, и он их больше не видел."
    "..."
    "Время от времени мы перекидывались с Филом комментариями, а когда я делал предположения, Фил охотно кивал \"Ага\", прислушиваясь к моему мнению."
    "Действительно, большинство моментов я угадывал не напрягаясь, а ближе к концовке происходящее наконец стало мне интересным."
    "Сказывался мой опыт просмотра разнообразных фильмов."
    "Когда история подошла к концу, я лишь огорчённо пожал плечами, а Фила аж пробило на скупую слезу."
    "Мне казалось, будто фильм говорит нам быть искренними в своих желаниях и искать счастье на пустом месте."
    "Хотя ни прошлый, ни нынешний я скорее всего не приняли бы этого."
    "А Фил воспринял всё близко к сердцу."
    "Но даже так я был рад этому, ведь не чувствовал чего-то фальшивого."
    "По итогу сегодняшнего вечера следовало бы сказать,"
    "что в отличие от меня, Фил не потерял прошлого себя, и в противовес главному герою фильма искренен с собой и окружающими."
    "Ох, почему-то на секунду завидно стало..."
    "Зато Фил был таким, каким он есть."
    "Я точно не знаю, какие фильмы он обычно смотрит, какие девушки ему нравятся..."
    "Что предпочитает читать. О чем думает, когда говорит."
    "Однако в душе я начал понимать, что за его легкомысленным мальчишеством стоит собственная гордость и упрямство в отношении общества."
    "Возможно, это как раз то, на что вскольз также упоминала Энджи."

    scene black
    with fade

    "Вскоре, после фильма, мы легли спать молча, а наши сердца были слегка отягощены."
    "На ночь мы договорились посмотреть нейтральный фильм, насколько это было возможно, а в итоге получили меланхолию."
    "Ну не подстава ли это?"
    "Впрочем, винить было некого и в данном случае не особо хотелось."

    # TODO: jump finish result chapter_1/district/start
