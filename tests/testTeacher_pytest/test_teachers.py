from main import Teacher, DisciplineTeacher


def test_teacher_init():
    teacher = Teacher('test_name', 'test_education', 'test_experience')
    assert len(teacher.employers_list) == 1
    assert isinstance(teacher.employers_list, list)


def test_teacher_get_discipline(teacher):
    assert teacher.get_name() == 'test_name'


def test_get_education(teacher):
    assert teacher.get_education() == 'test_education'


def test_get_experience(teacher):
    assert teacher.get_experience() == 'test_experience'


def test_set_experience(teacher):
    assert teacher.set_experience('test_new_experience') == 'test_new_experience'


def test_get_teacher_data(teacher):
    assert teacher.get_teacher_data() == 'test_name, образование test_education, опыт работы test_experience года.'


def test_add_mark(teacher):
    assert teacher.add_mark('test_student', 5) == 'test_name поставил оценку 5 студенту test_student.'


def test_remove_mark(teacher):
    assert teacher.remove_mark('test_student', 5) == 'test_name удалил оценку 5 студенту test_student.'


def test_give_a_consultation(teacher):
    assert teacher.give_a_consultation('test_class') == 'test_name провел консультацию в классе test_class.'


def test_fire_employer(teacher):
    assert teacher.fire_employer() == ('Сотрудник test_name, образование test_education, опыт работы test_experience '
                                       'года. был уволен.')


def test_discipline_teacher_init():
    discipline_teacher_1 = DisciplineTeacher('test_name', 'test_education', 'test_experience',
                                             'test_discipline', 'test_job_title')
    assert isinstance(discipline_teacher_1.employers_list, list)


def test_get_discipline(discipline_teacher):
    assert discipline_teacher.get_discipline() == 'test_discipline'


def test_get_job_title(discipline_teacher):
    assert discipline_teacher.get_job_title() == 'test_job_title'


def test_set_job_title(discipline_teacher):
    discipline_teacher.set_job_title('set_test_job_title')
    assert discipline_teacher.get_job_title() == 'set_test_job_title'


def test_get_teacher_data(discipline_teacher):
    assert discipline_teacher.get_teacher_data() == ('test_name, образование test_education, опыт работы '
                                                     'test_experience года.\nПредмет test_discipline, '
                                                     'должность test_job_title')


def test_add_mark(discipline_teacher):
    assert discipline_teacher.add_mark('test_mark', 'test_student_name',
                                       'test_discipline') == ('test_name поставил оценку test_student_name студенту '
                                                              'test_mark.\nПредмет: test_discipline')


def test_remove_mark(discipline_teacher):
    assert discipline_teacher.remove_mark('test_student_name',
                                          'test_mark') == ('test_name удалил оценку test_mark студенту '
                                                           'test_student_name.\nПредмет: test_discipline')


def test_give_a_consultation(discipline_teacher):
    assert discipline_teacher.give_a_consultation(
        'test_class_name') == ('test_name провел консультацию в классе test_class_name.\nПо предмету test_discipline '
                               'как test_job_title')
