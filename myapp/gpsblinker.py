from kivy.app import App
from kivy_garden.mapview import MapMarker
from kivy.animation import Animation
from kivy.utils import platform
class GpsBlinker(MapMarker):
    def blink(self,*args):
        anim=Animation(outer_opacity=0, blink_size=50)
        anim.bind(on_complete=self.reset)
        anim.start(self)
        if not App.get_running_app().ALLPERMS_GRANTED:
            if not App.get_running_app().FirstLoop:
                print("this is")
                print(App.get_running_app().FirstLoop)
                print("first loop")
                from kivy import platform
                print(platform)
                if platform == "android":
                    from android.permissions import request_permissions, Permission, request_permission
                    #request_permission(Permission.READ_PHONE_STATE)
                    print("requesting_my_permissions")
                    request_permissions([Permission.ACCESS_COARSE_LOCATION,Permission.ACCESS_FINE_LOCATION,Permission.READ_PHONE_STATE],self.callback)
        App.get_running_app().FirstLoop=False


    def reset(self, *args):
        self.outer_opacity=1
        self.blink_size=self.default_blink_size
        self.blink()
    def callback(self,permissions,results):
                if all([res for res in results]):
                    print(results)
                    print("Got all permissions")
                    App.get_running_app().ALLPERMS_GRANTED=True
                else:
                    print("did not get all permissions")
                    print(results)
                    print(dir(results))
