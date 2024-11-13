import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from box import point, Box, space, d1, d1D, project
import copy
import random
from timeit import default_timer as timer
from model import d2
from LanguageBoxGeneral import sampleC
from ss_tracker.ss_track import ss_track


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

phi5 = r"((always[0, 5] (x1 >= 0 and x1 <= 3)) and (always[6, 10] (x1 >= 50 and x1 <= 60)))"
B = Box(10)
B.Borders = [[0,3],[0,3],[0,3],[0,3],[0,3],[50,60],[50,60],[50,60],[50,60],[50,60]]
space5 = space(10)
space5.Boxes = [B]

space1 = phi1Set()
space2 = phi2Set()
space3 = phi3Set()
space4 = phi4Set()

spaces = [space1,space2,space3,space4,space5]
s = 0
def LCW(S):
    ptemp = point(10)
    pfail = point(10)
    test = sampleC(S,1000)
    results = []
    fail = 0
    print(s)
    min = 1000000
    countf = 0
    for i in test:
        count = 1
        ptemp.coord = i.coord
        while count < 40:
            track = ss_track(ptemp.coord)
            x_nl = track.trajectory()
            if x_nl == pfail.coord:
                fail += 1
                print("failed! for sure")
                countf += count
                break
            for i in range(len(x_nl)):
                ptemp.coord[i] = x_nl[i]
                pfail.coord[i] = x_nl[i]
            if d1D(ptemp,S)[0] >= 0:
                print("succesful tracking!",countf+count)
                results.append(countf+count)
                if count < min:
                    min = count
                countf = 0
                break
            else:
                ptemp.coord = project(ptemp,S).coord
                count += 1
        if count == 40:
            fail += 1
            print("failed!")
            countf += count
        # print(ptemp.coord)
    res = sum(results)/len(results)
    return fail,results,min,res


def LCP(S):
    print(len(S.Boxes))
    res = 100000
    for i in S.Boxes:
        print("#############################################################################BOX")
        SB = space(10)
        SB.addBoxes(i)
        ptemp = point(10)
        pfail = point(10)
        test = sampleC(SB,1000)
        results = []
        fail = 0
        print(s)
        min = 1000000
        countf = 0
        for i in test:
            count = 0
            ptemp.coord = i.coord
            while count < 40:
                track = ss_track(ptemp.coord)
                x_nl = track.trajectory()
                if x_nl == pfail.coord:
                    fail += 1
                    print("failed! for sure")
                    countf += count
                    break
                for i in range(len(x_nl)):
                    ptemp.coord[i] = x_nl[i]
                    pfail.coord[i] = x_nl[i]
                if d1D(ptemp,S)[0] >= 0:
                    print("succesful tracking!",countf+count)
                    results.append(countf+count)
                    if count < min:
                        min = count
                    countf = 0
                    break
                else:
                    ptemp.coord = project(ptemp,SB).coord
                    count += 1
            if count == 40:
                fail += 1
                print("failed!")
                countf += count
            # print(ptemp.coord)
        if len(results) > 0:
            print(sum(results)/len(results))
            if res > sum(results)/len(results): 
                res = sum(results)/len(results)
        else:
            res = countf
    return res

avrgResults = []
minA = []
s=6
while s < 5:
    fail,results,min = LCW(spaces[s])
    if len(results) > 0:
        avrgResults.append(sum(results)/len(results))
    else:
        avrgResults.append(0)
    minA.append(min)
    avrgResults.append(fail)
    avrgResults.append(len(results))
    print("Average number of iterations:",avrgResults[2*s])
    print("Number of failed tracking:",fail)
    print("min: ",min)
    s += 1


# print("Average number of iterations:",avrgResults)
# print("min: ",minA)
print(LCP(space4))
# fail,results,min,res = LCW(space4)
# print(res)
