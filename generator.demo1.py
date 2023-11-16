#! /usr/bin/python3

def devuelve_ciudades(*ciudades):
    for c in ciudades:
        yield c

cc = devuelve_ciudades("madrid","barcelona","zaragoza")

print(type(cc))

for c in cc:
    print(c)

