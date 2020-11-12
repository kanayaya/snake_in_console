import os, sys


class Menu:
    def __init__(self, menu_dict):
        self.menu_dict = menu_dict
        self.current_menu = change_menu(self.menu_dict, 'main_menu')
        self.launch_game_var = False
        self.difficulty = 0.2
        self.exitvar = False

    def show_menu(self):
        """Показывает меню, выбранным считается пункт со вторым пунктом True"""
        os.system('cls')
        print(self.current_menu[0])
        print(10 * '\n')
        tab = 6 * '\t'
        for i in range(1, len(self.current_menu)):
            if self.current_menu[i][1]:
                print(tab + '>' + self.current_menu[i][0] + '<')
            else:
                print(tab + ' ' + self.current_menu[i][0])

    def manage_menu(self, key):
        """Позволяет управлять меню с помощью кнопок W и S на клавиатуре. когда выбор произведен,
        нажат Enter, меняет переменную menu_dict_key и переходит в другое меню"""
        menu_keys_dict = {
            'w' : -1,
            's' : 1,
            'up' : -1,
            'down' : 1,
        }
        if key.name in menu_keys_dict:
            self.current_menu = self.change_position(menu_keys_dict, key)
            self.show_menu()

        elif key.name == 'enter':
            for i in range(1, len(self.current_menu)):
                if self.current_menu[i][1]:
                    if len(self.current_menu[i]) == 4:
                        os.system('cls')
                        self.current_menu = self.current_menu[i][2](self.menu_dict, self.current_menu[i][3])
                        self.show_menu()
                        break
                    elif len(self.current_menu[i]) == 3:
                        self.difficulty = self.current_menu[i][2]
                        self.launch_game_var = True
                        break
                    elif len(self.current_menu[i]) == 2:
                        self.exitvar = True


        else:
            pass

    def change_position(self, menu_keys_dict, key):
        """Меняет позицию выбора в менюшке, перетаскивая '> <' по пунктам"""
        position = 0
        for i in range(len(self.current_menu)):
            if self.current_menu[i][1]:
                position = i
        self.current_menu[position][1] = False

        if position + menu_keys_dict[key.name] == len(self.current_menu):
            position = 1
            self.current_menu[position][1] = True

        elif position + menu_keys_dict[key.name] < 1:
            position = len(self.current_menu) - 1
            self.current_menu[position][1] = True

        else:
            self.current_menu[position + menu_keys_dict[key.name]][1] = True

        return  self.current_menu

def change_menu(menu_dict, dict_key):
    return menu_dict[dict_key]

def exit_game(*no_args_needed_but_they_will_come):
    os.system('cls')
    return True

main_menu_list = [
    'Главное меню',
    ['Новая игра', True, change_menu, 'new_game'],
    ['Рекорды # Пока не работает', False, change_menu, 'scores'],
    ['Настройки # Пока не работает', False, change_menu, 'options'],
    ['Выход # Пока не работает', False],
]
newgame_settings_list = [
    'Выберите сложность:',
    ['Лёгкая', True, 0.4],
    ['Средняя', False, 0.3],
    ['Сложная', False, 0.2],
]
scores_list = [
    'Рекорды',
    ['Рекорды # Пока не работает', False, change_menu, 'scores'],
    ['Рекорды # Пока не работает', False, change_menu, 'scores'],
    ['Рекорды # Пока не работает', False, change_menu, 'scores'],
]
options_menu_list = [
    'Настройки',
    ['Настройки', True, change_menu, 'options'],
    ['Настройки', False, change_menu, 'options'],
    ['Настройки', False, change_menu, 'options'],
]

lose_menu_list = [
    'Вы проиграли, ваш счёт:   ',
    ['Новая игра', True, change_menu, 'new_game'],
    ['Выход', False],
]

all_menus_dict = {
    'main_menu' : main_menu_list,
    'options' : options_menu_list,
    'new_game' : newgame_settings_list,
    'lose_game' : lose_menu_list
}
