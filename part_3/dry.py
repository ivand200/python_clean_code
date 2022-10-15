"""DRY/OAOO"""
# The ideas of Don't Repeat Yourself (DRY) and Once and Only Once (OAOO) are
# closely related, so they were included together

# In this example, we have taken what is probably the simplest approach to
# eliminating duplication: creating a function.

def score_for_student(student):
    return student.passed * 11 - student.failed * 5 - student.years * 2


def process_students_list(students):
    # do some processing...

    students_ranking = sorted(students, key=score_for_student)
    # more processing
    for student in students_ranking:
        print(
            "Name: {0}, Score: {1}".format(
                student.name, score_for_student(student)
            )
        )