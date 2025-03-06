#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: March 1, 2025
# This program asks the user for the Length of
# the octagon in mm the apothem and height of prism. It then calculates and displays
# the volume and surface area using tau.
import math


def main():
    # get the length
    # get the apothem
    # get the height
    side_length = float(input("What is the side length of your octagonal prism"))
    apothem = float(input("What is the apothem of of your octagonal prism"))
    height = float(input("What is the height of the octagonal prism"))

    # process

    # Calculate the base area
    base_area = 4 * side_length * apothem

    # Calculate the lateral surface area
    lateral_surface_area = 8 * side_length * height

    # Calculate the surface area
    surface_area = 2 * base_area + lateral_surface_area

    # Calculate the volume
    volume = base_area * height

    # Display the results
    print("\n")
    print(
        "The surface area of the octagonal prism is: {:.2f} square units".format(
            surface_area
        )
    )
    print("The volume of the octagonal prism is: {:.2f} cubic units".format(volume))


if __name__ == "__main__":
    main()
