# Moment-of-Eterniry

Ссылка для скачивания .exe приложения под Windows:  
[Download](https://disk.yandex.ru/d/YFG8g5Rx18JlzA)  

Ссылка на медиа файлы в случае необходимости:  
[Media files](https://disk.yandex.ru/d/rOes6f58jpRrWg)  

## Клонирование репозитория
В репозитории включено Git LFS, поэтому в случае отсутствия LFS у вас будет отсутствовать доступ к этим файлам.  
Вам будет доступен только файл указателя на медиа файлы (прикрепленные в ссылке выше).  
С инструкцией по установке Git LFS можете ознакомиться по ссылке ниже:  
[Git LFS](https://docs.github.com/ru/repositories/working-with-files/managing-large-files/installing-git-large-file-storage)  
В процессе работы с Git LFS мы можете столкнуться с тем, что при использовании команды *git push* у вас будет запрашиваться пароль аутентификации для каждого LFS файла.  
Обойти это можно несколькими путями - самый простой, отказаться от пароля для *rsa.pub* ключа:  
[SSH Key passphrases](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases)  
Лично я просто добавил *config* файл по инструкции в первом ответе:   
[SSH Agent config](https://stackoverflow.com/questions/43371608/why-git-push-of-lfs-git-ask-password-3-times)  

## Обратная связь

Если у вас имеются идеи, которые вы хотите реализовать, то вы можете принять участие в создании визуальной новеллы в качестве сценариста, художника и т.п.  
[Дискорд канал](https://discord.gg/YbeeBtkxBA)  
tg: @Kadel_007  

## Изменения от 30.12.2022
1. Добавлен [*ActionEditor*](https://github.com/kyouryuukunn/renpy-ActionEditor3) для удобства настройки в самой игре.  
[Подробнее об использовании](https://www.youtube.com/watch?v=KoYXzREFx4A)  
2. В *screens.rpy* модифицирована строчка *if not renpy.variant("small"):* по причинам объясненным [здесь](https://www.twoandahalfstudios.com/2020/11/visual-novel-tips-and-tricks-with-gabmag-2).  
3.
## Изменения от 30.12.2022
1. Черное изображение *bg_nothing*, заменено на встроенное *black*;  
2. Переход в пролог и новую главу заменен с изображения на *screen textmiddle(text)*;  
3. Добавлен файл *clear_rpyc.bat*, который рекурсивно удаляет все временные файлы RenPy;  
4. Начато использование Git LFS в репозитории.  

## Изменения от 29.12.2022
1. Значительно переделан интерфейс главного меню;  
2. Изменено расположение *label splashscren*.  

## Изменения от 22.12.2022

В качестве демо-прохождения готов только пролог и кусок первой главы.  
Начато написание первой главы.  
Нет постоянных спрайтов и иных изображений, используются свободно-распространяемые изображения.  
Содержимое пролога и глав находятся в папке */game/scripts/prologue*
