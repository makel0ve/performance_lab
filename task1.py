def elem(a, n):
    return a + 1 if a < n else 1


def main():
    n, m = map(int, input().split())
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
    print(main()) 