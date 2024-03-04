import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import box
from box import point, Box, space, d1
import copy
import random
from timeit import default_timer as timer
from model import d2

def sample(U,N):
    n = U.dim
    result = []
    Area = []
    total = 0
    for boxes in U.Boxes:
        a = 1
        for i in range(0,n):
            a *= boxes.Borders[i][1] - boxes.Borders[i][0]
        Area.append(a)
        total += a

    for boxes in U.Boxes:
        nbPoints = int(N*Area[U.Boxes.index(boxes)]/total + 1)
        for i in range(0,nbPoints):
            bre = 0
            p = point(n)
            for j in range(0,n):
                if int(boxes.Borders[j][0]+1) >= int(boxes.Borders[j][1])-1:
                    p.coord[j] = boxes.Borders[j][0] + 0.5
                else:
                    p.coord[j] = random.randint(boxes.Borders[j][0]+1,boxes.Borders[j][1]-1)
            if bre == 0:
                result.append(p)
    return result

B1 = Box(10)
B2 = Box(10)
B3 = Box(10)
B4 = Box(10)
B5 = Box(10)
B6 = Box(10)
B7 = Box(10)
B8 = Box(10)
B9 = Box(10)
B10 = Box(10)
B11 = Box(10)
B12 = Box(10)
B13 = Box(10)
B14 = Box(10)
B15 = Box(10)
B16 = Box(10)
B17 = Box(10)
B18 = Box(10)
B19 = Box(10)
B20 = Box(10)

B1.Borders = [[-20,20],[-20,20],[-20,20],[-20,20],[-20,3],[10,20],[10,20],[-20,20],[-20,20],[-20,20]]
B2.Borders = [[-20,20],[-20,20],[-20,20],[-20,20],[-20,3],[-20,3],[10,20],[-20,20],[-20,20],[-20,20]]
B3.Borders = [[-20,20],[-20,20],[-20,20],[-20,20],[10,20],[-20,3],[-20,3],[-20,20],[-20,20],[-20,20]]
B4.Borders = [[-20,20],[-20,20],[-20,20],[-20,20],[-20,3],[-20,3],[-20,3],[-20,20],[-20,20],[-20,20]]
B5.Borders = [[-20,20],[-20,20],[0,10],[-20,20],[-20,3],[10,20],[-20,20],[-20,20],[-20,20],[-20,20]]
B6.Borders = [[-20,20],[-20,20],[-20,20],[-20,20],[10,20],[10,20],[-20,3],[-20,20],[-20,20],[-20,20]]
B7.Borders = [[-20,20],[0,10],[-20,20],[-20,20],[-20,20],[10,20],[-20,3],[-20,20],[-20,20],[-20,20]]
B8.Borders = [[-20,20],[-20,20],[0,10],[-20,20],[-20,3],[-20,3],[-20,20],[-20,20],[-20,20],[-20,20]]
B9.Borders = [[-20,20],[-20,20],[-20,20],[-20,20],[-20,3],[10,20],[-20,3],[-20,20],[-20,20],[-20,20]]
B10.Borders = [[-20,20],[-20,20],[-20,20],[-20,20],[10,20],[-20,3],[10,20],[-20,20],[-20,20],[-20,20]]
B11.Borders = [[-20,20],[-20,20],[-20,20],[-20,20],[10,20],[10,20],[10,20],[-20,20],[-20,20],[-20,20]]
B12.Borders = [[-20,20],[0,10],[-20,20],[-20,20],[-20,20],[-20,3],[10,20],[-20,20],[-20,20],[-20,20]]
B13.Borders = [[-20,20],[-20,20],[0,10],[-20,20],[10,20],[-20,3],[-20,20],[-20,20],[-20,20],[-20,20]]
B14.Borders = [[-20,20],[0,10],[-20,20],[-20,20],[-20,20],[-20,3],[-20,3],[-20,20],[-20,20],[-20,20]]
B15.Borders = [[-20,20],[-20,20],[0,10],[-20,20],[10,20],[10,20],[-20,20],[-20,20],[-20,20],[-20,20]]
B16.Borders = [[-20,20],[0,10],[-20,20],[-20,20],[-20,20],[10,20],[10,20],[-20,20],[-20,20],[-20,20]]
B17.Borders = [[-20,20],[0,10],[0,10],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20]]

# B1.Borders =[[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[10.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B2.Borders =[[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B3.Borders =[[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B4.Borders =[[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B5.Borders =[[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B6.Borders =[[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,3.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B7.Borders =[[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,3.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B8.Borders =[[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[10.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B9.Borders =[[-20.0,20.0],[0.0,10.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B10.Borders =[[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[10.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B11.Borders =[[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B12.Borders =[[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[10.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B13.Borders =[[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[10.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B14.Borders =[[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B15.Borders =[[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[10.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B16.Borders =[[-20.0,20.0],[0.0,10.0],[0.0,10.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]

# B1.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,3.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B2.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[10.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# B3.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B4.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B5.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,10.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B6.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B7.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B8.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# B9.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# B10.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B11.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[10.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B12.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# B13.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[10.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B14.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# B15.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# B16.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]

# IB1 = Box(20)
# IB2 = Box(20)
# IB3 = Box(20)
# IB4 = Box(20)
# IB5 = Box(20)
# IB6 = Box(20)
# IB7 = Box(20)
# IB8 = Box(20)
# IB9 = Box(20)
# IB10 = Box(20)
# IB11 = Box(20)
# IB12 = Box(20)
# IB13 = Box(20)
# IB14 = Box(20)
# IB15 = Box(20)
# IB16 = Box(20)
# IB17 = Box(20)
# IB18 = Box(20)
# IB19 = Box(20)
# IB20 = Box(20)

# IB1.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB2.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,3.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB3.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB4.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB5.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB6.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB7.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB8.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# IB9.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB10.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# IB11.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# IB12.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,3.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB13.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[10.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB14.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# IB15.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[10.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB16.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB17.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# IB18.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]
# IB19.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[10.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0]]
# IB20.Borders = [[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,3.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0],[0.0,10.0],[0.0,10.0],[-20.0,20.0],[-20.0,20.0],[-20.0,20.0]]

S = space(10)
S.Boxes = [B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17]

# S1 = space(20)
# S1.Boxes = [IB1,IB2,IB3,IB4,IB5,IB6,IB7,IB8,IB9,IB10,IB11,IB12,IB13,IB14,IB15,IB16,IB17,IB18,IB19,IB20]

B = Box(10)
B.Borders = [[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20]]

U = space(10)
U.Boxes = [B]
Sam = sample(U,10000)

over = 0
under = 0
for i in Sam:
    if (d2(i) <0 and d1(i,S) > 0):
        over += 1
    if (d2(i) >0 and d1(i,S) < 0):
        under += 1

print(over/10000 *100)
print(under/10000 *100)

# over = 0
# under = 0
# for i in Sam:
#     if (d2(i) <0 and d1(i,S1) > 0):
#         over += 1
#     if (d2(i) >0 and d1(i,S1) < 0):
#         under += 1

# print(over/1000 *100)
# print(under/1000 *100)




