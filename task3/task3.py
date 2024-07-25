import json


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


def main():
    global v
    a = input()
    b = input()
    c = input()
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


if __name__ == "__main__":
    main()