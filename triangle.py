#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on October 2020
# This program calculates the area of a triangle


def area(base_int, height_int):
    # This functions calculates area

    # Process
    area = (base_int * height_int) / 2.0

    # Output
    print("The area of the triangle is {0}cm²".format(area))


def main():
    # This function gets base length and height

    # Input
    while True:
        base_str = input("Enter the base length of the triangle (cm): ")

        try:
            base_int = int(base_str)
        except Exception:
            print("That is not an integer, please input a number!")
            print("")
        else:
            if base_int <= 0:
                print("You have not a valid base length, please input a"
                      " positive number!")
                print("")
            else:
                break
    while True:
        height_str = input("Enter the height of the triangle (cm): ")

        try:
            height_int = int(height_str)
        except Exception:
            print("That is not an integer, please input a number!")
            print("")
        else:
            if height_int <= 0:
                print("You have not a valid base length, please input a"
                      " positive number!")
                print("")
            else:
                break
    print("")

    # Call Functions
    area(base_int, height_int)


if __name__ == "__main__":
    main()
