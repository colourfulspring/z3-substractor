class Number(object):
    def __init__(self):
        self.__value = 0
        self.__binary = ''
        self.__len = 0

    def set_value(self, value):
        self.__value = value
        self.__binary = ''
        while value != 0:
            self.__binary = ('1' if value & 1 else '0') + self.__binary
            value >>= 1
        self.__len = len(self.__binary)

    def set_binary_str(self, str):
        self.__binary = str
        self.__len = len(str)
        self.__value = 0
        for c in str:
            self.__value <<= 1
            self.__value += 1 if c == '1' else 0

    def get_value(self):
        return self.__value

    def get_binary_str_index(self, index):
        return self.__binary[index]

    def set_n(self, n):
        while n > self.__len:
            self.__binary = '0' + self.__binary
            self.__len += 1

    def get_n(self):
        return self.__len
