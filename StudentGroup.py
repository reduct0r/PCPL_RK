class StudentGroup:
    def __init__(self, id, group_name, number_of_students, department_id):
        self.id = id
        self.group_name = group_name
        self.number_of_students = number_of_students
        self.department_id = department_id

    def __repr__(self):
        return (f"StudentGroup(id={self.id}, group_name='{self.group_name}', "
                f"number_of_students={self.number_of_students}, department_id={self.department_id})")
