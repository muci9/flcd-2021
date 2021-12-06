from lab5.Grammar import Grammar


# recursive descendent

def print_list(list):
    out = ""
    for elem in list:
        out += elem + " "
    print(out)


def print_productions(productions: dict):
    productions_items = productions.items()
    for item in productions_items:
        print(item)


def print_menu():
    print("0. exit")
    print("1. Read grammar from file")
    print("2. Print non terminals")
    print("3. Print terminals")
    print("4. Print productions")
    print("5. Print productions of a given non terminal")
    print("6. CFG check")


def read_from_file(grm: Grammar):
    file = input("File name: ")
    grm.read_from_file(file)


def print_productions_given_non_term(grm: Grammar):
    non_terminal = input("Non terminal: ")
    print(grm.get_production_by_non_terminal(non_terminal))

def print_is_cfg(result):
    if result is True:
        print("Grammar is CFG")
    else:
        print("Grammar is not CFG")


if __name__ == '__main__':
    gr = Grammar()
    menu = {
        "1": [read_from_file, gr],
        "2": [print_list, gr.get_non_terminals],
        "3": [print_list, gr.get_terminals],
        "4": [print_productions, gr.get_productions],
        "5": [print_productions_given_non_term, gr],
        "6": [print_is_cfg, gr.is_cfg]
    }
    while True:
        print_menu()
        opt = input("Choose an option: ")
        if opt == "0":
            break
        elif opt not in ["1", "5"]:
            menu[opt][0](menu[opt][1]())
        else:
            menu[opt][0](menu[opt][1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
