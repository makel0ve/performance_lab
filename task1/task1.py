import sys


def elem(a, n):
    return a + 1 if a < n else 1


def main(n, m):
    if not n and not m:
        print("Введите числа n и m через пробел:")
        n, m = map(int, input().split())
    else:
        n = n
        m = m
    e = 0
    mat = []
    s = ''

    while True:
        e = elem(e, n)
        mat.append(e)
        if mat[-1] == 1 and len(mat) == m:
            s += str(mat[0])
            return s
        if len(mat) == m:
            s += str(mat[0])
            mat = mat[-1:]
    
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(main(None, None)) 
    else:
        print(main(int(sys.argv[1]), int(sys.argv[2])))