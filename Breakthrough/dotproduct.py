from manim import *
import random

class QK(Scene):
    def construct(self):


        queryMatrix = Matrix([[1.4, 5.6, -3.6, 2.4, -5.1], [4.5, -2.9, 6.4, -0.5, 4.3], ["...", "...", "...", "...", "..."], [-8.1, 2.8, -4.4, 1.1, 4.9]]).scale(0.58).shift(UP*2.7)
        queryMatrix.set_column_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        # keyMatrix = Matrix([[3.9, -5.8, 5.2, -1.4, -5.1], [-9.2, -1.9, -3.1, 6.7, 4.0], ["...", "...", "...", "...", "..."], [-2.1, 1.4, -3.6, 3.1, 6.1]]).scale(0.58).next_to(queryMatrix, DOWN, 1)
        # keyMatrix.set_column_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        keyMatrixTransposed = Matrix([[3.9, -9.2, "...", -2.1 ], [-5.8, -1.9, "...", 1.4], [5.2, -3.1, "...", -3.6], [-1.4, 6.7, "...", 3.1], [-5.1, 4.0, "...", 6.1]]).scale(0.58).next_to(queryMatrix, DOWN, 0.5).shift(LEFT*4.75)
        keyMatrixTransposed.set_row_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        keyHe = MathTex(r"K_{he}")
        keySwung = MathTex(r"K_{swung}")
        keyThe = MathTex(r"K_{the}")
        keyBaseball = MathTex(r"K_{baseball}")
        keyBat = MathTex(r"K_{bat}")


        self.add(queryMatrix, keyMatrixTransposed, keyBaseball)

        self.wait()

        