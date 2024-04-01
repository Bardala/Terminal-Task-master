from datetime import datetime

class Todo:
  def __init__(self, id, task, status):
    self.id = id
    self.task = task
    self.status = status
    self.createdAt = datetime.now()
    
  def update_task(self, task):
    self.task = task
    return self.task
  
  def update_status(self, status):
    self.status = status
    return self.status

    