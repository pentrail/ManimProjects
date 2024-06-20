from manim import *
import random

class Values(Scene):
    def construct(self):

        attentionPatternMatrix = Matrix([[5.2, -92.1, -93.5, -86.2, -98.1], [-11.2, 1.6, -92.1, -31.7, 11.4], [-95.5, -87.5, 2.3, -95.2, -97.5], [-78.1, -82.4, -92.3, 10.6, 6.2], [-97.2, 72.2, -94.3, 89.4, 2.6]], h_buff=1.8, v_buff=2.5).scale(0.5)

        scalarBrackets = Matrix([[0, 0],[0, 0]], v_buff=3, h_buff=4).scale(0.5).next_to(attentionPatternMatrix, RIGHT, 0.5).shift(LEFT*4.5)
        scalarBrackets.get_columns().set_opacity(0)

        equals2 = MathTex("=").scale(1.5).next_to(scalarBrackets.get_right(), RIGHT, 0.35)

        scaledAttention = Matrix([[0.33, -5.76, -5.84, -5.39, -6.13], [-5.7, 0.23, -5.76, -1.98, 0.71], [-5.97, -5.47, 0.14, -5.95, -6.09], [-4.88, -5.15, -5.78, 0.66, 0.39], [-6.08, 4.51, -5.89, 5.59, 0.16]], h_buff=1.8, v_buff=2.5).scale(0.5).next_to(equals2, RIGHT, 0.35)
        
        softmaxMatrix = Matrix([[1, 0, 0, 0, 0], [0, 0.37, 0, 0.04, 0.59], [0, 0, 1, 0, 0], [0, 0, 0, 0.57, 0.43], [0, 0.25, 0, 0.75, 0]], h_buff=1.8, v_buff=2.5).scale(0.5).move_to(scaledAttention).shift(RIGHT*0.5)
        scaledAttention.shift(LEFT*8.8)

        softmaxStuff = VGroup()

        valueMatrix = Matrix([[3.2, -1.6, "...", 3.1], [-4.1, -3.2, "...", 3.1], [2.2, 5.3, "...", 3.0], [-4.2, 5.3, "...", -9.2], [3.0, 8.8, "...", -0.2]], v_buff=2.5).scale(0.5).next_to(softmaxMatrix.get_right(), RIGHT, 0.25).shift(LEFT*7.4, UP*1)
        valueMatrix.set_row_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        newSentence1 = Tex('He ', 'swung ', 'the ', 'baseball ', 'bat ').scale(1).copy().set_color_by_tex("He", ORANGE).set_color_by_tex("swung", RED).set_color_by_tex("the", YELLOW).set_color_by_tex("baseball", GREEN).set_color_by_tex("bat", BLUE)
        newSentence1.arrange(DOWN, buff=0.8, aligned_edge=RIGHT).shift(LEFT*5.8, UP*1)

        rectangles = VGroup()

        equals3 = MathTex("=").scale(1).next_to(valueMatrix.get_right(), RIGHT, 0.25)

        embeddingChanges = Matrix([[3.2, -1.6, "...", 3.1], [0.09, 4.22, "...", 0.66], [2.2, 5.3, "...", 3], [-1.1, 6.81, "...", -5.33], [-4.18, 3.18, "...", -6.13]], v_buff=2.5, h_buff=1.55).scale(0.5).next_to(equals3.get_right(), RIGHT, 0.25)
        embeddingChanges.set_row_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        for i in range(0, 5):
            rectangles.add(Rectangle(width=(newSentence1[i].width+0.3), height=(newSentence1[i].height+0.3), color=newSentence1[i].color).move_to(newSentence1[i]))

        delta = MathTex(r"\Delta").set_color(BLUE).next_to(rectangles[4].get_left(), LEFT, 0.1).shift(DOWN*1.75)

        self.add(scaledAttention)
        for i in range(0,5):
            workingSoftmaxText = MathTex("softmax(\\vec{v_%i})_i" % (i+1)).scale(0.6).move_to(scaledAttention.get_rows()[i]).shift(RIGHT*4.75).set_color(YELLOW)
            workingSoftmaxText.set_z_index(1)
            workingRectangle = SurroundingRectangle(workingSoftmaxText, color=YELLOW, buff=0.23, corner_radius=0.25, fill_color=BLACK, fill_opacity=1)
            workingArrow1 = Arrow(start=scaledAttention.get_rows()[i].get_right(), end=workingRectangle.get_left()).shift(RIGHT*0.15).set_color(YELLOW)
            workingArrow2 = Arrow(start=workingRectangle.get_right(), end=softmaxMatrix.get_rows()[i].get_left()).shift(LEFT*0.15).set_color(YELLOW)
            softmaxStuff.add(workingSoftmaxText, workingRectangle, workingArrow1, workingArrow2)
            # Repalcement Softmax Text
            self.add(workingSoftmaxText, workingRectangle)
            self.add(workingArrow1)
            self.add(workingArrow2)
        self.add(softmaxMatrix)
        self.wait()

        self.play(LaggedStart(
            Unwrite(VGroup(scaledAttention, softmaxStuff)),
            softmaxMatrix.animate().shift(LEFT*7.4, UP*1),
            lag_ratio=0.8,
            run_time=1
        ))
        self.play(softmaxMatrix.animate().set_column_colors(ORANGE, RED, YELLOW, GREEN, BLUE), Write(valueMatrix), Write(newSentence1), Create(rectangles), run_time=0.75)
        self.wait()
        self.play(Create(equals3), Create(embeddingChanges))
        self.wait()
        self.play(Create(delta), rectangles[4].copy().animate().shift(DOWN*1.75), newSentence1[4].copy().animate().shift(DOWN*1.75))
        self.play(softmaxMatrix.get_entries()[21].copy().animate().shift(DOWN*1.75))

        