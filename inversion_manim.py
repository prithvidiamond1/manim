
from manimlib.imports import *


class inversion(Scene):
    def construct(self):
        circle1 = Circle(color=BLUE_C, radius=2.0)
        circle2 = Circle(color=YELLOW_C, radius=1.0, arc_center=(ORIGIN+RIGHT))
        point1 = Dot(point=(ORIGIN+(2*RIGHT)), color=PINK)

        self.add(circle1)
        self.add(circle2)
        self.add(point1)
        self.wait()
