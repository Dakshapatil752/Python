# Multilevel Inheritance Example: Project -> Module -> Task

class Project:
	def __init__(self, project_id, project_name):
		self.project_id = project_id
		self.project_name = project_name
	def getProjectId(self):
		return self.project_id
	def getProjectName(self):
		return self.project_name

class Module(Project):
	def __init__(self, project_id, project_name, module_name):
		super().__init__(project_id, project_name)
		self.module_name = module_name
	def getModuleName(self):
		return self.module_name

class Task(Module):
	def __init__(self, project_id, project_name, module_name, task_name):
		super().__init__(project_id, project_name, module_name)
		self.task_name = task_name
	def getTaskName(self):
		return self.task_name

# Example usage
t = Task(101, "AI Project", "Vision Module", "Object Detection")
print("Project ID:", t.getProjectId())
print("Project Name:", t.getProjectName())
print("Module Name:", t.getModuleName())
print("Task Name:", t.getTaskName())
