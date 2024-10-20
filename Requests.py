from collections import defaultdict

"""Запрос 1: Студенческие группы, заканчивающиеся на key и их кафедры"""
def findGroupsEndWithKey(one_to_many, key, debug=True):
    # Фильтруем группы, названия которых заканчиваются на ключ
    filtered_groups = [
        {"group_name": group_name, "department_name": department_name}
        for group_name, _, department_name in one_to_many
        if group_name.endswith(key)
    ]

    if debug:
        print(f"Запрос 1: Студенческие группы, заканчивающиеся на '{key}' и их кафедры:")
        if not filtered_groups:
            print("Ничего не найдено")
        else:
            for item in filtered_groups:
                print(f"Группа: {item['group_name']}, Кафедра: {item['department_name']}")
        print("\n")

    return filtered_groups

"""Запрос 2: Кафедры, отсортированные по среднему кол-ву студентов в группах"""
def DepartmentsSortedByAvgNumberOfStudents(one_to_many, debug=True):

    # Сгруппируем количество студентов по названиям кафедр
    department_student_counts = defaultdict(list)
    for group_name, number_of_students, department_name in one_to_many:
        department_student_counts[department_name].append(number_of_students)

    # Вычислим среднее количество студентов для каждой кафедры
    average_students = [
        {
            "department_name": dept,
            "average_number_of_students": sum(counts) / len(counts)
        }
        for dept, counts in department_student_counts.items()
    ]

    # Отсортируем кафедры по среднему количеству студентов в порядке убывания
    sorted_average_students = sorted(
        average_students,
        key=lambda x: x["average_number_of_students"],
        reverse=True
    )

    if debug:
        print("Запрос 2: Кафедры со средним количеством студентов, отсортированные по среднему количеству:")
        for item in sorted_average_students:
            print(
                f"Кафедра: {item['department_name']}, "
                f"Среднее количество студентов: {item['average_number_of_students']:.2f}"
            )
        print("\n")

    return sorted_average_students


"""Запрос 3: Кафедры, начинающиеся на букву == key и их студенческие группы"""
def findDepartmentsStartWithKey(many_to_many, key, debug=True):
    # Сгруппируем группы по названиям кафедр
    department_to_groups = defaultdict(list)
    for group_name, department_name in many_to_many:
        department_to_groups[department_name].append(group_name)

    # Фильтруем кафедры, названия которых начинаются с ключа
    filtered_departments = {
        dept: groups
        for dept, groups in department_to_groups.items()
        if dept.startswith(key)
    }

    result = [
        {"department_name": dept, "student_groups": groups}
        for dept, groups in filtered_departments.items()
    ]

    if debug:
        print(f"Запрос 3: Кафедры, начинающиеся на '{key}', и их студенческие группы:")
        if not result:
            print("Ничего не найдено")
        else:
            for item in result:
                groups = "\n\t".join(item["student_groups"]) if item["student_groups"] else "Нет групп"
                print(f"Кафедра {item['department_name']}:\n\t{groups}")
        print("\n")

    return result

