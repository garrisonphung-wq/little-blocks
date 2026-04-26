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
    Level = 1 #random.randint(1, 25)
    MAX_LEVEL = 25
    light_green = "#51FF00"
    dark_green = "#006E02"
    red = "#FF0000"
    yellow = "#FCDB00"
    yellow_green = "#C8FF00"
    orange = "#EB8806"
    move = 'yes'
    x1 = 25
    y1 = 25
    x2 = 60
    y2 = 60
    CoinPosX = 45
    CoinPosY = 20
    index = 0
    level_on = 'Level: ' + str(Level)
    coins = 0 #random.randint(0, 99)
    Coins = 'coins: ' + str(coins)
    total_coins = 0
    Tot = 0
    Deaths = 0
    Pass = 0
    position = 'yes'
    Death_num = []
    Pass_num = []
    num_text = []
    coin_text = []
    num_total = []
    FstSnd = 'first'
    x_spot = 740
    y_spot = 660
    comment_num = [] 

    # to get the Window, we need this code and you can name your game anything you want
    Window = Tk()
    Window.title('Blocky')
    canvas = Canvas(Window, width=WIN_WIDTH, height=WIN_HEIGHT, bg='black')
    canvas.pack()
    Window.update()
    Window.resizable(False, False)

    class WaveStarter:
        def __init__(self, color, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(25, 25, 1460, 870, fill=color, outline=color)
            self.x = 0
            self.y = 0
            self.canvas = canvas
            self.canvas.move(self.id, -21, -21)
            self.canvas.move(self.id, 6000, 6000)

        def ComeBack(self):
            self.canvas.move(self.id, -6000, -6000)

        def GetAway(self):
            self.canvas.move(self.id, 6000, 6000)

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
                if position[0] <= 0:
                    self.canvas.move(self.id, 9, 0)
                elif position[2] >= 1440:
                    self.canvas.move(self.id, -9, 0)

            if (position[1] <= 0 or
                position[3] >= 850
                ):
                self.y = 0
                if position[1] <= 0:
                    self.canvas.move(self.id, 0, 9)
                elif position[3] >= 850:
                    self.canvas.move(self.id, 0, -9)

        def respawn(self):
            self.move = 'no'
            self.x = 0
            self.y = 0
            self.canvas.move(self.id, self.position[2] * -1 + 60, self.position[3] * -1 + 60)
            self.canvas.move(self.id, 680, 750)

        def teleport(self):
            self.x = 0
            self.y = 0
            if Level == 10:
                self.canvas.move(self.id, self.position[2] * -1, self.position[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 200)
            if Level == 11:
                self.canvas.move(self.id, self.position[2] * -1, self.position[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 600)
                self.y = 4
            if Level == 12:
                self.canvas.move(self.id, self.position[2] * -1, self.position[3] * -1)
                self.canvas.move(self.id, x_spot, y_spot)
            if Level == 13:
                self.canvas.move(self.id, self.position[2] * -1, self.position[3] * -1)
                self.canvas.move(self.id, x_spot, y_spot)

        def Backup(self):
            self.canvas.move(self.id, self.position[2] * -1, self.position[3] * -1)
            self.canvas.move(self.id, 60, 60)
            self.canvas.move(self.id, 680, 540 - 90)
        
        def freeze(self):
            self.x = 0
            self.y = 0

        # example: if the left key is press, the player will go left
        def left(self, evt):
            self.x = self.x - 4
            self.y = 0
            if self.x <= -8:
                self.x = -4

        def right(self, evt):
            self.x = self.x + 4
            self.y = 0
            if self.x >= 8:
                self.x = 4

        def up(self, evt):
            self.y = self.y - 4
            self.x = 0
            if self.y <= -8:
                self.y = -4

        def down(self, evt):
            self.y = self.y + 4
            self.x = 0
            if self.y >= 8:
                self.y = 4

        def Bounce(self):
            if self.y == 4 or self.y == -4:
                self.y = self.y * -1
            elif self.x == 4 or self.x == -4:
                self.x = self.x * -1

    # this is what the player go to, think stuff from the player class to here:
    class Goal:
        def __init__(self, color, player, wavestarter, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            self.x = 0
            self.y = 0
            self.player = player
            #self.enemy = enemy
            #self.dangerstuff = dangerstuff
            #self.coin = coin
            self.wavestarter = wavestarter
            self.canvas = canvas
            if (Level in levels
                ):
                self.canvas.move(self.id, 680, 0)
                self.visible = True
                self.x = 3
            else:
                pass

        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            self.GoalP = self.canvas.coords(self.id)
            self.Gx = self.GoalP[2]
            self.Gy = self.GoalP[1]
            self.G1x = self.GoalP[0]
            self.G1y = self.GoalP[3]
            self.xPos = self.GoalP[2]
            self.yPos = self.GoalP[3]

            global Level, index, coins, Pass
            if ((self.GoalP[0] <= self.player.Px) and (self.G1y >= self.player.Py)):
                if not (self.player.position[3] <= self.GoalP[1]):
                    if not (self.player.position[0] >= self.GoalP[2]):
                            player.respawn()
                            Level += 1
                            Pass += 1
                            Pass_T = 'Pass: ' + str(Pass)
                            level_on = 'Level: ' + str(Level)
                            coins = 0
                            Coins = 'coins: ' + str(coins)
                            Passes = canvas.create_text(40, CoinPosY + 60, text=Pass_T, font=('roman bold', 20), fill='white')
                            COINS = canvas.create_text(CoinPosX, CoinPosY, text=Coins, font=('roman bold', 20), fill='white')
                            text = canvas.create_text(45, 825, text=level_on, font=('roman bold', 20), fill='white')
                            num_text.append(text)
                            Death_num.append(Deaths)
                            Pass_num.append(Passes)
                            coin_text.append(COINS)
                            canvas.delete(num_text[0])
                            canvas.delete(coin_text[0])
                            canvas.delete(Pass_num[0])
                            del num_text[0]
                            del Pass_num[0]
                            del coin_text[0]
                            time.sleep(1)
                            # not usefull: wavestarter.ComeBack()
                            enemy.Check()
                            dangerstuff.Check()
                            coin.Check()
                            enemyp.Check()
                            jelly.Check()
                            mainportal.Check()
                            portal.Check()
                            wall.Check()
                            wally.Check()
                            walln.Check()
                            regwall.check()
                            Check()
                            if Level in levels and True:
                                self.x = 0
                                self.y = 0
                                self.canvas.move(self.id, self.GoalP[2] * -1 + 36, self.GoalP[3] * -1 + 36)
                                self.canvas.move(self.id, 740 - 36, 60 - 36)
                                self.x = 3
                            # not use full: #wavestarter.GetAway()


            if (pos[0] <= 0 or
                pos[2] >= 1440
                ):
                self.x = self.x * -1

            if (pos[1] <= 0 or
                pos[3] >= 850
                ):
                self.y = self.y * -1
            
        def position(self):
            self.x = 0
            self.y = 0
            self.canvas.move(self.id, self.GoalP[2] * -1 + 36, self.GoalP[3] * -1 + 36)
            self.canvas.move(self.id, 740 - 36, 60 - 36)
            self.x = 3

    # think stuff from player class to here:
    class Enemy:
        def __init__(self, color, speed, player, goal, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            self.starts = [-10, -9, -8, -7, -6, -5, -4, -3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            self.stop = 'yes'
            self.x = 0
            self.y = 0
            self.canvas = canvas
            self.speed = speed
            self.player = player
            self.goal = goal
            self.enemy_pos = self.canvas.coords(self.id)
            self.EnemyX = self.enemy_pos[0]
            self.EnemyY = self.enemy_pos[1]
            self.EnemyP = self.canvas.coords(self.id)
            self.canvas.move(self.id, 2000, 2000)


        def draw(self):
            # self.player.x
            # self.player.y
            self.starts = [-10, -9, -8, -7, -6, -5, -4, -3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            self.canvas.move(self.id, self.x, self.y)
            enemy_pos = self.canvas.coords(self.id)
            self.EnemyP = self.canvas.coords(self.id)
            self.Ex = self.EnemyP[2]
            self.Ey = self.EnemyP[1]
            self.E1x = self.EnemyP[0]
            self.E1y = self.EnemyP[3]

            if self.EnemyP[0] <= 0 or self.EnemyP[2] >= 1440:
                self.x = self.x * -1
            elif self.EnemyP[1] <= 0 or self.EnemyP[3] >= 850:
                self.y = self.y * -1
            global death
            if ((self.EnemyP[0] <= self.player.Px) and (self.E1y >= self.player.Py)):
                if not (self.player.position[3] <= self.EnemyP[1]):
                    if not (self.player.position[0] >= self.EnemyP[2]):
                        move = 'no'
                        player.respawn()
                        goal.position()

        def Check(self):
            self.x = 0
            self.y = 0
            self.xPos = [-30, -25, -20, -15, 15, 20, 25, 30]
            self.yPos = [-30, -25, -20, -15, 15, 20, 25, 30]
            if Level == 2:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 0, 0)
                self.canvas.move(self.id, 680, 380)
                self.x = random.choice(self.starts)
                self.y = random.choice(self.starts)
            elif Level == 4:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 0, 0)
                self.canvas.move(self.id, 680, 60)
                self.x = random.choice(self.starts)
                self.y = random.choice(self.starts)
            elif Level == 5:
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, self.EnemyP[2] * -1, self.EnemyP[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 380)
                self.x = 0
                self.y = -15
            elif Level == 7:
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 160, 380)
                self.y = 35
                self.x = 0
            elif Level == 8:
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, self.EnemyP[2] * -1, self.EnemyP[3] * -1)
                self.canvas.move(self.id, 2060, 2060)
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 680, 380)
                self.x = random.choice(self.xPos)
                self.y = random.choice(self.yPos)
            elif Level == 9:
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, self.EnemyP[2] * -1, self.EnemyP[3] * -1)
                self.canvas.move(self.id, 680, 650)
                self.y = random.choice(self.yPos)
                self.x = random.choice(self.xPos)
            elif Level == 10:
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, self.EnemyP[2] * -1, self.EnemyP[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 500)
                self.x = 100
            elif Level == 11:
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, self.EnemyP[2] * -1, self.EnemyP[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680 / 2, 600)
                self.x = 50
            elif Level == 12:
                self.canvas.move(self.id, self.EnemyP[2] * -1, self.EnemyP[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 380 / 2)
                self.x = 100
            elif Level == 13:
                self.canvas.move(self.id, self.EnemyP[2] * -1, self.EnemyP[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 495)
            elif Level == 14:
                self.canvas.move(self.id, self.EnemyP[2] * -1, self.EnemyP[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 0, 380 + (380 / 2))
                self.x = 18
                self.y = 0
            else:
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, self.EnemyP[2] * -1, self.EnemyP[3] * -1)
                self.canvas.move(self.id, 2060, 2060)

        def Bounce(self):
            if self.x > 1 or self.x < 1:
                self.x = self.x * -1
            if self.y > 1 or self.y < 1 and Level != 14:
                self.y = self.y * -1

        def Gone(self):
            self.canvas.move(self.id, self.EnemyP[2] * -1, self.EnemyP[3] * -1)
            self.canvas.move(self.id, 2060, 2060)


    class EnemyH:
        def __init__(self, color, player, goal, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            self.starts = [-10, -9, -8, -7, -6, -5, -4, -3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            self.x = 0
            self.y = 0
            self.canvas = canvas
            self.player = player
            self.goal = goal
            self.canvas.move(self.id, 2000, 2000)

        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            self.HPos = self.canvas.coords(self.id)
            self.Hx = self.HPos[2]
            self.Hy = self.HPos[1]
            self.H1x = self.HPos[0]
            self.H1y = self.HPos[3]
            if self.HPos[0] <= 0 or self.HPos[2] >= 1440:
                self.x = self.x * -1
            elif self.HPos[1] <= 0 or self.HPos[3] >= 850:
                self.y = self.y * -1

            if ((self.HPos[0] <= self.player.Px) and (self.H1y >= self.player.Py)):
                if not (self.player.position[3] <= self.HPos[1]):
                    if not (self.player.position[0] >= self.HPos[2]):
                        move = 'no'
                        player.respawn()
                        goal.position()

        def Check(self):
            self.xPos = [-30, -25, -20, -15, 15, 20, 25, 30]
            if Level == int('5'):
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 680, 380)
                self.x = random.choice(self.xPos)
                self.y = 0
            if Level == int('7'):
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 0, 750)
                self.x = 67.5
            elif Level == 8:
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, self.HPos[2] * -1, self.HPos[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 380)
                self.x = random.choice(self.xPos)
                self.y = random.choice(self.xPos)
            elif Level == 10:
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, self.HPos[2] * -1, self.HPos[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 500)
                self.x = -67.5
            elif Level == 12:
                self.x = 0
                self.y = 0
                self.canvas.move(self.id, self.HPos[2] * -1, self.HPos[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 380 / 2)
                self.x = -67.5
            else:
                self.canvas.move(self.id, self.HPos[2] * -1, self.HPos[3] * -1)
                self.canvas.move(self.id, 50, 50)
                self.canvas.move(self.id, 2000, 2000)

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
        def __init__(self, color, player, goal, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            self.x = 0
            self.y = 0
            self.player = player
            self.goal = goal
            self.canvas = canvas
            if (Level == 3 or
                Level == 4 or
                Level == 6
                ):
                self.canvas.move(self.id, 2060, 2060)
            else:
                self.canvas.move(self.id, 
                                 2000, 
                                 2000)
                
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
                        goal.position()
                        if True:
                            pass

        def Check(self):
            if Level == 3:
                self.canvas.move(self.id, -4000, -4000)
                self.canvas.move(self.id, 0, 0)
                self.canvas.move(self.id, 680, 380)
                self.canvas.move(self.id, -1000, -1000)
                self.canvas.move(self.id, 300 + 60, -240)
            if Level == 4:
                self.canvas.move(self.id, -740, -440)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 0, 0)
                self.canvas.move(self.id, 680, 380)
            if Level == 11 or Level == 12:
                self.canvas.move(self.id, self.DsPos[2] * -1, self.DsPos[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 600)
            else:
                self.canvas.move(self.id, -740, -440)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 2000, 2000)

    class COIN:
        def __init__(self, color, player, goal, canvas):
            self.id = canvas
            self.x = 0
            self.y = 0
            self.player = player
            self.goal = goal
            self.canvas = canvas
            self.id = canvas.create_oval(25, 25, 50, 50, fill=color, outline=color)
            if Level == 1:
                self.canvas.move(self.id, 685, 380)

        def draw(self):
            global coins, total_coins
            self.CoinP = self.canvas.coords(self.id)
            self.Cx = self.CoinP[2]
            self.Cy = self.CoinP[1]
            self.C1x = self.CoinP[0]
            self.C1y = self.CoinP[3]

            if ((self.CoinP[0] <= self.player.Px) and (self.C1y >= self.player.Py)):
                if not (self.player.position[3] <= self.CoinP[1]):
                    if not (self.player.position[0] >= self.CoinP[2]):
                        self.canvas.move(self.id, 2000, 2000)
                        if Level == 6:
                            player.respawn()
                            self.canvas.move(self.id, -2000, -2000)
                        else:
                            if Level == 12:
                                if total_coins == 9:
                                    total_coins = 10
                                elif total_coins == 8:
                                    total_coins = 9
                                elif total_coins == 7:
                                    total_coins = 8
                                elif total_coins == 6:
                                    total_coins = 7
                                elif total_coins == 5:
                                    total_coins = 6
                                elif total_coins == 4:
                                    total_coins = 5
                                elif total_coins == 3:
                                    total_coins = 4
                                elif total_coins == 2:
                                    total_coins = 3
                                elif total_coins == 1:
                                    total_coins = 2
                                coins += 1
                                coins = 2
                            else:
                                total_coins += 1
                                coins += 1
                            Coins = 'coins: ' + str(coins)
                            Tot = total_coins
                            COINS = canvas.create_text(CoinPosX, CoinPosY, text=Coins, font=('roman bold', 20), fill='white')
                            Total = canvas.create_text(70, CoinPosY + 30, text='Total Coins: ' + str(total_coins), font=('roman blod', 20), fill='white')
                            coin_text.append(COINS)
                            num_total.append(Total)
                            canvas.delete(num_total[0])
                            canvas.delete(coin_text[0])
                            del num_total[0]
                            del coin_text[0]

        def Check(self):
            if Level == 2:
                self.canvas.move(self.id, -685, -380) 
                self.canvas.move(self.id, -2100.0, -2100.0) 
                self.canvas.move(self.id, 50, 50) 
                self.canvas.move(self.id, 735, 430)
            if Level == 3:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 0, -70)
            if Level == 4:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 0, 60)
            if Level == 5:
                self.canvas.move(self.id, 0, -60)
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, -735, -360)
                self.canvas.move(self.id, 50, 50)
                self.canvas.move(self.id, 685, 380)
            if Level == 6:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, -685, -380)
                self.canvas.move(self.id, 685, 380)
            if Level == 7:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 25, 25)
                self.canvas.move(self.id, 685, 380)
                self.canvas.move(self.id, -685, -380)
                self.canvas.move(self.id, 0, 380)
                self.canvas.move(self.id, -2050, -2430)
                self.canvas.move(self.id, 50, 50)
                self.canvas.move(self.id, 0, 380)
                self.canvas.move(self.id, 1950, 1570)
                self.canvas.move(self.id, 50, 380 + 50)
                self.canvas.move(self.id, self.CoinP[2] * -1, self.CoinP[3] * -1)
                self.canvas.move(self.id, 50, 50)
                self.canvas.move(self.id, 0 ,380)
                self.canvas.move(self.id, 1925, 1925)
                self.canvas.move(self.id, 50, 50)
                self.canvas.move(self.id, 0, -760)
                self.canvas.move(self.id, 0, 380)
            elif Level == 8:
                self.canvas.move(self.id, self.CoinP[2] * -1, self.CoinP[3] * -1)
                self.canvas.move(self.id, 50, 50)
                self.canvas.move(self.id, random.randint(0, 855), random.randint(0, 1445))
            elif Level == 9:
                self.canvas.move(self.id, self.CoinP[2] * -1, self.CoinP[3] * -1)
                self.canvas.move(self.id, 50, 50)
                self.canvas.move(self.id, 745 - 50 - 20 + 10, 385 - 50 - 20)
            elif Level == 11:
                self.canvas.move(self.id, self.CoinP[2] * -1, self.CoinP[3] * -1)
                self.canvas.move(self.id, 50, 50)
                self.canvas.move(self.id, 745 - 50 - 20 + 10, 605)
            elif Level == 12:
                self.canvas.move(self.id, self.CoinP[2] * -1, self.CoinP[3] * -1)
                self.canvas.move(self.id, 50, 50)
                self.canvas.move(self.id, 685, 605)

        def Move(self):
            global total_coins, coins
            if Level == 12 and position == 'yes':
                self.canvas.move(self.id, self.CoinP[2] * -1, self.CoinP[3] * -1)
                self.canvas.move(self.id, 50, 50)
                self.canvas.move(self.id, 5, 95)
                total_coins += 1
                coins += 1
                Coins = 'coins: ' + str(coins)
                COINS = canvas.create_text(CoinPosX, CoinPosY, text=Coins, font=('roman bold', 20), fill='white')
                Total = canvas.create_text(70, CoinPosY + 30, text='Total Coins: ' + str(total_coins), font=('roman blod', 20), fill='white')
                coin_text.append(COINS)
                num_total.append(Total)
                canvas.delete(num_total[0])
                canvas.delete(coin_text[0])
                del num_total[0]
                del coin_text[0]

    class Jelly:
        def __init__(self, color, player, enemy, goal, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(25, 25, 60, 60, fill=color, outline=color)
            self.player = player
            self.enemy = enemy
            self.goal = goal
            self.canvas = canvas
            self.x = 0
            self.y = 0
            self.canvas.move(self.id, 2060, 2060)

        def draw(self):
            self.JellyP = self.canvas.coords(self.id)
            self.Jx = self.JellyP[2]
            self.Jy = self.JellyP[1]
            self.J1x = self.JellyP[0]
            self.J1y = self.JellyP[3]

            if ((self.JellyP[0] <= self.player.Px) and (self.J1y >= self.player.Py)):
                if not (self.player.position[3] <= self.JellyP[1]):
                    if not (self.player.position[0] >= self.JellyP[2]):
                        move = 'no'
                        player.Bounce()

            if ((self.JellyP[0] <= self.enemy.Ex) and (self.J1y >= self.enemy.Ey)):
                if not (self.enemy.EnemyP[3] <= self.JellyP[1]):
                    if not (self.enemy.EnemyP[0] >= self.JellyP[2]):
                        move = 'no'
                        enemy.Bounce()

        def Check(self):
            if Level == 9:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 740, 420)
            if Level == 11:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 620, 600)
            else:
                self.canvas.move(self.id, self.JellyP[2] * -1, self.JellyP[3] * -1)
                self.canvas.move(self.id, 2000, 2000)

    class MainPortal:
        def __init__(self, color, player, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(25, 25, 60, 60, fill=color, outline=color)
            self.canvas = canvas
            self.x = 0
            self.y = 0
            self.player = player
            self.canvas.move(self.id, 2000, 2000)

        def draw(self):
            global x_spot, y_spot
            self.PP = self.canvas.coords(self.id)
            self.PPx = self.PP[2]
            self.PPy = self.PP[3]
            self.PP1x = self.PP[0]
            self.PP1y = self.PP[3]

            if ((self.PP[0] <= self.player.Px) and (self.PP1y >= self.player.Py)):
                if not (self.player.position[3] <= self.PP[1]):
                    if not (self.player.position[0] >= self.PP[2]):
                        move = 'no'
                        portal.Move()
                        Check1()
                        if Level == 14:
                            player.Bounce()
                        else:
                            player.teleport()
                        if Level == 13 and FstSnd != 'out of ourder':
                            self.canvas.move(self.id, 0, -375)
                        elif Level == 13 and FstSnd == 'out of ourder':
                            wally.Gone()
                            walln.Gone()


        def Check(self):
            if Level == 10:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 900, 750)
            if Level == 11:
                self.canvas.move(self.id, self.PP[2] * -1, self.PP[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 380)
            if Level == 12:
                self.canvas.move(self.id, self.PP[2] * -1, self.PP[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680 / 4, 380)
            if Level == 13:
                self.canvas.move(self.id, self.PP[2] * -1, self.PP[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 540)
            if Level == 14:
                self.canvas.move(self.id, self.PP[2] * -1, self.PP[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 380 + (380 / 4))

    class Portal:
        def __init__(self, color, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(25, 25, 60, 60, fill=color, outline=color)
            self.canvas = canvas
            self.x = 0
            self.y = 0
            self.canvas.move(self.id, 2000, 2000)

        def draw(self):
            self.Ppos = self.canvas.coords(self.id)

        def Check(self):
            global x_spot, y_spot
            if Level == 10:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 680, 200)
            if Level == 11:
                self.canvas.move(self.id, self.Ppos[2] * -1, self.Ppos[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 600)
            if Level == 12:
                x_spot = 740
                y_spot = 660
            if Level == 13:
                self.canvas.move(self.id, self.Ppos[2] * -1, self.Ppos[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 540 - 90)
                x_spot = self.Ppos[2]
                y_spot = self.Ppos[3]
            if Level == 14:
                self.canvas.move(self.id, self.Ppos[2] * -1, self.Ppos[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 380 - (380 / 2.5))

        def Move(self):
            global x_spot, y_spot
            if Level == 12:
                self.canvas.move(self.id, self.Ppos[2] * -1, self.Ppos[3] * -1)
                self.canvas.move(self.id, 60, 150)
                x_spot = self.Ppos[2]
                y_spot = self.Ppos[3]
                coin.Move()
            if Level == 13:
                self.canvas.move(self.id, self.Ppos[2] * -1, self.Ppos[3] * -1)
                self.canvas.move(self.id, 60, 60)
                self.canvas.move(self.id, 680, 85)
        
    class Wall:
        def __init__(self, color, player, enemy, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(0, 0, 1440, 35, fill='red', outline='dark red')
            self.canvas = canvas
            self.x = 0
            self.y = 0
            self.player = player
            self.enemy =  enemy
            if Level == 13:
                self.canvas.move(self.id, 0, 150)
            else:
                self.canvas.move(self.id, 2000, 2000)

        def draw(self):
            self.WallP = self.canvas.coords(self.id)
            self.Wx = self.WallP[2]
            self.Wy = self.WallP[1]
            self.W1x = self.WallP[0]
            self.W1y = self.WallP[3]

            if ((self.WallP[0] <= self.player.Px) and (self.W1y >= self.player.Py)):
                if not (self.player.position[3] <= self.WallP[1]):
                    if not (self.player.position[0] >= self.WallP[2]):
                        move = 'no'
                        player.respawn()
                        goal.position()

            if ((self.WallP[0] <= self.enemy.Ex) and (self.W1y >= self.enemy.Ey)):
                if not (self.enemy.EnemyP[3] <= self.WallP[1]):
                    if not (self.enemy.EnemyP[0] >= self.WallP[2]):
                        move = 'no'
                        enemy.Bounce()

        def Check(self):
            if Level == 13:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 0, 150)
            if Level == 14:
                self.canvas.move(self.id, self.WallP[2] * -1, self.WallP[3] * -1)
                self.canvas.move(self.id, 2000, 2000)

    class WallY:
        def __init__(self, color, wall, player, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(0, 0, 35, 850, fill=color, outline='dark red')
            self.canvas = canvas
            self.wall = wall
            self.player = player
            self.x = 0
            self.y = 0
            self.canvas.move(self.id, 2000, 2000)
            if Level == 13:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 664, 0)


        def draw(self):
            self.YP = self.canvas.coords(self.id)
            self.Yx = self.YP[2]
            self.Yx = self.YP[1]
            self.Y1x = self.YP[0]
            self.Y1y = self.YP[3]

            if ((self.YP[0] <= self.player.Px) and (self.Y1y >= self.player.Py)):
                if not (self.player.position[3] <= self.YP[1]):
                    if not (self.player.position[0] >= self.YP[2]):
                        move = 'no'
                        player.respawn()
                        goal.position()

        def Check(self):
            if Level == 13:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 664, 0)

        def Gone(self):
            self.canvas.move(self.id, 2000, 2000)

    class WallN:
        def __init__(self, color, player, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(0, 0, 35, 850, fill='red', outline='dark red')
            self.player = player
            self.canvas = canvas
            self.x = 0
            self.y = 0
            if Level == 13:
                self.canvas.move(self.id, 670 + 76, 0)
            else:
                self.canvas.move(self.id, 2000, 2000)

        def draw(self):
            self.NP = self.canvas.coords(self.id)
            self.Nx = self.NP[2]
            self.Ny = self.NP[1]
            self.N1x = self.NP[0]
            self.N1y = self.NP[3]

            if ((self.NP[0] <= self.player.Px) and (self.N1y >= self.player.Py)):
                if not (self.player.position[3] <= self.NP[1]):
                    if not (self.player.position[0] >= self.NP[2]):
                        move = 'no'
                        player.respawn()
                        goal.position()

        def Check(self):
            if Level == 13:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 670 + 76, 0)

        def Gone(self):
            self.canvas.move(self.id, 2000, 2000)

    def Check():
        global x_spot, y_spot, FstSnd, comment_num
        if Level == 13 and FstSnd == 'first':
            x_spot = 680 + 60
            y_spot = (540 - 90) + 60
        if Level == 14:
            comment = canvas.create_text(1300, 25, text='''what happend to the portal?''', font=('roman bold', 20), fill='white')
            comment_num.append(comment)
        if Level == 15:
            canvas.delete(comment_num[0])
            del comment_num[0]

    def Check1():
        global x_spot, y_spot, FstSnd
        if Level == 13 and FstSnd == 'first':
            enemy.Gone()
            FstSnd = 'second'
            x_spot = 680 + 60
            y_spot = (540 - 90) + 60
        elif Level == 13:
            Check2()
            #player.Backup()

    def Check2():
        global x_spot, y_spot, FstSnd
        #enemy.Gone()
        if Level == 13 and FstSnd == 'second':
            x_spot = 680 + 60
            y_spot = 60 + 85
            print(f'{x_spot}, {y_spot}')
            FstSnd = 'out of ourder'

    class RegWall:
        def __init__(self, color, player, enemy, canvas):
            self.id = canvas
            self.id = canvas.create_rectangle(0, 0, 1440, 35, fill=color, outline=color)
            self.canvas = canvas
            self.x = 0
            self.y = 0
            self.player = player
            self.enemy = enemy
            if Level == 14:
                self.canvas.move(self.id, 0, (420 - 35))
            else:
                # to put away the Regular Wall
                # hint: there is a way to get pass this wall
                self.canvas.move(self.id, 2000, 2000)

        def draw(self):
            self.RP = self.canvas.coords(self.id)
            self.Rx = self.RP[2]
            self.Ry = self.RP[1]
            self.R1x = self.RP[0]
            self.R1y = self.RP[3]

            if ((self.RP[0] <= self.player.Px) and (self.R1y >= self.player.Py)):
                if not (self.player.position[3] <= self.RP[1]):
                    if not (self.player.position[0] >= self.RP[2]):
                        move = 'no'
                        player.freeze()

            if ((self.RP[0] <= self.enemy.Ex) and (self.R1y >= self.enemy.Ey)):
                if not (self.enemy.EnemyP[3] <= self.RP[1]):
                    if not (self.enemy.EnemyP[0] >= self.RP[2]):
                        move = 'no'
                        enemy.Bounce()

        def check(self):
            if Level == 14:
                self.canvas.move(self.id, -2000, -2000)
                self.canvas.move(self.id, 0, 420 - 35)
                print(comment_num)
            if Level == 15:
                self.canvas.move(self.id, self.RP[2] * -1, self.RP[3] * -1)
                self.canvas.move(self.id, 2000, 2000)

    # we make the stuff here:
    if (Level in levels):
        wavestarter = WaveStarter("#FFFFFF", canvas)
        portal = Portal('#78CDF4', canvas)
        player = Player('white', canvas)
        mainportal = MainPortal("#78CDF4", player, canvas)
        goal = Goal(light_green, player, wavestarter, canvas)
        dangerstuff = DangerStuff(orange, player, goal, canvas)
        enemy = Enemy(red, 2, player, goal, canvas)
        enemyp = EnemyH(red, player, goal, canvas)
        coin = COIN(yellow_green, player, goal, canvas)
        jelly = Jelly("#FA7BAE", player, enemy, goal, canvas)
        wall = Wall("#000000", player, enemy, canvas)
        wally = WallY('red', wall, player, canvas)
        walln = WallN('red', player, canvas)
        regwall = RegWall("#646464", player, enemy, canvas)
        #goal = Goal(light_green, dangerstuff, enemy, coin, canvas)
        wavestarter = WaveStarter("#FFFFFF", canvas)
    
    Passes = canvas.create_text(40, CoinPosY + 60, text='Pass: ' + str(Pass), font=('roman bold', 20), fill='white')
    Total = canvas.create_text(70, CoinPosY + 30, text='Total Coins: ' + str(total_coins), font=('roman bold', 20), fill='white')
    COINS = canvas.create_text(CoinPosX, CoinPosY, text=Coins, font=('roman bold', 20), fill='white')
    text = canvas.create_text(45, 825, text=level_on, font=('roman bold', 20), fill='white')
    Pass_num.append(Passes)
    num_total.append(Total)
    num_text.append(text)
    coin_text.append(COINS)
    # without the while True we do mainloop but i'll do while True instead:
    while True:
    # it sends a signal then the player or the goal will move but first it needs to detect if the level existed:
        if (Level in levels):
            # some of the .draw mean that it have a player colide if in one of the class in the whole code, define and if.
            player.draw()
            mainportal.draw()
            portal.draw()
            goal.draw()
            enemy.draw()
            enemyp.draw()
            dangerstuff.draw()
            coin.draw()
            jelly.draw()
            wall.draw()
            wally.draw()
            walln.draw()
            regwall.draw()
            Window.update_idletasks()
            Window.update()

elif sleep_mode == 'sleep':
    print('')
    print('the window is sleeping: wake it up by the code using the "up" at the very start of the code')
    print('')