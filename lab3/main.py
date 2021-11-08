from SymbolTable import SymbolTable
from Scanner import Scanner

if __name__ == '__main__':
    st = SymbolTable()

    s = Scanner("p1err.txt")
    s.scan()
    s.output()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
