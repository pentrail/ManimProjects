from manim import *
import random

class QK(Scene):
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

        for i in range(0, 5):
            rectangles.add(Rectangle(width=(sentence1[i].width+0.3), height=(sentence1[i].height+0.3), color=sentence1[i].color).move_to(sentence1[i]))
            rectangles.add(Rectangle(width=(sentenceQ[i].width+0.3), height=(sentenceQ[i].height+0.3), color=sentenceQ[i].color).move_to(sentenceQ[i]))


        compatabilityText = MathTex("Compatibility(     ,     )").move_to(rectangles[1]).shift(LEFT*4.9, DOWN*0.5).scale(0.75)

        self.add(queryMatrix, keyMatrixTransposed, sentence1, rectangles, sentenceQ, compatabilityText)

        self.wait()

        