from manim import *
import random

class Embedding(Scene):
    def construct(self):
        sentence1 = Tex('He ', 'swung ', 'the ', 'baseball ', 'bat ').scale(1.2)
        sentence2 = Tex('The ', 'cave ', 'housed ', 'a ', 'bat ').scale(1.2).next_to(sentence1, DOWN, 1)

        group1 = VGroup(sentence1, sentence2).move_to([0,0,0])

        newSentence1 = sentence1.copy().set_color_by_tex("He", ORANGE).set_color_by_tex("swung", RED).set_color_by_tex("the", YELLOW).set_color_by_tex("baseball", GREEN).set_color_by_tex("bat", BLUE)
        newSentence1.arrange(RIGHT, buff=1).shift(UP*3.2)

        newSentence2 = sentence2.copy().set_color_by_tex("The", YELLOW).set_color_by_tex("cave", PINK).set_color_by_tex("housed", DARK_BLUE).set_color_by_tex("a", PURPLE).set_color_by_tex("bat", BLUE)
        newSentence2.arrange(RIGHT, buff=1.25).shift(DOWN*0.65)

        rectangles = VGroup()

        matrices = VGroup()

        for i in range(0, 5):
            rectangles.add(Rectangle(width=(newSentence1[i].width+0.3), height=(newSentence1[i].height+0.3), color=newSentence1[i].color).move_to(newSentence1[i]))
            rectangles.add(Rectangle(width=(newSentence2[i].width+0.3), height=(newSentence2[i].height+0.3), color=newSentence2[i].color).move_to(newSentence2[i]))
            if i==4:
                matrices.add(MathTex(r"\begin{bmatrix}5 \\3 \\...\\4 \\\end{bmatrix}").next_to(newSentence1[i], DOWN, 0.5).scale(0.85))
                matrices.add(MathTex(r"\begin{bmatrix}5 \\3 \\...\\4 \\\end{bmatrix}").next_to(newSentence2[i], DOWN, 0.5).scale(0.85))
            elif i==0:
                matrices.add(MathTex(r"\begin{bmatrix}{%s} \\{%s} \\...\\{%s} \\\end{bmatrix}" %(str(random.randint(-5,10)), str(random.randint(-5,10)), str(random.randint(-5,10)))).next_to(newSentence1[i], DOWN, 0.5).scale(0.85))
                matrices.add(MathTex(r"\begin{bmatrix}2 \\-1 \\...\\9 \\\end{bmatrix}").next_to(newSentence2[i], DOWN, 0.5).scale(0.85))
            elif i==2:
                matrices.add(MathTex(r"\begin{bmatrix}3 \\-2 \\...\\8 \\\end{bmatrix}").next_to(newSentence1[i], DOWN, 0.5).scale(0.85))
                matrices.add(MathTex(r"\begin{bmatrix}{%s} \\{%s} \\...\\{%s} \\\end{bmatrix}" %(str(random.randint(-5,10)), str(random.randint(-5,10)), str(random.randint(-5,10)))).next_to(newSentence2[i], DOWN, 0.5).scale(0.85))
            else:
                matrices.add(MathTex(r"\begin{bmatrix}{%s} \\{%s} \\...\\{%s} \\\end{bmatrix}" %(str(random.randint(-5,10)), str(random.randint(-5,10)), str(random.randint(-5,10)))).next_to(newSentence1[i], DOWN, 0.5).scale(0.85))
                matrices.add(MathTex(r"\begin{bmatrix}{%s} \\{%s} \\...\\{%s} \\\end{bmatrix}" %(str(random.randint(-5,10)), str(random.randint(-5,10)), str(random.randint(-5,10)))).next_to(newSentence2[i], DOWN, 0.5).scale(0.85))


        bat1 = VGroup(newSentence1[4].copy(), matrices[8].copy(), rectangles[8].copy())
        bat2 = VGroup(newSentence2[4].copy(), matrices[9].copy(), rectangles[9].copy())

        arrow1 = Arrow(start=LEFT, end=RIGHT).shift(UP*1.4, LEFT*1).scale(2.5)
        arrow2 = Arrow(start=LEFT, end=RIGHT).shift(DOWN*2.6, LEFT*1).scale(2.5)

        attention1 = Text("Attention").next_to(arrow1, UP, SMALL_BUFF).scale(0.6)
        attention2 = Text("Attention").next_to(arrow2, UP, SMALL_BUFF).scale(0.6)

        newMatrix1 = MathTex(r"\begin{bmatrix}7 \\4 \\...\\4 \\\end{bmatrix}").next_to(arrow1, RIGHT, 0.5).scale(0.85)
        newMatrix2 = MathTex(r"\begin{bmatrix}5 \\1 \\...\\3 \\\end{bmatrix}").next_to(arrow2, RIGHT, 0.5).scale(0.85)

        self.play(Write(group1), run_time=1)
        self.wait(duration=1)
        self.play(LaggedStart(
            AnimationGroup(
            ReplacementTransform(sentence1, newSentence1), 
            ReplacementTransform(sentence2, newSentence2)
            ), Create(rectangles)
        ),
            run_time=0.8)
        self.wait(duration=1.5)
        self.play(Write(matrices), run_time=0.75)
        self.wait(duration=4)

        self.play(Flash(matrices[8], color=WHITE, flash_radius=matrices[8].width+SMALL_BUFF), Flash(matrices[9], color=WHITE, flash_radius=matrices[9].width+SMALL_BUFF), run_time=0.75)
        self.wait(duration=0.2)

        self.add(bat1, bat2)
        self.play(Uncreate(newSentence1), Uncreate(newSentence2), Uncreate(matrices), Uncreate(rectangles), run_time=0.75)
        self.play(bat1.animate.shift(LEFT*8), bat2.animate.shift(LEFT*8))
        self.wait(duration=2.5)

        self.play(
            LaggedStart(
                AnimationGroup(
                    Create(arrow1), Create(arrow2)
                ),
                AnimationGroup(
                    Create(attention1), Create(attention2)
                ), lag_ratio=0.5
            ), run_time=1.5
        )

        self.play(Write(newMatrix1), Write(newMatrix2))

        self.wait(duration=1.5)
        