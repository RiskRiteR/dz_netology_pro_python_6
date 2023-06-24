import pytest
from main import *
from unittest import TestCase


@pytest.mark.parametrize(
    'mentors_, expected', [
        [mentors, 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, '
                  'Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, '
                  'Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, '
                  'Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий']
    ]
)
def test_1(mentors_, expected):
    res = unique_name(mentors_)
    assert res == expected


@pytest.mark.parametrize(
    'mentors_, expected', [
        [mentors_1, 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)']
    ]
)
def test_2(mentors_, expected):
    res = top_3_unique_name(mentors_1)
    assert res == expected


@pytest.mark.parametrize(
    'mentors_, expected', [
        [mentors_2, "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим\n"
                    "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Евгений, Елена, Кирилл, Максим, Олег, Роман\n"
                    "На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений\n"
                    "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим\n"]
    ]
)
def test_3(mentors_, expected):
    res = super_teacher(mentors_2)
    assert res == expected


class TestYandex(TestCase):
    def test_crate_folder(self):
        self.assertEqual(akk_ya.create_folder('test'), 201, "folder created")

    def test_crate_folder_fail(self):
        self.assertEqual(akk_ya.create_folder('test'), 201, "folder not created")
