
# for creating views directly from the jupyter notebook 
# https://notebooks.gesis.org/binder/jupyter/user/manimcommunity-jupyter_examples-306evc63/notebooks/First%20Steps%20with%20Manim.ipynb
# for the documentation 
# https://docs.manim.community/en/stable/installation.html
from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))