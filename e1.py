distance= lambda p1,p2 : (p2[0]-p1[0])**2

def main():
    p1=(5,10)
    p2=(3,-2)
    d= distance(p1,p2)

    print(d)

main()