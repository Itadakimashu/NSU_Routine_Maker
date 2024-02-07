from PIL import Image, ImageDraw, ImageFont

class ImageCreator:

	def __init__(self):
		self.__table_data = [
		    ["","08:00am-09:15am", "09:25am-10:40am", "10:50am-12:05pm","12:15pm-01:30pm","01:40pm-02:55pm","03:05pm-04:20pm","04:30pm-05:45pm"],
		    ["Saturday", "", "", "", "", "", "", ""],
		    ["Sunday", "", "", "", "", "", "", ""],
		    ["Monday", "", "", "", "", "", "", ""],
		    ["Tuesday", "", "", "", "", "", "", ""],
		    ["Wednesday", "", "", "", "", "", "", ""],
		    ["Thursday", "", "", "", "", "", "", ""],
		    ["Friday", "", "", "", "", "", "", ""],
		]

		self.__cell_width = 168
		self.__cell_height = 75
		self.__font_size = 20
		self.__font = ImageFont.truetype("arial.ttf", self.__font_size)

	def __set_table(self,courses):
		dic = {
			'A': 1,
			'S': 2,
			'M': 3,
			'T': 4,
			'W': 5,
			'R': 6,
			'08:00 AM - 09:15 AM': 1,
			'09:25 AM - 10:40 AM': 2,
			'10:50 AM - 12:05 PM': 3,
			'12:15 PM - 01:30 PM': 4,
			'01:40 PM - 02:55 PM': 5,
			'03:05 PM - 04:20 PM': 6,
			'04:30 PM - 05:45 PM': 7,
		}
		for key,course in courses.items():
			cell = "{}\n{}\n{}".format(key,course['faculty'],course['room']) 
			row = 0
			col = 0
			days = course['time'].split(' ')[0]
			time = course['time'][len(days)+1:]
			for day in days:
				row = dic[day]
				col = dic[time]
				self.__table_data[row][col] = cell

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


