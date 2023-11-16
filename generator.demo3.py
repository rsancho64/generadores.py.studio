#! /usr/bin/python3
#
#  Clases generadoras: implementan los métodos:
#       __iter__()  
#       __next__().
#
# see: https://realpython.com/python-iterators-iterables/ to initialize (reset?)

class generaCuadrados:
    

    def __init__(self, howmany):
        self.howmany = howmany
        self.data = [n * n for n in range(howmany)]
        self.nextindex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.nextindex < self.howmany:
            it = self.data[self.nextindex]
            self.nextindex +=1
            return it
        else:
            raise StopIteration

if __name__ == "__main__":

    gc = generaCuadrados(4)
    print(next(gc))
    print(next(gc))
    print(next(gc))
    print(next(gc))        

