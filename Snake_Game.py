'''Snake Game'''

import turtle
import time
import random

#Now we will set up the screen
root = turtle.Screen()            #Staring the turtle module
root.title("Apratim's Snake Game")#Putting up the title on the window
root.bgcolor('steel blue')        #Setting the background color
root.setup(width=600,height=600)  #Setting the width and height of screen
root.tracer(0)                  #0 turns off the animation on the screen,turns off
                                #the screen updates

#Now we will create the
#SNAKE HEAD
head = turtle.Turtle() #Actually creating the snake
#Now we will put on some properties
head.speed(0) #Animation speed of the turtle module,not the speed of the snake
              #0 is the fastest animation speed
head.shape('square') #Shape of the snake
head.color('red4')   #Color of the snake
head.penup()         #Turtle modules are usually used to draw lines. since we are
                     #not drawing anything, so we have used the penup attribute
a = random.randint(-290,290) #x-axis
b = random.randint(-290,250) #y-axis
head.goto(a,b)       #To start the head at the center of the screen

head.direction = 'stop' #When the head starts,its going to sit in the middle

#Now we will create the
#SNAKE FOOD
food = turtle.Turtle()
food.speed(0)
food.shape('triangle')
food.color('dark green')
food.penup()
food.goto(100,100)
#Functions to actually do the moving

def move_up():
    if(head.direction!='down'):
        head.direction = 'up'

def move_down():
    if(head.direction!='up'):
        head.direction = 'down'

def move_left():
    if(head.direction!='right'):
        head.direction = 'left'

def move_right():
    if(head.direction!='left'):
        head.direction = 'right'
    
#Create a function to move the snake
def move():
    if head.direction == 'up':
        y = head.ycor() #Setting the head to y co-ordinate
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor() #Setting the head to y co-ordinate
        head.sety(y-20)
        
    if head.direction == 'left':
        x = head.xcor() #Setting the head to x co-ordinate
        head.setx(x-20)

    if head.direction == 'right':
        x = head.xcor() #Setting the head to x co-ordinate
        head.setx(x+20)


#Now we will create some keyboard bindings,i.e,
#we will make the pressed keys respond to our program
root.listen()

root.onkeypress(move_up,'w')
root.onkeypress(move_up,'W')
root.onkeypress(move_up,'Up')

root.onkeypress(move_down,'s')
root.onkeypress(move_down,'S')
root.onkeypress(move_down,'Down')

root.onkeypress(move_left,'a')
root.onkeypress(move_left,'A')
root.onkeypress(move_left,'Left')

root.onkeypress(move_right,'d')
root.onkeypress(move_right,'D')
root.onkeypress(move_right,'Right')

#Declaring score, delay and list
delay = 0.2
extended_body = []
score = 0
high_score = 0

#Now let's create a sccoreboard
board = turtle.Turtle()
board.speed(0)
board.shape('square')
board.color('black')
board.penup()
board.hideturtle()
board.goto(0,250)
board.write('Score : 0  High Score : 0',align='center',font=('arial',20,'bold'))

#Creating main loop of the game
while True:
    root.update()      #Everytime the program runs through the loop, it updates the
                     #screen, which is why we are able to see the head
    #Whoa Whoa! We'll now check for a COLLISION with the BORDERS! Cheggit out!
    #This part is damn easy
    if(head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290):
        time.sleep(1)
        a = random.randint(-290,290)
        b = random.randint(-290,250)
        head.goto(a,b)
        head.direction = 'stop'

        #We have to hide the extended body parts when the game ends, otherwise 
        #they remain on the screen in the collision area.
        for i in extended_body:
            i.goto(400,400)

        #Now we will clear the extended body list
        extended_body.clear()

        #Reset the score board
        score = 0
        board.clear()
        board.write('Score : {}  High Score : {}'.format(score,high_score),
                    align='center',font=('arial',20,'bold'))


    #Now we will check for a collision with the food
    if(head.distance(food)<20): #distance is an in-built function in turtle module
                                #to measure the distance between two turtles
                                #I have taken it 20 because ech of the turtle
                                #shapes are by default 20 pixels wide by 20 pixels
                                #tall
    #If the above condition is satisfied, we are gonna move the food to a random
    #spot
        x = random.randint(-290,290)
        y = random.randint(-290,250)
        food.goto(x,y)
        
    #Add an extended body to the snake

        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape('square')
        new_body.color('white')
        new_body.penup()
        extended_body.append(new_body)

    #Increement the score board

        score += 10

        if(score>high_score):
            high_score = score

        board.clear()
        board.write('Score : {}  High Score : {}'.format(score,high_score),
                    align='center',font=('arial',20,'bold'))

    #Now, we will move the last part of the extended body first and continue doing
    #it till the first part, but in a reverse order
    for i in range(len(extended_body)-1,0,-1):
        x = extended_body[i-1].xcor()
        y = extended_body[i-1].ycor()
        extended_body[i].goto(x,y)

    #Now, we need to move the new_body[i] to the head,i.e., we need to merge this
    #position with the head

    if(len(extended_body)>0):
        x = head.xcor()
        y = head.ycor()
        extended_body[0].goto(x,y)
                
    move()

    #Now, we'll check for head collision with the extended body parts
    for i in extended_body:
        if(i.distance(head)<20):
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            #We have to hide the extended body parts when the game ends, otherwise 
            #they remain on the screen in the collision area.
            for i in extended_body:
                i.goto(400,400)

            #Now we will clear the extended body list
            extended_body.clear()

            #Reset the score board
            score = 0
            board.clear()
            board.write('Score : {}  High Score : {}'.format(score,high_score),
                    align='center',font=('arial',20,'bold'))


    time.sleep(delay)

root.mainloop()
