class Tool(object):

    def add(a, b):
        return a + b
        
    @staticmethod
    def dec(c, d):
        return c - d

r = Tool().dec(3, 1)
print(r)