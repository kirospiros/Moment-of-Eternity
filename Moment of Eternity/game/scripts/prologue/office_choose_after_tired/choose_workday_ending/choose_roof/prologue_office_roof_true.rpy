label prologue_office_roof_enji_answer_true:

    $ enji_points += 1

    show enji_smiling_down with averagedissolve

    pause 0.8

    show enji_siding with fastdissolve
    hide enji_smilling_down
    show enji_usual  with fastdissolve

    "По её мимолетной улыбке я понял, что ей понравился мой искренний ответ."
    "..."
    "Пожалуй я рад, что смог не разочаровать её. Хотя я не планировал ничего такого."
    "Далее Энджи заговорила, будто подводя к немного другой теме."

    show enji_speaking with fastdissolve
    hide enji_usual

    enji "Открывающийся пейзаж действительно может быть разнообразно великолепен: даже самый обыденный вид может впечатлить."
    enji "Но твой ответ показывает, что ты задумывался не только о красоте, не так ли?"

    jump prologue_office_roof_after_answer
