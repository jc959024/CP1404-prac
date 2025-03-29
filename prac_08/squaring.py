from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Zhong Huayu'


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number"""

    def build(self):
        """Build the Kivy app from the kv file"""
        Window.size = (400, 300)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self):
        """Square the number and display it in the output label."""
        try:
            value = float(self.root.ids.input_number.text)
            result = value ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"

    def adjust_input_value(self, delta):
        """
        Adjust input value by a given delta (e.g. +1 or -1),
        update the input field and recalculate.
        """
        try:
            value = float(self.root.ids.input_number.text)
            value += delta
            self.root.ids.input_number.text = str(value)
            self.handle_calculate()
        except ValueError:
            pass

    def handle_up(self):
        """Increase the input number by 1."""
        self.adjust_input_value(1)

    def handle_down(self):
        """Decrease the input number by 1."""
        self.adjust_input_value(-1)


SquareNumberApp().run()
