
from queue import Queue # Для обхода в ширину

class Node:
    '''
    Класс для хранения единичного узла бинарного дерева
    '''
    def __init__(self, val):
        self.l = None  # Связь с левым потомком
        self.r = None  # Связь с правым потомком
        self.v = val   # Ключ (значение, которое хранится в узле)

class Tree:
    '''
    Класс для хранения бинарного дерева поиска
    '''
    def __init__(self):
        '''
        Создаем пустое дерево
        '''
        self.root = None

    def getRoot(self):
        '''
        Получение значения корня
        '''
        return self.root

    def add(self, val):
        '''
        Добавление узла.
        Если дерево не содержит элементов, создаем дерево из одного элемента.
        Если дерево не пустое, вызываем вспомогательную функцию добавления.
        '''
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        '''
        Вспомогательная рекурсивная функция добавления.
        Если элемент меньше значения текущего узла,
        добавляем его в левое поддерево.
        В противном случае добавляем его в правое поддерево.
        '''
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        '''
        Поиск узла.
        Если узел не пуст, вызываем вспомогательную функцию поиска,
        иначе возвращаем None.
        '''
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        '''
        Вспомогательная рекурсивная функция поиска.
        Если узел найден, возвращаем его. Если значение узла больше искомого,
        продолжаем поиск в левом поддереве, если оно не пустое. Если значение
        узла меньше искомого, продолжаем поиск в правом поддереве,
        если оно не пустое.
        '''
        if val == node.v:
            return node.v
        elif (val < node.v and node.l != None):
            return self._find(val, node.l)
        elif (val > node.v and node.r != None):
            return self._find(val, node.r)

    def deleteTree(self):
        '''
        Удаление дерева.
        Удаляем корень, все остальное делает сборщик мусора.
        '''
        self.root = None

    def printTree(self):
        '''
        Печать дерева.
        Вызываем вспомогательную функцию печати.
        '''
        if self.root is not None:
            print("Дерево:")
            self._printTree(self.root)
            print()
        else:
            print("Дерево не существует")

    def _printTree(self, node):
        '''
        Вспомогательная рекурсивная функция печати.
        '''
        if node is not None:
            print(str(node.v), end=' ')
            self._printTree(node.l)
            self._printTree(node.r)

    def BFS(self):
        '''
        Обход дерева в ширину.
        '''
        if self.root is not None:
            q = Queue()
            q.put(self.root)
            while not q.empty():
                x = q.get()
                print(str(x.v), end=' ')
                if x.l is not None:
                     q.put(x.l)
                if x.r is not None:
                     q.put(x.r)
            print()
        else:
            print("Дерево не существует")


    def generate_random_tree(n, min_val, max_val): #Генерирует бинарное дерево поиска из n случайных чисел в заданном диапазоне.
        import random
        tree = Tree()
        values = []


        for _ in range(n):
            value = random.randint(min_val, max_val)
            values.append(value)


        tree.add(values[0])


        for value in values[1:]:
            tree.add(value)

        return tree
    
    '''---------------------------'''

    def count_nodes(self): #Метод для подсчета количества узлов в дереве.
        return self.count_nodes_recursive(self.root)

    def count_nodes_recursive(self, node): #Рекурсивная функция для подсчета количества узлов в бинарном дереве.
        if node is None:
            return 0
        return 1 + self.count_nodes_recursive(node.l) + self.count_nodes_recursive(node.r)
    
    '''-----------------------------'''

    def count_leaves(self,node): #Рекурсивная функция для подсчета количества листьев в бинарном дереве.

        if node is None:
            return 0
        elif node.l is None and node.r is None:
            return 1
        else:
            return self.count_leaves(node.l) + self.count_leaves(node.r)

    def count_leaves_tree(self):  # Метод для подсчета количества листьев в дереве.

        return self.count_leaves(self.root)
    
    '''-----------------------------'''

    def get_height(self,node): # Рекурсивная функция для вычисления высоты бинарного дерева.

        if node is None:
            return 0
        else:
            return max(self.get_height(node.l), self.get_height(node.r)) + 1

    def get_height_tree(self): # Метод для вычисления высоты дерева.
        return self.get_height(self.root)
    
    '''----------------------------'''



    def depth_first_search(self):
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.v)
            if node.r:
                stack.append(node.r)
            if node.l:
                stack.append(node.l)
    
    



'''tree=Tree()
tree.add(3) # Поштучное добавление элементов (можно заменить циклом)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.add(-1)
tree.add(1)'''
tree=Tree()
tree=Tree.generate_random_tree(10, 1, 100)

tree.printTree() # Печать дерева

count = tree.count_nodes()
print("количество узлов:", count)

num_leaves = tree.count_leaves_tree()
print("Количество листьев:", num_leaves)

height = tree.get_height_tree()
print("Высота дерева:", height)

tree.depth_first_search()