label prologue_went_to_key:

    "..."
    "Я зевнул, завернул за угол и побрел к лифту."

    scene black
    with fade

    pause(0.7)

    jump prologue_office_report_key

# Вечер - Город - Предложение Кея
# Evening - City - Key's Proposal

label prologue_office_report_key:

    scene bg office head_office sunset
    with averagedissolve

    play music lounge fadeout 4

    if flag_roof:

        show key usual speaking kindly
        with averagedissolve

        key "Ты позднее, чем обычно."
        key "Снова наслаждался видом с крыши?"

        show key usual smiles
        with fastdissolve

        me "\"М-м-м...да. Так уж вышло, что мне пришлось дольше проветриваться.\""

        "..."

        key "Да, по тебе видно."

        hide key

    show key usual speaking kindly
    with fastdissolve

    key "Я так понял, что у тебя на сегодня с работой покончено. Всё успел?"

    show key usual
    with fastdissolve

    me "\"Не совсем, кое-что ещё осталось. Вот нужные отчеты, остальное донесу потом.\""

    hide key usual
    with fastdissolve

    "Я вытащил из портфеля папки с бумагой, и положил на стол Кея."

    show key usual worried
    with averagedissolve

    key "Работы было действительно много, поэтому я не удивлен, что ты не успел."
    key "Тем не менее, я надеюсь на то, что ты выполнял дело тщательно, и ни у кого не будет неприятностей."

    "Устало подчеркнул Кей."
    "Видимо, у него тоже был нелегкий день."

    if flag_prologue_office_retard:

        "Интересно, стоит ли ему признаться, что сегодня в обед я немного прохалявил?.."
        "..."
        "Всё же мне бы не хотелось создавать ему проблем."

    else:

        "Мне бы не хотелось создавать ему проблем."

    show key usual smiles
    with fastdissolve

    jump prologue_office_surprise_key


label prologue_office_surprise_key:

    key "Ладно, можешь уже расслабиться. Возвращаться домой нужно с хорошим настроением."

    "После столь формального и делового тона, Кей снова начал вести себя по-дружески, возвещая о конце рабочего дня."

    key "Энджи уже отрапортовала мне ранее,  а Фил заходил час назад. Ты последний."
    key "Раз уж вы все закончили, то мне тоже делать нечего. Я уже побеседовал с ребятами из лаборатории и подчиненными из основного зала, раздал нужные указания."
    key "Поэтому сегодня всё должно закончиться как по маслу."

    "..."

    show key usual speaking
    with fastdissolve

    key "И прежде чем мы завершим, я дам тебе кое-что важное."

    me "\"Неужели?\""

    key "Да, раз уж ты сам не можешь о себе позаботиться, то на этот раз придется сделать это мне."

    me "\"О чем ты?\""

    key "Я про твои частые опоздания."
    key "А вот с этим у тебя должно стать меньше проблем."

    show key usual
    with fastdissolve

    "Кей достал из заднего кармана часы и протянул их мне."
    "Но это были именно смарт-часы, а не что-то простое."
    "Я начал вращать их в руках и рассматривать."
    "Вау! Это мне?"

    show key usual smiles
    with fastdissolve

    "Каким бы равнодушным я не оставался, Кей смог заметить моё восхищение."
    "Он стоял, и выжидающе улыбался."
    "Часы были идеально гладкими и отдавали серебряным блеском."
    "На нежно-синем глянцевом дисплее в режиме блокировки отображалось текущее время в 24-часовом формате: {i}20:07{/i}"
    "Справа от экрана была небольшая кнопочка."

    show key usual speaking kindly
    with fastdissolve

    key "Кнопка переведет режим работы часов в голографический. Но для этого тебе сначала придется разблокировать экран."
    key "Так как теперь это лично твоё устройство, с помощью своего отпечатка пальца ты можешь снять блокировку, когда тебе будет угодно."
    key "Как видишь, я уже обо всём позаботился."
    key "Более того, когда будет время, посиди и покопайся в настройках."

    "..."
    key "А, вот что еще: с него спокойно можно звонить и отправлять сообщения. Мой номер там уже записан."

    show key usual worried
    with fastdissolve

    key "Я знаю, что ты не любишь, когда вмешиваются в твою личную жизнь, и тебе не в радость общаться с кем-то удаленно, но пришло время привыкать..."
    key "К тому же, это один из дополнительных способов наладить твои контакты с Энджи и Филом."
    key "Учитывая, что пора бы вам стать настоящей командой, а не группой людей, лишь имитирующих это понятие."

    show key usual
    with fastdissolve

    key "Я надеюсь, ты понимаешь меня."

    "Последнюю фразу он произнес довольно серьезно."
    "И не то, чтобы я как-то хотел перечить ему."
    "Даже если бы он был младше меня, его мнение практически по-любому поводу куда авторитетней, чем я могу себе представить."
    "В любом случае, я собирался искренне поблагодарить его за столь щедрый подар-"

    show key usual smiles
    with fastdissolve

    key "Вычту из твоей зарплаты (´.• ω •.`)"

    "Ха-а-а?"
    "Я тихо и нервно сглотнул."
    "Ну, да, конечно..."

    key "А ты думал, это за проcто так?"
    key "Вообще-то, тебе следовало купить нечто подобное уже давно, так что не благодари меня."

    "Э-э-эмм..."
    "Я горько усмехнулся."
    "Похоже, надо было купить обычный телефон или что-то подобное."
    "А так, похоже, я сам себя загнал в яму."
    "Думаю, не стоит даже думать о том, сколько на самом деле стоят такие часы."
    "И в этом месяце я уже точно останусь без зарплаты. В худшем случае - ещё и дополнительно придется отрабатывать."
    "Я прищурил глаза и начал сверлить этот дьявольский подарок."
    "..."
    "А ведь отказаться я уже никак не мог..."
    "..."
    "Кей, кажется, понял моё положение."

    show key speaking kindly
    with fastdissolve

    key "Не переживай!"
    key "Я сделал тебе большую скидку. К тому же, такое устройство сейчас есть буквально у единиц."
    key "А я уверен, что скоро оно станет хитовым брендом в высших слоях общества. Да-да, когда придет его время..."

    show key usual
    with fastdissolve

    "Что ж ... похоже у меня нет выбора."
    "Киваю в знак согласия, скрывая своё негодование."
    "Я переворачиваю часы на обратную сторону и вижу логотип кампании H-Dep в виде двух огибающих друг друга стрелок."
    "Кею явно нравятся всякие гаджеты, и поэтому я решил узнать еще кое-что."

    me "\"Я так понимаю, что это благодаря связям в лаборатории?\""

    show key usual speaking kindly
    with fastdissolve

    key "Именно. Я ведь также руковожу здешним отделом разработки, который непосредственно работает на XiJ в условиях временного взаимовыгодного контракта."
    key "Это именно ребята, взращенные H-Dep, а не государством и кампанией XiJ."
    key "Благодаря моему влиянию и небольшой прихоти, правилам эксплуатации и дыркам в контракте, мы смогли уделить время на то, что видишь."

    show key usual worried
    with fastdissolve

    key "По-моему, вышло неплохо, хотя в следующий раз мне нужно быть осмотрительнее."

    me "\"Ладно, я понял.\""

    "Я мягко прервал его, пока он не погрузил меня в пучину своих деловых мыслей, причем не слишком радостных..."

    show key usual speaking
    with fastdissolve

    key "В любом случае, доверие к H-Dep и её эффективность никогда не падали. И я, именем своей семьи, всеми силами не допущу этого."
    key "Итак, пока не будем об этом."

    show key usual speaking kindly
    with fastdissolve

    "Он снова стал самим собой."

    jump prologue_office_key_proposal


label prologue_office_key_proposal:

    key "У меня есть одно предложение. Воспринимай его чисто как дружеское. К работе почти отношения не имеет."
    key "Не желаешь ли ты остановиться в городе на недельку-другую?"

    show key usual smiles
    with fastdissolve

    "Если честно, я ожидал чего-то подобного."
    "С одной стороны это было гарантией для Кея, что я стану относиться ко всему серьезнее, то есть без моей привычной апатии."
    "Также, возможно, он просто заботился о том, чтобы мне нужно было меньше напрягаться утром и вечером, раньше отправляясь на работу и, соответственно, возвращаясь домой."
    "А ещё, ходили слухи: вроде этот месяц обещает быть особо трудным."
    "..."
    "Мне сложно увидеть что-то ещё в его предложении."
    "Но даже если я соглашусь, то где остановлюсь, и сколько это будет стоить?"
    "И будто читая мои мысли-"

    show key usual speaking kindly
    with fastdissolve

    key "На этот раз подвоха нет. У меня есть хорошая комната в приличном отеле, которую я снимаю каждый месяц."
    key "Дело в том, что я сам редко там бываю, так как обычно у меня много дел за пределами офиса. И возвращаться мне ближе домой."
    key "Так что платить тебе не придется. Всё за мой счет!"
    key "Более того, я собирался предложить тебе нечто подобное уже давно."

    show key usual smiles
    with fastdissolve

    "Заманчивое предложение, однако."
    "Возможно, жизнь в городе пойдет мне на пользу, хотя я не так давно сбежал от родителей."
    "..."
    "Впрочем, они живут далеко, и меня точно не найдут."
    "К тому же, мне понравилась мысль {i}бесплатно жить{/i} в роскошном номере и пользоваться его благами."
    "По сути, это будет означать, что я нахлебник, чего и пытался ранее избегать."

    show key usual
    with fastdissolve

    "Я попытался отделаться от этой мысли как можно скорее, но неприятное послевкусие дало о себе знать."
    "Кей сказал, что на этот раз никакого подвоха нет."
    "Но он ведь есть!"
    "Если я остаюсь в этом месяце без зарплаты, мне еле-еле хватит на квартплату моего дома."
    "А значит, если я откажусь и вернусь туда, то могу помереть с голоду."
    "..."
    "Сегодняшний день был вычеркнут мною из категории \"один из приятных\"."

    show key usual speaking
    with fastdissolve

    key "Так что ты решил?"

    show key usual
    with fastdissolve

    me "\"Я не откажусь.\""

    show key usual speaking
    with fastdissolve

    key "Тогда самое время выдвигаться."

    hide key
    with averagedissolve

    if flag_phil_proposition:

        "И тут я кое-что вспомнил."

        me "\"Постой!\""

        show key usual
        with averagedissolve

        me "\"Мне сегодня довелось поговорить с Филом. Не обижайся, что раньше не сказал. Дело в том, что он пригласил меня к себе, и я принял его предложение.\""
        me "\"Я просто только сейчас вспомнил об этом маленьком обещании.\""

        show key usual speaking kindly
        with averagedissolve

        key "Всё в порядке. Может, так даже лучше. Как выйдем на парковку, я позвоню Филу, и мы согласуем, стоит ли завозить тебя к нему сегодня."

        hide key
        with fastdissolve

    stop music fadeout 3

    jump prologue_office_key_end_conversation


label prologue_office_key_end_conversation:

    "Он больше ничего не сказал и покинул кабинет."
    "Я последовал за ним."

    scene black
    with fade

    "Таким образом, ко мне вернулась шумная городская жизнь."
    "Казалось бы, когда я уже от неё отвык."
    "Жизнь течет размеренно, и большую её часть я провожу на работе, поэтому я не сильно должен заметить смену обстановки."

    if not flag_phil_proposition:
        "Хоть и выбора особо не было..."

    "Но, возможно, принятое решение ознаменует начало новых нежелательных приключений..."

    jump chapter_1_start
