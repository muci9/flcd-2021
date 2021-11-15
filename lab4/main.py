from lab4.FA import FiniteAutomata


def print_list(list):
    out = ""
    for elem in list:
        out += elem + " "
    print(out)


def print_transitions(transitions):
    for transition in transitions:
        print(transition)


def print_menu():
    print("0. exit")
    print("1. display states")
    print("2. display alphabet")
    print("3. display initial state")
    print("4. display final states")
    print("5. display transitions")
    print("6. check sequence")


def read_sequence():
    return input("Sequence: ")


if __name__ == '__main__':
    fa = FiniteAutomata()
    fa.init_from_file("lab4/FA-integer.in")
    menu = {
        "1": [print_list, fa.get_states],
        "2": [print_list, fa.get_alphabet],
        "3": [print_list, fa.get_initial_state],
        "4": [print_list, fa.get_final_states],
        "5": [print_transitions, fa.get_transitions],
        "6": [fa.is_valid_sequence, read_sequence]
    }

    while True:
        print_menu()
        opt = input("Choose an option: ")
        if opt == "0":
            break
        else:
            menu[opt][0](menu[opt][1]())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
