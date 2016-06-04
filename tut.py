from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MainLay(BoxLayout):
	def search_movie(self):
		return SearchMovie()

class SearchMovie(BoxLayout):
	pass

class DwnldApp(App):
	def build(self):
		return MainLay()

if __name__ == '__main__':
	DwnldApp().run()