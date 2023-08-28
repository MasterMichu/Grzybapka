from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy_garden.mapview import MapMarker, MapView

Builder.load_string("""
<Mushroom_Marker>:
    source: 'kivymd/images/transparent.png'
    canvas:
        Color:
            rgba: 1, 0, 0, root.opacity
        Ellipse:
            pos: self.center_x - 5, self.center_y - 5
            size: 20, 20
""")
Builder.load_string("""
<Invisible_marker>:
    source: 'kivymd/images/transparent.png'
    canvas:
        Color:
            rgba: 1, 0, 0, root.opacity
        Ellipse:
            pos: self.center_x - 5, self.center_y - 5
            size: 20, 20
""")

class Invisible_marker(MapMarker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.opacity = 0

class Mushroom_Marker(MapMarker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.opacity = 0.5

class MushroomMapview(MapView):
    getting_points_timer = None
    mushrooms_points_id = []
    mappoints_values = []
    labels_added = []
    markers_added = []
    trans_markers_added=[]
    zoomvalue = 10

    def start_getting_points_in_fov(self, zoomvalue):
        try:
            self.getting_points_timer.cancel()
        except:
            pass
        self.clear_labels()
        self.zoomvalue = zoomvalue
        self.getting_points_timer = Clock.schedule_once(self.get_points_in_fov, 1)

    def clear_labels(self):
        for label in self.labels_added:
            self.remove_widget(label)
        self.labels_added = []
        for trans_marker in self.trans_markers_added:
            self.remove_marker(trans_marker)
        self.trans_markers_added=[]
    def clear_points(self):
        for point in self.markers_added:
            self.remove_marker(point)
        self.markers_added=[]

    def get_points_in_fov(self, *args):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        self.mappoints_values = []
        app = App.get_running_app()
        #print(self.zoomvalue)
        sql_extra_filter=app.filterconfig
        if self.zoomvalue > 12:
            sql_statement = "SELECT * FROM mushrooms WHERE x>%s AND x<%s AND y>%s AND y<%s%s" % (
                min_lon, max_lon, min_lat, max_lat,sql_extra_filter)
            fetching = app.cur.execute(sql_statement)
            points = app.cur.fetchall()
            for mushroom in points:
                id = mushroom[0]
                if id in self.mushrooms_points_id:
                    continue
                else:
                    self.add_mushroom(mushroom)
        elif self.zoomvalue>6:
            self.clear_points()
            self.place_numeric_values()
            

    def place_numeric_values(self):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        segments_on_map = 15
        boxsize_lat = (max_lat - min_lat) / segments_on_map
        boxsize_lon = (max_lon - min_lon) / segments_on_map
        app = App.get_running_app()
        sql_extra_filter=app.filterconfig
        for i in range(0, segments_on_map):
            x_min = i * boxsize_lon + min_lon
            x_max = (i + 1) * boxsize_lon + min_lon
            x_pos = x_min + boxsize_lon / 2
            for j in range(0, segments_on_map):
                y_min = j * boxsize_lat + min_lat
                y_max = (j + 1) * boxsize_lat + min_lat
                y_pos = y_min + boxsize_lat / 2
                sql_statement = "SELECT COUNT(*) FROM mushrooms WHERE x>%s AND x<%s AND y>%s AND y<%s%s " % (
                    x_min, x_max, y_min, y_max,sql_extra_filter)
                app.cur.execute(sql_statement)
                points = app.cur.fetchall()
                if points[0][0] > 0:
                    self.mappoints_values.append((y_pos, x_pos, points[0][0]))
        self.place_numbers_on_map()

    def place_numbers_on_map(self):
        for mappointvalue in self.mappoints_values:
            marker = Invisible_marker(lat=mappointvalue[0], lon=mappointvalue[1], opacity=0)
            self.add_widget(marker)
            self.trans_markers_added.append(marker)
            label = Label(text=str(mappointvalue[2]), pos=marker.pos, font_size='20', color=(0, 0, 0, 1), size_hint=(None, None))
            self.add_widget(label)
            self.labels_added.append(label)

    def add_mushroom(self, mushroom):
        lat, lon = mushroom[8], mushroom[7]
        marker = Mushroom_Marker(lat=lat, lon=lon)
        self.add_widget(marker)
        id = mushroom[0]
        self.mushrooms_points_id.append(id)
        self.markers_added.append(marker)

class MyMapApp(App):
    def build(self):
        return MushroomMapview()

if __name__ == '__main__':
    MyMapApp().run()