import logging
import math
from typing import Any

import numpy as np
import plotly.graph_objects as go
import staliro

from staliro.core import best_eval, best_run
from staliro.models import State, ode
from staliro.optimizers import UniformRandom
from staliro.options import Options
from staliro.specifications import RTAMTDense
from staliro.staliro import simulate_model, staliro
from box import point

from typing import Callable, Generic, Iterable, Iterator, Sequence, Tuple, TypeVar, Union
import time

# THIS FILE CONTAINS THE REAL FORMULAS AND THE ORECAL FUNCTION

T = TypeVar("T")
def _time(func: Callable[[], T]) -> Tuple[float, T]:
    start_time = time.perf_counter()
    result = func()
    stop_time = time.perf_counter()
    duration = stop_time - start_time

    return duration, result

# THE FORMULAS

phi = r"(always[1,2] (eventually[3,4] (x1 >= 3 and x1 <= 10)) -> (x1 >= 0 and x1 <= 10)) and (always (x1 >= -20 and x1 <= 20))"
# phi = r"always !(a >= -1.6 and a <= -1.4  and b >= -1.1 and b <= -0.9)"
phi1 = r"(always[1,2] (eventually[3,4] (x1 >= 3 and x1 <= 10)) -> (x1 >= 0 and x1 <= 10)) and (always (x1 >= -20 and x1 <= 20))"
phi2 = r"(always[0,1] (eventually[7,8] (x1 >= 3 and x1 <= 10)) -> (always[0,1] (eventually[14,15] (x1 >= 0 and x1 <= 10)))) and (always (x1 >= -20 and x1 <= 20))"
phi100= r"(always[0,1] (eventually[30,31] (x1 >= 3 and x1 <= 10)) -> (always[0,1] (eventually[60,70] (x1 >= 0 and x1 <= 10)))) and (always (x1 >= -20 and x1 <= 20))"
phi50 = r"(always (x1 >= -20 and x1 <= 3) -> (eventually (x1 >= 3 and x1 <= 45))) and (always (x1 >= -50 and x1 <= 50))"
phi = r"(always[0,15] (x1 >=0 and x1<=2350)) and (always (x1 >= -2350 and x1 <= 2350))"
phi = r"(eventually(x1 >=-10 and x1<=10)) and (always (x1 >= -50 and x1 <= 50))"

phi = r"eventually[0,7] (x1 >= 5 and x1 <= 10) and eventually[5,15] (x1 >= 20 and x1 <= 25) and eventually[12,20] (x1 >= 50 and x1 <= 55) and always (x1 >= 0 and x1 <= 60)"

#### EXPERIMENTS FOR PAPER
phi1 = r"always(x1 >= 0 and x1 <= 10) and always not (x1 >= 3 and x1 <= 5) and always(x1 >= -20 and x1 <= 20)"
phi2 = r"eventually[0,7](x1 >= 3 and x1 <= 7) and always[7,10](x1 >=0 and x1 <= 3) and always(x1 >= -20 and x1 <= 20)"
phi3 = r"always (eventually[0, 10] (x1 = 2) and eventually[0, 10] (x1 = 8)) and always (-20 <= x1 <= 20)"
phi4 = r"eventually[0, 3] (x1 >= 0 and x1 <= 3) and eventually[3, 6] (x1 >= 3 and x1 <= 6) and eventually[6, 9] (x1 >= 6 and x1 <= 9) and always (-20 <= x1 <= 20)" 

# Choose the specification to use
phi = phi1
specification = RTAMTDense(phi, {"x1":0})

# THE ORECAL FUNCTION
def d2(p):
    # return ReqMonitor([p.coord])
    point_coord = [p.coord]
    point_time = []
    for i in range(0,p.dim):
        point_time.append(i)
    compute_cost = lambda: specification.evaluate(point_coord, point_time)
    cost_duration, cost = _time(compute_cost)
    return cost

def ReqMonitor(x1):
    sig = np.array(x1[0])
    phi_a = -1*np.min([3-sig,sig+20], 0)
    phi_b = []
    for j in range(len(sig)):
        phi_b.append(max(np.min([sig[j:]-3,45-sig[j:]], 0)))
    phi_b = np.array(phi_b)
    
    phi = np.min(np.max([phi_a, phi_b],0))

    # Change this back to -50,50 if you are not changing bounds
    const = min(min(150-sig), min(sig-(-50)))

    return min(phi, const)

if __name__ == "__main__":
    pass
    # logging.basicConfig(level=logging.DEBUG)
    # point_coord = [[5,3,5]]
    # point_time = [1,2,3]
    # compute_cost = lambda: specification.evaluate(point_coord, point_time)
    # cost_duration, cost = _time(compute_cost)
    # print(cost)
    # p = point(10)
    # p.coord = [9]*10
    # print(d2(p))



    # result = staliro(nonlinear_model, specification, optimizer, options)

    # best_run_ = best_run(result)
    # best_sample = best_eval(best_run_).sample
    # best_result = simulate_model(nonlinear_model, options, best_sample)

    # xEnd = best_result.trace.states[0][-1]
    # yEnd = best_result.trace.states[1][-1]

    # sample_xs = [evaluation.sample[0] for evaluation in best_run_.history]
    # sample_ys = [evaluation.sample[1] for evaluation in best_run_.history]

    # figure = go.Figure()
    # figure.add_trace(
    #     go.Scatter(
    #         name="Falsification area",
    #         x=[-1.6, -1.4, -1.4, -1.6],
    #         y=[-1.1, -1.1, -0.9, -0.9],
    #         fill="toself",
    #         fillcolor="red",
    #         line_color="red",
    #         mode="lines+markers",
    #     )
    # )
    # figure.add_trace(
    #     go.Scatter(
    #         name="Initial condition region",
    #         x=[-1, 1, 1, -1],
    #         y=[-1, -1, 1, 1],
    #         fill="toself",
    #         fillcolor="green",
    #         line_color="green",
    #         mode="lines+markers",
    #     )
    # )
    # figure.add_trace(
    #     go.Scatter(
    #         name="Samples",
    #         x=sample_xs,
    #         y=sample_ys,
    #         mode="markers",
    #         marker=go.scatter.Marker(color="lightblue", symbol="circle"),
    #     )
    # )
    # figure.add_trace(
    #     go.Scatter(
    #         name="Best evaluation trajectory",
    #         x=best_result.trace.states[0],
    #         y=best_result.trace.states[1],
    #         mode="lines+markers",
    #         line=go.scatter.Line(color="blue", shape="spline"),
    #     )
    # )
    # figure.write_image("nonlinear.jpeg")
