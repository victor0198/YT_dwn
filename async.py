import multiprocessing as mp
import time

result_list = []

def foo_pool(x):
    print("Foo ", x)
    time.sleep(2)
    return x*x

def log_result(result):
    print("Log ", result)
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

def apply_async_with_callback():
    print("Apply")
    pool = mp.Pool(mp.cpu_count())
    for i in range(10):
        pool.apply_async(foo_pool, args = (i, ), callback = log_result)
    pool.close()
    pool.join()
    print(result_list)

if __name__ == '__main__':
    print("Main")
    apply_async_with_callback()