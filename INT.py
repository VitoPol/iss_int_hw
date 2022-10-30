def custom_add(func):
    def inner(self, other):
        if type(other) is not str:
            return func(self, other)
        match str(other).lower():
            case "один":
                return self.real + 1
            case "два":
                return self.real + 2
            case "три":
                return self.real + 3
            case "четыре":
                return self.real + 4
            case "пять":
                return self.real + 5
            case _:
                raise TypeError("справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.")
    return inner


class Int(int):
    @custom_add
    def __add__(self, other):
        return super().__add__(other)

    # def __add__(self, other):
    #     if type(other) is not str:
    #         return super().__add__(other)
    #     match str(other).lower():
    #         case "один":
    #             return self.real + 1
    #         case "два":
    #             return self.real + 2
    #         case "три":
    #             return self.real + 3
    #         case "четыре":
    #             return self.real + 4
    #         case "пять":
    #             return self.real + 5
    #         case _:
    #             raise TypeError("справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.")
