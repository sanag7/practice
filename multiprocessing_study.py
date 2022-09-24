from concurrent.futures import process
import multiprocessing as mp
import os
import time


def work_func(x):
    print(f"value {x} is in PID: {os.getpid()}")
    time.sleep(1)
    return x**5

# def main():
#     start = int(time.time())
#     print(list(map(work_func,range(0,12))))
#     print("***rin time(sec) : ", int(time.time())-start)

start_time = time.time()


def count(name):
    for i in range(1,50001):
        print(name,":",i)

num_list = ['p1','p2','p3','p4']
# for num in num_list:
#     count(num)

# print(f'---- {(time.time()-start_time)} ----')


if __name__ == '__main__':
    pool = mp.Pool(processes = 4)
    pool.map(count, num_list)
    pool.close()
    pool.join()

# def main():
#     start = int(time.time())
#     num_cores = 2
#     pool = mp.Pool(num_cores)
#     print(pool.map(work_func, range(1,13)))
#     print("***run time(sec) :", int(time.time()) - start)

# if __name__ == '__main__':

#     # p = mp.Pool(processes=2)

#     # result = p.map(multipro, [(1,2),(3,4)])
#     # print(result)

#     main()