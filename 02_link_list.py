class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class LinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def get_elem(self, i):
        """返回i位置的元素"""
        p = self.__head
        j = 1
        while p and j < i:
            p = p.next
            j += 1
        assert p and j <= i, "There is no node at %d" % i
        return p.elem

    def get_length(self):
        """得到链表的长度"""
        count = 0
        p = self.__head
        while p:
            p = p.next
            count += 1
        return count

    def add(self, e):
        """链表头部添加元素"""
        n = Node(e)
        p = self.__head
        n.next = p
        self.__head = n

    def append(self, e):
        """链表尾部添加元素"""
        n = Node(e)
        p = self.__head
        if self.__head:
            while p.next:
                p = p.next
            p.next = n
        else:
            self.__head = n

    def list_insert(self, i, e):
        """在i位置后面插入元素e"""
        j = 1
        p = self.__head
        if i == 0:
            self.add(e)
            return True
        if i >= self.get_length():
            self.append(e)
            return True
        else:
            while p and j < i:
                p = p.next
                j += 1
            n = Node(e)
            n.next = p.next
            p.next = n
            return True

    def travel(self):
        """遍历整个链表"""
        p = self.__head
        li = []
        while p:
            li.append(p.elem)
            p = p.next
        print(li)
        return True

    def list_delete(self, i):
        """将i位置元素删除"""
        assert 0 < i <= self.get_length(), "There is no node at %d" % i
        p = self.__head
        pre = None
        j = 1
        if i == 1:
            self.__head = p.next
        else:
            while p and j < i:
                pre = p
                p = p.next
                j += 1
            if p.next:
                pre.next = p.next
            else:
                pre.next = None
        return True

    
