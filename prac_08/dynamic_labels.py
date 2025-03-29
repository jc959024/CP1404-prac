"""
CP1404/CP5632 Practical
Kivy GUI program that dynamically creates labels from a list of names.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main application class to create labels dynamically."""

    def __init__(self, **kwargs):
        """Initialize the app and the list of names."""
        super().__init__(**kwargs)
        self.names = None

    def build(self):
        """Build the GUI from the KV file and add dynamic labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.names = ["Alice", "Bob", "Charlie", "Diana"]
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create and add Label widgets dynamically for each name."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
