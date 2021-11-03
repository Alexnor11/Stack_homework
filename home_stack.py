class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            removed = self.items.pop()
            return removed

    def peek(self):
        if self.isEmpty():
            return 'Стек пустой'
        else:
            return self.items[-1]

    def size(self):
        return self.items


# Поверка стека:
st = Stack()

print('Stack empty?:', st.isEmpty())

st.push(1)
st.push(2)
st.push(3)

print('Add Elements:', st.items)

st.pop()

print(st.items)
print('Stack empty?:', st.isEmpty())

print('Get the size:', st.size())
print('Get the peek:', st.peek())


# проверка сбалансированности скобок:
def checkBraces(my_str):
    s = Stack()
    balanced = True
    index = 0
    while index < len(my_str) and balanced:
        symbol = my_str[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not staples(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return 'Сбалансированная последовательность!'
    else:
        return 'Не сбалансированная последовательность!'


def staples(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


print(checkBraces('{{[()]}}'))
print(checkBraces('{{[(])]}}'))



