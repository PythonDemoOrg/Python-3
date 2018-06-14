# -*- coding: UTF-8 -*-

# Filename : hash_map.py
# author by : WeiQi

class LinearMap(object):
    def __init__(self):
        self.items = []

    def add(self, k, v):
        self.items.append((k, v))

    def get(self, k):
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError

class BetterMap(object):
    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)

class HashMap(object):
    def __init__(self):
        self.maps = BetterMap(2)
        self.num = 0

    def get(self, k):
        return self.maps.get(k)

    def add(self, k, v):
        if self.num == len(self.maps.maps):
            self.resize()

        self.maps.add(k, v)
        self.num += 1
        print(self.maps.maps)

    def resize(self):
        new_map = BetterMap(self.num * 2)
        for m in self.maps.maps:
            for k, v in m.items:
                new_map.add(k, v)

        self.maps = new_map
        print('resize -> %d'%len(self.maps.maps))

def main():
    import string
    m=HashMap()
    s='0e306561559aa787d00bc6f70bbdfe3404cf03659e704f8534c00ffb659c4c8740cc942feb2da115a3f4155cbb8607497386656d7d1f34a42059d78f5a8dd1ef'
    #s=string.ascii_letters
    #s=string.ascii_lowercase
    print(s)
    for k, v in enumerate(s):
        m.add(k, v)

    for k in range(len(s)):
        print k, m.get(k)

if __name__ == '__main__':
    main()