[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# ArrayFIFO

A FIFO buffer (queue) for efficient sharing of numpy arrays between multiple processes. Faster than multiprocessing.Queue because it uses shared memeory as a ring buffer, rather than pickling data and sending it over slow pipes.

Inspired by the [ArrayQueues](https://github.com/portugueslab/arrayqueues). ArrayFIFO uses locks to support more than one producer and comsumer process, and it supports arrays whose shape and dtype can change arbitrarily with every `put` call.

## Usage example
```python
import multiprocessing as mp
import numpy as np
from arrayfifo import ArrayFIFO

class Producer(mp.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
    def run(self):
        for i in range(10):
            random_shape = np.random.randint(2,10, size=3)
            array = np.random.randn(*random_shape)
            self.queue.put(array, meta=i)
            print(f'produced {type(array)} {array.shape} {array.dtype}; meta: {i}\n')

class Consumer(mp.Process):
    def __init__(self, queue, p_num):
        super().__init__()
        self.queue = queue
        self.p_num = p_num
    def run(self):
        while True:
            array, meta = self.queue.get()
            print(f'{self.p_num}: consumed {type(array)} {array.shape} {array.dtype}; meta: {meta}\n')

que = ArrayFIFO(10e6)
producer = Producer(que)
consumers = [Consumer(que, p_num=i) for i in range(3)]
[c.start() for c in consumers]
producer.start()

```