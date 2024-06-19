from manim import *

class Embedding2(ThreeDScene):
    def construct(self):

        ax = ThreeDAxes(x_range=[-7,7], y_range=[-5,5], z_range=[-5,5]).scale(0.6)

        self.set_camera_orientation(phi=2*PI/5, theta=7*PI/5, gamma=0)
        
        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([5*0.6, 3*0.6, 4*0.6]),
            resolution=8
        ).set_color(BLUE)

        attention = Arrow3D(
            start=arrow.get_end(),
            end=np.array([5*0.6, 1*0.6, 3*0.6]),
            resolution=8
        ).set_color(YELLOW)

        new = Arrow3D(
            start=np.array([0,0,0]),
            end=np.array([5*0.6, 1*0.6, 3*0.6]),
            resolution=8
        ).set_color(PURPLE)

        self.begin_ambient_camera_rotation(rate=0.04)

        self.play(Create(ax), Create(arrow))
        self.wait(1)
        self.play(Create(attention))
        self.wait(0.5)
        self.play(Create(new))
        self.wait(1)