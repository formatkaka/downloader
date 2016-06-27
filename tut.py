from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout

from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

import time

from download import DownloadFile

class MainLay(Screen):

    layout_content = ObjectProperty(None)
    
    def search_movie(self):
        self.manager.current = 'search'

    def search_tv(self):
        print "hello"
        self.manager.current = 'tvseries'
        download(url)
    # def show_tv(self, *args):
    #     print args[0]




def download_vid(download_url):
    df = DownloadFile(download_url)
    df.download_file()
    # raise ValueError("Errorrrrr")


class SearchMovie(Screen):
    pass

class TvSeries(Screen):
    pass

class ErrorScreen(Screen):
    error = StringProperty()

    def error_report(self):
        self.error = "Errrrooooorrrr"


class Dwnld1App(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainLay(name='main'))
        sm.add_widget(SearchMovie(name='search'))
        sm.add_widget(ErrorScreen(name='error'))
        sm.add_widget(TvSeries(name='tvseries'))
        return sm

if __name__ == '__main__':
    Dwnld1App().run()
