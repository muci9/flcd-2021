class FiniteAutomata:

    def __init__(self, states=None, alphabet=None, initial_state=None,
                 final_states=None, transitions=None):
        self.__states = states
        self.__alphabet = alphabet
        self.__initial_state = initial_state
        self.__final_states = final_states
        self.__transitions = transitions

    def init_from_file(self, input_file):
        fd = open(input_file, 'r')
        self.__states = fd.readline().split()
        self.__alphabet = fd.readline().split()
        self.__initial_state = fd.readline().strip()
        self.__final_states = fd.readline().split()
        self.__transitions = []
        for line in fd:
            parsed_line = line.strip().split(' ')
            self.__transitions.append([(parsed_line[0], parsed_line[1]), parsed_line[2]])

    def get_states(self):
        return self.__states

    def get_initial_state(self):
        return self.__initial_state

    def get_final_states(self):
        return self.__final_states

    def get_transitions(self):
        return self.__transitions

    def get_alphabet(self):
        return self.__alphabet

    def is_valid_sequence(self, sequence):
        current_state = self.__initial_state
        sequence_length = len(sequence)
        is_valid = False
        for elem in sequence:
            print(current_state, elem)
            for transition in self.__transitions:
                if transition[0][0] == current_state and transition[0][1] == elem:
                    is_valid = True
                    print(transition)
                    current_state = transition[1]
                    break
            if not is_valid:
                break
            else:
                sequence_length -= 1
            is_valid = False
        if current_state not in self.__final_states or sequence_length != 0:
            print("Failed")
            return False
        print("Success")
        return True
