from collections import deque
import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, cmap=plt.cm.Blues)
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


# Ітеративна реалізація алгоритму DFS
def dfs_iterative(root):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [root]
    step = 0
    while stack:
        step += 1
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex.val, end=' ')
            vertex.color = step
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            if vertex.left:
                stack.append(vertex.left)
            if vertex.right:
                stack.append(vertex.right)


# Ітеративна реалізація алгоритму BFS
def bfs_iterative(root):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([root])

    step = 0
    while queue:  # Поки черга не порожня, продовжуємо обхід
        step += 1
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex.val, end=" ")
            vertex.color = step
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            if vertex.left:
                queue.extend(set([vertex.left]) - visited)
            if vertex.right:
                queue.extend(set([vertex.right]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited


dfs_iterative(root)
# Відображення дерева
draw_tree(root)

bfs_iterative(root)
# Відображення дерева
draw_tree(root)
