import requests
from bs4 import BeautifulSoup

class Scrapper:
	def __init__(self,address):
		self.__address = address
		self.__req = requests.get(address)
		self.soup = BeautifulSoup(self.__req.content,'html.parser')
		self.table = self.soup.find('table',id='offeredCourseTbl')
		self.tbody = self.table.find('tbody')
		self.trs = self.tbody.find_all('tr')

	def get_link(self):
		return self.__address

	def find_all_course(self):
		courses = {}
		for tr in self.trs:
			tds = tr.find_all('td')

			course_initial = tds[1].text.strip()
			section = tds[2].text.strip()
			faculty = tds[3].text.strip()
			time = tds[4].text.strip()
			room = tds[5].text.strip()

			if '/' in course_initial:
				for course in course_initial.split('/'):
					courses[f'{course}.{section}'] = {
						'course': course,
						'section': section,
						'faculty': faculty,
						'time': time,
						'room': room,
					}

			else:
				course = f'{course_initial}.{section}'
				courses[course] = {
					'course': course_initial,
					'section': section,
					'faculty': faculty,
					'time': time,
					'room': room,
				}

		return courses
