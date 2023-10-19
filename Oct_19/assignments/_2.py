import sanitization

# Implementation
grading = [
    (0,  "不及格"),
    (60, "及格"),
    (70, "中等"),
    (80, "良好"),
    (90, "优秀")
]

def get_grade(score: int):
    # Validate input
    if not 0 <= score <= 100:
        # In a production environment,
        # throw an error instead
        print("Score is out of bounds (0 <= score <= 100)")
        exit(-1)
        return None

    for i, gradeInfo in enumerate(grading):
        if gradeInfo[0] > score:
            return grading[max(0, i - 1)][1]

    return grading[-1][1]

# Testing
while True:
    (shouldContinue, number) = sanitization.filter_integer(input("请输入正整数："))

    if not shouldContinue:
        break;

    print(get_grade(number))
    pass