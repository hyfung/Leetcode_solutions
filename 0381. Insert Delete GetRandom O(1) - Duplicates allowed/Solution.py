class RandomizedCollection:
    import random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = dict()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.hashmap:
            self.hashmap[val] = 1
            return True
        else:
            self.hashmap[val] += 1
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.hashmap:
            return False
        else:
            if self.hashmap[val] == 1:
                del self.hashmap[val]
            else:
                self.hashmap[val] -= 1
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        ls = list()
        for k,v in self.hashmap.items():
            ls += [k] * v
        return random.choice(ls)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
