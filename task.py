import datetime
import numpy as np 

class Task:
    def __init__(self, description):
        self.id = int(np.random.randint(100000, 999999))
        self.description = description
        self.completed = False
        self.created_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        task = Task(data['description'])
        task.id = data['id']
        task.completed = data['completed']
        task.created_at = data['created_at']
        return task