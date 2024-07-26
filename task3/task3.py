import json
import sys


def list_to_dict(t):
    for i in t:
        if i.get("value") == '':
            i["value"] = get_value(i.get("id"))
            
        if i.get("values"):
            list_to_dict(i.get("values"))


def get_value(id):
    for val in v:
        if val.get("id") == id:
            return val.get("value")


def main(a, b, c):
    global v
    if not a and not b and not c:
        print("Введите путь к файлу values.json:")
        a = input()
        print("\nВведите путь к файлу tests.json:")
        b = input()
        print("\nВведите путь к файлу report.json:")
        c = input()
    else:
        a = a
        b = b
        c = c
        
    f1 = open(a, 'r')
    f2 = open(b, 'r')
    f3 = open(c, 'w')

    values = json.load(f1)
    test = json.load(f2)
    t = test.get("tests")
    v = values.get("values")
    
    list_to_dict(t)
    
    json.dump(test, f3, indent=2)
    f1.close()
    f2.close()
    f3.close()

    print(f"\nФайл готов и находится\n{c}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main(None, None, None)
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])