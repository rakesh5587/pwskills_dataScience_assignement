#!/usr/bin/env python
# coding: utf-8

# ##Question 1

# In[4]:


# Multiprocessing is a module in Python that enables you to run multiple processes concurrently on a single CPU or multiple CPUs. It allows you to divide a program into several tasks that can be executed simultaneously and independently of each other.
# reasons why multiprocessing is useful in Python:
#     Improved Performance
#     Increased Throughput
#     Simplified Code


# ##Question 2

# In[6]:


Both multiprocessing and multithreading are techniques used to achieve parallelism in computing, but they differ in the way they utilize CPU resources and handle memory.

CPU resources: In multiprocessing, each process runs on a separate CPU core, while in multithreading, multiple threads share the same CPU core.

Memory: Each process in multiprocessing has its own memory space, while threads share the same memory space in multithreading.

Overhead: Multiprocessing can have higher overhead due to the need for inter-process communication and synchronization, while multithreading has lower overhead due to the shared memory.

Scalability: Multiprocessing is more scalable since you can add more CPU cores to increase performance, while multithreading has limited scalability due to the constraints of a single CPU core.

Safety: Multiprocessing is safer since each process has its own memory space, while multithreading can lead to data race conditions and synchronization issues when multiple threads access the same memory location.


# ##Question 3

# In[10]:


import multiprocessing
def process_function():
    print("this is the child function")

if __name__ == "__main__":
    new_process = multiprocessing.Process(target=process_function)
    print("this is the main function")
    new_process.start()
    new_process.join()


# ##Question 4

# In[11]:


The multiprocessing module provides a Pool class that represents a pool of worker processes. The Pool class provides methods for creating worker processes, submitting tasks to the pool, and retrieving results from the pool.

Here are some reasons why you might want to use a Pool in Python:

Parallel processing: A Pool can be used to execute a function in parallel on multiple CPUs, which can significantly reduce the time required to perform the computation.

Load balancing: The Pool automatically distributes the workload across the available CPUs, which ensures that all CPUs are utilized efficiently.

Simplified code: The Pool provides a simple and easy-to-use interface for performing parallel processing in Python, which can simplify your code and make it easier to understand and maintain


# ##Question 5

# In[ ]:


import multiprocessing

def worker_function(data):
    result = data * 2
    return result

if __name__ == "__main__":
    pool = multiprocessing.Pool()
    results = pool.map(worker_function, [1, 2, 3, 4, 5])
    pool.close()
    pool.join()


# ##Question 6

# In[ ]:


import multiprocessing

def print_number(number):
    print(f"Process {number}: {number}")
if __name__ == "__main__":
    processes = []
    for i in range(1, 5):
        process = multiprocessing.Process(target=print_number, args=(i,))
        processes.append(process)
    for process in processes:
        process.start()
    for process in processes:
        process.join()

