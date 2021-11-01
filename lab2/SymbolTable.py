class SymbolTable:

    def __init__(self):
        # size of hash table is a large prime number in order to avoid rehashing
        self.__size = 863
        self.__table = []
        for i in range(self.__size):
            self.__table.append(None)

    def insert(self, token):
        # calculate hash value
        hash_value = 0
        if isinstance(token, int):
            hash_value = token % self.__size
        elif isinstance(token, str):
            for c in token:
                hash_value += ord(c)
            hash_value = hash_value % self.__size

        # check for collision and add new token
        if self.__table[hash_value] is not None:
            new_hash = (hash_value + 1) % self.__size
            while new_hash is not hash_value and new_hash < self.__size:
                if self.__table[new_hash] is None:
                    hash_value = new_hash
                    break
                new_hash += 1
        self.__table[hash_value] = token

    def pos(self, token):
        if self.__table.count(token) == 0:
            self.insert(token)
        return self.__table.index(token)
