# Moment-of-Eterniry

Ссылка для скачивания .exe приложения под Windows:  
[Download](https://disk.yandex.ru/d/Dnn1-Bs6JUl5Dg)  

Ссылка на медиа файлы в случае необходимости:  
[Media files](https://disk.yandex.ru/d/qYxQoUyCMfmR0g)  

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

## Изменения от 1.01.2023

1. Полностью отрефакторены скрипты вызова спрайтов персонажей;  
2. Добавлены *side* изображения для некоторых моментов: главного персонажа, неизвестных персонажей и для случаев группового диалога.  
3. Изображения персонажей прогнаны через *UPScale* и разделены на *side* версии.  
