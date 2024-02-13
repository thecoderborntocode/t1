from manim import *
import math
class StickFigure(Scene):
    def construct(self):
        rec = Rectangle()
        star = Star()

        self.play(Create(rec))
        self.play(Create(star))
        flip = 0
        for i in range(0,11):
            if(flip%2==0):
                self.play(rec.animate.shift(UP))
                self.play(star.animate.rotate(30*i * math.pi / 180))  # Convert degrees to radians

            else:
                self.play(rec.animate.shift(DOWN))
                self.play(star.animate.rotate(30*i * math.pi / 180))  # Convert degrees to radians

            flip = flip+1

