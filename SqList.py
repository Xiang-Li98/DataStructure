MaxSize = 100


class SqList:  # 线性表
    def __init__(self, length):
        self.data = [None for i in range(MaxSize)]
        self.length = length


def init_list():  # 初始化操作，建立一个空表
    sql = SqList(0)
    return sql


def list_empty(sql):
    try:
        if sql.data[0] is None:
            return False
        else:
            return True
    except AttributeError:
        print("Sequence List must be initiated first!")


def clear_list(sql):
    try:
        for i in range(0, sql.length):
            sql.data[i] = None
    except AttributeError:
        print("Sequence List must be initiated first!")


def list_insert(sql, i, e):  # 在0 <= i <= sql.length的位置插入e
    try:
        assert sql.length < MaxSize, "The sequence list is full"
        assert 0 <= i <= sql.length, "The position you give is out of range"
        if i != sql.length:  # 不是在表尾插入
            for j in range(sql.length - 1, i - 1, -1):
                sql.data[j+1] = sql.data[j]
        sql.data[i] = e
        sql.length += 1
        return True
    except AttributeError:
        print("Sequence List must be initiated first!")


def list_delete(sql, i):  # 把0 <= i <= sql.length-1位置的数删除
    try:
        assert sql.length != 0, "The list is empty"
        assert 0 <= i <= sql.length - 1, "The position you give is out of range"
        if i != sql.length - 1:
            for j in range(i+1, sql.length):
                sql.data[j-1] = sql.data[j]
        sql.length -= 1
        return True
    except AttributeError:
        print("Sequence List must be initiated first!")


def get_elem(sql, i):  #返回i位置的值
    assert 0 <= i < sql.length, "The position you give is out of range"
    e = sql.data[i]
    return e


