#!/usr/bin/python3.4

class ToDoList:
	def __init__(self):
		self.list = []
		self.categories = []

	def addItem(self, task, *cat):
		self.list.append(task)
		self.categories.append(cat)

	def deleteItem(self, task):
		index = self.list.index(task)
		self.list.remove(task)
		self.categories.pop(index)


	def viewList(self, *catinput):
		if catinput:
			print("----" + " & ".join(catinput).upper() + "----")
			for j, cat in enumerate(self.categories):
				if cat == catinput:
					print(self.list[j])

			return

		differentCats = tuple(set(self.categories))

		for i in range(len(differentCats)):
			print("----" + " & ".join(differentCats[i]).upper() + "----")
			for j, cat in enumerate(self.categories):
				if cat == differentCats[i]:
					print(self.list[j])



	def updateItem(self, oldtask, newtask):
		self.list[self.list.index(oldtask)] = newtask

t = ToDoList()

t.addItem("Go to work", "work")
t.addItem("Take a bath before work", "work", "important")
t.addItem("Figure out how to jump", "school")
t.addItem("Do that assignment", "school")
t.addItem("Buy gift for girlfriend", "other")
t.viewList()

# OUTPUT:
#
# ----OTHER----
# Buy gift for girlfriend
# ----WORK----
# Go to work
# ----WORK & IMPORTANT----
# Take a bath before work
# ----SCHOOL----
# Figure out how to jump
# Do that assignment
