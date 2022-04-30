#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates whether a student can attend an exam
#   Given their attendance


def main():
    # I calculate circumference

    # input
    str_number_of_classes_held = input("How many classes were held?: ")
    str_number_of_classes_attended = input("How many classes were attended?: ")

    # process & output
    try:
        int_number_of_classes_held = int(str_number_of_classes_held)
        int_number_of_classes_attended = int(str_number_of_classes_attended)
        if (
            int_number_of_classes_attended >= 0 and
            int_number_of_classes_held >= 0 and
            int_number_of_classes_attended <= int_number_of_classes_held
        ):
            attendance_percentage = round(
                (100 * int_number_of_classes_attended / int_number_of_classes_held), 1
            )
            if attendance_percentage >= 75:
                print(
                    "\nYou can attend the exam with an attendance of {}%".format(
                        attendance_percentage
                    )
                )
            elif attendance_percentage < 75:
                print(
                    "\nYou can’t attend the exam with an attendance of {}%".format(
                        attendance_percentage
                    )
                )
            else:
                # you shouldn't be here
                print("\nyou shouldn't be there")
        else:
            print("\nPlease enter realistic values")
    except Exception:
        print("\nPlease enter an integer")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
