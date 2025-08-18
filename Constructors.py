class TodoList:
    def __init__(self, title, items=None):   # good: default is None
        self.title = title
        self.items = list(items) if items else []  # make a new list

    def add(self, task):
        self.items.append(task)

todo = TodoList("Daily Tasks")
todo.add("Study Python")
print(todo.items, todo.title)  # ['Study Python']
