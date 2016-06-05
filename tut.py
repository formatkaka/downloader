from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.properties import StringProperty

import time

class MainLay(Screen):
	def search_movie(self):
		print "hello"
		movie_name = self.ids.movie_name.text
		# time.sleep(10)
		self.manager.current = 'search'
		
		try:
			download(movie_name)
		except Exception as e:
			error = str(e)
			self.manager.current = 'error'

	def show_tv(self,*args):
		pass

def download(movie_name):
	pass
	# raise ValueError("Errorrrrr")

class SearchMovie(Screen):
	pass

class ErrorScreen(Screen):
	error = StringProperty()
	def error_report(self):
		self.error = "Errrrooooorrrr"

class DwnldApp(App):
	def build(self):
		sm = ScreenManager(transition=FadeTransition())
		sm.add_widget(MainLay(name='main'))
		sm.add_widget(SearchMovie(name='search'))
		sm.add_widget(ErrorScreen(name='error'))
		return sm

if __name__ == '__main__':
	DwnldApp().run()