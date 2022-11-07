






from colorama import init, Fore
import random




# Kode # alg labyrint

# definer variabler til lab
cell = "c"
wall = "w"

# Definer lab

def init_maze(width, height):
    maze = []
    for i in range(0,height):
        line = []
        for j in range(0, width):
            line.append('u')
        maze.append(line)
    return maze


# print og skap lab

# størrelse
height=11
width=27

def print_maze(maze):
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if maze [i][j] == 'u':
                print(Fore.WHITE,f'{maze[i][j]}')
            elif maze[i][j] == 'c':
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            else:
                print(Fore.RED, f'{maze[i][j]}', end="")
        print('\n')


print(maze)

#starting points
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)

# kan ikke starte på enden av lab

if starting_height == 0:
    starting_height += 1
if starting_height == height-1:
    starting_height -= 1
if starting_width == 0:
    starting_width += 1
if starting_width == width-1:
    starting_width -= 1


maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height-1, starting_width])
walls.append([starting_height, starting_width-1])
walls.append([starting_height, starting_width+1])
walls.append([starting_height+1, starting_width])


maze[starting_height-1][starting_width] = wall
maze[starting_height][starting_width-1] = wall
maze[starting_height][starting_width+1] = wall
maze[starting_height+1][starting_width] = wall



# vanskelig delen av algoritmen


while walls:
    rand_walls:



