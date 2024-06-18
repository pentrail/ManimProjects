from manim import *
import random

class QK1(Scene):
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

        blankMatrixQuery = Matrix([[0.0], [0.0], ["..."], [0.0]], h_buff=3).scale(0.58).move_to(compatabilityText).shift(DOWN*1.35, LEFT*2.15)
        blankMatrixQuery.get_columns()[0].set_opacity(0)

        dot = MathTex(r"\cdot").next_to(blankMatrixQuery, RIGHT, 0.1).scale(0.7)

        blankMatrixKey = Matrix([[0.0, 0.0, "...", 0.0]], v_buff=1.7).scale(0.58).next_to(dot, RIGHT, 0.1)
        blankMatrixKey.get_rows()[0].set_opacity(0)

        equals = MathTex("=").next_to(blankMatrixKey, RIGHT, 0.15).scale(0.7)

        self.add(background)
        self.add(queryMatrix, keyMatrixTransposed, sentence1, rectangles, sentenceQ, compatabilityText, blankMatrixKey, blankMatrixQuery, table, equals, dot)
        self.wait()

        