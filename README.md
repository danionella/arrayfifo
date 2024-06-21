[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# ArrayFIFO

A FIFO buffer (queue) for efficient sharing of numpy arrays between multiple processes. Faster than multiprocessing.Queue because it uses shared memeory as a ring buffer, rather than pickling data and sending it over slow pipes.

Inspired by the [ArrayQueues](https://github.com/portugueslab/arrayqueues) project, with the difference that ArrayFIFO uses locks to support more than one producer and comsumer process, and that it supports arrays whose shape and dtype can change arbitrarily with every `put` call.

## Usage example
```python
from arrayfifo import ArrayFIFO

```