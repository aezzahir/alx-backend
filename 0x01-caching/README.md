# ALX Backend Project: Caching Algorithms

## Introduction
This project is part of the ALX Backend specialization curriculum focusing on caching algorithms. Throughout this project, you will delve into different caching methodologies and their implementations.

## Short Specializations
- **0x01. Caching**
  - **Back-end**
  - **Weight:** 1
  - **Project Duration:** May 7, 2024, 4:00 AM - May 9, 2024, 4:00 AM
  - **Checker Release:** May 7, 2024, 4:00 PM
  - **Auto Review:** A review will be launched automatically at the deadline.

## Background Context
This project aims to provide an understanding of various caching algorithms, including FIFO, LIFO, LRU, MRU, and LFU.

## Resources
To successfully complete this project, you should read or watch the following resources:
- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First-in-first-out_(FIFO))
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last-in-first-out_(LIFO))
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU))
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_recently_used_(MRU))
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-frequently_used_(LFU))

## Learning Objectives
By the end of this project, you are expected to:
- Explain what a caching system is
- Understand FIFO, LIFO, LRU, MRU, and LFU caching policies
- Recognize the purpose and limitations of caching systems

## Requirements
### Python Scripts
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the project folder, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All files must be executable
- The length of your files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation should be a real sentence explaining the purpose of the module, class, or method

### More Info
#### Parent class BaseCaching
All classes must inherit from BaseCaching defined below:

```python
#!/usr/bin/python3

class BaseCaching():
    """ BaseCaching module """

    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key """
        raise NotImplementedError("get must be implemented in your cache class")
