from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0 / 255, 0 / 255, 0 / 255, 1) #Set the Color of the Background (Optional)


class FirstApp(App): # Initiate MyApp Class and Inherit from App Class(inbuilt)
    def build(self):

        text1 = Label(text="Hello World",
                      font_size=60,
                      italic=True,
                      color=(0, 0, 0, 1),
                      bold=True
                      )

        button1 = Button(text="exit",
                         color=(1, 1, 1,1),
                         size_hint=(0.5,0.2),
                         font_size=30,
                         pos_hint= {'center_x':0.5,'center_y':0.5} #Center of the Screen

                         )
        return button1

    pass


FirstApp().run() #run app
