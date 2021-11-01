from SymbolTable import SymbolTable
from Scanner import Scanner

if __name__ == '__main__':
    st = SymbolTable()
    print(st.pos(1))
    print(st.pos(0))
    print(st.pos("abc"))

    s = Scanner("p1.txt")
    s.scan()
    s.output()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
