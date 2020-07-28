DB_CONFIG = {
    "host": "120.25.251.110", 
    "port": 3306, 
    "user": "root", 
    "password": "123456", 
    "database": "schema_pm"
}

from KanbanDBManager import KanbanDBManager
from flask import Flask, abort, request, jsonify
from flask_restful import Resource, Api
from flask.views import MethodView

kanban_manager = KanbanDBManager(db_config = DB_CONFIG)

app = Flask(__name__)

class SignUp(MethodView):
    def post(self):
        json_data = request.get_json(force=True)
        return jsonify({"message": kanban_manager.sign_up_project(json_data["project_id"], json_data["password"])})
app.add_url_rule('/signup', view_func = SignUp.as_view(name='signup'))

class SignIn(MethodView):
    def post(self):
        json_data = request.get_json(force=True)
        return jsonify({"message": kanban_manager.sign_in_project(json_data["project_id"], json_data["password"])})
app.add_url_rule('/signin', view_func = SignIn.as_view(name='signin'))

class ToDo(MethodView):
    def get(self):
        project_id = str(request.args["project_id"])
        return jsonify({"todo": kanban_manager.get_todo_task(project_id)})
    def post(self):
        json_data = request.get_json(force=True)
        return jsonify({"message": kanban_manager.create_todo_task(json_data["project_id"], json_data["task_name"])})
app.add_url_rule('/todo', view_func = ToDo.as_view(name='todo'))

class InProgress(MethodView):
    def get(self):
        project_id = str(request.args["project_id"])
        return jsonify({"todo": kanban_manager.get_inprogress_task(project_id)})
    def post(self):
        json_data = request.get_json(force=True)
        return jsonify({"message": kanban_manager.create_inprogress_task(json_data["project_id"], json_data["task_name"])})
app.add_url_rule('/inprogress', view_func = InProgress.as_view(name='inprogress'))

class Done(MethodView):
    def get(self):
        project_id = str(request.args["project_id"])
        return jsonify({"todo": kanban_manager.get_done_task(project_id)})
    def post(self):
        json_data = request.get_json(force=True)
        return jsonify({"message": kanban_manager.create_done_task(json_data["project_id"], json_data["task_name"])})
app.add_url_rule('/done', view_func = Done.as_view(name='done'))

class Task(MethodView):
    def put(self):
        json_data = request.get_json(force=True)
        return jsonify({"message": kanban_manager.change_task_status(json_data["project_id"], json_data["task_name"], json_data["new_status"])})
    def delete(self):
        project_id = str(request.args["project_id"])
        task_name = str(request.args["task_name"])
        return jsonify({"message": kanban_manager.delete_task(project_id, task_name)})
app.add_url_rule('/task', view_func = Task.as_view(name='task'))

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = 8383)