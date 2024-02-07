import tkinter as tk

from webscrapper.webscrapper import Scrapper
from imagecreator.imagecreator import ImageCreator
from window_application import Application

web = Scrapper('https://rds2.northsouth.edu/index.php/common/showofferedcourses')
imgcreator = ImageCreator()


def main():
	course_data = web.find_all_course()

	root = tk.Tk()
	root.title('NSU Routine Maker 1.0')
	app = Application(course_data,imgcreator,master=root)
	app.mainloop()

if __name__ == '__main__':
	main()