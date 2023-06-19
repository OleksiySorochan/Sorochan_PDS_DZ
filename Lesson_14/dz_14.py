class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Прямий обхід
    def travers_pre_order(self):
        print(self.val, end=' ')
        if self.left:
            self.left.travers_pre_order()
        if self.right:
            self.right.travers_pre_order()

    # Зворотній обхід
    def travers_in_order(self):
        if self.left:
            self.left.travers_in_order()
        print(self.val, end=' ')
        if self.right:
            self.right.travers_in_order()

    # Обхід із середини
    def travers_enter_order(self):
        if self.left:
            self.left.travers_enter_order()

        if self.right:
            self.right.travers_enter_order()
        print(self.val, end=' ')


    # Метод додавання нового елементу
    def insert(self, key):
        if key < self.val:
            if self.left:
                self.left.insert(key)
            else:
                self.left = Node(key)
                return
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = Node(key)



    # Друк дерева
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    ######################################################
   # 2 завдання
    # пошук мінімального  та максимального значення

    def find_min(self):
        if not self.left:
            return self.val
        return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.val
        return self.right.find_max()

    # 3 завдання
    # Видалення елементів

    def del_node(self, key):
        if key < self.val:
            if self.left:
                self.left = self.left.del_node(key)
        elif key > self.val:
            if self.right:
                self.right = self.right.del_node(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_node = self.right.find_min()
                self.val = min_node
                self.right = self.right.del_node(min_node)
        return self


    # 1 завдання
    # додавання до дерева списком
def bild(lst):
    tree = Node(lst[0])
    tree.root = Node(lst[0])
    for i in range(1, len(lst)):
        if lst[i] is not None:
            tree.insert(lst[i])
    return tree
######################################################

tree = [8, 3, 10, 1, 6, None, 154, None, None, 4, 7, None, None, 13, None]
t = bild(tree)
t.display()
print(f'min: {t.find_min()}')
print(f'max: {t.find_max()}')

t.del_node(6)
t.display()