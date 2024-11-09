import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from box import point, Box, space, d1, d1D
import copy
import random
from timeit import default_timer as timer
from model import d2
from LanguageBoxGeneral import sampleC
from ss_tracker.ss_track import ss_track


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

S = space(10)
S.Boxes = [B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17]

ALL = space(10)
B0 = Box(10)
B0.Borders = [[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20],[-20,20]]
ALL.Boxes = [B0]

ptemp = point(10)
test = sampleC(ALL,1000)
results = []
for i in test:
    count = 0
    crd = 0
    if d1(i,S) >= 0:
        ptemp.coord = i.coord
        while True:
            track = ss_track(ptemp.coord)
            x_nl = track.trajectory()
            ptemp.coord = x_nl
            if d1(ptemp,S) >= 0:
                print("succesful tracking!",count)
                break
            else:
                print("failed tracking! projecting...",count)
                while d1D(ptemp,S)[0] < 0:
                    dist, crd = d1D(ptemp,S)
                    ptemp.coord[abs(crd)-1] -= abs(dist)*abs(crd)/crd
                count += 1
    results.append(count)

print("Average number of iterations:",sum(results)/len(results))
print("number of iterations:",results)