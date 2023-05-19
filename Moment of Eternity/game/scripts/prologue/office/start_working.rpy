label prologue_office_start_working:

    # Пролог: День - Город - Безделье и Работа 2
    # Prologue: Noon - Lounging and Working 2

    scene bg office main_character workroom v1
    with slowdissolve

    "Какое-то время я сидел в своем кабинете."
    "Было немного пыльно, повсюду лежали коробки."
    "Я открывал каждую, брал нужное, потом перетаскивал их на место."
    "Делать было действительно много..."
    "Мой рабочий день официально заканчивается в шесть..."
    "Но похоже я тут задержусь, в лучшем случае, до восьми."
    "Я начал бубнить себе под нос, чтобы немного приободриться."

    me "\"Это отсортировать, тут проверить, там посчитать...\""
    me "\"Вот здесь написать отчет, там составить накладную...\""
    me "\"Это занести в базу. А вот это еще нужно отправить в отдел кадров.\""
    me "\"Вот эти вещи потом в лабораторию...\""

    play music lounge fadeout 2

    "Я занимался делами, ставшими для меня рутиной совсем недавно."
    "Как я и говорил, я был всего лишь мальчиком на побегушках у Кея."
    "То есть он сваливал на меня подобного рода работу."
    "Как директор своего отдела, и как будущий директор кампании H-Dep, он был весьма трудолюбив, однако лидеру не пристало решать такие низкосортные проблемы."
    "Но игнорировать существование таких вещей - нельзя. Всё до мелочи должно быть выполнено."
    "Поэтому, есть я - третий ассистент Кея."
    "Честно говоря, я имею мало представлений, чем сейчас занимаются Энджи и Фил."
    "Из того, что я знаю, Фил задействуется везде, где только возможно. По крайней мере, я думаю, что Фил за день успевает побывать как и в тех. отделе, так и в архивах."
    "А Энджи, в свою очередь, Кей всё время держит при себе."
    "Иногда может показаться, что Энджи - это вице-президент компании."
    "Тем не менее, это не так. Как я понял, Энджи действительно выполняет самую ответственную работу, если сравнивать со мной и Филом."
    "У неё хорошие академические способности, поэтому я не удивлюсь, если ей уже поручают руководить небольшими проектами,"
    "связанными с изучением и анализом данных."
    "Думаю, она без особых проблем сможет получить должность бизнес-аналитика."
    "А учитывая её способность смотреть в корень вещей..."
    "Её таланты точно пригодятся компании."
    "Я думаю, у Кея большие планы на неё, учитывая, как внимательно он её наставляет."
    "А вот что можно сказать про меня..."
    "То я до сих пор удивляюсь, что я тут делаю, и почему меня вообще взяли..."
    "..."
    "Отогнав все лишние мысли прочь, я тщательнее погрузился в чтение внушительной кипы бумаг с метаданными, связанных с моим текущим заданием..."

    scene bg office main_character workroom v1
    with fade

    jump prologue_office_tired


label prologue_office_tired:

    "..."
    "\"Э-эхх.\""
    "Я сладко потянулся."
    "Часы на стене тут не работали, но начался обеденный перерыв..."
    "Ведь сейчас из одного динамика на противоположной стене играла мягкая мелодия."
    "Она всегда оповещает нас о начале и конце перерыва..."
    "Обычно это время я проводил в одиночестве."
    "Ходил в столовую, покупал какую-нибудь еду, и возвращался сюда."
    "Хорошо было бы взять перерыв."
    "Но с другой стороны, может мне стоит работать дальше, чтобы пораньше вернуться домой?"

    stop music fadeout 2

    menu:
        "Хотелось бы всё-таки отдохнуть":
            jump prologue_office_retard

        "Продолжить работать":
            jump prologue_office_work
