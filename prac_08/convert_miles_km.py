from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Kivy app to convert miles to kilometers."""
    output_km = StringProperty()

    def build(self):
        """Load the .kv layout and initialize the output."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_km = "0.0"
        return self.root

    def handle_calculate(self):
        """Update output based on current input."""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.output_km = str(result)

    def handle_increment(self, change):
        """Adjust input by change amount and recalculate."""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Return float value from input, or 0.0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
