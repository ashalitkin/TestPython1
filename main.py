# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def STriangle(s):
    return abs(((int(s[3]) - int(s[15])) * (int(s[11]) - int(s[17])) - (int(s[9]) - int(s[15])) * (
                int(s[5]) - int(s[17]))) / 2)

f = open('C:/Users/Гед/PycharmProjects/PythonProject1/file.txt', 'r')


try:
    for line in f:
         s = line
         print(s)
         print('Площадь треугольника ' + str(STriangle(s)))
except:
    print('ERROR')
finally:
     f.close








