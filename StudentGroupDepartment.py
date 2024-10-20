class StudentGroupDepartment:
    def __init__(self, student_group_id, department_id):
        self.student_group_id = student_group_id
        self.department_id = department_id

    def __repr__(self):
        return f"StudentGroupDepartment(student_group_id={self.student_group_id}, department_id={self.department_id})"
