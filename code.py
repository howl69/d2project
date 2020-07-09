import requests
import json
import design
import os
import time
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

def fill_herostats(): #update herostats
    od = requests.get("https://api.opendota.com/api/heroStats")
    count_heroes = len(od.json())
    d = list(od.json()[0].keys())
    with open("heroes_stats.json", "w") as out:
        flag = 0
        for i in d:
            if flag == 0:
                flag = 1
            else:
                out.write(';')
            out.write(i)
        out.write('\n')
        for i in range(count_heroes):
            flag = 0
            for j in d:
                if flag == 0:
                    flag = 1
                else:
                    out.write(';')
                out.write(str(od.json()[i][j]))
            out.write('\n')

def winrates_fill(d): #update winrates
    with open("winrates.json", "w") as out:
        with open("heroes_stats.json", "r") as f:
            out.write('id;name;roles;winrate_Herald;winrate_Guardian;winrate_Crusader;winrate_Archon;'
                      'winrate_Legend;winrate_Ancient;winrate_Divine;winrate_Immortal;winrate_pro' + '\n')
            s = f.readlines()
            n = len(s)
            i = 1
            while i < n:
                substr = s[i].split(';')
                wr_1 = str(int(substr[d['1_win']]) / int(substr[d['1_pick']])) + ';'
                wr_2 = str(int(substr[d['2_win']]) / int(substr[d['2_pick']])) + ';'
                wr_3 = str(int(substr[d['3_win']]) / int(substr[d['3_pick']])) + ';'
                wr_4 = str(int(substr[d['4_win']]) / int(substr[d['4_pick']])) + ';'
                wr_5 = str(int(substr[d['5_win']]) / int(substr[d['5_pick']])) + ';'
                wr_6 = str(int(substr[d['6_win']]) / int(substr[d['6_pick']])) + ';'
                wr_7 = str(int(substr[d['7_win']]) / int(substr[d['7_pick']])) + ';'
                wr_8 = str(int(substr[d['8_win']]) / int(substr[d['8_pick']])) + ';'
                wr_pro = str(int(substr[d['pro_win']]) / int(substr[d['pro_pick']]))
                out.write(substr[d['id']] + ';' + substr[d['localized_name']] + ';' + substr[d['roles']]
                          + ';' + wr_1 + wr_2 + wr_3 + wr_4 + wr_5 + wr_6 + wr_7 + wr_8 + wr_pro + '\n')
                i += 1

def key_sort(strs):
    return strs[0]

#pyuic5 C:\Prog\dota\venv\design.ui -o C:\Prog\dota\venv\design.py

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.print_wr)

    def print_wr(self):
        self.listWidget.clear()
        with open("winrates.json", "w") as f:
            
        for i in range(n):
            self.listWidget.addItem(str(strs[i][2])+(20-len(strs[i][2]))*" " + strs[i][0])

with open('heroes_stats.json', 'r') as f:
    s = f.readlines()
    keys = s[0].split(';')
    len_keys = len(keys)
    keys[len_keys - 1] = keys[len_keys - 1][:-1]
    head_dict = {keys[i]: i for i in range(len_keys)}
    substr = s[5].split(';')
    wr_1 = str(int(substr[head_dict['1_win']]) / int(substr[head_dict['1_pick']])) + ';'
    print(wr_1)
    # for i in range(115):
    #     k = s[i].split(';')
    #     if k[d['id']]=='111':
    #         break
    # print(k[d['name']])   blablabla


# size = 4
# strs = []
# with open('heroes_nums.json', 'r') as f:
#     s = f.readlines()
#     n = len(s)
#     for i in range(n - 1):
#         strs.append(s[i + 1].split('; '))
#     strs = sorted(strs, key=key_sort, reverse = True)
#
# app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
# window = ExampleApp()  # Создаём объект класса ExampleApp
# window.show()  # Показываем окно
# sys.exit(app.exec_())  # и запускаем приложение

#print(data)
#highest_wr(data)



