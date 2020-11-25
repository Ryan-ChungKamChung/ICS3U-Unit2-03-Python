#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Program finding a circle's circumference with Tau


import constants


def main():
    # This program calculates the circumference of a circle
    # Using tau and user inputs
    print("I find the circumference of a circle using Tau!")

    # Input
    radius = int(input("Please enter the radius (mm): "))

    # Process
    circumference = radius * constants.TAU

    # Output
    print("The circumference is {}mm".format(circumference))


if __name__ == "__main__":
    main()
