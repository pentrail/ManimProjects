from manim import *
import random

class Embedding(Scene):
    def construct(self):
        sentence1 = Tex('He ', 'swung ', 'the ', 'baseball ', 'bat ').scale(1.2)
        sentence2 = Tex('The ', 'cave ', 'housed ', 'a ', 'bat ').scale(1.2).next_to(sentence1, DOWN, 1)

        group1 = VGroup(sentence1, sentence2).move_to([0,0,0])

        newSentence1 = sentence1.copy().set_color_by_tex("He", ORANGE).set_color_by_tex("swung", RED).set_color_by_tex("the", YELLOW).set_color_by_tex("baseball", GREEN).set_color_by_tex("bat", BLUE)
        newSentence1.arrange(DOWN, buff=1, aligned_edge=RIGHT).shift(LEFT*5.6)

        newSentence2 = sentence2.copy().set_color_by_tex("The", YELLOW).set_color_by_tex("cave", PINK).set_color_by_tex("housed", DARK_BLUE).set_color_by_tex("a", PURPLE).set_color_by_tex("bat", BLUE)
        newSentence2.arrange(DOWN, buff=1, aligned_edge=RIGHT).shift(RIGHT*1.6)

        rectangles = VGroup()

        divider = DashedLine(config.top, config.bottom)

        matrices = VGroup()

        for i in range(0, 5):
            rectangles.add(Rectangle(width=(newSentence1[i].width+0.3), height=(newSentence1[i].height+0.3), color=newSentence1[i].color).move_to(newSentence1[i]))
            rectangles.add(Rectangle(width=(newSentence2[i].width+0.3), height=(newSentence2[i].height+0.3), color=newSentence2[i].color).move_to(newSentence2[i]))
            # if i==4:
            #     matrices.add(MathTex(r"\begin{bmatrix}5 \\3 \\...\\4 \\\end{bmatrix}").next_to(newSentence1[i], DOWN, 0.5).scale(0.85))
            #     matrices.add(MathTex(r"\begin{bmatrix}5 \\3 \\...\\4 \\\end{bmatrix}").next_to(newSentence2[i], DOWN, 0.5).scale(0.85))
            # elif i==0:
            #     matrices.add(MathTex(r"\begin{bmatrix}{%s} \\{%s} \\...\\{%s} \\\end{bmatrix}" %(str(random.randint(-5,10)), str(random.randint(-5,10)), str(random.randint(-5,10)))).next_to(newSentence1[i], DOWN, 0.5).scale(0.85))
            #     matrices.add(MathTex(r"\begin{bmatrix}2 \\-1 \\...\\9 \\\end{bmatrix}").next_to(newSentence2[i], DOWN, 0.5).scale(0.85))
            # elif i==2:
            #     matrices.add(MathTex(r"\begin{bmatrix}3 \\-2 \\...\\8 \\\end{bmatrix}").next_to(newSentence1[i], DOWN, 0.5).scale(0.85))
            #     matrices.add(MathTex(r"\begin{bmatrix}{%s} \\{%s} \\...\\{%s} \\\end{bmatrix}" %(str(random.randint(-5,10)), str(random.randint(-5,10)), str(random.randint(-5,10)))).next_to(newSentence2[i], DOWN, 0.5).scale(0.85))
            # else:
            #     matrices.add(MathTex(r"\begin{bmatrix}{%s} \\{%s} \\...\\{%s} \\\end{bmatrix}" %(str(random.randint(-5,10)), str(random.randint(-5,10)), str(random.randint(-5,10)))).next_to(newSentence1[i], DOWN, 0.5).scale(0.85))
            #     matrices.add(MathTex(r"\begin{bmatrix}{%s} \\{%s} \\...\\{%s} \\\end{bmatrix}" %(str(random.randint(-5,10)), str(random.randint(-5,10)), str(random.randint(-5,10)))).next_to(newSentence2[i], DOWN, 0.5).scale(0.85))

        # index 0
        matrices.add(Matrix([[3.4, 9.2,"...", 10.7]], h_buff=1.4).scale(0.6).next_to(newSentence1[0].get_right(), RIGHT, 0.5))
        matrices.add(Matrix([[2.0, -1.7,"...", 9.4]], h_buff=1.4).scale(0.6).next_to(newSentence2[0].get_right(), RIGHT, 0.5))
        # index 1
        matrices.add(Matrix([[9.1, 3.6,"...", 8.8]], h_buff=1.4).scale(0.6).next_to(newSentence1[1].get_right(), RIGHT, 0.5))
        matrices.add(Matrix([[2.4, -1.7,"...", 9.2]], h_buff=1.4).scale(0.6).next_to(newSentence2[1].get_right(), RIGHT, 0.5))
        # index 2
        matrices.add(Matrix([[2.9, -2.1,"...", 9.4]], h_buff=1.4).scale(0.6).next_to(newSentence1[2].get_right(), RIGHT, 0.5))
        matrices.add(Matrix([[5.8, 3.1,"...", 7.6]], h_buff=1.4).scale(0.6).next_to(newSentence2[2].get_right(), RIGHT, 0.5))
        # index 3
        matrices.add(Matrix([[14.1, -3.7,"...", -2.3]], h_buff=1.4).scale(0.6).next_to(newSentence1[3].get_right(), RIGHT, 0.5))
        matrices.add(Matrix([[-6.2, 12.1,"...", 7.5]], h_buff=1.4).scale(0.6).next_to(newSentence2[3].get_right(), RIGHT, 0.5))
        # index 4
        matrices.add(Matrix([[5.1, 3.2,"...", 4.0]], h_buff=1.4).scale(0.6).next_to(newSentence1[4].get_right(), RIGHT, 0.5))
        matrices.add(Matrix([[5.1, 3.2,"...", 4.0]], h_buff=1.4).scale(0.6).next_to(newSentence2[4].get_right(), RIGHT, 0.5))

        bat1 = VGroup(newSentence1[4].copy(), matrices[8].copy().set_color(BLUE), rectangles[8].copy())
        bat2 = VGroup(newSentence2[4].copy(), matrices[9].copy().set_color(BLUE), rectangles[9].copy())

        arrow1 = Arrow(start=UP, end=DOWN).scale(1.35).next_to(matrices[8], DOWN, 0.35).shift(UP*6).set_color(YELLOW)
        arrow2 = Arrow(start=UP, end=DOWN).scale(1.35).next_to(matrices[9], DOWN, 0.35).shift(UP*6).set_color(YELLOW)

        attention1 = Text("Attention Layer").next_to(matrices[8], UP, 4.05).scale(0.55).set_color(YELLOW).set_z_index(1)
        attention2 = Text("Attention Layer").next_to(matrices[9], UP, 4.05).scale(0.55).set_color(YELLOW).set_z_index(1)

        newMatrix1 = Matrix([[7.3, 5.2,"...", -1.5]], h_buff=1.4).scale(0.6).set_color(RED).next_to(arrow1, DOWN, 0.25)
        newMatrix2 = Matrix([[5.3, 1.7,"...", 2.9]], h_buff=1.4).scale(0.6).set_color(PURPLE).next_to(arrow2, DOWN, 0.25)

        self.play(Write(group1), run_time=1)
        self.wait(duration=1)
        self.play(LaggedStart(
            AnimationGroup(
            ReplacementTransform(sentence1, newSentence1), 
            ReplacementTransform(sentence2, newSentence2)
            ), Create(rectangles)
        ),
            run_time=0.8)
        self.play(AnimationGroup(Create(divider), run_time=1))
        self.wait(duration=0.5)
        self.play(Write(matrices), run_time=0.75)
        self.wait(duration=4)

        self.play(Flash(matrices[8], color=WHITE, flash_radius=matrices[8].height+SMALL_BUFF), Flash(matrices[9], color=WHITE, flash_radius=matrices[9].height+SMALL_BUFF), run_time=0.75)
        self.wait(duration=0.2)

        self.add(bat1, bat2)
        self.play(Uncreate(newSentence1), Uncreate(newSentence2), Uncreate(matrices), Uncreate(rectangles), run_time=0.75)
        self.play(bat1.animate.shift(UP*6), bat2.animate.shift(UP*6))
        self.wait(duration=2.5)

        self.play(
            LaggedStart(
                AnimationGroup(
                    Create(arrow1), Create(arrow2)
                ),
                AnimationGroup(
                    Create(attention1), Create(SurroundingRectangle(attention1, color=YELLOW, buff=0.23, corner_radius=0.25, fill_color=BLACK, fill_opacity=1)), Create(attention2), Create(SurroundingRectangle(attention2, color=YELLOW, buff=0.23, corner_radius=0.25, fill_color=BLACK, fill_opacity=1))
                ), lag_ratio=0.5
            ), run_time=1.5
        )

        self.play(Write(newMatrix1), Write(newMatrix2))

        self.wait(duration=1.5)
        