# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""

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


"""



class Triangle:
        def __init__(self, x1, y1, x2, y2, x3, y3):
            self.x1 = x1
            self.x2 = x2
            self.x3 = x3
            self.y1 = y1
            self.y2 = y2
            self.y3 = y3
        def square_method(self):
            return abs((self.x1-self.x3)*(self.y2-self.y3) - (self.x2-self.x3)*(self.y1-self.y3))/2


class Rectangle:
        def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
            self.x1 = x1
            self.x2 = x2
            self.x3 = x3
            self.x4 = x4
            self.y1 = y1
            self.y2 = y2
            self.y3 = y3
            self.y4 = y4
        def square_method(self):
            return (self.x3-self.x1)*(self.y3-self.y1)


class Circle:
        def __init__(self, x1, y1, r):
            self.x1 = x1
            self.y1 = y1
            self.r = r
        def square_method(self):
            return 3.14*self.r*self.r


with open('C:/Users/Гед/PycharmProjects/PythonProject1/file.txt', 'r') as f:
    array = f.readlines()

#print(array)

dict1 = {}
i=0
for s in array:
    s = array[i]
    i = i+1
    if s[0] == 'T':
        Tr = Triangle(int(s[3]), int(s[5]), int(s[9]), int(s[11]), int(s[15]), int(s[17]))
        s = Tr.square_method()
        dict1[i] =('Площадь=' + str(s) + ' Треугольник  x1=' + str(Tr.x1) + ', y1=' + str(Tr.y1) +
                      ' x2=' + str(Tr.x2) + ', y2=' + str(Tr.y2) +
                      ' x3=' + str(Tr.x3) + ', y3=' + str(Tr.y3)
                      )
        del Tr
    elif s[0] == 'R':
        Rc = Rectangle(int(s[3]), int(s[5]), int(s[9]), int(s[11]), int(s[15]), int(s[17]), int(s[21]), int(s[23]))
        s = Rc.square_method()
        dict1[i] =('Площадь=' + str(s) + ' Прямоугольник  x1=' + str(Rc.x1) + ', y1=' + str(Rc.y1) +
                      ' x2=' + str(Rc.x2) + ', y2=' + str(Rc.y2) +
                      ' x3=' + str(Rc.x3) + ', y3=' + str(Rc.y3) +
                      ' x4=' + str(Rc.x4) + ', y4=' + str(Rc.y4)
                    )
        del Rc
    elif s[0] == 'C':
        Cr = Circle(int(s[3]), int(s[5]), int(s[8]))
        s = Cr.square_method()
        dict1[i] =('Площадь=' + str(s) + ' Круг  x1=' + str(Cr.x1) + ', y1=' + str(Cr.y1) +
                      ' R=' + str(Cr.r)
                      )
        del Cr


list_d = list(dict1.items())

list_d.sort(key=lambda i: i[1])

for i in list_d:
     print(i[1])


