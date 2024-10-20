from Department import Department
from StudentGroup import StudentGroup
from StudentGroupDepartment import StudentGroupDepartment
from Requests import findGroupsEndWithKey, DepartmentsSortedByAvgNumberOfStudents, findDepartmentsStartWithKey

# Список кафедр
departments = [
    Department(id=1, name="Прикладная математика"),
    Department(id=2, name="Информатика"),
    Department(id=3, name="Физика"),
    Department(id=4, name="Астрономия"),
    Department(id=5, name="История"),
    Department(id=6, name="Археология"),
    Department(id=7, name="Астрофизика"),
]

# Список студенческих групп
student_groups = [
    StudentGroup(id=1, group_name="Группа 101", number_of_students=30, department_id=1),
    StudentGroup(id=2, group_name="Группа 102", number_of_students=25, department_id=2),
    StudentGroup(id=3, group_name="Группа 103", number_of_students=28, department_id=1),
    StudentGroup(id=4, group_name="Группа 104", number_of_students=22, department_id=3),
    StudentGroup(id=5, group_name="Группа 105", number_of_students=27, department_id=4),
    StudentGroup(id=6, group_name="Группа 1003", number_of_students=20, department_id=4),
    StudentGroup(id=7, group_name="Группа 104А", number_of_students=21, department_id=5),
    StudentGroup(id=8, group_name="Группа 105А", number_of_students=24, department_id=6),
    StudentGroup(id=9, group_name="Группа 1003А", number_of_students=23, department_id=7),
    StudentGroup(id=10, group_name="Группа 104Б", number_of_students=21, department_id=5),
    StudentGroup(id=11, group_name="Группа 145Б", number_of_students=20, department_id=4),
    StudentGroup(id=12, group_name="Группа 1Б03", number_of_students=19, department_id=7),

]

group_deps = [
    StudentGroupDepartment(student_group_id=1, department_id=1),
    StudentGroupDepartment(student_group_id=2, department_id=2),
    StudentGroupDepartment(student_group_id=3, department_id=1),
    StudentGroupDepartment(student_group_id=4, department_id=3),
    StudentGroupDepartment(student_group_id=5, department_id=4),
    StudentGroupDepartment(student_group_id=6, department_id=4),
    StudentGroupDepartment(student_group_id=7, department_id=5),
    StudentGroupDepartment(student_group_id=8, department_id=6),
    StudentGroupDepartment(student_group_id=9, department_id=7),
    StudentGroupDepartment(student_group_id=10, department_id=5),
    StudentGroupDepartment(student_group_id=11, department_id=4),
    StudentGroupDepartment(student_group_id=12, department_id=7),
]

# Таблица для отношения один-ко-многим
one_to_many = [(g.group_name, g.number_of_students, d.name)
               for d in departments
               for g in student_groups
               if g.department_id == d.id]

# Соединение таблицы многие-ко-многим
temp = [(group.group_name, group_dep.department_id)
    for group in student_groups
    for group_dep in group_deps
    if group.id == group_dep.student_group_id
]

many_to_many = [(group_name, dept.name)
    for dept in departments
    for group_name, dep_id in temp
    if dep_id == dept.id
]

if __name__ == '__main__':
    # Запрос 1: Студенческие группы, заканчивающиеся на key и их кафедры (один-ко-многим)
    findGroupsEndWithKey(one_to_many, "03")

    # Запрос 2: Кафедры, отсортированные по среднему кол-ву студентов в группах (один-ко-многим)
    DepartmentsSortedByAvgNumberOfStudents(one_to_many)

    # Запрос 3: Кафедры, начинающиеся на букву == key и их студенческие группы (многие-ко-многим)
    findDepartmentsStartWithKey(many_to_many, "А")
