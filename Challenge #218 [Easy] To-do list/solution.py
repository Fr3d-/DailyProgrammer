#!/usr/bin/python3.4

class ToDoList:
	def __init__(self):
		self.list = []

	def addItem(self, task):
		self.list.append(task)

	def deleteItem(self, task):
		self.list.remove(task)

	def viewList(self):
		print("\n".join(self.list))

MyTodoList = ToDoList()

MyTodoList.addItem('Take a shower');
MyTodoList.addItem('Go to work');
MyTodoList.viewList();

# OUTPUT:
#
# Take a shower
# Go to work
