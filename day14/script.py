import numpy as np
import matplotlib.pyplot as plt

import os
import re

nb_epochs = 100
x_tiles = 101
y_tiles = 103

tot_quads =[0, 0, 0, 0]

with open('input.txt') as file:
    for line in file:
        robot_info = re.findall(r'(-*[0-9]+)', line)
        robot_x, robot_y = int(robot_info[0]), int(robot_info[1])
        robot_vx, robot_vy = int(robot_info[2]), int(robot_info[3])

        robot_final_x = (robot_x + nb_epochs * robot_vx) % x_tiles
        if robot_final_x < 0:
            robot_final_x = x_tiles - robot_final_x

        robot_final_y =  (robot_y + nb_epochs * robot_vy) % y_tiles
        if robot_final_y < 0:
            robot_final_y = y_tiles - robot_final_y

        if robot_final_x < x_tiles//2:
            if robot_final_y < y_tiles//2:
                tot_quads[0] +=1
            elif robot_final_y > y_tiles//2:
                tot_quads[1] += 1
        elif robot_final_x > x_tiles//2:
            if robot_final_y < y_tiles//2:
                tot_quads[2] +=1
            elif robot_final_y > y_tiles//2:
                tot_quads[3] += 1

print(np.prod(tot_quads))

### Part 2 ### 

image = np.zeros((y_tiles, x_tiles))
image_folder = "tree_images"
robots = []

with open('input.txt') as file:
    for line in file:
        robot_info = re.findall(r'(-*[0-9]+)', line)
        robot_x, robot_y = int(robot_info[0]), int(robot_info[1])
        robot_vx, robot_vy = int(robot_info[2]), int(robot_info[3])
        robots.append([robot_x, robot_y, robot_vx, robot_vy])

for k in range(6490,6495):
    for robot in robots:
        robot_x, robot_y, robot_vx, robot_vy = robot
        robot_final_x = (robot_x + k * robot_vx) % x_tiles
        if robot_final_x < 0:
            robot_final_x = x_tiles - robot_final_x

        robot_final_y =  (robot_y + k * robot_vy) % y_tiles
        if robot_final_y < 0:
            robot_final_y = y_tiles - robot_final_y
        
        image[robot_final_y][robot_final_x] += 1

    '''
    # Stop condition to figure which image is the tree. If no robots are on the same tile, we assume that it means the tree is formed. For me it was 6493. 
    stop = np.max(image) 
    if stop == 1:  
        print(k, stop)
    '''

    plt.imshow(image, cmap='gray', interpolation='nearest')
    plt.axis('off')

    image_name = "image_bw" + str(k) + ".png"
    image_path = os.path.join(image_folder, image_name)
    plt.savefig(image_path, bbox_inches='tight', pad_inches=0)

    image = np.zeros((y_tiles, x_tiles))



