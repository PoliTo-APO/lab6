from typing import Any


class Node:
    def __init__(self, value: Any = None, next_node=None) -> None:
        self._next = next_node
        self._value = value

    def get_next(self) -> "Node":
        return self._next

    def set_next(self, next_node: "Node"):
        self._next = next_node

    def get_value(self) -> Any:
        return self._value

    def set_value(self, value) -> None:
        self._value = value


class LinkedList:
    def __init__(self) -> None:
        self._head = None
        self._num_elm = 0

    def __len__(self) -> int:
        return self._num_elm

    def insert_front(self, value: Any) -> None:
        new_elm = Node(value, next_node=self._head)
        self._head = new_elm
        self._num_elm += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx == 0:
            self.insert_front(value)
        else:
            curr_node = self._head
            for i in range(idx-1):
                curr_node = curr_node.get_next()
            new_node = Node(value, next_node=curr_node.get_next())
            curr_node.set_next(new_node)
            self._num_elm += 1

    def remove(self, idx: int) -> None:
        if idx == 0:
            self._head = self._head.get_next()
        else:
            curr_node = self._head
            for i in range(idx-1):
                curr_node = curr_node.get_next()
            next_node = curr_node.get_next().get_next()
            curr_node.set_next(next_node)
        self._num_elm-=1

    def __getitem__(self, idx) -> Any:
        curr_node = self._head
        for i in range(idx):
            curr_node = curr_node.get_next()
        return curr_node.get_value()

    def __setitem__(self, idx, value) -> None:
        curr_node = self._head
        for i in range(idx):
            curr_node = curr_node.get_next()
        curr_node.set_value(value)

    def __repr__(self) -> str:
        str_repr = "["
        curr_node = self._head
        for i in range(len(self)-1):
            str_repr += str(curr_node.get_value()) + ", "
            curr_node = curr_node.get_next()
        str_repr += str(curr_node.get_value()) + "]"
        return str_repr


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

