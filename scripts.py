from random import randrange
from datacenter.models import (
    Schoolkid,
    Mark,
    Chastisement,
    Commendation,
    Lesson
    )


def find_student(name):
	from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
	try:
        return Schoolkid.objects.get(full_name__contains=name)
    except ObjectDoesNotExist:
        print("Ученик не найден")
    except MultipleObjectsReturned:
        print("Нашёл несколько учеников с указанными совпадениями в имени")


def fix_marks(kidname):
    Mark.objects.filter(schoolkid=find_student(kidname), points__lt=4).update(points=5)	

		
def remove_chastisements(kidname):
    Chastisement.objects.filter(schoolkid=find_student(kidname)).delete()
	

def create_commendation(kidname, subject_title="Математика"):
    texts = ["Молодец!","Отлично!","Хорошо!","Гораздо лучше, чем я ожидал!",
             "Ты меня приятно удивил!","Великолепно!","Прекрасно!","Ты меня очень обрадовал!",
             "Именно этого я давно ждал от тебя!","Сказано здорово – просто и ясно!","Ты, как всегда, точен!",
             "Очень хороший ответ!","Талантливо!","Ты сегодня прыгнул выше головы!","Я поражен!",
             "Уже существенно лучше!","Потрясающе!","Замечательно!","Прекрасное начало!","Так держать!",
             "Ты на верном пути!","Здорово!","Это как раз то, что нужно!","Я тобой горжусь!",
             "С каждым разом у тебя получается всё лучше!","Мы с тобой не зря поработали!",
             "Я вижу, как ты стараешься!","Ты растешь над собой!","Ты многое сделал, я это вижу!",
             "Теперь у тебя точно все получится!"]
	lessons = Lesson.objects.filter(year_of_study=6, group_letter="А", subject__title=subject_title)
	rand_text = texts[randrange(len(texts))]
    rand_num = randrange(len(lessons))
	lesson_date = lessons[rand_num].date
	lesson_teacher = lessons[rand_num].teacher
	lesson_subject = lessons[rand_num].subject
	Commendation.objects.create(text=rand_text, schoolkid=find_student(kidname), created=lesson_date, subject=lesson_subject, teacher=lesson_teacher)
