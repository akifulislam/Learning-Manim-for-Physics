#!/usr/bin/env python3

from manim import *
import numpy as np

# Set background color
config.background_color = ManimColor("#030303")

class ScalarField3DTransform(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        # Title of the scene
        title = MathTex(r"\text{Say Hello! to Scalar Fields}").set_color_by_gradient(BLUE, GREEN).scale(1.0)
        # Create an underline with the same width as the title
        underline = Line(
            start=title.get_left(), 
            end=title.get_right(), 
            color=BLUE
        ).next_to(title, DOWN, buff=0.1)
        upper_right_group = VGroup(title, underline).to_corner(UP + RIGHT, buff=0.25)
        # Add Axes and First Surface
        for mobj in upper_right_group:
            self.play(Write(mobj), run_time=1.5, rate_func=smooth)
        self.add_fixed_in_frame_mobjects(upper_right_group)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=1.5)
        # 3D Axes and Labels
        axes_3D = ThreeDAxes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-1, 1, 0.5],
            axis_config={"include_ticks": True, "include_tip": True, "tip_length": 0.2}
        )
        x_label = MathTex("x").next_to(axes_3D.x_axis.get_end(), RIGHT, buff=0.2).rotate(PI / 2, axis=RIGHT)
        y_label = MathTex("y").next_to(axes_3D.y_axis.get_end(), UP, buff=0.2).rotate(PI / 2, axis=RIGHT)
        z_label = MathTex("z").next_to(axes_3D.z_axis.get_end(), UP * 0.75, buff=0.2).rotate(PI / 2, axis=RIGHT)

        # Physics-related Scalar Fields
        surface_1 = Surface(
            lambda u, v: np.array([u, v, np.sin(np.sqrt(u**2 + v**2))]),  # Wave propagation
            u_range=[-3, 3], v_range=[-3, 3], resolution=(150, 150)
        )

        surface_2 = Surface(
            lambda u, v: np.array([u, v, np.cos(u) * np.cos(v)]),  # Harmonic potential
            u_range=[-3, 3], v_range=[-3, 3], resolution=(150, 150)
        )

        surface_3 = Surface(
            lambda u, v: np.array([u, v, 2 * np.exp(-u**2 - v**2)]),  # Higher peak Gaussian distribution
            u_range=[-3, 3], v_range=[-3, 3], resolution=(150, 150)
        )

        surface_4 = Surface(
            lambda u, v: np.array([u, v, np.tanh(u * v)]),  # Hyperbolic field
            u_range=[-3, 3], v_range=[-3, 3], resolution=(150, 150)
        )

        surface_5 = Surface(
            lambda u, v: np.array([u, v, np.log(1 + u**2 + v**2)]),  # Logarithmic potential
            u_range=[-3, 3], v_range=[-3, 3], resolution=(150, 150)
        )

        # Labels for the Scalar Fields with Distinct Color Gradients
        label_1 = MathTex(r"f(x, y) = \sin(\sqrt{x^2 + y^2})") \
            .to_corner(UP + LEFT, buff=0.25) \
            .set_color_by_gradient(BLUE, GREEN).scale(1.00)
        
        label_2 = MathTex(r"g(x, y) = \cos(x) \cos(y)") \
            .to_corner(UP + LEFT, buff=0.25) \
            .set_color_by_gradient(YELLOW, ORANGE).scale(1.00)
        
        label_3 = MathTex(r"h(x, y) = 2 e^{-x^2 - y^2}") \
            .to_corner(UP + LEFT, buff=0.25) \
            .set_color_by_gradient(RED, PURPLE).scale(1.00)
        
        label_4 = MathTex(r"p(x, y) = \tanh(x y)") \
            .to_corner(UP + LEFT, buff=0.25) \
            .set_color_by_gradient(TEAL, GOLD).scale(1.00)
        
        label_5 = MathTex(r"q(x, y) = \log(1 + x^2 + y^2)") \
            .to_corner(UP + LEFT, buff=0.25) \
            .set_color_by_gradient(PINK, BLUE).scale(1.00)

        # Helper function to add labels as fixed-in-frame mobjects
        def create_fixed_label(label):
            self.add_fixed_in_frame_mobjects(label)
            
        grouped_mobjects = VGroup(axes_3D, x_label, y_label, z_label, surface_1)
        self.play(Create(grouped_mobjects), rate_func = smooth, run_time = 1.5)
        create_fixed_label(label_1)
        self.wait(2)
        # Begin rotating the camera to enhance the 3D view
        self.begin_ambient_camera_rotation(rate=0.1)
        
        self.play(
            Transform(surface_1, surface_2),
            Transform(label_1, label_2),
            run_time=2
        )
        self.wait(1)
        self.play(
            Transform(surface_1, surface_3),
            Transform(label_1, label_3),
            run_time=2
        )
        self.wait(1)
        self.play(
            Transform(surface_1, surface_4),
            Transform(label_1, label_4),
            run_time=2
        )
        self.wait(1)
        self.play(
            Transform(surface_1, surface_5),
            Transform(label_1, label_5),
            run_time=2
        )
        self.wait(1)
        self.play(
            Unwrite(x_label), Unwrite(y_label), Unwrite(z_label),
            Uncreate(axes_3D), Uncreate(surface_1), Unwrite(label_1)
        )
        self.stop_ambient_camera_rotation()
        # Unwrite the title and underline
        for mobj in upper_right_group:
            self.play(Unwrite(mobj), run_time=0.5, rate_func=smooth)
        self.wait(1)