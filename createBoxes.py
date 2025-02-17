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
import itertools
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import box
from box import point, Box, space, d1,d1D,actd1
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


phi1 = r"(always(x1 >= 0 and x1 <= 10) and always not (x1 >= 3 and x1 <= 5)) and (always(x1 >= 0 and x1 <= 10))"
phi2 = r"((eventually[0,7](x1 >= 0 and x1 <= 3)) and (always[8,10](x1 >=0 and x1 <= 3))) and (always(x1 >= 0 and x1 <= 10))"
phi3 = r"((eventually[0, 10] (x1 >= 0 and x1 <= 3)) and (eventually[0, 10] (x1 >= 7 and x1 <= 10))) and (always(x1 >= 0 and x1 <= 10))"
phi4 = r"((eventually[0, 3] (x1 >= 0 and x1 <= 2)) and (eventually[3, 6] (x1 >= 4 and x1 <= 6)) and (eventually[6, 9] (x1 >= 15 and x1 <= 17))) and (always(x1 >= 0 and x1 <= 20))"



phi1 = r"(always(x1 >= 0 and x1 <= 10) and always not (x1 >= 3 and x1 <= 5)) and (always(x1 >= 0 and x1 <= 10))"
def phi1Set():
    space1 = space(10)
    Bo = Box(10)
    Bo.Borders = [[5,10],[5,10],[5,10],[5,10],[5,10],[5,10],[5,10],[5,10],[5,10],[5,10]]
    B = copy.deepcopy(Bo)
    done = False
    while done == False:
        i = 0
        while True:
            if B.Borders[i] == [5,10]:
                B.Borders[i] = [0,3]
                break
            else:
                B.Borders[i] = [5,10]
                i += 1
            if i == 10:
                done = True
                break
        space1.addBoxes(B)
        B = copy.deepcopy(B)
    return space1


phi2 = r"((eventually[0,7](x1 >= 0 and x1 <= 3)) and (always[8,10](x1 >=0 and x1 <= 3))) and (always(x1 >= 0 and x1 <= 10))"
def phi2Set():
    space1 = space(10)
    Bo = Box(10)
    Bo.Borders = [[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,3],[0,3]]
    for j in range(8):
        B = copy.deepcopy(Bo)
        B.Borders[j] = [0,3]
        space1.addBoxes(B)
    return space1

phi3 = r"((eventually[0, 10] (x1 >= 0 and x1 <= 3)) and (eventually[0, 10] (x1 >= 7 and x1 <= 10))) and (always(x1 >= 0 and x1 <= 10))"

def phi3Set():
    space1 = space(10)
    for i in range(10):
        Bo = Box(10)
        Bo.Borders = [[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,10]]
        Bo.Borders[i] = [0,3]
        for j in range(10):
            B = copy.deepcopy(Bo)
            if i == j:
                continue
            else:
                B.Borders[j] = [7,10]
            space1.addBoxes(B)
    return space1


phi4 = r"((eventually[0, 3] (x1 >= 0 and x1 <= 2)) and (eventually[3, 6] (x1 >= 4 and x1 <= 6)) and (eventually[6, 9] (x1 >= 15 and x1 <= 17))) and (always(x1 >= 0 and x1 <= 20))"
def phi4Set():
    space1 = space(10)
    for i in range(3):
        Bo = Box(10)
        Bo.Borders = [[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,10],[0,10]]
        Bo.Borders[i] = [0,2]
        for j in range(3,6):
            B = copy.deepcopy(Bo)
            B.Borders[j] = [4,6]
            for k in range(6,10):
                B1 = copy.deepcopy(B)
                B1.Borders[k] = [15,17]
                space1.addBoxes(B1)
    return space1

space1 = phi1Set()
space2 = phi2Set()
space3 = phi3Set()
space4 = phi4Set()



### TANMAY formulas
const = r"(always(y54 >= -30 and y54 <= 200))"
CC1 = r"(not(always[0, 100](y54 <= 40)))"


def repeatBox(B,a,b):
    for i in range(B.dim):
        B.Borders[i] = [a,b]
    return B

def CC1Set():
    space1 = space(100)
    Bo = Box(100)
    Bo = repeatBox(Bo,-30,200)
    B = copy.deepcopy(Bo)
    for i in range(100):
        B.Borders[i] = [-30,40]
        space1.addBoxes(B)
        B = copy.deepcopy(Bo)
    return space1

CC2 = r"(not(always[0, 70](eventually[0, 30](y54 >= 10))))"
CC2 = r"((eventually[0, 70](always[0, 30](y54 <= 10))))"

def CC2Set():
    space1 = space(100)
    Bo = Box(100)
    Bo = repeatBox(Bo,-30,200)
    B = copy.deepcopy(Bo)
    for i in range(70):
        for j in range(31):
            B.Borders[i+j] = [-30,10]
        space1.addBoxes(B)
        B = copy.deepcopy(Bo)
    return space1

CC3 = r"(not(always[0, 80]((always[0, 20](y54 <= 32)) or (eventually[0, 20](y54 >= 33)))))"
CC3 = r"((eventually[0, 80]((eventually[0, 20](y54 >= 32)) and (always[0, 20](y54 <= 33)))))"

def CC3Set():
    space1 = space(100)
    Bo = Box(100)
    Bo = repeatBox(Bo,-30,200)
    B = copy.deepcopy(Bo)
    for i in range(80):
        for j in range(20):
            B.Borders[i+j] = [-30,33]
        for k in range(20):
            B1 = copy.deepcopy(B)
            B1.Borders[i+k] = [32,33]
            space1.addBoxes(B1)
        B = copy.deepcopy(Bo)
    return space1

CC4 = r"(not(always[0, 79]((always[0, 19](y54 <= 30)) or (eventually[0, 19](y54 >= 35)))))"

def CC4Set():
    space1 = space(100)
    Bo = Box(100)
    Bo = repeatBox(Bo,-30,200)
    B = copy.deepcopy(Bo)
    for i in range(80):
        for j in range(20):
            B.Borders[i+j] = [-30,35]
        for k in range(20):
            B1 = copy.deepcopy(B)
            B1.Borders[i+k] = [30,35]
            space1.addBoxes(B1)
        B = copy.deepcopy(Bo)
    return space1

CC5 = r"(not(always[0, 64](eventually[0, 30](always[0, 4](y54 >= 10)))))"
CC5 = r"((eventually[0, 64](always[0, 30](eventually[0, 4](y54 <= 10)))))"

CC5 = r"(not(always[0, 20](eventually[0, 30](always[0, 4](y54 >= 10)))))"

def CC5Set():
    space1 = space(100)
    Bo = Box(100)
    Bo = repeatBox(Bo,-30,200)
    B = copy.deepcopy(Bo)
    for i in range(1):
        print(i)
        space1.Boxes += reqCC5(B,0,i).Boxes
    print(len(space1.Boxes))
    # count = 0
    # for b in space1.Boxes:
    #     print(count)
    #     count += 1
    #     Bt = copy.deepcopy(b)
    #     for i in range(65):
    #         Bt.Borders.pop()
    #         Bt.Borders.insert(0,[-30,200])
    #         space1.addBoxes(Bt)
    #         Bt = copy.deepcopy(Bt)

    return space1

def reqCC5(B,i,o,a=5):
    # print(i)
    B1 = Box(100)
    B2 = Box(100)
    B3 = Box(100)
    B4 = Box(100)
    B5 = Box(100)
    s1 = space(100)
    s2 = space(100)
    s3 = space(100)
    s4 = space(100)
    s5 = space(100)
    for j in range(100):
        B1.Borders[j] = B.Borders[j]
        B2.Borders[j] = B.Borders[j]
        B3.Borders[j] = B.Borders[j]
        B4.Borders[j] = B.Borders[j]
        B5.Borders[j] = B.Borders[j]
    B1.Borders[o+i] = [-30,10]
    B2.Borders[o+i+1] = [-30,10]
    B3.Borders[o+i+2] = [-30,10]
    B4.Borders[o+i+3] = [-30,10]
    B5.Borders[o+i+4] = [-30,10]
    if i + 1 < 30:
        if a < 2:
            s1 = reqCC5(B1,i+1,o,5)
        if a < 3:
            s2 = reqCC5(B2,i+2,o,4)
        if a < 4:
            s3 = reqCC5(B3,i+3,o,3)
        if a < 5:
            s4 = reqCC5(B4,i+4,o,2)
        s5 = reqCC5(B5,i+5,o,1)
        sT = space(100)
        sT.Boxes = s1.Boxes + s2.Boxes + s3.Boxes + s4.Boxes + s5.Boxes
        return sT
    else:
        sT = space(100)
        sT.Boxes = [B1,B2,B3,B4,B5]
        return sT

CC1space = CC1Set()
# CC2space = CC2Set()
# CC3space = CC3Set()
# CC4space = CC4Set()
# CC5space = CC5Set()

def plot_space(space, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(title)
    space.plot3D(ax, 1,0,230,3)
    plt.show()


for i in CC1space.Boxes:
    print(i.Borders)

plot_space(CC1space, "CC1 Space")

# plot_space(space2, "Space 2")
# plot_space(space3, "Space 3")
# plot_space(space4, "Space 4")
# plot_space(CC1space, "CC1 Space")
# plot_space(CC2space, "CC2 Space")
# plot_space(CC3space, "CC3 Space")
# plot_space(CC4space, "CC4 Space")
# plot_space(CC5space, "CC5 Space")



# for i in space5.Boxes[34400*19:]:
#     print(i.Borders)

# p = point(100)
# p.coord = [0]*100

# S = space5
# B = Box(100)
# B = repeatBox(B,-30,10)

# U = space(100)
# U.Boxes = [B]
# Sam = sample(U,1000)
# Sam[0] = p
# over = 0
# under = 0
# accurate = 0
# for i in Sam:
#     print(i.coord)
#     D2 = d2(i)
#     print(D2)
#     D1 = d1D(i,S)[0]
#     print(D1)
#     # if d2(i) > 0:
#     #     print(i.coord)
#     #     print(d2(i))
#     #     print(d1D(i,S))

#     if (D2 <0 and D1 > 0):
#         over += 1
#     if (D2 >0 and D1 < 0):
#         under += 1
#     if (d2(i) == d1D(i,S)[0]):
#         accurate += 1
#     elif d2(i) > 0:
#         print(i.coord)
#         print(d2(i))
#         print(d1(i,S))
#         print(d1D(i,S))
#         print(" ")

# print(accurate/10000 *100)
# print(over/10000 *100)
# print(under/10000 *100)



# phi5 = r"((always[0,2](x1 >= 0 and x1 <=5)) and (eventually[3, 26] (x1 >= 80 and x1 <= 90)) and (eventually[27, 49] (x1 >= 10 and x1 <= 15))) and ((always(x1 >= 0 and x1 <= 100) and (not(eventually[0,9](x1 >=30 and x1 <= 60)) and (not(eventually[40,49](x1 >=30 and x1 <= 60))))))"

# def phi5Set():
#     space1 = space(100)
#     Bo = Box(100)
#     Bo.Borders = repeatBox(Bo,0,100)
#     Bo.Borders[0] = [0,5]
#     Bo.Borders[1] = [0,5]
#     for i in range(10):
#         Bo.Borders[i] = [0,30]
#         Bo.Borders[i+40] = [0,30]
#     B = copy.deepcopy(Bo)
#     space1.addBoxes(B)
#     for i in range(2,27):
#         B.Borders[i] = [80,90]
    


