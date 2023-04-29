from random import randrange
from datacenter.models import (
    Schoolkid,
    Mark,
    Chastisement,
    Commendation,
    Lesson
    )

PRAISE_WORDS = ["Молодец!", "Отлично!", "Хорошо!",
                "Гораздо лучше, чем я ожидал!", "Ты меня приятно удивил!",
                "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!",
                "Именно этого я давно ждал от тебя!",
                "Сказано здорово – просто и ясно!", "Ты, как всегда, точен!",
                "Очень хороший ответ!", "Талантливо!",
                "Ты сегодня прыгнул выше головы!", "Я поражен!",
                "Уже существенно лучше!", "Потрясающе!", "Замечательно!",
                "Прекрасное начало!", "Так держать!", "Ты на верном пути!",
                "Здорово!", "Это как раз то, что нужно!", "Я тобой горжусь!",
                "С каждым разом у тебя получается всё лучше!",
                "Мы с тобой не зря поработали!", "Я вижу, как ты стараешься!",
                "Ты растешь над собой!", "Ты многое сделал, я это вижу!",
                "Теперь у тебя точно все получится!"]


def find_student(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        print("Ученик не найден")
    except Schoolkid.MultipleObjectsReturned:
        print("Нашёл несколько учеников с указанными совпадениями в имени")


def fix_marks(kidname):
    Mark.objects.filter(
        schoolkid=find_student(kidname),
        points__lt=4
        ).update(points=5)


def remove_chastisements(kidname):
    Chastisement.objects.filter(schoolkid=find_student(kidname)).delete()


def create_commendation(kidname, subject_title="Математика"):
    schoolkid = find_student(kidname)
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject_title
        ).order_by('-date').first()
    rand_text = PRAISE_WORDS[randrange(len(PRAISE_WORDS))]
    lesson_date = lesson.date
    lesson_teacher = lesson.teacher
    lesson_subject = lesson.subject
    Commendation.objects.create(
        text=rand_text,
        schoolkid=schoolkid,
        created=lesson_date,
        subject=lesson_subject,
        teacher=lesson_teacher
        )
