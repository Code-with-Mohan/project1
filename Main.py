from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
#from kivy.label import Label

class DrawingApp(App):
    def build(self):
        # Create the drawing area
        self.drawing_area = DrawingArea()
       
        return self.drawing_area

class DrawingArea(Widget):
    def on_touch_down(self, touch):
        # Set the color based on touch pressure
        color = (1, 1, 1)  # White color
        with self.canvas:
            Color(*color)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        # Draw lines while moving
        touch.ud['line'].points += [touch.x, touch.y]



class DrawingApp(App):
    def build(self):
        # Create the drawing area
        self.drawing_area = DrawingArea()
        return self.drawing_area

     
if __name__ == '__main__':
    DrawingApp().run()
