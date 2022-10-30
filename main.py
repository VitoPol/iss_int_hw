from INT import Int


def iss(obj1, obj2):
    print(f"Две переменные ссылаются на {'один и тот же адрес' if obj1 is obj2 else 'разные адреса'} в памяти, имеют {'одинаковые' if obj1 == obj2 else 'разные'} значения.")
    print(f"id первой переменной: {id(obj1)}\nid первой переменной: {id(obj2)}")
    print(f"Значение первой переменной: {obj1}\nЗначение первой переменной: {obj2}")


if __name__ == '__main__':
    a, b = Int(10), 13
    a += "три"
    iss(a, b)
