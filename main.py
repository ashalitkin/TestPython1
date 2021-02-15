# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def STriangle(s):
    return abs(((int(s[3]) - int(s[15])) * (int(s[11]) - int(s[17])) - (int(s[9]) - int(s[15])) * (
                int(s[5]) - int(s[17]))) / 2)

with open('C:/Users/Гед/PycharmProjects/PythonProject1/file.txt', 'r') as f:
    array = f.readlines()

    array1 = []
    i=0
    for s in array:
        s = array[i]
        i=i+1
        array1.append(STriangle(s))

    array1 = sorted(array1)
    print('Площадь треугольников в порядке возрастания: ')
    print(array1)






