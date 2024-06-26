![Python Version](https://img.shields.io/badge/python-3.7+-blue)
[![PyPI - Version](https://img.shields.io/pypi/v/arrayfifo)](https://pypi.org/project/arrayfifo/)
[![Conda Version](https://img.shields.io/conda/v/danionella/arrayfifo)](https://anaconda.org/danionella/arrayfifo)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub last commit](https://img.shields.io/github/last-commit/danionella/arrayfifo)

# ArrayFIFO

A FIFO buffer (queue) for efficient sharing of numpy arrays between multiple processes. Faster than multiprocessing.Queue because it uses shared memeory as a ring buffer, rather than pickling data and sending it over slow pipes.

Inspired by [ArrayQueues](https://github.com/portugueslab/arrayqueues). ArrayFIFO uses locks to support more than one producer and comsumer process, and it supports arrays whose shape and dtype can change arbitrarily between queue items.

As with other queues in Python, data is transmitted via `put` and `get` calls. `.put(array, meta=None)` accepts a second parameter for optional metadata, which can be any Python object, including tuple and dict. It will be serialized and sent through a conventional Queue, so try to keep this small for best performance.

Auto-generated API documentation: https://danionella.github.io/arrayfifo

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
