"""
This is the main entry point of the script.
"""

import math
# Test import an external lib
import pandas


def main():
    """Run the main function"""
    print("Hello. The program has started to run.")
    print(f"The circumference of a circle of r=3 is {circumference(3)}")
    print(f"The pandas version installed is: {pandas.__version__}")


def circumference(radius):
    """Return the circumference to 2 decimal places

    c = 2r * pi
    """
    return round(2 * radius * math.pi, 2)


if __name__ == '__main__':
    main()
