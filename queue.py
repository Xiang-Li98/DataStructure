class Queue(object):
    """List实现顺序队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """进队列"""
        self.__list.append(item)

    def dequeue(self):
        """出队列"""
        return self.__list.pop(0)

    def get_head(self):
        """返回队头元素"""
        return self.__list[0]

    def is_empty(self):
        """判空"""
        return self.__list == []

    def size(self):
        """返回队列大小"""
        return len(self.__list)