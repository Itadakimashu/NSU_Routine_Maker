from PIL import Image, ImageDraw, ImageFont
from cell import Cell

class ImageCreator:

	def __init__(self):
		self.__table_data = [		    
		    ['Saturday','','','','','',''],
		    ['Sunday','','','','','',''],
		    ['Monday','','','','','',''],
		    ['Tuesday','','','','','',''],
		    ['Wednesday','','','','','',''],
		    ['Thursday','','','','','',''],
		]

		self.__cell_width = 172
		self.__cell_height = 75
		self.__font_size = 20
		self.__font = ImageFont.truetype("arial.ttf", self.__font_size)

	
	def __my_sort(self,s: str):
	    s = s.split("-")[0]

	    if "12:" in s:
	        s = s.replace("12:", "00:")

	    return int(s[0:2]) * 60 + int(s[3:5]) + ('pm' in s or 'PM' in s) * 720

	def __set_table(self,courses):
		dic = {
			'A': 0,
			'S': 1,
			'M': 2,
			'T': 3,
			'W': 4,
			'R': 5,
		}

		cells = [[] for i in range(7)]
		for course in courses.values():
			row = 0
			cell = Cell(course)
			for day in cell.days:
				row = dic[day]
				cells[row].append(cell)

		for i in range(len(cells)):
			cells[i].sort(key=lambda cell: self.__my_sort(cell.time))
		
		for row in range(len(self.__table_data)):
			for i in range(len(cells[row])):
				cell = cells[row][i]
				self.__table_data[row][i+1] = cell.cell_txt


	def create_image(self,courses):

		self.__set_table(courses);

		image_width = len(self.__table_data[0]) * self.__cell_width
		image_height = len(self.__table_data) * self.__cell_height


		image = Image.new("RGB", (image_width, image_height), "white")
		draw = ImageDraw.Draw(image)


		for i, row in enumerate(self.__table_data):
		    for j, cell in enumerate(row):
		        x = j * self.__cell_width
		        y = i * self.__cell_height
		        draw.rectangle([x, y, x + self.__cell_width, y + self.__cell_height], outline="black")
		        draw.text((x + 5, y + 5), cell, fill="black", font=self.__font)

		image.save("semester_routine.png")


