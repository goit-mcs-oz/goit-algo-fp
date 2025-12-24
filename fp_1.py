'''
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
- написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
- розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
- написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
'''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.sorted_head = None

    def __str__(self):
        str = ''
        current = self.head
        while current:
            str += f"{current.data} "
            current = current.next
        return str

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

# Функція, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами
    def reverce(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def insert_by_order_from(self, node, from_node):
        cur = from_node
        prev = None
        while cur:
            if cur.data > node.data:
                break
            prev = cur
            cur = cur.next
        if prev:
            prev.next = node
        else:
            self.head = node
        node.next = cur

    def _insert_by_order(self, node):
        cur = self.sorted_head
        prev = None
        while cur:
            if cur.data > node.data:
                break
            prev = cur
            cur = cur.next
        if prev:
            prev.next = node
        else:
            self.sorted_head = node
        node.next = cur

    # Сортування вставками
    def insertion_sort(self):
        if not self.head is None:
            self.sorted_head = self.head
            cur = self.head.next
            self.delete_node(self.sorted_head.data)
            self.sorted_head.next = None
            while cur:
                next = cur.next
                self.delete_node(cur.data)
                self._insert_by_order(cur)
                cur = next
            self.head = self.sorted_head
            self.sorted_head = None


# Функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список
def merge_linked_list(list_1, list_2):
    merged_list = LinkedList()

    cur = list_1.head
    while cur:
        merged_list.insert_at_end(cur.data)
        cur = cur.next

    cur = list_2.head
    insert_node_prev = merged_list.head
    while cur:
        insert_node = Node(cur.data)
        merged_list.insert_by_order_from(insert_node, insert_node_prev)
        insert_node_prev = insert_node
        cur = cur.next

    return merged_list


llist = LinkedList()
llist.insert_at_end(5)
llist.insert_at_end(20)
llist.insert_at_end(10)
llist.insert_at_end(15)

print(llist)
llist.reverce()
print(f'Reverced: {llist}')
llist.insertion_sort()
print(f'Sorted: {llist}')


llist1 = LinkedList()
llist1.insert_at_end(5)
llist1.insert_at_end(7)
llist1.insert_at_end(30)
llist1.insert_at_end(10)

print('')
print(llist1)
llist1.insertion_sort()
print(f'Sorted: {llist1}')

llist2 = LinkedList()
llist2.insert_at_end(3)
llist2.insert_at_end(1)
llist2.insert_at_end(12)
llist2.insert_at_end(7)
llist2.insert_at_end(2)

print('')
print(llist2)
llist2.insertion_sort()
print(f'Sorted: {llist2}')

merged_list = merge_linked_list(llist1, llist2)
print('')
print(f'Merged list: {merged_list}')
