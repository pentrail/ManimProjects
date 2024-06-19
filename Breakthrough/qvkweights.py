from manim import *
import random

class Weights(Scene):
    def construct(self):
        newSentence1 = Tex('He ', 'swung ', 'the ', 'baseball ', 'bat ').scale(1).copy().set_color_by_tex("He", ORANGE).set_color_by_tex("swung", RED).set_color_by_tex("the", YELLOW).set_color_by_tex("baseball", GREEN).set_color_by_tex("bat", BLUE)
        newSentence1.arrange(DOWN, buff=1, aligned_edge=RIGHT).shift(LEFT*5.6)

        rectangles = VGroup()

        matrices = Group()

        matrix = Matrix([[3.4, 9.2, "…", 10.7], [9.1, 3.6, "…", 8.8], [2.9, -2.1, "…", 9.4], [14.1, -3.7, "…", -2.3], [5.1, 3.2, "…", 4.0]]).next_to(newSentence1[0].get_center(), DOWN, 0.2).shift(RIGHT*2.65).scale(0.58)
        matrix.set_row_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        matrixBrackets = Matrix([[3.4, 9.2, "...", 10.7], [9.1, 3.6, "...", 8.8], [2.9, -2.1, "...", 9.4], [14.1, -3.7, "...", -2.3], [5.1, 3.2, "...", 4.0]]).next_to(newSentence1[0].get_center(), DOWN, 0.2).shift(RIGHT*2.65).scale(0.58)
        matrixBrackets.get_columns().set_opacity(0)
        keyMatrix = matrix.copy().shift(DOWN*0.5)

        valueMatrix = matrix.copy().shift(DOWN*3)

        qmultiplication = MathTex(r"\times \ W_q =").next_to(matrix, RIGHT, 1.3).scale(2).shift(UP*2)
        kmultiplication = MathTex(r"\times \ W_k =").next_to(keyMatrix, RIGHT, 1.3).scale(2)
        vmultiplication = MathTex(r"\times \ W_v =").next_to(valueMatrix, RIGHT, 1.3).scale(2)


        newQueryMatrix = Matrix([[3.9, -9.2, "...", -2.1], [-5.8, -1.9, "...", 1.4], [5.2, -3.1, "...", -3.6], [-1.4, 6.7, "...", 3.1], [-5.1, 4.0, "...", 6.1]]).next_to(matrix.get_center(), RIGHT, 4.65).shift(UP*2).scale(0.58)
        newQueryMatrix.set_row_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        newKeyMatrix = Matrix([[1.4, 4.5, "...", -8.1], [5.6, -2.9, "...", 2.8], [-3.6, 6.4, "...", -4.4], [2.4, -0.5, "...", 1.1], [-5.1, 4.3, "...", 4.9]]).next_to(keyMatrix.get_center(), RIGHT, 4.65).scale(0.58)
        newKeyMatrix.set_row_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        newValueMatrix = Matrix([[3.2, -1.6, "...", 3.1], [-4.1, -3.2, "...", 3.1], [2.2, 5.3, "...", 3.0], [-4.2, 5.3, "...", -9.2], [3.0, 8.8, "...", -0.2]]).next_to(valueMatrix.get_center(), RIGHT, 4.65).scale(0.58)
        newValueMatrix.set_row_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        for i in range(0, 5):
            rectangles.add(Rectangle(width=(newSentence1[i].width+0.3), height=(newSentence1[i].height+0.3), color=newSentence1[i].color).move_to(newSentence1[i]))

        matrices.add(Matrix([[3.4, 9.2,"…", 10.7]], h_buff=1.4).scale(0.6).next_to(newSentence1[0].get_right(), RIGHT, 0.5).set_color(ORANGE))
        matrices.add(Matrix([[9.1, 3.6,"…", 8.8]], h_buff=1.4).scale(0.6).next_to(newSentence1[1].get_right(), RIGHT, 0.5).set_color(RED))
        matrices.add(Matrix([[2.9, -2.1,"…", 9.4]], h_buff=1.4).scale(0.6).next_to(newSentence1[2].get_right(), RIGHT, 0.5).set_color(YELLOW))
        matrices.add(Matrix([[14.1, -3.7,"…", -2.3]], h_buff=1.4).scale(0.6).next_to(newSentence1[3].get_right(), RIGHT, 0.5).set_color(GREEN))
        matrices.add(Matrix([[5.1, 3.2,"…", 4.0]], h_buff=1.4).scale(0.6).next_to(newSentence1[4].get_right(), RIGHT, 0.5).set_color(BLUE))

        self.add(newSentence1, rectangles, matrices)
        self.wait(duration=1.5)

        self.play(LaggedStart(
            TransformMatchingShapes(matrices, matrix),
            Create(matrixBrackets)
        , lag_ratio=0.5))
        self.wait(duration=0.5)
        self.play(matrixBrackets.animate(run_time=0.05).set_opacity(0), matrix.animate.shift(UP*2), ReplacementTransform(matrix.copy(), keyMatrix), ReplacementTransform(matrix.copy(), valueMatrix))
        self.play(Write(qmultiplication), Write(kmultiplication), Write(vmultiplication))
        self.play(AnimationGroup(Create(newQueryMatrix), Create(newKeyMatrix), Create(newValueMatrix), run_time=0.75))
        self.wait(duration=0.25)
        self.play(AnimationGroup(Wiggle(newQueryMatrix, run_time=0.75, n_wiggles=2, scale_value=1.05, rotation_angle=0.01*TAU), rate_func=rate_functions.ease_out_sine))
        self.play(AnimationGroup(Wiggle(newKeyMatrix, run_time=0.75, n_wiggles=2, scale_value=1.05, rotation_angle=0.01*TAU), rate_func=rate_functions.ease_out_sine))
        self.play(AnimationGroup(Wiggle(newValueMatrix, run_time=0.75, n_wiggles=2, scale_value=1.05, rotation_angle=0.01*TAU), rate_func=rate_functions.ease_out_sine))
        self.wait()

        