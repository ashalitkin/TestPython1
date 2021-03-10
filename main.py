# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from figure import Point, Circle, Triangle, Rectangle

def main():
    with open('file.txt', 'r') as f:
        array = f.readlines()

    list = []
    for line in array:
        if line[0] == 'T':
            figure = Triangle(line)
        elif line[0] == 'R':
            figure = Rectangle(line)
        elif line[0] == 'C':
            figure = Circle(line)
        else:
            raise Exception("wrong figure")

        list.append(figure)


    list.sort(key=lambda el: el.square())

    for el in list:
        print(el)


if __name__ == "__main__":
    main()



