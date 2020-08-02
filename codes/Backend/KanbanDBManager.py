import pymysql
import logging

class KanbanDBManager:
    def __init__(self, db_config: dict):
        self.db_connection = pymysql.connect(host = db_config["host"], 
                                             port = db_config["port"], 
                                             user = db_config["user"], 
                                             password = db_config["password"], 
                                             database = db_config["database"])
        self.cursor = self.db_connection.cursor()
        self.name = "KanbanDBManager-"+ db_config["user"] + "-" + db_config["host"] + "-" + db_config["database"]
        print(self.name)
        logging.basicConfig(filename = self.name + ".log")
        self.logger = logging.getLogger()
        print("Log File:", self.name + ".log")
    
    def __del__(self):
        self.db_connection.commit()
        self.db_connection.close()
        
    def sign_up_project(self, project_id: str, password: str):
        try:
            self.cursor.execute("insert into register (project_id, password) values ('%s', '%s')" % (project_id, password))
            self.db_connection.commit()
            return True
        except Exception as e:
            self.logger.error("error in sign_up_project: " + str(e))
            return False
        
    def sign_in_project(self, project_id: str, password: str):
        try:
            self.cursor.execute("select count(*) from register where project_id = '%s' and password = '%s'" % (project_id, password))
            result = self.cursor.fetchall()[0][0]
            return True if result else False
        except Exception as e:
            self.logger.error("error in sign_in_project: " + str(e))
            return False
    
    def get_todo_task(self, project_id: str):
        try:
            self.cursor.execute("select task_name from task where project_id = '%s' and status = 1" % (project_id))
            result = [item[0] for item in self.cursor.fetchall()]
            return result
        except Exception as e:
            self.logger.error("error in get_todo_task: " + str(e))
            return []
            
    def get_inprogress_task(self, project_id: str):
        try:
            self.cursor.execute("select task_name from task where project_id = '%s' and status = 2" % (project_id))
            result = [item[0] for item in self.cursor.fetchall()]
            return result
        except Exception as e:
            self.logger.error("error in get_inprogress_task: " + str(e))
            return []
            
    def get_done_task(self, project_id: str):
        try:
            self.cursor.execute("select task_name from task where project_id = '%s' and status = 3" % (project_id))
            result = [item[0] for item in self.cursor.fetchall()]
            return result
        except Exception as e:
            self.logger.error("error in get_done_task: " + str(e))
            return []
    
    def create_todo_task(self, project_id: str, task_name: str):
        try:
            self.cursor.execute("insert into task (project_id, task_name, status) values ('%s', '%s', 1)" % (project_id, task_name))
            self.db_connection.commit()
            return True
        except Exception as e:
            self.logger.error("error in create_todo_task: " + str(e))
            return False
    
    def create_inprogress_task(self, project_id: str, task_name: str):
        try:
            self.cursor.execute("insert into task (project_id, task_name, status) values ('%s', '%s', 2)" % (project_id, task_name))
            self.db_connection.commit()
            return True
        except Exception as e:
            self.logger.error("error in create_inprogress_task: " + str(e))
            return False
    
    def create_done_task(self, project_id: str, task_name: str):
        try:
            self.cursor.execute("insert into task (project_id, task_name, status) values ('%s', '%s', 3)" % (project_id, task_name))
            self.db_connection.commit()
            return True
        except Exception as e:
            self.logger.error("error in create_done_task: " + str(e))
            return False
    
    def change_task_status(self, project_id: str, task_name: str, new_status: int):
        try:
            self.cursor.execute("update task set status = %s where project_id = '%s' and task_name = '%s'" % (str(new_status), project_id, task_name))
            self.db_connection.commit()
            return True
        except Exception as e:
            self.logger.error("error in change_task_status: " + str(e))
            return False
    
    def delete_task(self, project_id: str, task_name: str):
        try:
            self.cursor.execute("delete from task where project_id = '%s' and task_name = '%s'" % (project_id, task_name))
            self.db_connection.commit()
            return True
        except Exception as e:
            self.logger.error("error in delete_task: " + str(e))
            return False
    

    