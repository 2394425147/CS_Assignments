from Student import Student


SUBJECTS = ["Math", "English", "C-Programming"]


def display(arr: list[Student]):
    """
    Displays statistics for all the students in an array

    Parameters:
    arr: A list of students to be displayed
    """
    for student in arr:
        student.print_stats()

def sort_by_total_score(arr: list[Student]):
    """
    Sorts a list of students by total score in-place

    Parameters:
    arr: A list of students to be sorted
    """
    for comp_goal in range(0, len(arr) - 1):
        greatest_index = 0
        greatest_value = 0
        for comp_target in range(comp_goal + 1, len(arr)):
            if arr[comp_target].total_score > greatest_value:
                greatest_index, greatest_value = comp_target, arr[comp_target].total_score

        if greatest_index != comp_goal:
            arr[comp_goal], arr[greatest_index] = arr[greatest_index], arr[comp_goal]

def course_average(arr: list[Student]):
    """
    Finds the average value of each subject defined in SUBJECTS

    Parameters:
    arr: A list of students to take average from

    Returns:
    A dictionary containing pairs of subjects and its average value
    """
    return { subject: sum(map(lambda stu: stu.get_score(subject), arr)) / len(arr) for subject in SUBJECTS }

def count_fail(arr: list[Student]):
    """
    Counts all the failed students in each subject defined in SUBJECTS

    Parameters:
    arr: A list of students to find failing grades in

    Returns:
    A dictionary containing pairs of subjects and its amount of failed students
    """
    return { subject: sum(map(lambda stu: 0 if stu.get_score(subject) >= 60 else 1, arr)) for subject in SUBJECTS }

def main():
    student_arr: list[Student] = [Student() for _ in range(30)]
    for index, student in enumerate(student_arr):
        student.init_data(index)

    display(student_arr)

    sort_by_total_score(student_arr)

    averages, fails = course_average(student_arr), count_fail(student_arr)

    print()
    for subject in SUBJECTS:
        print(format(f"{subject} average", "<30"), format(averages[subject], ".2f"))

    print()
    for subject in SUBJECTS:
        print(format(f"{subject} fails", "<30"), fails[subject])
    
if __name__ == "__main__":
    main()
