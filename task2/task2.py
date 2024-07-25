def check_circle(x, y, r, x0, y0):
    if (x - x0)**2 + (y - y0)**2 < r**2:
        return 1
    if (x - x0)**2 + (y - y0)**2 == r**2:
        return 0
    return 2


def main():
    a = input()
    f1 = open(a, 'r')
    x0, y0 = map(float, f1.readline().split())
    r = int(f1.readline(1))
    f1.close()
    
    b = input()
    f2 = open(b, "r")
    
    for line in f2:
        x, y = map(float, line.split())
        print(check_circle(x, y, r, x0, y0))
    
    f2.close()
    
if __name__ == "__main__":
    main()