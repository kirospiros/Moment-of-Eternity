label chapter1:
    scene bg_chapter1_ru
    with averagedissolve
    $ renpy.pause(3.0)
    if flague_phil_proposition == 1:
        jump phil_home

    else:
        jump your_hotel

    # Глава 1: Утро. Дом Фила. Прийти в себя

label phil_home:
    scene bg_nothing with fade
    $ renpy.pause(1.5)
    "..."
    "Голова раскалывается..."
    "Сознание плывет."
    "Я едва ли могу соображать..."
    "Я еще сплю, или нет?.."
    "Что я помню, а что я забыл?.."
    "В голове проносились разные не однозначные варианты событий, но одно мне показалось наиболее вероятным, и..."
    un_p "\"Х\#р\#\#о \@ак в\@\$\%л, да?...\""
    "..."
    "Что это?"
    "Я услышал голос, но звучал он так, будто меня только что вытащили из воды."
    "Я открыл глаза и заставил поднять своё тяжелое тело."
    scene bg_phil_room_blured2 with fade
    $ renpy.pause(1.5)
    me "Че--ёрт..."
    "Всё что я мог сделать - это простонать, в ожидании того, когда я начну ощущать хотя бы признаки нормального состояния."
    "Я закрыл глаза."
    scene bg_phil_room_blured1 with fade
    $ renpy.pause(1.5)
    "И открыл их снова."
    scene bg_phil_room with fade
    $ renpy.pause(0.5)
    show phil_casual_smiling with fastdissolve
    me "А-а-а!"
    phil "Йо."
    "Несмотря на то, что я увидел знакомую личность, я издал нелепый вскрик и слегка попятился назад."
    "!"
    me "Ить..."
    "В итоге ударился затылком о стену."
    show phil_casual_speaking
    hide phil_casual_smiling with averagedissolve
    phil "Хех, прости."
    phil "Ты выглядел таким несобранным, что мне очень захотелось подшутить."
    show phil_casual
    hide phil_casual_speaking with fastdissolve
    me "...Что происходит?"
    show phil_casual_relief
    hide phil_casual with fastdissolve
    phil "А-а, так ты не помнишь... Получается, здорово ты нахрючился."
    phil "Но не волнуйся, сегодня суббота, так что никто об этом не знает, кроме меня."
    show phil_casual_relief_2
    hide phil_casual_relief with averagedissolve
    me "Я не очень понимаю, но чтобы я тут не вытворял, пожалуйста, оставь это в секрете."
    me "Не вздумай проболтаться Кею или Энджи."
    show phil_casual_speaking with slowdissolve
    hide phil_casual_relief_2
    phil "Конечно. Я умею хранить секреты."
    "Ага, так я и поверил."
    hide phil_casual_speaking with fade
    me "Эххх..."
    "Я потянулся, и вскоре начал приходить в себя."
    "Я с трудом мог вспомнить, что происходило вчера после работы."
    "Похоже, что я действительно перебрал. А я ведь обычно не пью."
    "Однако, как доказательство моего преступления, я увидел много разбросанных бутылок по комнате."
    "Когда я привстал и осмотрелся, я понял, что всю ночь провалялся на полу."
    "Мятая подушка упёрлась в стену, а покрывало с кровати сползло, будто его дернули вниз."
    "..."
    "Сползло..? Погодите."
    show phil_casual_speaking with fastdissolve
    phil "Вообще, предполагалось, что я уложу тебя где-нибудь в другом месте, но в том состоянии тебя было трудно доставить в другую комнату."
    phil "В итоге, когда я лег спать на кровать, ты, кажется, разозлился, то ли на меня, то ли на себя, что перебрал. И силой стащил меня отсюда, а сам рухнул."
    phil "Я был пьян, но точно помню, что ночью ты ворочался и мычал, хех, бедняга. А под утро съехал на пол, обнимая подушку."
    show phil_casual with averagedissolve
    hide phil_casual_speaking
    "Кринж."
    "Мне стало немного стыдно, когда я представил себе такую картину. Наверное, и повода не было столько выпивать."
    "Я на сто процентов уверен, что всё это дело рук Фила."
    show phil_casual_smiling with slowdissolve
    hide phil_casual
    "Скорее всего, я просто оказался здесь по-случайности, он начал рассказывать какие-то нелепые вещи со серьёзным лицом."
    "И вскоре беззаботный я почему-то решил повеселиться на всю катушку."
    "Одолеваемый противоречивыми чувствами, я переводил взгляд то на Фила, то на себя."
    me "Извини, но просить прощения я у тебя не буду."
    show phil_casual_speaking with averagedissolve
    hide phil_casual_smiling
    phil "Извинения приняты! Но, похоже, ты еще не полностью пришел в себя."
    "Грхх..!"
    me "Мне надо прогуляться. Пока."
    hide phil_causal_speaking
    phil "Постой!"
    phil "А кто поможет убрать комнату?"
    "Слегка шатаясь и..."
    "Игнорируя просьбу Фила, я быстро обулся и вышел на улицу."

    # Глава 1: Утро - Прогулка

    scene bg_sleep_district_morning with slowdissolve
    pause(2.0)
    "Какое прекрасное утро!"
    "Я решил избавиться от похмелья благодатной прогулкой."
    "В надежде на то, что воспоминания предыдущего дня вернутся."
    "..."
    "Я топал по дороге спального района, за моей спиной возвышалось здание корпорации, в которой я работаю."
    "Так как до этого я не бывал в этих местах, всё казалось мне довольно незнакомым."
    "Несмотря на то, что утро было субботним, я часто натыкался на прохожих, а один раз умудрился невнимательно перейти дорогу в неположенном месте."
    "Так уж случилось, что на дороге меня окликнул какой-то дядкя. Я тут же остановился, а через секунду мимо меня пронеслась машина и завернула в какой-то переход."
    "А еще во время моей прогулки я, завернув в очередной угол, случайно столкнул какую-то женщину."
    "Эххх..."
    "Вспонимая утро прошедшего дня, я никак не мог не сравнить шум и суету спального района мегаполиса и спокойствие моего дома."
    "Но жизнь в большом городе всегда требует темпа и сосредоточенности."
    "Отчего даже гуляя по улицам, изматываешься быстрее."
    me "Ничего, я скоро привыкну."
    "..."
    "Я достаточно далеко ушел к югу от дома Фила. Здание корпорации всё еще величественно возвышалось на горизонте."
    "Чтобы не всегда идти по главной дороге и в одном и том же направлении, я начал петлять по улочкам."
    "Неизвестное манило меня."
    "Или из-за того, что похмелье еще не прошло, я был более {w=0.8}...азартным?"
    scene bg_vending_machine with slowdissolve
    pause(1.5)
    me "Фух..."
    "Кажется, я немного запыхался."
    "Достаточно побродив в окрестностях, и, чувствуя небольшое утомление, я случайнно обнаружил себя во дворе."
    "Я направился в западную его часть и увидел крытое строение из лакированного дерева, где можно было передохнуть."
    "Я не помню, когда сегодня проснулся, но я нащупал в своем кармане часы, что подарил мне Кей. По 24 часовому формату времени сейчас было 14:01."
    "Я оперся об стену и присел на плитку. Во дворе кроме деревьев и клумб ничего не было, даже ни намека на лавочку."
    "Поэтому пришлось выбирать более удобное место дальше по списку... Внутри также не было никаких специальных мест для сидения."
    "..."
    scene bg_nothing with fade
    pause(0.5)
    "Редкий ветерок, иногда посещавший этот двор, слегка трепетал мои волосы."
    "Вдалеке я слышал легкий шум улиц спального района."
    "Я посидел в таком состоянии несколько минут, и, открывая глаза,"
    scene bg_vending_machine with slowdissolve
    pause(0.5)
    "заметил, что похмелье, благодаря проведенному времени на улице, немного выветрилось."
    "..."
    "Я не собирался дальше идти в западную часть двора. Всё, что я могу увидеть, сидя на плитке крытого здания, так это часть магазинчика, выглядывающего из-за угла слева..."
    "... и напоминающий мне тип магазинов с заправки."
    "Справа от него шел высокий кирпичный забор, а за ним виднелся недостроенный трехэтажный панельный дом."
    "Сам я уставился прямо на торговые автоматы, которые, к моему облегчению, не продавали алкогольные напитки."
    "Посидев немного, я решил что-нибудь купить, чтобы промочить горло, да и захотелось почувстовать какой-то вкус жизни."
    "Или лишь его имитацию... Сейчас я был в настроении получить простое короткосрочное наслаждение."
    "Подойдя к нужному автомату и прикинув, что я хочу приобрести, я стал шарить по своим карманам."
    "Я отправился на прогулку в своей универсальной ветровке. У неё был карман с застежкой у левой части груди, и по два обычных кармана ниже. Также был внутренний карман куртки."
    "В тех случаях, когда я ходил без своего портфеля, я обычно хранил важные вещи в верхних карманах. Так что те же смарт часы я взял с собой."
    me "Неужели я не взял с собой..?"
    "Карточку."
    "Я искал свою банковскую карточку, так как налички у меня не было. А ведь все торговые автоматы позволяют платить электронными деньгами."
    me "Есть!"
    "Проверив карманы своих штанов, я достал небольшой футляр, в котором хранились мой код-индикатор и банковская карта."
    "Выбрав напиток с помощью электронного меню, и прислонив чип карточки к устройству на торговом автомате, я услышал звук списывания средств."
    "Амбивалетное чувство, на самом деле..."
    "Чтобы в тот же момент увидеть на терминале автомата фразу \"Недостаточно средств!\" и последовавший за ней соответствующий сигнал."
    "{w=0.9}(•_•)"
    "Наверное, та карточка, которую я взял с собой, как раз-таки и была карточкой, предназначенной для покупки всякой мелочевки."
    "Но мне периодически нужно переводить средства сюда с зарплатной карты. И то, что они выглядят очень схоже, иногда сбивает с толку..."
    "Больше с собой у меня ничего не было, и просить деньги у прохожих ради удовлетворения своего маленького желания я точно не буду."
    "И всё нужное мне сейчас лежало среди вещей дома у Фила..."
    "Как только я собирался уйти, мой взгляд упал на кармашек другого близстоящего автомата."
    "В котором я увидел другой напиток - кажется, подслащенную воду с цитрусовым привкусом."
    "Странно, что я не заметил её до этого, но с той стороны, с которой я подошел к торговым автоматам, было бы затруднительно заметить что-то в этом кармашке."
    "Учитывая, что кармашек сам по себе глубокий..."
    "Возможно, что от полированного металла отразился свет, а дальше вода в пластиковой бутылке тажке частично отсветила его, и луч слегка задел мой глаз."
    "..."
    "Я немедленно подошел и взял воду."
    me "Ну хоть уже что-то."
    "И в тот момент, когда я задумался, а чья же это вода ..."
    un_s "Э ̄ то ... "
    un_s "Прошу прощения, но не могли бы вы отдать мне мою воду..?"
    "Я услышал мягкий, но слегка обеспокоенный голос."
    "И я замер, призадумавшись."
    "Первая фраза, которая я услышал, скорее всего прозвучала на общевосточном."
    "Не то чтобы я не понимал, что она означала, ведь это было междометие. К тому же, все ученики в школе учат три основных мировых языка, один из которых - общевосточный."
    "Я медленно повернулся к неожиданному собеседнику, пытаясь смастерить улыбку на лице."
    show sae_unf_confused at center
    with slowdissolve
    me "Так это вы оставили воду, простите."
    "Как только она попыталась заговорить..."
    show sae_unf_badly_surprised with averagedissolve
    hide sae_unf_confused
    show sae_unf_confused_speaking with averagedissolve
    hide sae_unf_confused
    show sae_unf_confused with averagedissolve
    hide sae_unf_confused_speaking
    show sae_unf_badly_surprised with averagedissolve
    hide sae_unf_confused
    "На её милом лице отразилась смесь разнообразных эмоций, отчего я сам пришел в замешательство."
    "Однако спустя секунду"
    hide sae_unf_badly_surprised superfastdissolve
    "с завидной скоростью для такой малышки,"
    "она выхватила бутылку с водой из моей раслабленной руки"
    "и унеслась прочь, что-то промямлив себе под нос."
    "И всё, что я успел сделать, так это сдвинуть ногу и лишь слегка протянуть руку по направлению её стремительно удаляющегося силуэта."
    "С крытой постройки, где находились торговые автоматы, она выбежала на другую сторону двора, где в лучах дневного солнца нагревались бетонные плиты недостроенного здания."
    "Как только она завернула за угол, я перестал думать о том, чтобы последовать за ней."
    "Всё, что я напоследок смог увидеть, так это {w=1}её нижнее белье под юбкуй, приподнятой то ли внезапным порывом ветра, то ли её скоростью бега..."
    "..."
    "Как неловко вышло."
    "Я её впервые вижу, и не заслужил такого отношения к себе."
    "Может быть, она трусиха и испугалась общения с незнакомым человеком?"
    "Или я как-то странно выгляжу..?"
    "Да и вообще, может эта бутылка с водой и не была её собственностью, и всё, что я сейчас лицезрел - лишь представление мелкой хулиганки?"
    "Нежелая больше об этом думать, я резко провел ладонью по лбу, взъерошив челку, чтобы собраться с мыслями."
    "Мне сильно хотелось выбить что-нибудь сладенького и холодненького."
    "И тогда мне в голову пришла одна идея."
    "Я достал смарт часы, прикрепил их себе на левую руку."
    "Разблокировал экран с помощью проверки отпечатка пальца."
    "Вывел режим отображения экрана в голографический."
    "Перед моим лицом вспыхнула приятная глазу бледно-синяя картинка."
    "Я проверил, есть ли мобильная связь."
    me "Хорошо, что счёт оплачен."
    "Зашел в список контактов, увидел там лишь один номер, и позвонил."
    "..."
    "..."
    "..."
    key "Приятно тебя слышать, но я сейчас занят, поэтому говори быстрее."
    me "Я сейчас отправлю сообщение, в котором будет содержаться сумма и номер моей карты. Думаю, ты понял, что..."
    key "Без проблем. Но потом вернешь. До связи."
    me "Конечно."
    "Не успел я договорить, как звонок завершился."
    "Последняя  его фраза прозвучала довольно резко, но не то чтобы он злился - скорее был напряжен."
    "Это был единственный человек, которого я не стеснялся просить помощи."
    "А в данной ситуации на кого-то другого тем более невозможно было положиться."
    "Я постоял пару минут, ожидая, когда Кей отправит на мою карточку немного денег."
    "Способа проверить, пришла ли сумма или нет, у меня не было, так как я еще не особо разбирался с функционалом смарт часов и к тому же сейчас не имел доступа к элекронному кабинету банка."
    "Кей явно был занят, поэтому вряд ли напишет в ответ или тем более перезвонит."
    "Но зная то, как Кей быстро решает всякие мелочи, я был вполне уверен в успехе моей задумки."
    "И через пару минут мои надежды оправдались: я потягивал вкусную газировочку, продолжая свою прогулку по улицам."
    scene bg_sleep_district_day with averagedissolve
    pause(0.5)
    "Тем не менее, газировка не могла улучшить моё дурное настроение."
    "Голова болела, пускай не так сильно, как раньше, и не все симптомы похмелья прошли."
    "Набравшись сил, я какое-то время бродил по району. Даже нашел неплохое место, где можно перекусить."
    "Вскоре я пришел к выводу, что пора возвращаться."
    "..."
    "Я петлял по незнакомым улицам, стараясь найти дорогу назад. Точного адреса дома Фила я не помню, но пытался возвращаться по памяти."
    "Я был все еще слегка дезориентированным и чувствовал слабость в теле."
    "И зря я раньше надеялся, что это пройдет к вечеру."
    "На часах сейчас было шесть минут пятого."
    "Я не решался спрашивать у прохожих дорогу, ведь верил, что не ошибся в выборе направления."
    "..."
    "Это ведь та самая улица, правильно?"
    "Чем больше я ходил, тем больше во мне просыпалось сомнений."
    "В основном я ориентировался по большому зданию корпорации - сейчас оно было ближе, чем раньше, но это не удивительно, ведь сегодня утром я отправился на юг."
    "А сейчас иду в противоположном направлении."
    "Несмотря на то, что у меня не было никаких проблем с запоминанием местности, я всё же с трудом находил обратную дорогу, ведь спальный район был усеян похожими друг на друга двуэтажными домишками."
    "Также на это влияло то, что я сегодня довольно много куда заворачивал, тем самым усложняя себе маршрут."
    "Я решил оглядеться, и внезапно в моё поле зрения попало кое-что знакомое."
    show enji_siding with averagedissolve
    pause(0.5)
    hide enji_siding with slowdissolve
    pause(0.3)
    scene bg_sleep_district_day with fade
    pause(0.5)
    "Это ведь была Энджи? На пару секунд мне привиделась знакомая фигура, которая скрылась за придорожной клумбой и вскоре исчезла за углом другой улицы."
    "Во мне разыгралось нешуточное любопытство. Что же она тут делает?"
    "Хотя я всё еще не пришел в себя, и наверное, лучше бы следовало вернуться домой пораньше и извиниться перед Филом за то, что я погарячился..."
    "И тогда я решил-"
    menu:
        "Проследить за Энджи":
            jump follow

        "Вернуться домой":
            jump go_home
    jump choice3_done


label follow:
    "Всё-таки мне интересно, что она там задумала."
    "Я зашевелил ногами и перешел с шага на легкий бег, ведь я запросто мог потерять её из виду..."
    "Останавливаться уже поздно, а необычное поведение Энджи всё еще кажется мне любопытным."
    "И спустя час..."
    scene bg_cafe with slowdissolve
    pause(1.5)
    "{w=1}я оказался здесь..."
    wa "Пожалуйста, вот ваш заказ."
    "Официант вежливо поставил на стол две чашки: одну с латте ближе ко мне, а вторую - с черным кофе - моему собеседнику."
    "Мы поблагодарили официанта, и на какое-то время повисла тишина, но для меня это был не добрый знак."
    "Временное спокойствие нарушила Энджи."
    show enji_speaking_down with averagedissolve
    enj "Однажды некий Шарль Талейран сказал, что кофе должен быть горячим как ад, черным как черт, чистым как ангел и сладким как любовь."
    enj "Классика жанра, если выразиться проще."
    show enji_siding with averagedissolve
    hide enji_speaking_down
    enj "..."
    show enji_angry_speaking with fastdissolve
    hide enji_siding
    enj "Но боюсь, две последние аналогии я точно не могу применить ни к тебе, ни к сложившейся ситуации!"
    enj "Наоборот, сейчас на языке только и вертятся, что ад да чертики..."
    show enji_siding with fastdissolve
    hide enji_angry_speaking
    me "А я слышал, что кофе, как и коньяк, нельзя пить кружками..."
    "Я пытался как-то разбавить её настроение, вспомнив какую-то цитату из той же темы, но..."
    show enji_thinking with averagedissolve
    hide enji_siding
    "Она просто сделала аккуратный глоток кофе, прикрыв глаза, явно пытаясь насладиться его вкусом в стой неловкой ситуации."
    "..."
    hide enji_thinking with slowdissolve
    "Мы уже какое-то время сидели в этом странном кафе."
    "Не то, что бы место было плохим. Напротив, тут витал смешанный аромат разнообразных кофе, а также приятный душок выпечки."
    "А там, где нельзя было удовлетвориться запахами кофе и выпечки, можно было насладиться легким благоуханием свежей древесины."
    "Само кафе было не широким, но вытянутым по длине, и обладало множеством странных закутков, будто специально построенных для парочек."
    "Если смотреть со входа и основного коридора, то оно было просто заполнено разнообразными столиками на любой вкус и цвет."
    "Закутки не были отгорожены чем-то особенным, но явно могли создавать впечатление уединения, ведь ветвились они от основного прохода."
    "И со стороны были прикрыты клумбами с разной растительностью."
    me "?"
    "Была ли растительность настоящей или искусственной? Этого я не заметил."
    "Со стороны выглядело, будто мы с Энджи - парочка, но я думаю, что не стоит ей лишний раз это напоминать."
    "Сейчас в кафе было довольно людно. И возраст этих людей разнился от мала до велика."
    "Беззаботные дети, веселые семьи, угрюмые одиночки в основном располагались в передней части кафе, ближе ко входу."
    "А личности, предпочитавшие шуму покой и уединение, обычно забирались подальше."
    "..."
    "Кому-то могло показаться, что я и Энджи сидим и отдыхаем, но это ошибочное мнение."
    "Попали мы сюда по нелепому стечению обстоятельств, и \"попивание\" кофейка в углу, на самом деле, было вынужденной мерой."
    "В определенный момент, мое преследование Энджи превратилось не в просто развлечение, а в миссию, навязанной последне упомянутой личностью."
    "А объектом этой миcсии был..."
    show key_usual with averagedissolve
    pause(1.5)
    hide key_usual with averagedissolve
    "Кей..."
    "Мы спрятались в таком углу, в котором Энджи могла наблюдать за столиком Кея и его спиной, в то же время оставаясь незамеченной."
    "Сам Кей пришел в это кафе явно не прятаться. Более того, у него здесь был забронирован шикарный столик, который стояль чуть ли не по центру задней части кафе."
    "Я уверен, скоро у него будет очередная важная встреча."
    "Сам я Кея видеть не могу, если не повернусь на стуле, а вот Энджи то и дело постоянно бросает в него взгляды."
    "Бр-р-р."
    "Она делает это настолько бессовестно, что если  бы я был на месте Кея, то почувствовал себя некомфортно просто так, без причины..."
    "Но Энджи едва ли выглядела взволнованной, так что всё в порядке, и нас не заметили."
    "По сути я стал заложником Энджи."
    me "И как мы к этому пришли..."
    "Вслух вздохнул я."
    show enji_speaking with superfastdissolve
    enj "Это моя фраза. А вообще по большей части это твоя вина."
    "Вот тут я не мог согласиться."
    show enji_usual with fastdissolve
    hide enji_speaking
    me "О чем ты? Никогда бы не подумал, что Энджи окажется сталкершой."
    show enji_angried with averagedissolve
    hide enji_usual
    enj "Хмфф...То, что я делала, никак тебя не касается. А твоё внезапное любопытство и слежка за мной вот к чему привели..."
    enj "После этого чувствую себя не в своей тарелке. Сам-то доволен ситуацией?"
    "Кисло бросила Энджи."
    hide enji_angried with fastdissolve
    "Я промолчал. В любом случае, мне не очень приятно было застрять с ней в таком месте и особенно при таких обстоятельствах."
    "Даже без слов было понятно, что я чувствую."
    scene bg_nothing with averagedissolve
    "Выглядело так, будто она пытается ото всех спрятаться."
    "Если что, прикроюсь тем, что я искал дорогу и заблудился."
    "Хотя это худшее из всех возможных оправданий!"
    "..."
    "Значит надо сделать так, чтобы меня не заметили."
    me "Итак."
    "Я подбежал к тому углу, где в последний раз видел её, аккуратно заглянул за него - кажется, всё в порядке."
    "Энджи шла по людной улице, иногда останавливаясь и выжидая чего-то, изредка заворачивая в переулок. Но если смотреть на здание корпорации, то двигалась она на восток."
    "Я медленно следовал за ней, соблюдая такую дистанцию, что если бы она решила обернуться, я тут же стал бы частью толпы или слился бы с деревом."
    "Иногда прохожие бросали то на меня, то на неё какие-то странные взгляды."
    "В голову лезло пару неприятных мыслей."
    "Мало ли, а вдруг меня застопит неудачно попавшийся сотрудник Центрального Ордена Безопасности(COS), будучи в плохом настроении или придумавший что-то нелепое."
    "По крайней мере сейчас моё поведение точно отличалось от серой массы..."
    "Энджи похоже даже не думала об этом или не обращала внимания, а вот мне становилось неприятно."
    "А затем..."
    scene bg_cafe with fastdissolve
    show enji_angry_speaking with fastdissolve
    hide enji_angried
    enj "Подумать только... Я завернула в переулок, чтобы через минуту вернуться и обнаружить тебя, якобы \"случайно\" шатающегося неподалеку."
    me "..."
    me "Чтобы просто обречь меня следить за Кеем вместе с тобой?.."
    show enji_irritated with averagedissolve
    hide enji_angry_speaking
    pause(1.5)
    show enji_angry_speaking with averagedissolve
    hide enji_irritated
    enj "А что мне еще оставалось делать? У меня не было времени отчитывать тебя. Потеряв из виду Кея, я бы потратила впустую последние несколько часов и мою операцию."
    show enji_siding with slowdissolve
    hide enji_angry_speaking
    me "Но это ж был твой план залезть в это кафе. Я даже не..."
    show enji_speaking with fastdissolve
    hide enji_siding
    enj "Не перегибай палку. В той ситуации ничего не оставалось, кроме как спрятаться здесь. Нам даже повезло, что я подумала об этом плане отхода заранее и нашла более-менее незаметное место для слежки."
    show enji_usual with averagedissolve
    hide enji_speaking
    me "Но как ты вообще поняла, что он внезапно решит обернуться и пойти в эту сторону? А еще держу в курсе: мы тут надолго..."
    show enji_siding
    hide enji_usual
    pause(1.0)
    show enji_speaking_down with fastdissolve
    hide enji_siding
    enj "На самом деле, я была уверена в том, что он зайдет в это кафе, но это должно было произойти гораздо позже!"
    enj "К тому же твое появление подействовало мне на нервы, и я потеряла концентрацию."
    show enji_thinking with averagedissolve
    hide enji_speaking_down
    me "Твоя осведомленность графиком Кея меня пугает."
    me "Да и вообще, а если я действительно заблудился и искал дорогу, случайно наткнувшись на тебя? А вдруг я просто гулял?"
    enj "Может я и сталкерша, но я не собиралась заходить так далеко и следить за ним еще и в кафе. Мне просто нужно было кое в чем убедиться."
    enj "А всё пошло наперекосяк: твоё появление, измененные планы Кея... и вот мы здесь."
    return



label go_home:
    "Да, лучше вернуться домой."
    "К тому же, наверняка уйдет еще некоторое время, чтобы найти туда дорогу."
    "А бегать за кем-то по всему району мне особо-то и хочется."
    return

label your_hotel:
    pass

return
