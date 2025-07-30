from datetime import *
class Project:
    def __init__(self,name,startDate,EndDate):
        self.name=name
        self.startDate=startDate
        self.EndDate=EndDate
        self.tasks=[]
    def addTask(self,task):
        self.tasks.append(task)
        
class Task:
    def __init__(self,name,taskId,duration):
        self.name=name
        self.taskId=taskId
        self.duration=duration
        self.resources=[]
    def addResource(self,resource):
        self.resources.append(resource)
    
class Resource:
    def __init__(self,name,empid,skill):
        self.name=name
        self.empid=empid
        self.skill=skill

project=Project('Gen AI',date(2021,9,2),date(2022,9,2))
task=Task("Creating a Bot",100,90)
resource=Resource("Arthika","A202","Python")
task.addResource(resource)
project.addTask(task)

print(f"Project: {project.name}")
for t in project.tasks:
    print(f" Task: {t.name}, Duration: {t.duration}")
    for r in t.resources:
        print(f"  Resource: {r.name}, Skill: {r.skill}")
