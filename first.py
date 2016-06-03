from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MainLay(App):
	def build(self):
		g = GridLayout(cols=2, rows=2)
		l1 = Button(text="Friends")
		l2 = Button(text="Silicon Valley")
		l3 = Button(text="Big Bang Theory")
		l4 = Button(text="Flash")
		g.add_widget(l1)
		g.add_widget(l2)
		g.add_widget(l3)
		g.add_widget(l4)
		# b.add_widget(l)
		return g

# class MainApp(App):
# 	def build(self):
# 		return MainLay()

if __name__ == '__main__':
	MainLay().run()
