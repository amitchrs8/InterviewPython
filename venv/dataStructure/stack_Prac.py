class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        if len(self.__items) == 10:
            raise OverflowError("Stack is already Full. Don't push anymore!!!")
        self.__items.append(item)

    def pop(self):
        if len(self.__items) <= 0:
            raise IndexError("No element in Stack to be popped out")
        return self.__items.pop()

    def get_count(self):
        return len(self.__items)

    def print_stack(self):
        print('Stack content')
        [print(i) for i in self.__items]


def isBalanced(exp):
    s = Stack()
    d = {'}': '{',
         ')': '(',
         ']': '['}
    for i in exp:
        if i in d.values() or i in d.keys():
            if i in d.values():
                s.push(i)
            elif i in d.keys():
                top_item = s.pop()
                if d.get(i) != top_item:
                    return False
        else:
            return False
    return True


def reverseString(s):
    stk = Stack()
    [stk.push(i) for i in s]
    rev = ''
    while stk.get_count() > 0:
        rev = rev + stk.pop()
    print('Reversed String : {}'.format(rev))


def convert_dec_to_bin(num):
    s = Stack()
    while num >= 1:
        rem = num % 2
        num = num // 2
        s.push(rem)
    s.push(num)
    bin_number = ''
    while s.get_count() > 0:
        bin_number = bin_number + str(s.pop())
    print('Binary Number : {}'.format(bin_number))


if __name__ == '__main__':
    #print('Executing')
    #a = "{}{}[({})]{}"
    #b = "{}{}[({})]{]}"
    #print(isBalanced(a))
    #print(isBalanced(b))
    #reverseString("amit")
    convert_dec_to_bin(10)
