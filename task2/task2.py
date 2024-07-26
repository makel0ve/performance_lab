import sys


def check_circle(x, y, r, x0, y0):
    if (x - x0)**2 + (y - y0)**2 < r**2:
        return 1
    
    if (x - x0)**2 + (y - y0)**2 == r**2:
        return 0
    
    return 2


def main(a, b):
    if not a and not b:
        print('Введите путь к файлу описывающий окружность:')
        a = input().replace('"', '')
        print("Введите путь к файлу с координатами:")
        b = input().replace('"', '')
    else:
        a = a
        b = b
        
    f1 = open(a, 'r')
    x0, y0 = map(float, f1.readline().split())
    r = int(f1.readline(1))
    
    f2 = open(b, "r")
    for line in f2:
        x, y = map(float, line.split())
        print(check_circle(x, y, r, x0, y0))
        
    f1.close()
    f2.close()
    
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        main(None, None)
    else:
        main(sys.argv[1], sys.argv[2])