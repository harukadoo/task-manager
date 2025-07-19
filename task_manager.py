import json
from task import Task
import requests 

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self._load_tasks()
        self._load_quote_of_the_day() 

    def _load_tasks(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
            
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def _load_quote_of_the_day(self):
        try:
            response = requests.get("https://zenquotes.io/api/random")
            response.raise_for_status() 
            quote_data = response.json()
            
            if quote_data and isinstance(quote_data, list) and len(quote_data) > 0:
                print(f"\nQuote of the day: \"{quote_data[0]['q']}\" - {quote_data[0]['a']}\n")

            else:
                print("\nFailed to retrieve quote of the day.\n")

        except requests.exceptions.RequestException as e:
            print(f"\nError fetching quote of the day: {e}\n")

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        self._save_tasks()
        print(f"Task '{description}' added (ID: {new_task.id}).")

    def get_all_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✓ Completed" if task.completed else "✗ Not Completed"
            yield f"{i+1}. [ID: {task.id}] {task.description} ({status}) | Created: {task.created_at}"

    def get_uncompleted_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def mark_task_completed(self, task_id):
        try:
            task_id = int(task_id)
            for task in self.tasks:
                if task.id == task_id:
                    task.completed = True
                    self._save_tasks()
                    print(f"Task with ID {task_id} marked as completed.")
                    return 
                
            raise ValueError(f"Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def delete_task(self, task_id):
        initial_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != int(task_id)]
        
        if len(self.tasks) < initial_len:
            self._save_tasks()
            print(f"Task with ID {task_id} deleted.")

        else:
            print(f"Error: Task with ID {task_id} not found.")