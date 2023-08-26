from kivy_garden.mapview import MapMarker
from kivy.uix.image import Image

class Mushroom_Marker(MapMarker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.opacity = 0.5  # Set the opacity for the marker

        self.image = Image(source='path_to_red_dot_image.png')  # Replace with the path to your red dot image
        self.image.size_hint = (None, None)
        self.image.size = (20, 20)  # Set the size of the red dot
        self.add_widget(self.image)

    def on_pos(self, instance, value):
        self.image.pos = value

    def on_opacity(self, instance, value):
        self.image.color = (1, 0, 0, value)  # Set the color with the desired opacity

    def on_size(self, instance, value):
        self.image.size = value