from first_exercise import first_exercise
from second_exercise import second_exercise
from third_exercise import third_exercise_1, third_exercise_2


def main_menu():
    print("which exercise do you want to execute? (1-6)")
    selection = int(input())
    if selection == 1:
        first_exercise()
    elif selection == 2:
        second_exercise()
    elif selection == 3:
        third_exercise_1()
    elif selection == 4:
        third_exercise_2()
    else:
        print("TBA")


if __name__ == '__main__':
    main_menu()
