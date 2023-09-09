from __future__ import annotations


class Graph:
    __matrix: list[list[int]]
    __vertex: list[str]

    def __init__(self):
        self.__matrix = []
        self.__vertex = []

    def __find_index_by_mark(self, mark: str) -> int:
        for index, vertex in enumerate(self.__vertex):
            if vertex == mark:
                return index

        return -1

    def first(self) -> str:
        if not len(self.__vertex):
            raise Exception(f'Graph is empty')

        return self.__vertex[0]

    def next(self, v: str):
        index_v = self.__find_index_by_mark(v)
        if index_v == -1:
            raise Exception(f'Vertex {v} not found!')

        for index_w, col in enumerate(self.__matrix[index_v]):
            if col == 1:
                yield self.__vertex[index_w]

    def vertex(self):
        pass

    def add_v(self, mark: str):
        self.__vertex.append(mark)

        for row in self.__matrix:
            row.append(0)

        new_size_rows = len(self.__matrix) + 1
        self.__matrix.append([0] * new_size_rows)

    def add_e(self, v: str, w: str):
        v_index = self.__find_index_by_mark(v)
        if v_index == -1:
            raise Exception(f'Vertex {v} not found!')

        w_index = self.__find_index_by_mark(w)
        if w_index == -1:
            raise Exception(f'Vertex {w} not found!')

        self.__matrix[v_index][w_index] = 1

    def del_v(self):
        pass

    def del_e(self):
        pass

    def edit_v(self):
        pass

    def edit_e(self):
        pass

    def get_transpose_graph(self) -> Graph:
        result = Graph()
        for vertex in self.__vertex:
            result.add_v(vertex)

        for row_index, row in enumerate(self.__matrix):
            for col_index, col in enumerate(row):
                if col == 0:
                    continue

                v = self.__vertex[col_index]
                w = self.__vertex[row_index]

                result.add_e(v, w)

        return result
