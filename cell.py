class Cell:
	def __init__(self,course):
		self.course = f'{course['course']}.{course['section']}({course['faculty']})'
		self.days = course['time'].split(' ')[0]
		self.time = ''.join(course['time'][len(self.days)+1:].split())
		self.room = course['room']
		self.cell_txt = f'{self.course}\n{self.time}\n{self.room}'
