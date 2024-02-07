import tkinter as tk

from webscrapper import Scrapper
from imagecreator import ImageCreator
from window_application import Application

APP_VERSION = '1.1.0'
web = Scrapper('https://rds2.northsouth.edu/index.php/common/showofferedcourses')
imgcreator = ImageCreator()


def main():
	course_data = web.find_all_course()

	root = tk.Tk()
	root.title(f'NSU Routine Maker {APP_VERSION}')
	app = Application(course_data,imgcreator,master=root)
	app.mainloop()

if __name__ == '__main__':
	main()