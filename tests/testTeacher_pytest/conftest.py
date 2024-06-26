import pytest
from main import Teacher, DisciplineTeacher


@pytest.fixture
def teacher():
    Teacher.employers_list.clear()
    teacher = Teacher('test_name', 'test_education', 'test_experience')
    return teacher


@pytest.fixture
def discipline_teacher():
    Teacher.employers_list.clear()
    discipline_teacher = DisciplineTeacher('test_name', 'test_education', 'test_experience',
                                           'test_discipline', 'test_job_title')
    return discipline_teacher
