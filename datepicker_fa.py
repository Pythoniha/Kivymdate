from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import CircularRippleBehavior
from kivymd.uix.dialog import BaseDialog
from pcalender import arabic_reshaper
from bidi import algorithm
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty , NumericProperty , ListProperty
from persiantools.jdatetime import JalaliDate
import bidi.algorithm
import arabic_reshaper
from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles

Builder.load_string(
'''
<MDLabeldayweek@MDLabel>
    font_style:'Caption'
    theme_text_color: 'Hint'
    font_name: 'sahel.ttf'
    halign: 'center'

<DayButton>:
    size_hint: None,None
    size:  
        (dp(42),dp(42))\
        if app.theme_cls.device_orientation == 'portrait'\
        else (dp(47),dp(42))

    on_release: 
        root.select_day(day_text.text)

    canvas.before:
        Color:
            rgba: root.day_color
        Ellipse:
            size: root.size 
            pos: self.pos

    MDLabel:
        id: day_text
        text: root.text
        font_name: 'sahel.ttf'
        font_style:'Caption'    
        theme_text_color: 'Primary'
        halign: 'center'
        valign: 'middle'
        pos_hint: {'center_x': .5 , 'center_y': .5}

<DatePickerFa>:
    id: date_picker
    font_name: 'sahel.ttf'
    size_hint: None,None
    size: 
        (dp(302), dp(450))\
        if app.theme_cls.device_orientation == 'portrait'\
        else (dp(450) , dp(340))

    BoxLayout:
        orientation: 
            'vertical'\
            if app.theme_cls.device_orientation == 'portrait'\
            else 'horizontal'

        canvas.before:
            Color:
                rgba: app.theme_cls.bg_normal
            RoundedRectangle:
                size: self.size 
                pos: self.pos    

        BoxLayout:
            orientation:
                'horizontal'\
                if app.theme_cls.device_orientation == 'portrait'\
                else 'vertical'

            size_hint_y: 
                None\
                if app.theme_cls.device_orientation == 'portrait'\
                else 1

            size_hint_x: 
                1\
                if app.theme_cls.device_orientation == 'portrait'\
                else None

            height: 
                dp(90)\
                if app.theme_cls.device_orientation == 'portrait'\
                else root.height

            width: 
                root.width\
                if app.theme_cls.device_orientation == 'portrait'\
                else dp(110)

            canvas.before:
                Color:
                    rgba: app.theme_cls.primary_color
                RoundedRectangle:
                    size: self.size 
                    pos: self.pos 
                    radius:
                        [(10.0, 10.0), (10.0, 10.0), (0, 0), (0, 0)]\
                        if app.theme_cls.device_orientation == 'portrait'\
                        else [(10,10),(0,0),(0,0),(10,10)]


            FloatLayout:
                size_hint_x: 
                    0.15\
                    if app.theme_cls.device_orientation == 'portrait'\
                    else 1

                MDIconButton:
                    pos_hint: {'center_x': .5 , 'center_y': .5}
                    icon:'chevron-left'
                    theme_text_color: 'Custom'
                    text_color: 1,1,1,1                    
                    on_release: root.add_month()
            
            BoxLayout:
                orientation:'vertical'
                font_name: 'sahel.ttf'
                size_hint_x: 
                    .7\
                    if app.theme_cls.device_orientation == 'portrait'\
                    else 1

                padding: dp(5)
                spacing: dp(1)
                MDLabel:
                    id: month_name
                    font_style: "JetBrainsMono"
                    text: ''
                    text_size : "25"
                    font_name: "sahel.ttf"
                    halign: 
                        'center'\
                        if app.theme_cls.device_orientation == 'portrait'\
                        else 'center'

                    theme_text_color: 'Custom'
                    font_name: 'sahel.ttf'
                    text_color: 1,1,1,1
                    font_style:'Caption'
                MDSeparator:
                    color: app.theme_cls.bg_normal
                MDLabel:    
                    id: year_name      
                    font_name: 'sahel.ttf'        
                    text: ''
                    halign: 
                        'right'\
                        if app.theme_cls.device_orientation == 'portrait'\
                        else 'center'
                        
                    theme_text_color: 'Custom'
                    text_color: 1,1,1,1
                    font_style:'H6'


            FloatLayout:
                size_hint_x: 
                    0.15\
                    if app.theme_cls.device_orientation == 'portrait'\
                    else 1
                    
                MDIconButton:
                    pos_hint: {'center_x': .5 , 'center_y': .5}
                    icon:'chevron-right'
                    theme_text_color: 'Custom'
                    text_color: 1,1,1,1                    
                    on_release : root.sub_month()
            
        BoxLayout:
            orientation: 'vertical'  
            font_name: 'sahel.ttf'           
            BoxLayout:
                size_hint_y: None
                font_name: 'sahel.ttf'
                height: dp(40)
                canvas.before:
                    Color:
                        rgba: app.theme_cls.bg_dark
                    RoundedRectangle:
                        size: self.size 
                        pos: self.pos 
                        radius:
                            [(0,0) , (0,0) , (0,0) , (0,0)]\
                            if app.theme_cls.device_orientation == 'portrait'\
                            else [(0,0) , (10,10) , (0,0) , (0,0)]

                MDLabeldayweek:
                    font_name: 'sahel.ttf'
                    text: root.reshaper('??')
                MDLabeldayweek:
                    font_name: 'sahel.ttf'
                    text: root.reshaper('??')
                MDLabeldayweek:
                    font_name: 'sahel.ttf'
                    text: root.reshaper('??')
                MDLabeldayweek:
                    font_name: 'sahel.ttf'
                    text: root.reshaper('??')
                MDLabeldayweek:
                    font_name: 'sahel.ttf'
                    text: root.reshaper('??')
                MDLabeldayweek:
                    font_name: 'sahel.ttf'
                    text: root.reshaper('??')
                MDLabeldayweek:
                    font_name: 'sahel.ttf'
                    text: root.reshaper('??')                                                                                                                       

            GridLayout:
                id: days_col
                spacing: dp(1)
                cols: 7
            
            BoxLayout:
                canvas.before:
                    Color:
                        rgba: app.theme_cls.bg_dark
                    RoundedRectangle:
                        size: self.size 
                        pos: self.pos
                        radius: [(0.0, 10.0), (0.0, 10.0), (10, 10), (10, 10)]            
                size_hint_y: None
                height: dp(40)
                padding: [dp(10) , 0]
                spacing: dp(10)
                MDFlatButton:
                    font_name: 'sahel.ttf'
                    text: root.reshaper('??????')
                    pos_hint: {'center_x': .5 , 'center_y': .5}
                    on_release: root.cancel()
                MDFlatButton:
                    font_name: 'sahel.ttf'
                    text: root.reshaper('????????????')
                    pos_hint: {'center_x': .5 , 'center_y': .5}
                    on_release: root.choose()
'''
)                    

class DatePickerFa(BaseDialog):
    month_sel = None
    year_sel = None
    day_sel = None     

    def reshaper(self, name):
        name = arabic_reshaper.reshape(name)
        name = algorithm.get_display(name)
        name = str(name)
        return name

    def __init__(self,callback=None,**kwargs):
        super(DatePickerFa,self).__init__(**kwargs)
        self.callback = callback
        def farsi_saz(self):
            reshaped_text = arabic_reshaper.reshape(self)
            fa_text = bidi.algorithm.get_display(reshaped_text)
            return fa_text
        self.month_names={
            '1': self.reshaper('??????????????'),
            '2': self.reshaper('????????????????'),
            '3': self.reshaper('??????????'),
            '4': self.reshaper('??????'),
            '5': self.reshaper('??????????'),
            '6': self.reshaper('????????????'),
            '7': self.reshaper('??????'),
            '8': farsi_saz('????????'),
            '9': self.reshaper('??????'),
            '10': self.reshaper('????'),
            '11': self.reshaper('????????'),
            '12': self.reshaper('??????????'),
        }
        self.day_names={
            '1': self.reshaper('????????'), 
            '2': self.reshaper('????????????'),  
            '3': self.reshaper('????????????'),     
            '4': self.reshaper('???? ????????'),   
            '5': self.reshaper('????????????????'),
            '6': self.reshaper('??????????????'),
            '7': self.reshaper('????????'),
                         
        }

    def on_open(self):
        self.day_sel=JalaliDate.today().day
        self.month_sel = JalaliDate.today().month
        print(self.month_sel)
        self.year_sel = JalaliDate.today().year
        self.render_dates(self.day_sel, self.month_sel, self.year_sel  )

    def cancel(self):
        self.dismiss()
    
    def choose(self):
        if not self.callback:
            return
        self.callback('%d/%d/%d'%(self.year_sel,self.month_sel,self.day_sel) )
        return self.dismiss()

    def render_dates(self,day,month,year):
        if not day:
            day = JalaliDate.today().day
            self.day_sel = day
        if not month:
            month = JalaliDate.today().month
            self.month_sel = month
        if not year:
            year = JalaliDate.today().year
            self.year_sel = year

        if 1<=month<=6:
            days = 31
        elif 7<=month<=11:
            days = 30
        elif month==12:
            days=29

        day_of_week = JalaliDate(self.year_sel , self.month_sel , 1).weekday()

        self.ids.days_col.clear_widgets()
        for x in range(day_of_week):
            self.ids.days_col.add_widget(DayButton(text='',disabled=True))

        for x in range(1,days+1):
            if x == JalaliDate.today().day and self.month_sel==JalaliDate.today().month and self.year_sel==JalaliDate.today().year :
                self.ids.days_col.add_widget(DayButton(text='%d'%x , day_color=self.theme_cls.primary_color))
            else:
                self.ids.days_col.add_widget(DayButton(text='%d'%x ))
        self.ids.month_name.text = self.month_names['%d'%self.month_sel]
        self.ids.year_name.text = '%d'%self.year_sel
    
    def add_month(self):
        if self.month_sel==12:
            self.month_sel = 1
            self.year_sel +=1
        else:
            self.month_sel += 1
        self.render_dates(self.day_sel,self.month_sel , self.year_sel)

    def sub_month(self):
        if self.month_sel==1:
            self.month_sel = 12
            self.year_sel -=1
        else:
            self.month_sel -= 1
        self.render_dates(self.day_sel,self.month_sel , self.year_sel)

class DayButton(CircularRippleBehavior,ButtonBehavior,BoxLayout):
    text= StringProperty()
    day_color =ListProperty([1,1,1,0])
    
    def __init__(self,day_color=[1,1,1,0], **kwargs):
        super(DayButton,self).__init__(**kwargs)
        self.day_color = day_color

    def select_day(self,day):
        for x in self.parent.children:
            if x.day_color == MDApp.get_running_app().theme_cls.primary_color or x.day_color == [1,0,0,1]:
                continue 
            else:
                x.day_color = [1,1,1,0]

        if self.day_color!= MDApp.get_running_app().theme_cls.primary_color and self.day_color!=[1,0,0,1]:
            self.day_color= MDApp.get_running_app().theme_cls.bg_darkest
        
        self.parent.parent.parent.parent.day_sel =int(day)

        month = self.parent.parent.parent.parent.ids.month_name.text 
        month = month.split()[0]
        print(month)
        self.parent.parent.parent.parent.ids.month_name.text = month+' '+day 
