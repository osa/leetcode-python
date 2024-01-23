'''
https://leetcode.com/problems/lru-cache/
146. LRU Cache
Medium
Topics
Companies
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''
import unittest
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value = self.cache.pop(key)

        self.cache[key] = value

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value



class TestLruCache(unittest.TestCase):
    def setUp(self):
        self.capacity = 2
        self.sut = LRUCache(capacity = self.capacity)

    def tearDown(self):
        pass

    def test_get_on_empty_cache(self):
        # action
        actual = self.sut.get(1)

        # asserts
        self.assertEqual(actual, -1)
        self.assertEqual(list(self.sut.cache.keys()), [])

    def test_get_not_in_cache(self):
        # set up
        self.sut.put(2, 2)

        # action
        actual = self.sut.get(1)

        # asserts
        self.assertEqual(actual, -1)
        self.assertEqual(list(self.sut.cache.keys()), [2])

    def test_get(self):
        # set up
        self.sut.put(1, 2)

        # action
        actual = self.sut.get(1)

        # asserts
        self.assertEqual(actual, 2)
        self.assertEqual(list(self.sut.cache.keys()), [1])

    def test_put_at_capacity(self):
        # set up
        for i in range(self.capacity):
            self.sut.put(i, i)

        # action
        self.sut.put(self.capacity, self.capacity)
        actual = self.sut.get(0)

        # asserts
        self.assertEqual(actual, -1)
        self.assertEqual(list(self.sut.cache.keys()), [1, 2])

    def test_put_at_capacity_after_touch(self):
        # set up
        for i in range(self.capacity):
            self.sut.put(i, i)
        self.sut.get(0) # touch first element

        # action
        self.sut.put(self.capacity, self.capacity)
        actual = self.sut.get(0)

        # asserts
        self.assertEqual(actual, 0)
        self.assertEqual(list(self.sut.cache.keys()), [2, 0])

    def test_put(self):
        # set up
        self.sut.put(1, 10)

        # action
        actual = self.sut.get(1)

        # asserts
        self.assertEqual(actual, 10)

