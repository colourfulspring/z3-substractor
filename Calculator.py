from z3 import *
from Number import Number


class Calculator(object):
    def __init__(self):
        pass

    def substract(self, NumberSum, NumberOperand):
        len = max(NumberSum.get_n(), NumberOperand.get_n())
        NumberSum.set_n(len)
        NumberOperand.set_n(len)
        a = [Bool('a%i' % i) for i in range(len)]
        b = [Bool('b%i' % i) for i in range(len)]
        c = [Bool('c%i' % i) for i in range(len + 1)]
        d = [Bool('d%i' % i) for i in range(len)]
        premiseA = [a[i] if NumberOperand.get_binary_str_index(i) == '1' else Not(a[i]) for i in
                    range(len)]
        premiseB = []
        premiseD = [d[i] if NumberSum.get_binary_str_index(i) == '1' else Not(d[i]) for i in
                    range(len)]
        result = [d[i] == (a[i] == (b[i] == c[i + 1])) for i in range(len)]
        carry = [c[i] == Or(And(a[i], b[i]), And(a[i], c[i + 1]), And(b[i], c[i + 1])) for i in range(len)]
        edge = [Not(c[0]), Not(c[len])]
        s = Solver()
        s.add(result + carry + premiseA + premiseB + premiseD + edge)
        if s.check() == sat:
            ans = 0
            for i in range(len):
                ans <<= 1
                if is_true(s.model()[b[i]]):
                    ans += 1
            print('the answer is %d.' % ans)
        else:
            print('no solution!')


if __name__ == '__main__':
    cal = Calculator()
    print("请输入被减数：")
    sum = Number()
    sum.set_value(int(input()))
    print("请输入减数：")
    operand = Number()
    operand.set_value(int(input()))
    cal.substract(sum, operand)
