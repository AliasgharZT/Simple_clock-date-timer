
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.properties import ObjectProperty
import datetime
import time
from kivy.clock import Clock

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    timer=ObjectProperty()
    dates=ObjectProperty()
    clocks=ObjectProperty()
    sec=0
    min=0
    h=0

    def _reset(self):
        self.timer.text='00:00:00'
        self.sec=0
        self.min=0
        self.h=0
        self._stop()
    def _start(self,*args):
        self.sec+=1
        if self.sec==59:
            self.sec=0
            if self.min==59:
                self.min=0
                self.h+=1
            self.min+=1

        self.timer.text=str(self.h)+':'+str(self.min)+':'+str(self.sec)
    def active_start(self):
        Clock.schedule_interval(self._start,0.98) 
    def _stop(self):
        Clock.unschedule(self._start) 
    
    def _dates(self):
        self.dates.text=str(datetime.date.today())
    def _clocks(self,*args):
        q=time.localtime()
        qq=str(q.tm_hour)+':'+str(q.tm_min)+':'+str(q.tm_sec)
        self.clocks.text=qq
    def active_clock(self):
        Clock.schedule_interval(self._clocks,1)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'
        return Style()

MainApp().run()

