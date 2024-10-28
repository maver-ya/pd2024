class InvalidArgumentError(Exception):
    pass


class InvalidStatusError(Exception):
    pass


class Task:
    def __init__(self, task_id, description, status='Todo'):
        self.id = task_id
        self.description = description
        self.status = status


class TodoList:
    def __init__(self):
        self.tasks = []
        self.current_id = 1  # Счетчик для ID задач

    def add_task(self, description, status='Todo'):
        # Проверка на типы аргументов
        if not isinstance(description, str) or (status and not isinstance(status, str)):
            raise InvalidArgumentError('INVALIDE_ARGUMENT')

        # Проверка статуса
        if status and status not in ['Todo', 'In Progress', 'Done']:
            raise InvalidStatusError('INVALIDE_STATUS')

        # Добавление задачи
        self.tasks.append(Task(self.current_id, description, status))
        self.current_id += 1

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True  # Задача успешно удалена
        return False  # Задача не найдена

    def change_status(self, task_id, status):
        if status not in ['Todo', 'In Progress', 'Done']:
            raise InvalidStatusError('INVALIDE_STATUS')

        for task in self.tasks:
            if task.id == task_id:
                if task.status == status:
                    return False  # Статус уже установлен
                task.status = status
                return True  # Статус успешно изменен
        return False  # Задача не найдена

    def show_list(self):
        grouped_tasks = {
            'Todo': [],
            'In Progress': [],
            'Done': []
        }

        for task in self.tasks:
            grouped_tasks[task.status].append(f'{task.id} "{task.description}"')

        for status, tasks in grouped_tasks.items():
            print(f'{status}:')
            if tasks:
                print(',\n  '.join(tasks))
            else:
                print('-')
        print()


# Пример использования
todo_list = TodoList()

try:
    todo_list.add_task('create a task')
    todo_list.add_task('make a bed', 'Todo')
    todo_list.add_task('write a post', 'In Progress')
    todo_list.add_task('finish homework', 'Done')

    todo_list.show_list()

    todo_list.change_status(1, 'In Progress')
    todo_list.change_status(2, 'Done')

    todo_list.show_list()

    todo_list.delete_task(3)  # Удаляем задачу с ID 3
    todo_list.show_list()

    todo_list.delete_task(3)  # Попытка удалить уже удаленную задачу
except (InvalidArgumentError, InvalidStatusError) as e:
    print(e)
