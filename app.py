from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.clock import Clock
import cv2
from numpy import size
import webbrowser

class Qrcodedetector(MDApp):

    def build(self):
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='Yellow'
        layout=MDBoxLayout(orientation='vertical')
        self.image=Image()
        layout.add_widget(self.image)
        self.save_img_button=(MDFillRoundFlatButton(text="Detect URL",pos_hint={'center_x':0.5,'center_y':0.3},size_hint=(None,None)))
        self.save_img_button.bind(on_press=self.take_picture)
        layout.add_widget(self.save_img_button)
        self.capture=cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        Clock.schedule_interval(self.load_video,1.0/30.0)
        return layout
    def load_video(self,*args):
        ret,frame=self.capture.read()
        self.image_frame=frame
        data, bbox, _ = self.detector.detectAndDecode(self.image_frame)
        self.data=data
        buffer=cv2.flip(frame,0).tostring()
        texture=Texture.create(size=(frame.shape[1],frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture
    def take_picture(self, *args):
       self.b=webbrowser.open(str(self.data))

if __name__ == '__main__':
    Qrcodedetector().run()