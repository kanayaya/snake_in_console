import copy
import sys, os
import random
from time import sleep

import keyboard


class Snake:
    def __init__(self):
        self.head = []
        self.body = []
        self.direction = []
        self.bbreak = False
        self.counter = 0

    def New_snake(self):
        '''Создает новую змейку на указанных координатах, начиная новую игру'''
        self.head = [3, 1]
        self.body = [[2, 1], [1, 1]]
        self.direction = [1, 0]# -- вправо, [0, 1] -- вниз, [-1, 0] -- влево, [0, -1] -- вверх

    def Move(self):
        '''Приравнивает координаты сзадистоящих блоков тела к впередистоящим.
        координаты самого переднего блока приравнивает к координатам головы,
        а координаты головы модифицирует с помощью переменной direction.
        По умолчанию вправо.'''
        for i in range((len(self.body) - 1), 0, -1):
            self.body[i] = self.body[i - 1]
        self.body[0] = self.head
        self.head = [(self.head[0]+self.direction[0]), (self.head[1]+self.direction[1])]

    def Manage(self, key):

        managing_keys_dict = {
            'esc' : self.direction,
            '' : self.direction,
            'w' : [0, -1],
            'a' : [-1, 0],
            's' : [0, 1],
            'd' : [1, 0],
            'ц': [0, -1],
            'ф': [-1, 0],
            'ы': [0, 1],
            'в': [1, 0],
            'up': [0, -1],
            'left': [-1, 0],
            'down': [0, 1],
            'right': [1, 0],
        }
        try:
            if key.name == 'esc':
                self.bbreak = True
            self.direction = managing_keys_dict[key.name]
        except KeyError:
            pass


def Build_map(maplist):
    """Заменяет единицы и нули (ноль -- пол, единица -- стена)
     на заданные в самой функции "текстуры\""""
    for i in range(len(maplist)):
        for j in range(len(maplist[i])):
            maplist[i][j] = maplist[i][j].replace('1', 'U')
            maplist[i][j] = maplist[i][j].replace('0', ' ')

def View_objects(maplist):
    '''На уже построенной карте показывает змейку и еду, заменяя символы
    на заданных в объекте класса Snake и переменной food координатах'''
    vmap = copy.deepcopy(maplist)
    vmap[Nsnake.head[1]][Nsnake.head[0]] =  vmap[Nsnake.head[1]][Nsnake.head[0]].replace(' ', 'O')
    for i in range(len(Nsnake.body)):
        vmap[Nsnake.body[i][1]][Nsnake.body[i][0]] = vmap[Nsnake.body[i][1]][Nsnake.body[i][0]].replace(' ', '=')
    vmap[food[1]][food[0]] = vmap[food[1]][food[0]].replace(' ', 'x')
    return vmap

def ReshowMap(maplist):
    '''Показывает конечный вид карты в виде сетки'''
    print('Счет:  ' + str(Nsnake.counter))
    for i in range(len(maplist)):
        row = ''
        for j in range(len(maplist[i])):
            row += str(maplist[i][j])
            row += ' '
        print(row)

def Set_food():
    '''Задает положение еды'''
    while True:
        food = [random.randint(0, len(firstMap[1]) - 1), random.randint(0, len(firstMap) - 1)]
        if food in Nsnake.body or food == Nsnake.head or food in blacklist:
            continue
        break
    return food

def Food_getting(food):
    '''Действие если голова змеи наезжает на еду.
    меняет положение еды, удлинняет змейку'''
    if Nsnake.head == food:
        food = Set_food()
        Nsnake.body.append(Nsnake.body[-1])
        Nsnake.counter += 1
    return food

def Collision():
    '''Действие при столкновении головы с препятствием или телом змейки'''
    if Nsnake.head in Nsnake.body or Nsnake.head in blacklist:
        print(20 * '\n')
        print(7 * '\t' + 'Проиграл))))')
        print(10 * '\n')
        sys.exit()


#menu will be added later
if __name__ == '__main__':

    firstMap = '1 1 1 1 1 1 1 1 1 1,\
1 0 0 0 0 0 0 0 0 1,\
1 0 0 0 0 0 0 0 0 1,\
1 0 0 0 0 0 0 0 0 1,\
1 0 0 0 0 0 0 0 0 1,\
1 0 0 0 0 0 0 0 0 1,\
1 0 0 0 0 0 0 0 0 1,\
1 0 0 0 0 0 0 0 0 1,\
1 0 0 0 0 0 0 0 0 1,\
1 0 0 0 0 0 0 0 0 1,\
1 1 1 1 1 1 1 1 1 1'

    firstMap = firstMap.split(',')
    #for i in range(len(firstMap)):
    #    firstMap[i] = firstMap[i].split(' ')
    firstMap = [i.split(' ') for i in firstMap]

    blacklist = []
    for i in range(len(firstMap)):
        for j in range(len(firstMap[i])):
            if firstMap[i][j] == '1':
                blacklist.append([j, i])

    Nsnake = Snake()
    Build_map(firstMap)
    Nsnake.New_snake()
    food = Set_food()
    vmap = View_objects(firstMap)
    ReshowMap(vmap)
    print('Нажмите Shift')
    keyboard.wait('Shift')
    while True:
        Collision()
        food = Food_getting(food)
        vmap = View_objects(firstMap)
        os.system('cls')
        print(10 * '\n')
        ReshowMap(vmap)
        keyboard.on_press(Nsnake.Manage)
        sleep(0.2)
        Nsnake.Move()
        if Nsnake.bbreak:
            break

    os.system('cls')
    sys.exit()
