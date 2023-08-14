from kivy_garden.mapview import MapMarker
from kivy.graphics import Color, Ellipse

class Mushroom_Marker(MapMarker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas:
            Color(1, 0, 0, 0.5)  # Red color with opacity 0.5
            self.marker = Ellipse(pos=self.pos, size=(20, 20))  # Adjust the size as needed

    def on_pos(self, instance, value):
        self.marker.pos = value

    def on_size(self, instance, value):
        self.marker.size = value