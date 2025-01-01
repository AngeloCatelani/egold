def __init__(self):
        self.numList =[]
        self.hashmap = {}
        

def insert(self, val: int) -> bool:
        res =  val not in self.hashmap
        if res:
            self.hashmap[val] = len(self.numList)
            self.numList.append(val)
        return res
        

def remove(self, val: int) -> bool:
        res = val in self.hashmap
        if res:
            idx = self.hashmap[val]
            lastVal =self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()

            self.hashmap[lastVal] = idx
            del self.hashmap[val]
        return res
        

def getRandom(self) -> int:
        return random.choice(self.numList)