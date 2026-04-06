class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            return True
        return False

    def delete_task(self, index):
        try:
            self.tasks.pop(index)
            return True
        except IndexError:
            return False

    def edit_task(self, index, new_text):
        if new_text:
            try:
                self.tasks[index] = new_text
                return True
            except IndexError:
                return False
        return False

    def load_from_file(self, filepath):
        self.tasks.clear()
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                task = line.strip()
                if task:
                    self.tasks.append(task)

    def save_to_file(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(task + "\n")