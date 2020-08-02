from KanbanDBManager import KanbanDBManager

test = KanbanDBManager({
    "host": "120.25.251.110", 
    "port": 3306, 
    "user": "root", 
    "password": "123456", 
    "database": "schema_pm"
})

test.sign_up_project("project_1", "1")
print(test.sign_in_project("project_12", "123456"))
print(test.sign_up_project("project_2", "123456"))
print(test.get_todo_task("project_1"))
print(test.get_inprogress_task("project_1"))
print(test.get_done_task("project_1"))
print(test.create_todo_task("project_1", "task_111"))
print(test.create_inprogress_task("project_1", "task_222"))
print(test.create_done_task("project_1", "task_333"))
print(test.change_task_status("project_1", "teask_23", 3))
print("END")
