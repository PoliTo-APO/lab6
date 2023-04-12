from typing import Any


class LinkedList:
    def __init__(self) -> None:
        pass

    def __len__(self) -> int:
        pass

    def insert_front(self, value: Any) -> None:
        pass

    def insert(self, idx: int, value: Any) -> None:
        pass

    def remove(self, idx: int) -> None:
        pass

    def __getitem__(self, idx) -> Any:
        pass

    def __setitem__(self, idx, value) -> None:
        pass

    def __repr__(self) -> str:
        pass


def main():
    lista = LinkedList()

    lista.insert_front("H")     # [H]
    lista.insert_front("F")     # [F, H]
    lista.insert_front("D")     # [D, F, H]
    print(lista, len(lista))

    lista.insert(0, "C")            # [C, D, F, H]
    lista.insert(2, "E")            # [C, D, E, F, H]
    lista.insert(len(lista), "I")   # [C, D, E, F, H, I]
    print(lista, len(lista))

    lista.remove(0)             # [D, E, F, H, I]
    lista.remove(2)             # [D, E, H, I]
    lista.remove(len(lista)-1)  # [D, E, H]
    print(lista, len(lista))

    print(lista[0], lista[1], lista[len(lista)-1])
    
    lista[0] = "X"  # [X, E, H]
    lista[1] = "Y"  # [X, Y, H]
    lista[2] = "Z"  # [X, Y, Z]
    print(lista)


if __name__ == "__main__":
    main()

