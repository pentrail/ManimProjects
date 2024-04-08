from manim import *
import numpy as np

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class GetIntersections:
    def get_coord_from_proportion(self,vmob,proportion):
        return vmob.point_from_proportion(proportion)

    def get_points_from_curve(self, vmob, dx=0.002):
        coords = []
        for point in Range(0, 1, dx):
            dot = Dot(self.get_coord_from_proportion(vmob,point))
            coords.append(dot.get_center())
        return coords

    def get_intersections_between_two_vmobs(self, vmob1, vmob2,
                                            tolerance=0.02,
                                            radius_error=0.2,
                                            use_average=True,
                                            use_first_vmob_reference=False):
        coords_1 = self.get_points_from_curve(vmob1)
        coords_2 = self.get_points_from_curve(vmob2)
        intersections = []
        for coord_1 in coords_1:
            for coord_2 in coords_2:
                distance_between_points = np.linalg.norm(coord_1 - coord_2)
                if use_average:
                    coord_3 = (coord_2 - coord_1) / 2
                    average_point = coord_1 + coord_3
                else:
                    if use_first_vmob_reference:
                        average_point = coord_1
                    else:
                        average_point = coord_2
                if len(intersections) > 0 and distance_between_points < tolerance:
                    last_intersection=intersections[-1]
                    distance_between_previus_point = np.linalg.norm(average_point - last_intersection)
                    if distance_between_previus_point > radius_error:
                        intersections.append(average_point)
                if len(intersections) == 0 and distance_between_points < tolerance:
                    intersections.append(average_point)
        return intersections


class Scene2(Scene, GetIntersections):
    def construct(self):

        line = Line().set_length(2)

        startPoint = always_redraw(lambda :
        Circle(arc_center=line.get_start(), radius=0.02, stroke_color=RED).set_fill(color=WHITE, opacity=1))

        endPoint = always_redraw(lambda :
        Circle(arc_center=line.get_end(), radius=0.02, stroke_color=RED).set_fill(color=WHITE, opacity=1))


        leftCircle = always_redraw(lambda :
        Circle(arc_center=line.get_start(), radius=line.width, stroke_color=WHITE))

        rightCircle = always_redraw(lambda :
        Circle(arc_center=line.get_end(), radius=line.width, stroke_color=WHITE)).flip(axis=Y_AXIS)

        intersection = Circle(radius=0.02, stroke_color=RED).set_fill(color=WHITE, opacity=1).move_to(self.get_intersections_between_two_vmobs(leftCircle, rightCircle)[0])

        triangle = always_redraw(lambda :
        Polygon(intersection.get_center(), line.get_left(), line.get_right(), stroke_color=RED, stroke_width=5)) 


        line2 = Line(stroke_color=RED, stroke_width=5).set_length(line.width).next_to(line, DOWN, buff=2.1)
        line1 = Line(stroke_color=RED, stroke_width=5).set_length(line.width).next_to(line2, LEFT, buff=0)
        line3 = Line(stroke_color=RED, stroke_width=5).set_length(line.width).next_to(line2, RIGHT, buff=0)

        finalLine = Line(stroke_color=RED, stroke_width=5).set_length((line.width)*3).next_to(line2, DOWN, buff=0.6)


        self.play(Create(line))
        self.play(LaggedStart(Create(leftCircle), Create(rightCircle), run_time=2.5, lag_ratio=0.75))
        self.play(LaggedStart(Create(startPoint), Create(endPoint), Create(intersection), Create(triangle), run_time=2.5, lag_ratio=0.75))
        self.play(line.animate.shift(UP * 1), intersection.animate.shift(UP * 1), run_time=1)
        self.play(LaggedStart(ReplacementTransform(line.copy(), line1), ReplacementTransform(line.copy(), line2), ReplacementTransform(line.copy(), line3), run_time=2, lag_ratio=0.75))
        self.play(ReplacementTransform(triangle.copy(), finalLine), run_time=1.5)
        self.wait(1)