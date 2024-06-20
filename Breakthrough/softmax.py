from manim import *
import random

class Soft(Scene):
    def construct(self):


        queryMatrix = Matrix([[1.4, 5.6, -3.6, 2.4, -5.1], [4.5, -2.9, 6.4, -0.5, 4.3], ["...", "...", "...", "...", "..."], [-8.1, 2.8, -4.4, 1.1, 4.9]], h_buff=3).scale(0.58).shift(UP*2, RIGHT*2.8)
        queryMatrix.set_column_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        # keyMatrix = Matrix([[3.9, -5.8, 5.2, -1.4, -5.1], [-9.2, -1.9, -3.1, 6.7, 4.0], ["...", "...", "...", "...", "..."], [-2.1, 1.4, -3.6, 3.1, 6.1]]).scale(0.58).next_to(queryMatrix, DOWN, 1)
        # keyMatrix.set_column_colors(ORANGE, RED, YELLOW, GREEN, BLUE)

        keyMatrixTransposed = Matrix([[3.9, -9.2, "...", -2.1 ], [-5.8, -1.9, "...", 1.4], [5.2, -3.1, "...", -3.6], [-1.4, 6.7, "...", 3.1], [-5.1, 4.0, "...", 6.1]], v_buff=1.7).scale(0.58).next_to(queryMatrix, DOWN, 0.25).shift(LEFT*5.8)
        keyMatrixTransposed.set_row_colors(ORANGE, RED, YELLOW, GREEN, BLUE)
        
        rectangles = VGroup()

        sentence1 = Tex("He ", "swung ", "the ", "baseball ", "bat ").scale(1).set_color_by_tex("He", ORANGE).set_color_by_tex("swung", RED).set_color_by_tex("the", YELLOW).set_color_by_tex("baseball", GREEN).set_color_by_tex("bat", BLUE)
        sentence1.arrange(DOWN, buff=0.55, aligned_edge=RIGHT, center=False).next_to(keyMatrixTransposed, LEFT, buff=0.3)

        sentenceQ = Tex("He ", "swung ", "the ", "baseball ", "bat ").scale(1).set_color_by_tex("He", ORANGE).set_color_by_tex("swung", RED).set_color_by_tex("the", YELLOW).set_color_by_tex("baseball", GREEN).set_color_by_tex("bat", BLUE)
        sentenceQ.arrange(RIGHT, buff=0.55).next_to(queryMatrix, UP, buff=0.3)

        rectangleWord = []

        for i in range(0, 5):
            rectangles.add(Rectangle(width=(sentence1[i].width+0.3), height=(sentence1[i].height+0.3), color=sentence1[i].color).move_to(sentence1[i]))
            rectangles.add(Rectangle(width=(sentenceQ[i].width+0.3), height=(sentenceQ[i].height+0.3), color=sentenceQ[i].color).move_to(sentenceQ[i]))

            rectangleWord.append(VGroup(sentenceQ[i], rectangles[i*2+1]))
            rectangleWord.append(VGroup(sentence1[i], rectangles[i*2]))

        table = Table([
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]], v_buff=1.6, h_buff=3.25).scale(0.42).move_to(queryMatrix.get_center()).shift(DOWN*3.42).set_opacity(0.7)
        # .set_color_by_gradient([BLUE, GREEN, YELLOW, RED, ORANGE])
        table.get_rows()[0:5].set_opacity(0)


        background = Rectangle(height=2.85, width=5.6).move_to(queryMatrix).shift(LEFT*7, UP*0.42)
        background.set_fill(opacity=.10)
        background.set_stroke(opacity=0.9)
        background.set_color(WHITE)


        compatabilityText = MathTex(r"Compatibility(\qquad\qquad ,\qquad\qquad)=").scale(0.85).move_to(rectangles[1]).shift(LEFT*3.76, UP*0.07).scale(0.75)

        queryColumns = queryMatrix.get_columns()
        keyRows = keyMatrixTransposed.get_rows()

        blankMatrixQuery = Matrix([[0.0, 0.0, "...", 0.0]], v_buff=1.7).scale(0.58).move_to(compatabilityText).shift(DOWN*1.35, LEFT*1.08)
        blankMatrixQuery.get_rows()[0].set_opacity(0)

        dot = MathTex(r"\cdot").next_to(blankMatrixQuery, RIGHT, 0.1).scale(0.7)

        blankMatrixKey = Matrix([[0.0], [0.0], ["..."], [0.0]], h_buff=3).scale(0.58).next_to(dot, RIGHT, 0.1)
        blankMatrixKey.get_columns()[0].set_opacity(0)

        equals = MathTex("=").next_to(blankMatrixKey, RIGHT, 0.15).scale(0.7)

        attentionPattern = VGroup(
            MathTex("5.2"), MathTex("-92.1"), MathTex("-93.5"), MathTex("-86.2"), MathTex("-98.1"),
            MathTex("-91.2"), MathTex("3.6"), MathTex("-92.1"), MathTex("-31.7"), MathTex("11.4"),
            MathTex("-95.5"), MathTex("-87.5"), MathTex("2.3"), MathTex("-95.2"), MathTex("-97.5"),
            MathTex("-78.1"), MathTex("-82.4"), MathTex("-92.4"), MathTex("10.6"), MathTex("6.2"),
            MathTex("-97.2"), MathTex("72.2"), MathTex("-94.3"), MathTex("89.4"), MathTex("2.6"),
        )

        attentionPatternMatrix = Matrix([[5.2, -92.1, -93.5, -86.2, -98.1], [-11.2, 1.6, -92.1, -31.7, 11.4], [-95.5, -87.5, 2.3, -95.2, -97.5], [-78.1, -82.4, -92.3, 10.6, 6.2], [-97.2, 72.2, -94.3, 89.4, 2.6]], h_buff=1.8, v_buff=2.5).scale(0.5)
        scalarBrackets = Matrix([[0, 0],[0, 0]], v_buff=3, h_buff=4).scale(0.5).next_to(attentionPatternMatrix, RIGHT, 0.5).shift(LEFT*4.5)
        scalarBrackets.get_columns().set_opacity(0)
        dot2 = MathTex(r"\cdot").scale(0.7).move_to((attentionPatternMatrix.get_right()+scalarBrackets.get_left())/2).shift(LEFT*2.25)
        scalar = MathTex(r"\frac{1}{\sqrt{d_k}}").move_to(scalarBrackets)
        scalarWithNum = MathTex(r"\frac{1}{\sqrt{256}}").move_to(scalarBrackets)

        equals2 = MathTex("=").scale(1.5).next_to(scalarBrackets.get_right(), RIGHT, 0.35)

        scaledAttention = Matrix([[0.33, -5.76, -5.84, -5.39, -6.13], [-5.7, 0.23, -5.76, -1.98, 0.71], [-5.97, -5.47, 0.14, -5.95, -6.09], [-4.88, -5.15, -5.78, 0.66, 0.39], [-6.08, 4.51, -5.89, 5.59, 0.16]], h_buff=1.8, v_buff=2.5).scale(0.5).next_to(equals2, RIGHT, 0.35)

        softmaxText = MathTex(r"softmax(\vec{v_1})_i").move_to(scaledAttention).shift(LEFT*4.1, UP*2.3)
        
        softmaxMatrix = Matrix([[1, 0, 0, 0, 0], [0, 0.37, 0, 0.04, 0.59], [0, 0, 1, 0, 0], [0, 0, 0, 0.57, 0.43], [0, 0.25, 0, 0.75, 0]], h_buff=1.8, v_buff=2.5).scale(0.5).move_to(scaledAttention).shift(RIGHT*0.5)
        softmaxBrackets = Matrix([[1, 0, 0, 0, 0], [0, 0.37, 0, 0.04, 0.59], [0, 0, 1, 0, 0], [0, 0, 0, 0.57, 0.43], [0, 0.25, 0, 0.75, 0]], h_buff=1.8, v_buff=2.5).scale(0.5).move_to(scaledAttention).shift(RIGHT*0.5)
        softmaxBrackets.get_rows().set_opacity(0)

        self.add(background)
        self.add(queryMatrix, keyMatrixTransposed, sentence1, rectangles, sentenceQ, compatabilityText, blankMatrixKey, blankMatrixQuery, table, equals, dot)
        for i in range(0,5):
            workingQueryText = rectangleWord[2*i].copy()
            workingQueryMatrix = queryColumns[i].copy()
            self.add(workingQueryText.scale(0.6).move_to(compatabilityText).shift(RIGHT*0.11), workingQueryMatrix.move_to(blankMatrixQuery))
            for j in range(0,5):
                workingKeyText = rectangleWord[2*j+1].copy()
                workingKeyMatrix = keyRows[j].copy()
                self.add(
                    workingKeyText.scale(0.6).move_to(compatabilityText).shift(RIGHT*1.5), 
                    workingKeyMatrix.move_to(blankMatrixKey), 
                    attentionPattern[i*5+j].scale(0.5).next_to(equals, RIGHT, 0.18))
                self.add(attentionPattern[i*5+j].scale(1.2).move_to(table.get_cell(pos=(i+1, j+1))))
                self.remove(workingKeyText, workingKeyMatrix)
            self.remove(workingQueryText, workingQueryMatrix)
        self.wait()
        self.play(Uncreate(VGroup(background, queryMatrix, keyMatrixTransposed, compatabilityText, blankMatrixKey, blankMatrixQuery, equals, dot, rectangles, sentence1, sentenceQ), run_time=0.5))
        self.play(ReplacementTransform(VGroup(attentionPattern, table), attentionPatternMatrix))
        self.play(attentionPatternMatrix.animate(run_time=0.6).shift(LEFT*4.5))
        self.play(Write(scalarBrackets), Write(scalar), Write(dot2), Write(equals2), run_time=0.5)
        self.wait(duration=0.5)
        self.play(Write(scaledAttention), TransformMatchingTex(scalar, scalarWithNum))
        self.wait()
        self.play(Unwrite(VGroup(attentionPatternMatrix, dot2, equals2, scalarBrackets, scalarWithNum)), run_time=0.35)
        self.play(scaledAttention.animate(run_time=0.6).shift(LEFT*8.8))
        for i in range(0,5):
            workingSoftmaxText = MathTex("softmax(\\vec{v_%i})_i" % (i+1)).scale(0.6).move_to(scaledAttention.get_rows()[i]).shift(RIGHT*4.75).set_color(YELLOW)
            workingSoftmaxText.set_z_index(1)
            workingRectangle = SurroundingRectangle(workingSoftmaxText, color=YELLOW, buff=0.23, corner_radius=0.25, fill_color=BLACK, fill_opacity=1)
            workingArrow1 = Arrow(start=scaledAttention.get_rows()[i].get_right(), end=workingRectangle.get_left()).shift(RIGHT*0.15).set_color(YELLOW)
            workingArrow2 = Arrow(start=workingRectangle.get_right(), end=softmaxMatrix.get_rows()[i].get_left()).shift(LEFT*0.15).set_color(YELLOW)
            # Repalcement Softmax Text
            self.play(Write(workingSoftmaxText), Create(workingRectangle), run_time=0.2)
            self.play(Create(workingArrow1), run_time=0.4)
            self.play(Create(workingArrow2), run_time=0.2)
            self.play(Write(softmaxMatrix.get_rows()[i]), run_time=0.3)
        self.play(Write(softmaxBrackets))
        self.wait()

        