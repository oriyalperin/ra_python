import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

cp_time = []
np_time = []


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        if orig_func.__name__ == "solved_by_np":
            np_time.append(t2)
        else:
            cp_time.append(t2)
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result

    return wrapper


def eq_generator(sizes: list):
    for size in sizes:
        left = np.random.randint(1, 30, size=(size, size))
        right = np.random.randint(1, 30, size=size)
        print(left, right)
        sol_np = solved_by_np(left, right)
        print(f"numpy solution: {sol_np}")
        x = cp.Variable(shape=(size, 1), name="x")
        B = np.array([[item] for item in right])
        constraints = [cp.matmul(left, x) == B]
        objective = cp.Minimize(cp.sum(x, axis=0))
        solved_by_cp(constraints, objective)
        print(f"cvxpy solution: {x.value}")

@my_timer
def solved_by_np(left, right):
    solution = np.linalg.solve(left, right)
    return solution


@my_timer
def solved_by_cp(constraints, objective):
    problem = cp.Problem(objective, constraints)
    solution = problem.solve()
    return solution


sizes = [2, 3, 5, 7, 10]
eq_generator(sizes)
[cp_plt] = plt.plot(sizes, cp_time)
[np_plt] = plt.plot(sizes, np_time)
plt.legend([cp_plt,np_plt], ["cvxpy","numpy"], loc=1)
plt.show()
