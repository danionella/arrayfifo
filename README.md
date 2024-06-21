[![Python Version](https://img.shields.io/pypi/pyversions/arrayfifo.svg)](https://pypi.org/project/arrayfifo)
[![PyPI version](https://badge.fury.io/py/arrayfifo.svg)](https://badge.fury.io/py/arrayfifo)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# ArrayFIFO

A FIFO buffer (queue) for efficient sharing of numpy arrays between multiple processes. Faster than multiprocessing.Queue because it uses shared memeory as a ring buffer, rather than pickling data and sending it over slow pipes.

Inspired by [ArrayQueues](https://github.com/portugueslab/arrayqueues). ArrayFIFO uses locks to support more than one producer and comsumer process, and it supports arrays whose shape and dtype can change arbitrarily with every `put` call.

## Usage example
```python
import numpy as np
from multiprocessing import Process
from arrayfifo import ArrayFIFO

def produce(queue):
    for i in range(20):
        random_shape = np.random.randint(5,10, size=3)
        array = np.random.randn(*random_shape)
        queue.put(array, meta=i)
        print(f'produced {type(array)} {array.shape} {array.dtype}; meta: {i}; hash: {hash(array.tobytes())}\n')

def consume(queue, pid):
    while True:
        array, meta = queue.get()
        print(f'consumer {pid} consumed {type(array)} {array.shape} {array.dtype}; meta: {meta}; hash: {hash(array.tobytes())}\n')

queue = ArrayFIFO(bytes=10e6)
producer = Process(target=produce, args=(queue,))
consumers = [Process(target=consume, args=(queue, pid)) for pid in range(3)]
for c in consumers:
    c.start()
producer.start()
```
