from kivy_garden.mapview import MapMarker
from kivy.animation import Animation
class GpsBlinker(MapMarker):
    def blink(self,*args):
        anim=Animation(outer_opacity=0, blink_size=50)
        anim.bind(on_complete=self.reset)
        anim.start(self)
        pass


    def reset(self, *args):
        print("reset")
        self.outer_opacity=1
        self.blink_size=self.default_blink_size
        self.blink()