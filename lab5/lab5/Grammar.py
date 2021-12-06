from collections import defaultdict

__separator__ = '~'


class Grammar:

    def __init__(self, non_terminals=None, terminals=None, start_symbol=None, productions=None):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.start_symbol = start_symbol
        self.productions = productions

    def read_from_file(self, file):
        with open(file, 'r') as fd:
            self.non_terminals = fd.readline().strip('\n').split()
            self.terminals = fd.readline().strip('\n').split()
            self.start_symbol = fd.readline().strip('\n')
            self.productions = defaultdict(list)
            for line in fd:
                non_terminal, production, *tail = line.strip('\n').split()
                self.productions[non_terminal].append(production.split(__separator__))

    def get_non_terminals(self):
        return self.non_terminals

    def get_terminals(self):
        return self.terminals

    def get_productions(self):
        return self.productions

    def get_production_by_non_terminal(self, non_terminal):
        return self.productions[non_terminal]

    def get_start_symbol(self):
        return self.start_symbol

    def is_cfg(self):

        if self.start_symbol not in self.productions.keys():
            return False
        # check lhs of productions consists only of non-terminals
        keys_list = list(self.productions.keys())
        res = all(keys_list[i] == self.non_terminals[i]
                  if len(keys_list) == len(self.non_terminals)
                  else False for i in range(len(self.non_terminals)))
        if res is False:
            return False
        # check rhs of productions consists of non-terminals, terminals and epsilon
        for productions in self.productions.values():
            for production in productions:
                for symbol in production:
                    print(symbol)
                    if symbol not in self.non_terminals and symbol not in self.terminals and symbol != 'epsilon':
                        return False
        return True
