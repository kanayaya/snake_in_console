import copy
import sys, os
import random
from time import sleep


class Snake:
    def __init__(self):
        self.head = [3, 1]
        self.body = [[2, 1], [1, 1]]
        self.direction = [1, 0]# -- вправо, [0, 1] -- вниз, [-1, 0] -- влево, [0, -1] -- вверх
        self.bbreak = False
        self.counter = 0

    def move(self):
        '''Приравнивает координаты сзадистоящих блоков тела к впередистоящим.
        координаты самого переднего блока приравнивает к координатам головы,
        а координаты головы модифицирует с помощью переменной direction.
        По умолчанию вправо.'''
        for i in range((len(self.body) - 1), 0, -1):
            self.body[i] = self.body[i - 1]
        self.body[0] = self.head
        self.head = [(self.head[0]+self.direction[0]), (self.head[1]+self.direction[1])]

    def manage(self, key):
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
        if key.name in managing_keys_dict and managing_keys_dict[key.name][0] != self.direction[0] and managing_keys_dict[key.name][1] != self.direction[1]:
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

def view_objects(maplist, snake, food):
    """На уже построенной карте показывает змейку и еду, заменяя символы
    на заданных в объекте класса Snake и переменной food координатах"""
    vmap = copy.deepcopy(maplist)
    vmap[snake.head[1]][snake.head[0]] =  vmap[snake.head[1]][snake.head[0]].replace(' ', 'O')
    for i in range(len(snake.body)):
        vmap[snake.body[i][1]][snake.body[i][0]] = vmap[snake.body[i][1]][snake.body[i][0]].replace(' ', '=')
    vmap[food[1]][food[0]] = vmap[food[1]][food[0]].replace(' ', 'x')
    return vmap

def show_map(maplist, counter):
    """Показывает конечный вид карты в виде сетки"""
    os.system('cls')
    print(4*'\n')
    print('Счет:  ' + str(counter))
    for i in range(len(maplist)):
        row = ''
        for j in range(len(maplist[i])):
            row += str(maplist[i][j])
            row += ' '
        print(row)

def set_food(map_lengh, map_width, blacklist, snake):
    """Задает положение еды"""
    while True:
        food = [random.randint(0, map_lengh - 2), random.randint(0, map_width - 2)]
        if food in snake.body or food == snake.head or food in blacklist:
            continue
        break
    return food

def food_getting(map_lengh, map_width, blacklist, snake):
    """Действие если голова змеи наезжает на еду.
    меняет положение еды, удлинняет змейку"""
    food = set_food(map_lengh, map_width, blacklist, snake)
    snake.body.append(snake.body[-1])
    snake.counter += 1
    return food, snake

def lose_game():
    """Действие при столкновении головы с препятствием или телом змейки"""
    return True

def start_game(new_snake):
    first_map = '1 1 1 1 1 1 1 1 1 1,\
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
    current_map = first_map.split(',')
    current_map = [i.split(' ') for i in current_map]
    map_lengh = len(current_map)
    map_width = len(current_map[0])

    blacklist = []
    for i in range(len(current_map)):
        for j in range(len(current_map[i])):
            if current_map[i][j] == '1':
                blacklist.append([j, i])

    current_map = build_map(current_map)

    food = set_food(map_lengh, map_width, blacklist, new_snake)
    viewed_map = view_objects(current_map, new_snake, food)
    show_map(viewed_map, new_snake.counter)

    return current_map, blacklist, map_lengh, map_width, food

def do_step(new_snake, current_map, blacklist, map_lengh, map_width, food):
    if new_snake.head in blacklist or new_snake.head in new_snake.body:
        new_snake.bbreak = lose_game()
        return
    if new_snake.head == food:
        food, new_snake = food_getting(map_lengh, map_width, blacklist, new_snake)
    viewed_map = view_objects(current_map, new_snake, food)

    show_map(viewed_map, new_snake.counter)
    return food