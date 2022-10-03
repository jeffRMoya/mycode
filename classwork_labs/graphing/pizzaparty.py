#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'jalapenos', 'pineapple', 'olives', 'mushrooms'
    sizes = [7, 79, 7, 7]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

    plt.savefig("/home/student/static/perfectPizza.png")

if __name__ == "__main__":
    main()
