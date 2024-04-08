from manim import *

class PlaceValue(Scene):
    def construct(self):
        number = Tex('342', substrings_to_isolate=["3", "4", "2"]).scale(3)
        numberTransformed = Tex('3 4 2', substrings_to_isolate=["3", "4", "2"]).scale(3)

        numberColored = Tex('3 4 2', substrings_to_isolate=["3", "4", "2"]).scale(3).set_color_by_tex('3', YELLOW).set_color_by_tex('4', BLUE).set_color_by_tex('2', RED).shift(DOWN * 2)

        numberOnes = Tex('2', substrings_to_isolate=["2"]).scale(3).set_color(RED)
        numberTens = Tex('4 0', substrings_to_isolate=["4"]).scale(3).set_color(BLUE)
        numberHundreds = Tex('3 0 0', substrings_to_isolate=["3"]).scale(3).set_color(YELLOW)

        plusSign = Text("+").scale(0.95)

        text = VGroup(numberHundreds, numberTens, numberOnes).arrange(DOWN, center=True, aligned_edge=RIGHT)
        line = DashedLine(start=numberTransformed.get_left(), end=numberTransformed.get_right())

        self.play(Write(number))
        self.play(LaggedStart(
            ReplacementTransform(number, numberTransformed),
        ), run_time=2, lag_ratio=0.1, rate_func=rate_functions.ease_out_expo)
        self.play(ReplacementTransform(numberTransformed, numberColored))
        # self.play(numberTransformed.animate.shift(DOWN * 2))
        self.play(LaggedStart(
            ReplacementTransform(numberColored.copy(), text.next_to(numberColored.get_center(), UP, 1.5)),
            Create(line.next_to(numberColored.get_center(), UP, 1)),
            Create(plusSign.next_to(line.get_left(), UP, 0.3).shift(RIGHT*0.3)),
        ), run_time=3, lag_ratio=0.35, rate_func=rate_functions.ease_out_sine)
        self.wait()