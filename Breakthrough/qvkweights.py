from manim import *
import random

class Weights(Scene):
    def construct(self):
        newSentence1 = Tex('He ', 'swung ', 'the ', 'baseball ', 'bat ').scale(1).copy().set_color_by_tex("He", ORANGE).set_color_by_tex("swung", RED).set_color_by_tex("the", YELLOW).set_color_by_tex("baseball", GREEN).set_color_by_tex("bat", BLUE)
        newSentence1.arrange(RIGHT, buff=1).shift(UP*3.5)

        rectangles = VGroup()

        matrices = VGroup()

        matrix = Matrix([[3, 9, 3, -3, 5], [9, 3, -2, 5, 3], ["...", "...", "...", "...", "..."], [10, 10, 8, 0, 4]]).next_to(newSentence1.get_center(), DOWN, 0.2).scale(0.58)
        matrix.set_column_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        keyMatrix = matrix.copy().shift(DOWN*2.25, LEFT*4)

        valueMatrix = matrix.copy().shift(DOWN*4.5, LEFT*4)

        qmultiplication = MathTex(r"\times \ W_q =").next_to(matrix, RIGHT, 1.3).scale(2).shift(LEFT*4)
        kmultiplication = MathTex(r"\times \ W_k =").next_to(keyMatrix, RIGHT, 1.3).scale(2)
        vmultiplication = MathTex(r"\times \ W_v =").next_to(valueMatrix, RIGHT, 1.3).scale(2)


        newQueryMatrix = Matrix([[1.4, 5.6, -3.6, 2.4, -5.1], [4.5, -2.9, 6.4, -0.5, 4.3], ["...", "...", "...", "...", "..."], [-8.1, 2.8, -4.4, 1.1, 4.9]]).next_to(matrix.get_center(), RIGHT, 0.85).scale(0.58)
        newQueryMatrix.set_column_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        newKeyMatrix = Matrix([[3.9, -5.8, 5.2, -1.4, -5.1], [-9.2, -1.9, -3.1, 6.7, 4.0], ["...", "...", "...", "...", "..."], [-2.1, 1.4, -3.6, 3.1, 6.1]]).next_to(keyMatrix.get_center(), RIGHT, 4.85).scale(0.58)
        newKeyMatrix.set_column_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        newValueMatrix = Matrix([[3.2, -1.6, -4.9, 2.1, 3.1], [-4.1, -3.2, 0.5, -2.1, 3.1], ["...", "...", "...", "...", "..."], [2.2, 5.3, 2.8, -0.1, 3.0]]).next_to(valueMatrix.get_center(), RIGHT, 4.85).scale(0.58)
        newValueMatrix.set_column_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        for i in range(0, 5):
            rectangles.add(Rectangle(width=(newSentence1[i].width+0.3), height=(newSentence1[i].height+0.3), color=newSentence1[i].color).move_to(newSentence1[i]))
            if i==0:
                matrices.add(MathTex(r"\begin{bmatrix}3 \\9 \\...\\10 \\\end{bmatrix}").next_to(newSentence1[i], DOWN, 0.5).scale(0.85).set_color(ORANGE))
            elif i==1:
                matrices.add(MathTex(r"\begin{bmatrix}9 \\3 \\...\\10 \\\end{bmatrix}").next_to(newSentence1[i], DOWN, 0.5).scale(0.85).set_color(RED))
            elif i==2:
                matrices.add(MathTex(r"\begin{bmatrix}3 \\-2 \\...\\8 \\\end{bmatrix}").next_to(newSentence1[i], DOWN, 0.5).scale(0.85).set_color(YELLOW))
            elif i==3:
                matrices.add(MathTex(r"\begin{bmatrix}-3 \\5 \\...\\0 \\\end{bmatrix}").next_to(newSentence1[i], DOWN, 0.5).scale(0.85).set_color(GREEN))
            else:
                matrices.add(MathTex(r"\begin{bmatrix}5 \\3 \\...\\4 \\\end{bmatrix}").next_to(newSentence1[i], DOWN, 0.5).scale(0.85).set_color(BLUE))

        self.add(newSentence1, rectangles, matrices)
        self.wait(duration=1.5)

        self.play(ReplacementTransform(matrices, matrix))
        self.wait(duration=0.5)
        self.play(matrix.animate.shift(LEFT*4), ReplacementTransform(matrix.copy(), keyMatrix), ReplacementTransform(matrix.copy(), valueMatrix))
        self.play(Write(qmultiplication), Write(kmultiplication), Write(vmultiplication))
        self.play(AnimationGroup(Create(newQueryMatrix), Create(newKeyMatrix), Create(newValueMatrix), run_time=0.75))
        self.wait(duration=0.25)
        self.play(AnimationGroup(Wiggle(newQueryMatrix, run_time=0.75, n_wiggles=2, scale_value=1.05, rotation_angle=0.01*TAU), rate_func=rate_functions.ease_out_sine))
        self.play(AnimationGroup(Wiggle(newKeyMatrix, run_time=0.75, n_wiggles=2, scale_value=1.05, rotation_angle=0.01*TAU), rate_func=rate_functions.ease_out_sine))
        self.play(AnimationGroup(Wiggle(newValueMatrix, run_time=0.75, n_wiggles=2, scale_value=1.05, rotation_angle=0.01*TAU), rate_func=rate_functions.ease_out_sine))
        self.wait()

        