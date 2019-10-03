"""Description"""
# The function below must return the minimum number of candies Alice must buy.
# candies has the following parameter(s):
# n: an integer, the number of children in the class
# arr: an array of integers representing the ratings of each student.

def give_candies(number_students, students_rate):
    """get minimum number of candies that should be given to students in a class."""
    # at least 1 candy should be given to a student
    candies_given = [1] * number_students
    # for each student, except for the 1st student.
    for i in range(1, number_students):  # check the candies of the student to the left.
        # The student must have more candies than the 1 to his left if his rate is bigger.
        if students_rate[i] > students_rate[i - 1]:
            candies_given[i] = candies_given[i - 1] + 1
    # for each student, except for the last student.
    for i2 in range(number_students - 2, -1, -1):  # check the candies of the student to the right.
        # The student must have more candies than the 1 to his right if his rate is bigger.
        # and if the candies given to the student after him is more than his.
        if students_rate[i2] > students_rate[i2 + 1] and candies_given[i2] < candies_given[i2 + 1] + 1:
            candies_given[i2] = candies_given[i2 + 1] + 1


    total_candies = sum(candies_given)
    return total_candies


number_students = int(input())

students_rate = []

for i in range(number_students):
    student_rate = int(input())
    students_rate.append(student_rate)

print(give_candies(number_students, students_rate))





