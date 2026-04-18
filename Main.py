# to wake up the window or make the window keep on sleeping:
sleep_mode = 'up'
if sleep_mode == 'up':

    # import the stuff we needed and the tkinter is the most importent if you needed it to do something
    from tkinter import *
    import time
    import random
    import math

    # tkinter's width, height and other varible that will be used
    WIN_WIDTH = 1500
    WIN_HEIGHT = 1200
    levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    Level = 1
    MAX_LEVEL = 25
    light_green = "#51FF00"
    dark_green = "#006E02"
    red = "#FF0000"
    yellow = "#FCDB00"
    move = 'yes'
    x1 = 25
    y1 = 25
    x2 = 60
    y2 = 60

    # to get the Window, we need this code and you can name your game anything you want
    Window = Tk()
    Window.title('Little Block')
    canvas = Canvas(Window, width=WIN_WIDTH, height=WIN_HEIGHT, bg='black')
    canvas.pack()
    Window.update()

    # for my player i use a class because it needs arrow keys to move and other stuff
    class Player:
        def __init__(self, color, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(25, 25, 60, 60, fill=color, outline=color)
            self.canvas = canvas
            self.x = 0
            self.y = 0
            self.move = 'yes'

            # at the start we will had to know which level we are in and put the player somewhere
            if (Level in levels):
                self.canvas.move(self.id, 680, 750)
                self.visible = True

            # it detects the keys you press then makes the player move
            if self.move == 'yes':
                self.canvas.bind_all('<KeyPress-Left>', self.left)
                self.canvas.bind_all('<KeyPress-Right>', self.right)
                self.canvas.bind_all('<KeyPress-Up>', self.up)
                self.canvas.bind_all('<KeyPress-Down>', self.down)


        # for this we need [self.canvas.move(self.id, self.x, self.y)] to move the player
        def draw(self):
            position = self.canvas.coords(self.id)
            self.canvas.move(self.id, self.x, self.y)
            self.position = self.canvas.coords(self.id)
            self.Px = self.position[2]
            self.Py = self.position[1]
            self.P1x = self.position[0]
            self.P1y = self.position[3]

            # when the player touch the edge, self.x = 0 and self.y = 0
            if (position[0] <= 0 or
                position[2] >= 1440
                ):
                self.x = 0

            if (position[1] <= 0 or
                position[3] >= 850
                ):
                self.y = 0

        def respawn(self):
            self.move = 'no'
            self.x = 0
            self.y = 0

        # example: if the left key is press, the player will go left
        def left(self, evt):
            self.x = self.x - 3
            self.y = 0
            if self.x <= -6:
                self.x = -3

        def right(self, evt):
            self.x = self.x + 3
            self.y = 0
            if self.x >= 6:
                self.x = 3

        def up(self, evt):
            self.y = self.y - 3
            self.x = 0
            if self.y <= -6:
                self.y = -3

        def down(self, evt):
            self.y = self.y + 3
            self.x = 0
            if self.y >= 6:
                self.y = 3


    # this is what the player go to, think stuff from the player class to here:
    class Goal:
        def __init__(self, color, player, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            self.x = 0
            self.y = 0
            self.player = player
            self.canvas = canvas
            if (Level == 1 or
                Level == 2 or
                Level == 3
                ):
                self.canvas.move(self.id, 680, 0)
                self.visible = True
                self.x = 3
            else:
                self.canvas.move(self.id, random.randint(0, WIN_WIDTH), random.randint(0, WIN_HEIGHT))

        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            self.GoalP = self.canvas.coords(self.id)
            self.Gx = self.GoalP[2]
            self.Gy = self.GoalP[1]
            self.G1x = self.GoalP[0]
            self.G1y = self.GoalP[3]

            global Level
            if ((self.GoalP[0] <= self.player.Px) and (self.G1y >= self.player.Py)):
                if not (self.player.position[3] <= self.GoalP[1]):
                    if not (self.player.position[0] >= self.GoalP[2]):
                        player.respawn()
                        Level += 1
                        # if (Level in levels):
                            # i figured out that the self.canvas.move is not putting the squares at the right spot, their just actully moving it even more.
                            # self.canvas.move(self.id, 680, 0)
                            # self.visible = True
                            # self.x = 3
                        # else:
                            # pass


            if (pos[0] <= 0 or
                pos[2] >= 1440
                ):
                self.x = self.x * -1

            if (pos[1] <= 0 or
                pos[3] >= 850
                ):
                self.y = self.y * -1
    # think stuff from player class to here:
    class Enemy:
        def __init__(self, color, speed, player, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            starts = [-10, -9, -8, -7, -6, -5, -4, -3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            self.x = 0
            self.y = 0
            self.canvas = canvas
            self.speed = speed
            self.player = player
            self.enemy_pos = self.canvas.coords(self.id)
            self.EnemyX = self.enemy_pos[0]
            self.EnemyY = self.enemy_pos[1]
            if (Level == 2 or
                Level == 4
                ):
                self.canvas.move(self.id, 680, 380)
            else:
                self.canvas.move(self.id, 2000, 2000)

        def draw(self):
            # self.player.x
            # self.player.y
            enemy_pos = self.canvas.coords(self.id)
            self.EnemyP = self.canvas.coords(self.id)
            self.Ex = self.EnemyP[2]
            self.Ey = self.EnemyP[1]
            self.E1x = self.EnemyP[0]
            self.E1y = self.EnemyP[3]

            if ((self.EnemyP[0] <= self.player.Px) and (self.E1y >= self.player.Py)):
                if not (self.player.position[3] <= self.EnemyP[1]):
                    if not (self.player.position[0] >= self.EnemyP[2]):
                        move = 'no'
                        player.respawn()

            #if sleep_mode == 'sleep':
                #DirX = 0
                #DirY = 0
                #dx =  - EnemyX          
                #dy = self.player.y
                #distances = math.sqrt(dx ** 2 + dy ** 2)
                #if (distances > 0):
                    #DirX = dx / distances
                    #DirY = dy / distances
                    #self.canvas.move(self.id, (DirX * self.speed), (DirY * self.speed))
                    #print(f'{player.PlayerX_I}, {player.PlayerY_I}, {player.PlayerX_II}, {player.PlayerY_II}')

            if False:
                self.x = self.player.PlayerX - self.EnemyX
                self.y = self.player.PlayerY - self.EnemyY
                print(f'{player.PlayerX}, {player.PlayerX}')



    class DangerStuff:
        def __init__(self, color, player, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            self.x = 0
            self.y = 0
            self.player = player
            self.canvas = canvas
            if (Level == 3 or
                Level == 4 or
                Level == 6
                ):
                self.canvas.move(self.id, 680, 510)
            else:
                self.canvas.move(self.id, 
                                 random.randint(0, 1440), 
                                 random.randint(0, 850))
                
        def draw(self):
            self.DsPos = self.canvas.coords(self.id)
            self.DsX = self.DsPos[2]
            self.Dsy = self.DsPos[1]
            self.Ds1x = self.DsPos[0]
            self.Ds1y = self.DsPos[3]
            
            if ((self.DsPos[0] <= self.player.Px) and (self.Ds1y >= self.player.Py)):
                if not (self.player.position[3] <= self.DsPos[1]):
                    if not (self.player.position[0] >= self.DsPos[2]):
                        player.respawn()

    # we make the stuff here:
    if (Level in levels):
        player = Player('white', canvas)
        goal = Goal(light_green, player, canvas)
        dangerstuff = DangerStuff(yellow, player, canvas)
        enemy = Enemy(red, 2, player, canvas)
        

    # without the while True we do mainloop but i'll do while True instead:
    while True:
    # it sends a signal then the player or the goal will move but first it needs to detect if the level existed:
        if (Level in levels):
            # some of the .draw mean that it have a player colide if in one of the class in the whole code, define and if.
            player.draw()
            goal.draw()
            enemy.draw()
            dangerstuff.draw()
            Window.update_idletasks()
            Window.update()

elif sleep_mode == 'sleep':
    print('')
    print('the window is sleeping: wake it up by the code using the "up" at the very start of the code')
    print('')
