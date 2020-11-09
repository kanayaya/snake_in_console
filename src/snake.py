import copy
import sys, os
import random
from time import sleep

import keyboard


class Snake:
    def __init__(self, snake):
        self.head = [3, 1]
        self.body = [[2, 1], [1, 1]]
        self.direction = [1, 0]# -- вправо, [0, 1] -- вниз, [-1, 0] -- влево, [0, -1] -- вверх
        self.bbreak = False
        self.counter = 0

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
        if key.name in managing_keys_dict:
            self.direction = managing_keys_dict[key.name]
        else:
            pass


def build_map(maplist):
    """Заменяет единицы и нули (ноль -- пол, единица -- стена)
     на заданные в самой функции "текстуры\""""
    for i in range(len(maplist)):
        for j in range(len(maplist[i])):
            maplist[i][j] = maplist[i][j].replace('1', 'U')
            maplist[i][j] = maplist[i][j].replace('0', ' ')
    return maplist

def view_objects(maplist, snake_head, snake_body, food):
    """На уже построенной карте показывает змейку и еду, заменяя символы
    на заданных в объекте класса Snake и переменной food координатах"""
    vmap = copy.deepcopy(maplist)
    vmap[snake_head[1]][snake_head[0]] =  vmap[snake_head[1]][snake_head[0]].replace(' ', 'O')
    for i in range(len(snake_body)):
        vmap[snake_body[i][1]][snake_body[i][0]] = vmap[snake_body[i][1]][snake_body[i][0]].replace(' ', '=')
    vmap[food[1]][food[0]] = vmap[food[1]][food[0]].replace(' ', 'x')
    return vmap

def show_map(maplist, counter):
    """Показывает конечный вид карты в виде сетки"""
    os.system('cls')
    print('Счет:  ' + str(counter))
    for i in range(len(maplist)):
        row = ''
        for j in range(len(maplist[i])):
            row += str(maplist[i][j])
            row += ' '
        print(row)

def set_food(map_lengh, map_width, blacklist, snake_head, snake_body):
    """Задает положение еды"""
    while True:
        food = [random.randint(0, map_lengh - 1), random.randint(0, map_width - 1)]
        if food in snake_body or food == snake_head or food in blacklist:
            continue
        break
    return food

def food_getting(snake_body, counter):
    """Действие если голова змеи наезжает на еду.
    меняет положение еды, удлинняет змейку"""
    food = set_food()
    snake_body.append(snake_body[-1])
    counter += 1
    return food, snake_body, counter

def lose_game():
    """Действие при столкновении головы с препятствием или телом змейки"""
    os.system('cls')
    print(20 * '\n')
    print(7 * '\t' + 'Проиграл))))')
    print(10 * '\n')
    sys.exit()
#
# def start_game(map):
#     map = map.split(',')
#     # for i in range(len(firstMap)):
#     #    firstMap[i] = firstMap[i].split(' ')
#     map = [i.split(' ') for i in map]
#
#     blacklist = []
#     for i in range(len(map)):
#         for j in range(len(map[i])):
#             if map[i][j] == '1':
#                 blacklist.append([j, i])
#
#     nsnake = Snake()
#     Build_map(map)
#     nsnake.New_snake()
#     food = Set_food()
#     vmap = View_objects(map)
#     ReshowMap(vmap)
#     print('Нажмите Shift')
#     keyboard.wait('Shift')
#     while True:
#         Collision()
#         food = Food_getting(food)
#         vmap = View_objects(map)
#         print(10 * '\n')
#         ReshowMap(vmap)
#         keyboard.on_press(nsnake.Manage)
#         sleep(0.2)
#         nsnake.Move()
#         if nsnake.bbreak:
#             break
#
#     os.system('cls')
#     sys.exit()
#
#
# #menu will be added later
# if __name__ == '__main__':
#
#     first_map = '1 1 1 1 1 1 1 1 1 1,\
# 1 0 0 0 0 0 0 0 0 1,\
# 1 0 0 0 0 0 0 0 0 1,\
# 1 0 0 0 0 0 0 0 0 1,\
# 1 0 0 0 0 0 0 0 0 1,\
# 1 0 0 0 0 0 0 0 0 1,\
# 1 0 0 0 0 0 0 0 0 1,\
# 1 0 0 0 0 0 0 0 0 1,\
# 1 0 0 0 0 0 0 0 0 1,\
# 1 0 0 0 0 0 0 0 0 1,\
# 1 1 1 1 1 1 1 1 1 1'
#
#     start_game(first_map)