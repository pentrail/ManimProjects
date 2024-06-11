from manim import *

class MyCamera(ThreeDCamera):
    def transform_points_pre_display(self, mobject, points):
        if getattr(mobject, "fixed", False):
            return points
        else:
            return super().transform_points_pre_display(mobject, points)
      
class MyThreeDScene(ThreeDScene):
    def __init__(self, camera_class=MyCamera, ambient_camera_rotation=None,
                 default_angled_camera_orientation_kwargs=None, **kwargs):
        super().__init__(camera_class=camera_class, **kwargs)

def make_fixed(*mobs):
    for mob in mobs:
        mob.fixed = True
        for submob in mob.family_members_with_points():
            submob.fixed = True

class DotProduct(MyThreeDScene):
    def construct(self):

        ax = ThreeDAxes().scale(0.8)

        label = Tex("Dot Product:").shift(DOWN*3.2)

        labelmath1 = MathTex(r"\vec{v}").set_color(RED).next_to(label, RIGHT, buff=0.2)
        labelmath2 = MathTex(r"\cdot").next_to(labelmath1, RIGHT, buff=0.1)
        labelmath3 = MathTex(r"\vec{u}").set_color(BLUE).next_to(labelmath2, RIGHT, buff=0.1)
        labelmath4 = Tex("=").next_to(labelmath3, RIGHT, buff=0.1)


        x1 = ValueTracker(-2)
        y1 = ValueTracker(-2.5)
        z1 = ValueTracker(1) 

        label2 = always_redraw(lambda: Tex("{}".format(np.round(np.dot(np.array([2, 2, 2]), np.array([x1.get_value(), y1.get_value(), z1.get_value()])), 1))).next_to(labelmath4, RIGHT, buff=0.2))
        
        make_fixed(label, label2, labelmath1, labelmath2, labelmath3, labelmath4)

        bottomText = VGroup(label, label2, labelmath1, labelmath2, labelmath3, labelmath4)

        bottomText.move_to(aligned_edge=BOTTOM)

        self.set_camera_orientation(phi=2*PI/5, theta=7*PI/5, gamma=0)
        
        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 2, 2]),
            resolution=8
        ).set_color(RED)

        arrow2 = always_redraw(lambda: Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([x1.get_value(), y1.get_value(), z1.get_value()]),
            resolution=8
        ).set_color(BLUE))
        
        self.add(ax, arrow, label, arrow2, label2, labelmath1, labelmath2, labelmath3, labelmath4)
        self.begin_ambient_camera_rotation(rate=0.07)

        self.play(x1.animate.set_value(2), y1.animate.set_value(2), z1.animate.set_value(2), run_time=3, rate_func=linear)