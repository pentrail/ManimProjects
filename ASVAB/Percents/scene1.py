from manim import *

class PercentVisual(Scene):
    def construct(self):
        question = MathTex(r"Find\:8\%\:of\:250", substrings_to_isolate=["8"]).shift(UP*3).scale(1.25)
        hint = Text("8% means '8 for each 100'", substrings_to_isolate=["8"]).next_to(question.get_bottom(), DOWN, buff=0.3)

        square1 = Square(side_length=2).shift(LEFT*2.5).set_fill()
        square2 = Square(side_length=2).next_to(square1.get_right(), RIGHT, 0.5)
        square3 = Square(side_length=2).next_to(square2.get_right(), RIGHT, 0.5)

        label = Tex(100)

        innerLabelLeft = Tex('8', substrings_to_isolate=["8"])
        innerLabelMiddle = Tex('8', substrings_to_isolate=["8"])
        innerLabelRight = Tex(4)
        innerLabelFinal = Tex(4)

        innerLabels = VGroup(innerLabelLeft, innerLabelMiddle, innerLabelRight)

        separator = DashedLine(start=square3.get_top(), end=square3.get_bottom())

        smallerRectangleLeft = Rectangle(width=1, height=2).next_to(square3.get_left(), RIGHT, 0)
        smallerRectangleRight = Rectangle(width=1, height=2).next_to(square3.get_right(), LEFT, 0)

        self.play(Write(question))
        self.play(ReplacementTransform(question.copy(), hint))
        self.play(Succession(
            Create(square1),
            Create(square2),
            Create(square3)
        ), run_time=2, lag_ratio=0.8)
        self.play(Succession(
            Write(label.next_to(square1.get_bottom(), DOWN, 0.18)),
            Write(label.copy().next_to(square2.get_bottom(), DOWN, 0.18)),
            Write(label.copy().next_to(square3.get_bottom(), DOWN, 0.18))
        ), run_time=2, lag_ratio=0.8)
        self.play(Create(separator))
        self.play(Succession(
            ReplacementTransform(hint.copy(), innerLabelLeft.move_to(square1.get_center())), 
            ReplacementTransform(hint.copy(), innerLabelMiddle.move_to(square2.get_center())), 
            AnimationGroup(
                ReplacementTransform(hint.copy(), innerLabelRight.move_to(smallerRectangleLeft.get_center())),
                ReplacementTransform(hint.copy(), innerLabelFinal.move_to(smallerRectangleRight.get_center()))
            )
        ), run_time=2, lag_ratio=0.8)
        self.wait()
        self.play(square1.animate.set_fill(BLUE, 0.5),square2.animate.set_fill(BLUE, 0.5), smallerRectangleLeft.animate.set_fill(BLUE, 0.5))
        self.play(innerLabels.animate.shift(DOWN*2.5))
        self.play(
            Write(Tex('+').set_color(YELLOW).next_to(innerLabelLeft.get_right(), RIGHT, 1)),
            Write(Tex('+').set_color(YELLOW).next_to(innerLabelMiddle.get_right(), RIGHT, 0.75)),
            Write(Tex('=').set_color(YELLOW).next_to(innerLabelRight.get_right(), RIGHT, 0.5)),
            Write(Tex(20).set_color(BLUE).next_to(innerLabelRight.get_right(), RIGHT, 1.25))
        )
        self.wait()