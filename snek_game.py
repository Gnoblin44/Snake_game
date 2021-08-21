# // THIS SNAKE GAME IS NOT WORKING ON LINUX. It could work on another OS but I am not sure
# original snek game

import curses
from curses import KEY_UP, KEY_LEFT, KEY_RIGHT, KEY_DOWN
from random import randint

# terminal setup
curses.initscr()                                                     # Initializes curses
stdscr = curses.newwin(20, 60, 0, 0)                                 # The coordinates are (y,x) instead of (x,y). Also creates the border of the terminal
stdscr.keypad(1)                                                     # The arrows will work
curses.noecho()                                                      # Echo characters will not work
curses.curs_set(0)                                                   # The cursor is off
stdscr.border(0)                                                     # The border :) (idk)
stdscr.nodelay(1)                                                    # .nodelay() waits for the user to enter a key...


# snek position n food

snake = [(4, 12), (4, 11), (4, 10)]
food = [10, 30]

stdscr.addch(food[0], food[1], '%')

# game code or game logic

ESC = 27
key = KEY_RIGHT

score = 0

while key != ESC:
    
    stdscr.addstr(0, 2, 'Score ' + str(score) + ' ') 
    stdscr.timeout(150 - (len(snake))//5 + len(snake)//10 % 120)     # increases speed as the snake increases in length
    
    prevKey = key
    event = stdscr.getch()                                           # .getch() refreshes the screen and then waits for the user to hit a key
    key = event if event != -1 else prevKey
    
    if key not in [KEY_LEFT, KEY_DOWN, KEY_RIGHT, KEY_UP, ESC]:      # If an invalid key is pressed...
        key = prevKey
        
    y = snake[0][0]                                                  # Grabs the first tuple and then gets the y coordinate (4)
    x = snake[0][1]                                                  # Grabs the same tuple and then gets the x coordinate (12)
    
    if key == KEY_UP:
        y -= 1
    if key == KEY_LEFT:
        x -= 1
    if key == KEY_RIGHT:
        x += 1
    if key == KEY_DOWN:
        y += 1
        
    snake.insert(0, (y, x))
    
    # The snek will go through the boundaries, and out to the other side
    if y == 0: y = 18
    if y == 19: y = 1
    if x == 0: x = 58
    if x == 59: x = 1
    
    # if the snek hits itself it will break the program
    if snake[0] in snake[1:]:
        print("You hit yourself...")
        break
    
    if snake[0] == food:
        """
        If the snek eats the food, the food will move to a random location within the boundaries
        """
        score += 1
        food = ()
        while food == ():
            food = (randint(1, 18), randint(1, 58))
            if food in snake:
                food = ()
        stdscr.addch(food[0], food[1], '%')
    else:
        last = snake.pop()
        stdscr.addch(last[0], last[1], ' ')
    stdscr.addch(snake[0][0], snake[0][1], '*')

curses.endwin()
print("\nYour final score: %s" % score)


    
