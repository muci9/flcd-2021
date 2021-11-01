class PIF:

    def __init__(self):
        self.__pif = []

    def add(self, token, pos):
        self.__pif.append((token, pos))

    def get_pif(self):
        return self.__pif
