from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pickle
import warnings
warnings.filterwarnings("ignore",category=FutureWarning)
warnings.filterwarnings('ignore',category=UserWarning)

from matplotlib.pyplot import text


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="ML integration kivy "))
        self.value1 = TextInput(multiline=False)
        self.value2 = TextInput(multiline=False)
        self.value3 = TextInput(multiline=False)
        self.value4=TextInput(multiline=False)
        self.value5 = TextInput(multiline=False)
        self.inside.add_widget(self.value1)
        self.inside.add_widget(self.value2)
        self.inside.add_widget(self.value3)
        self.inside.add_widget(self.value4) 
        self.inside.add_widget(self.value5)
        self.add_widget(self.inside)
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        self.modelfile=pickle.load(open('model.pkl','rb'))
        self.pred =self.modelfile.predict([[self.value1.text,self.value2.text,self.value3.text,self.value4.text,self.value5.text]])
        self.add_widget(Label(text=str(self.pred)))
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()