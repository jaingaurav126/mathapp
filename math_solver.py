from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy import *
from kivymd import *
from kivy.properties import ListProperty

Window.size=(350,600)

from kivy.properties import ListProperty
class SignButton(Button):
    bg_color=ListProperty([1,1,1,1])
class OptionButton(Button):
    bg_color=ListProperty([1,1,1,1])


class MathSolver(MDApp):

    selected_sign=""
    answer=""
    
    def build(self):
        global screen_manager
        screen_manager= ScreenManager(transition=NoTransition())
        screen_manager.add_widget(Builder.load_file("start.kv"))
        screen_manager.add_widget(Builder.load_file("select_sign.kv"))
        screen_manager.add_widget(Builder.load_file("quiz.kv"))
        #screen_manager.add_widget(Builder.load_file("final_score.kv"))
        return screen_manager
    def select_sign(self,sign):
        self.selected_sign=sign
        num1=random.randint(1,10)
        num2=random.randint(1,10)
        screen_manager.get_screen("quiz").ids.question.text=f"{num1} {sign} {num2}= ?"
        if sign=="+":
            self.answer=str(num1+num2)
        elif sign=="-":
             self.answer=str(num1-num2)
        elif sign=="*":
             self.answer=str(num1*num2)
        elif sign=="/":
             self.answer=str(num1/num2)

        while option_len<4:
            if sign=="+":
                option=str(random.randint(1,20))
            elif sign=="-":
                option=str(random.randint(-10,10))
            elif sign=="*":
                option=str(random.randint(1,20))
            elif sign=="/":
                option=str(random.randint(1,20))
            if option not in option_list:
                option_list.append(option)
            else:
                option_len=-1
            option_len+=1
            random.shuffle(option_list)
          

       
        screen_manager.current="quiz"


if __name__=='__main__':
    LabelBase.register(name="LuckiestGuy", fn_regular='regular.ttf')
    MathSolver().run()




