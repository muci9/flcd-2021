from SymbolTable import SymbolTable
from PIF import PIF
import re

class Scanner:

    def __init__(self, input_file):
        self.__input_file = input_file
        self.__predefined_tokens = self.__get_predefined_tokens__()
        self.__st_constants = SymbolTable()
        self.__st_identifiers = SymbolTable()
        self.__pif = PIF()

    def __get_predefined_tokens__(self):
        tokens = []
        with open("token.in") as file:
            for line in file:
                tokens.append(line.strip("\n"))
        return tokens

    def __is_constant__(self, token):
        pattern_zero = re.compile("0")
        pattern_integer = re.compile("(\+|-){,1}1-90-9*")
        pattern_string = re.compile("\"[a-zA-Z0-9]+\"")
        return pattern_zero.match(token) or pattern_string.match(token) or pattern_integer.match(token)

    def __is_identifier__(self, token):
        pattern_identifier = re.compile("[a-zA-Z][a-zA-z0-9]*")
        return pattern_identifier.match(token)

    def __detect__(self, line):
        line = line.strip("\t\n")
        tokens = re.split("([^a-zA-Z0-9\"])", line)
        tokens = list(filter(lambda x: x != " " and x != "" and x != "\n" and x != "\t", tokens))
        return tokens

    def __generate_pif__(self, token, pos):
        self.__pif.add(token, pos)

    def scan(self):
        current_line = 0
        is_correct = True
        with open(self.__input_file) as file:
            for line in file:
                current_line += 1
                tokens = self.__detect__(line)
                for token in tokens:
                    if token in self.__predefined_tokens:
                        self.__generate_pif__(token, -1)
                    elif self.__is_constant__(token):
                        index = self.__st_constants.pos(token)
                        self.__generate_pif__(0, index)
                    elif self.__is_identifier__(token):
                        index = self.__st_identifiers.pos(token)
                        self.__generate_pif__(1, index)
                    else:
                        print("Lexical error at line: ", current_line, " on token: ", token)
                        is_correct = False
        if is_correct:
            print("Lexically correct")

    def output(self):
        pif = open("PIF.out", "w")
        for elem in self.__pif.get_pif():
            pif.write(str(elem) + "\n")
        pif.close()

        st = open("ST.out", "w")
        st.write("Identifiers:\n")
        for entry in self.__st_identifiers.get_table():
            st.write(str(entry) + "\n")

        st.write("Constants:\n")
        for entry in self.__st_constants.get_table():
            st.write(str(entry) + "\n")
        st.close()

