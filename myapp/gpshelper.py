from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock

class GpsHelper():
    has_centered_map=False
    def run(self):
        #print(App.get_running_app().root.ids.mapview)
        print(dir(App.get_running_app().root.ids))
        print(App.get_running_app().root.screens)
        for screen in App.get_running_app().root.screens:
            print(screen)
            if screen.name=="main":
                gps_blinker=screen.ids.mapview.ids.blinker
        Clock.schedule_once(gps_blinker.blink,2)
        #if platform=='android':
        #    from android.permissions import Permission, request_permission
        #    def callback(permissions,results):
        #        if all([res for res in results]):
        #            print("Got all permissions")
        #        else:
        #            print("did not get all permissions")
        #    request_permission([Permission.ACCESS_COARSE_LOCATION,Permission.ACCESS_FINE_LOCATION],callback)
        #request permisions
        #configure gps
        if platform=='android' or platform =='ios':
            from plyer import gps
            gps.configure(on_location=self.update_blinker_position,
                          on_status=self.on_auth_status)
            gps.start(minTime=1000, minDistance=0)
    def update_blinker_position(self,*args,**kwargs):
        my_lat=kwargs['lat']
        my_lon= kwargs['lon']
        my_lat=30.0
        my_lon=30.0
        print("GPS POSITION",my_lat,my_lon)  
        #update gpsblinker possition
        for screen in App.get_running_app().root.screens:
            print(screen)
            if screen.name=="main":
                gps_blinker=screen.ids.mapview.ids.blinker
                mapa=screen.ids.mapview
        if not self.has_centered_map:
            mapa.center_on(my_lat,my_lon)
            self.has_centered_map=True
        gps_blinker.lat=my_lat
        gps_blinker.lon=my_lon
    def on_auth_status(self,general_status,status_message):
        if general_status=='provider-enabled':
            pass
        else:
            self.open_gps_acces_popup()
    
    def open_gps_acces_popup(self):
        dialog=MDDialog(title="GPS ERROR", text="You need to enable gps acces for app to function properly")
        dialog.size_hint=[0.8,0.8]
        dialog.pos_hint={'center_x':.5, 'center_y':0.5}
        dialog.open()