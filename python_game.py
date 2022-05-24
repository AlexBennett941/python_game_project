import turtle
import random

screen = turtle.Screen()
screen.setup(435,500)

#Prudhomme
def setup_enemies(unit, index):
    unit.hideturtle()
    unit.penup()
    unit.color('red')
    unit.shapesize(2)
    unit.speed(0)
    unit.seth(270)
    x_pos = int()
    if index == 0:
        x_pos = random.randint(-170, -110)
    elif index == 1:
        x_pos = random.randint(-100, -40)
    elif index == 2:
        x_pos = random.randint(-30, 30)
    elif index == 3:
        x_pos = random.randint(40, 100)
    elif index == 4:
        x_pos = random.randint(110, 170)
    # x_pos = random.randint(-170, 170)
    unit.setx(x_pos)
    unit.sety(120)
    unit.showturtle()

#Prudhomme
def reset_enemy(unit, index):
    unit.hideturtle()
    x_pos = int()
    if index == 0:
        x_pos = random.randint(-170, -110)
    elif index == 1:
        x_pos = random.randint(-100, -40)
    elif index == 2:
        x_pos = random.randint(-30, 30)
    elif index == 3:
        x_pos = random.randint(40, 100)
    elif index == 4:
        x_pos = random.randint(110, 170)
    # x_pos = random.randint(-170, 170)
    unit.setx(x_pos)
    unit.sety(120)
    unit.showturtle()

#Robert
def check_hitboxes(enemy_unit, hit, list):
    unit_index = int()
    if enemy_unit.xcor() - 30 <= player.xcor() <= enemy_unit.xcor() + 25 and enemy_unit.ycor() - 25 <= player.ycor() <= enemy_unit.ycor() + 25:
        player.write('   OW!', align='left', font=('Arial', 15, 'bold') )
        hit = True
        unit_index = list.index(enemy_unit)
    return hit, unit_index 

#Robert
def reset_hitboxes(hp, enemy_index, list):
    hit = bool()
    hit = True
    enemy_unit = list[enemy_index]
    if enemy_unit.ycor() - 25 > player.ycor() or player.ycor() > enemy_unit.ycor() + 25:
        player.clear()
        hit = False
        hp -= 100
        health_hit(hp)
        LivesCounter(hp)
    return hit, hp

#Alex    
def health_meter(health):
    healthbar.seth(0)
    healthbar.speed(0)
    healthbar.penup()
    healthbar.setpos(-200, 190)
    healthbar.color('green')
    healthbar.pendown()
    healthbar.begin_fill()
    for x in range(2):
        healthbar.forward(health)
        healthbar.right(90)
        healthbar.forward(20)
        healthbar.right(90)
    healthbar.end_fill()

#Alex    
def health_hit(hp):
    health = 300
    lost_hp = int()
    lost_hp = health - hp
    healthbar.penup()
    healthbar.setpos(100,190)
    healthbar.begin_fill()
    healthbar.seth(180)
    healthbar.color('red')
    healthbar.forward(lost_hp)
    healthbar.left(90)
    healthbar.forward(20)
    healthbar.left(90)
    healthbar.forward(lost_hp)
    healthbar.left(90)
    healthbar.forward(20)
    healthbar.end_fill()

#Alex
def LivesCounter(hp):
    livecounter.clear()
    livecounter.color('green')
    if hp == 300:
        livecounter.write("Lives: 3", font=('Arial', 15, 'bold'))
    elif hp == 200:
        livecounter.write("Lives: 2", font=('Arial', 15, 'bold'))
    elif hp == 100:
        livecounter.write("Lives: 1", font=('Arial', 15, 'bold'))
    else:
        livecounter.write("Sorry, you lose!", font=('Arial', 15, 'bold'))

#Robert
def L():
    if player.xcor() > -170:
        player.setx(player.xcor()-10)
def R():
    if player.xcor() < 170:
        player.setx(player.xcor()+10)

player = turtle.Turtle()
player.shape('circle')
player.color('blue')
healthbar = turtle.Turtle('turtle')
healthbar.hideturtle()
livecounter = turtle.Turtle('turtle')
livecounter.hideturtle()
livecounter.penup()
livecounter.setpos(-200, 200)
livecounter.speed(0)

#Collaborative
def main():
    running = bool()
    collision = bool()
    health = int()
    move = float()
    move = float(10)
    try_again = str()
    running = True
    collision = False
    health = 300

    player.penup()
    player.speed(0)
    player.setpos(0,-160)

    enemy_1 = turtle.Turtle('arrow')
    enemy_2 = turtle.Turtle('arrow')
    enemy_3 = turtle.Turtle('arrow')
    enemy_4 = turtle.Turtle('arrow')
    enemy_5 = turtle.Turtle('arrow')
    enemies = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5]
    for enemy in enemies:
        setup_enemies(enemy, enemies.index(enemy))

    health_meter(health)
    LivesCounter(health)

    while running == True:
        if health == 0:
            running = False
            try_again = screen.textinput("You Lost!, Try again?", "Enter Y to continue or N to stop")
            try_again = try_again.capitalize()
            if try_again != "N":
                health = 300
                running = True
                health_meter(health)
                LivesCounter(health)
        for enemy in enemies:
            enemy.fd(move)
            move = move + .005
            collision, index = check_hitboxes(enemy, collision, enemies)
        if collision == True:
            collision, health = reset_hitboxes(health, index, enemies)
        for enemy in enemies:
            if enemy.ycor() < -220:
                reset_enemy(enemy,enemies.index(enemy))
                
        screen.listen()
        screen.onkey(L,'Left')
        screen.onkey(R,'Right')
    

main()