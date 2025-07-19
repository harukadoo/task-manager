import unittest
import os
from task_manager import TaskManager
from task import Task 

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_tasks.json"
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        self.manager = TaskManager(self.test_filename)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_task(self):
        self.manager.add_task("Test Task 1")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].description, "Test Task 1")

    def test_mark_task_completed(self):
        self.manager.add_task("Test task to complete")
        task_id = self.manager.tasks[0].id
        self.manager.mark_task_completed(task_id)
        self.assertTrue(self.manager.tasks[0].completed)

    def test_delete_task(self):
        self.manager.add_task("Test task to delete")
        task_id = self.manager.tasks[0].id
        self.manager.delete_task(task_id)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_get_all_tasks_generator(self):
        self.manager.add_task("Task A")
        self.manager.add_task("Task B")
        tasks_list = list(self.manager.get_all_tasks())
        self.assertEqual(len(tasks_list), 2)
        self.assertIn("Task A", tasks_list[0])
        self.assertIn("Task B", tasks_list[1])

    def test_get_uncompleted_tasks_list_comprehension(self):
        self.manager.add_task("Uncompleted Task")
        self.manager.add_task("Completed Task")
        self.manager.tasks[1].completed = True 
        uncompleted_tasks = self.manager.get_uncompleted_tasks()
        self.assertEqual(len(uncompleted_tasks), 1)
        self.assertEqual(uncompleted_tasks[0].description, "Uncompleted Task")

    def test_invalid_task_id_mark(self):
        with self.assertLogs('root', level='INFO') as cm: 
            self.manager.mark_task_completed("999999")
            self.assertIn("Error: Task with ID 999999 not found.", cm.output[0]) 

    def test_invalid_task_id_delete(self):
        with self.assertLogs('root', level='INFO') as cm:
            self.manager.delete_task("999999")
            self.assertIn("Error: Task with ID 999999 not found.", cm.output[0])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)