from __future__ import division
from __future__ import print_function

import time

import numpy as np


def numpy_vec(scale, X, Y, result):
    result = (scale * X) + Y

    return


def numpy_loop(N, scale, X, Y, result):
    for i in range(N):
        result[i] = (scale * X[i]) + Y[i]

    return


def main():

    N = 2 * 1000 * 1000
    num_run_times = 5

    # penalty for using a double (np.float64)?
    scale = 2.0

    arrayX = np.empty(shape=(N), dtype=np.float32)
    arrayY = np.empty(shape=(N), dtype=np.float32)
    result = np.empty(shape=(N), dtype=np.float32)

    print('Number of repeats: {}'.format(num_run_times))

    # initialize array values
    # ...do it the naive way for now
    for i in range(N):
        arrayX[i] = i
        arrayY[i] = i
        result[i] = 0.0

    list_X = [i for i in range(N)]
    list_Y = [i for i in range(N)]
    list_r = [0.0 for i in range(N)]

    min_numpy_vec = 1.0e30
    for i in range(num_run_times):
        start_time = time.time()
        numpy_vec(scale, arrayX, arrayY, result)
        end_time = time.time()
        min_numpy_vec = min(min_numpy_vec, end_time - start_time)

    print('[numpy vec]:\t\t{}'.format(min_numpy_vec))

    # clear out the buffer
    result[:] = 0.0

    min_numpy_loop = 1.0e30
    for i in range(num_run_times):
        start_time = time.time()
        numpy_loop(N, scale, arrayX, arrayY, result)
        end_time = time.time()
        min_numpy_loop = min(min_numpy_loop, end_time - start_time)

    print('[numpy loop]:\t\t{}'.format(min_numpy_loop))

    # clear out the buffer
    result[:] = 0.0

    min_list_loop = 1.0e30
    for i in range(num_run_times):
        start_time = time.time()
        numpy_loop(N, scale, list_X, list_Y, list_r)
        end_time = time.time()
        min_list_loop = min(min_list_loop, end_time - start_time)

    print('[list loop]:\t\t{}'.format(min_list_loop))

    print('[numpy loop]/[numpy vec]:\t\t{}'.format(min_numpy_loop / min_numpy_vec))
    print('[numpy loop]/[list loop]:\t\t{}'.format(min_numpy_loop / min_list_loop))
    print('[list loop]/[numpy vec]:\t\t{}'.format(min_list_loop / min_numpy_vec))

    return

if __name__ == '__main__':
    main()
