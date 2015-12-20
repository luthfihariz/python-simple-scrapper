from bs4 import BeautifulSoup
from urllib2 import urlopen
import json

BASE_URL = "http://www.kompas.com/"

def get_editor_choices_link():
	soup = BeautifulSoup(urlopen(BASE_URL),"lxml")
	leftsidefix = soup.select_one("#leftsidefix")
	editor_choices = leftsidefix.select_one(".kcm-editor-choices")
	topics = editor_choices.find("ul").find_all("li")
	data = []
	for topic in topics:
		title = topic.select_one(".list-editor-choices").string
		url = topic.a["href"]
		data.append({"title":title,"url":url})
	return data;

if __name__ == '__main__':
	print json.dumps(get_editor_choices_link())