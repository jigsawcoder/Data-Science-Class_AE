class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.item == []

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balances = True
    index = 0

    while index < len(paren_string) and is_balance:
        paren = paren_string[index]
        if paren in "[({":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = Flase
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balance = Flase
        index += 1

    if s.empty() and is_balanced:
        return True
    else:
        return False

paren_string = input("Enter set of pranthesis")

if paren_string in "(){}[]":
    print(is_paren_balanced)
else:
    print("Invalid Entry")
