from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex('#0f172a')

class SpeedTestApp(App):
    def build(self):
        self.title = "Speed Test App v1.0"
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        title_label = Label(
            text="Project: Speed Build Test",
            font_size='26sp',
            bold=True,
            color=get_color_from_hex('#38bdf8'),
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title_label)
        
        self.number_input = TextInput(
            text="5",
            font_size='22sp',
            multiline=False,
            input_filter='int',
            background_color=get_color_from_hex('#1e293b'),
            foreground_color=get_color_from_hex('#f8fafc'),
            padding=[15, 15, 15, 15],
            size_hint_y=None,
            height=60
        )
        layout.add_widget(self.number_input)
        
        btn = Button(
            text="Multiply by 100",
            font_size='20sp',
            bold=True,
            background_normal='',
            background_color=get_color_from_hex('#10b981'),
            color=get_color_from_hex('#ffffff'),
            size_hint_y=None,
            height=60
        )
        btn.bind(on_press=self.calculate)
        layout.add_widget(btn)
        
        self.result_label = Label(
            text="Result will appear here",
            font_size='18sp',
            color=get_color_from_hex('#94a3b8')
        )
        layout.add_widget(self.result_label)
        
        return layout

    def calculate(self, instance):
        try:
            val = int(self.number_input.text)
            res = val * 100
            self.result_label.text = f"Calculation Done: {res}"
            self.result_label.color = get_color_from_hex('#f43f5e')
        except ValueError:
            self.result_label.text = "Please enter a valid number!"

if __name__ == '__main__':
    SpeedTestApp().run()
