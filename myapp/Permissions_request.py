from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
from plyer import gps



def Request_permissions_function():
    if platform=='android':  
            permissions_result=permissions_request_func
            return permissions_result
    else:
        return True
        

def callback(permissions,results):
                if all([res for res in results]):
                    return True
                else:
                    Clock.schedule_once(permissions_request_func,2)

def permissions_request_func(dt):
        from android import permissions
        from android.permissions import Permission, request_permissions
        return request_permissions([Permission.ACCESS_COARSE_LOCATION,Permission.ACCESS_FINE_LOCATION],callback)


