#!/usr/bin/env python3

from manim import *
import numpy as np

# Set background color
config.background_color = ManimColor("#030303")

class VectorField3DTransform(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES, zoom = 0.85)
        # Create a number axes_2D
        axes_2D = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-3.0, 3.0, 0.5),
            axis_config={
                "include_numbers": False,
                "include_ticks": True,
                "include_tip": True,
                "tip_length": 0.2
            },
            background_line_style={
                "stroke_opacity": 0.15,
                "stroke_color": BLUE,
                "stroke_width": 1,
            },
        )
        
        # Title of the scene
        title = MathTex(r"\text{Say Hello! to Vector Fields}").set_color_by_gradient(BLUE, GREEN).scale(1.0)
        # Create an underline with the same width as the title
        underline = Line(
            start=title.get_left(), 
            end=title.get_right(), 
            color=BLUE
        ).next_to(title, DOWN, buff=0.1)
        upper_right_group = VGroup(title,underline).to_corner(UP + RIGHT, buff=0.25)
        for mobj in upper_right_group:
            self.play(Write(mobj), run_time=1.5, rate_func=smooth)
        self.add_fixed_in_frame_mobjects(upper_right_group)
        
        # Axis labels with updaters
        x_label = always_redraw(lambda: MathTex("x").next_to(axes_2D.x_axis.get_end(), RIGHT, buff=0.2))
        y_label = always_redraw(lambda: MathTex("y").next_to(axes_2D.y_axis.get_end(), UP + LEFT, buff=0.2))
        self.move_camera(phi=0 * DEGREES, theta=-90* DEGREES, run_time=0.1)
        # Display axes_2D and labels
        self.play(Create(axes_2D), Write(x_label), Write(y_label), zoom = 0.85, run_time=1.5)
        
        # Define new vector field functions with their corresponding labels and colors
        functions_2D = [
            {
                "func": lambda pos: np.array([-pos[1], pos[0], 0]),  # Rotation around the origin
                "label": r"\vec{F}(x, y) = -y\hat{i} + x\hat{j}",
                "color": [RED, PURPLE],
            },
            {
                "func": lambda pos: np.array([pos[0] * np.sin(pos[1]), pos[1] * np.cos(pos[0]), 0]),  # Sin-Cos pattern
                "label": r"\vec{F}(x, y) = x\sin(y)\hat{i} + y\cos(x)\hat{j}",
                "color": [YELLOW, BLUE],
            },
            {
                "func": lambda pos: np.array([np.exp(-pos[0]**2), np.exp(-pos[1]**2), 0]),  # Gaussian decay
                "label": r"\vec{F}(x, y) = e^{-x^2}\hat{i} + e^{-y^2}\hat{j}",
                "color": [GREEN, ORANGE],
            },
            {
                "func": lambda pos: np.array([np.tan(pos[0]), np.tan(pos[1]), 0]),  # Tangent field
                "label": r"\vec{F}(x, y) = \tan(x)\hat{i} + \tan(y)\hat{j}",
                "color": [BLUE, RED],
            },
            {
                "func": lambda pos: np.array([np.sin(pos[0] * pos[1]), np.cos(pos[0] + pos[1]), 0]),  # Mixed sin-cos pattern
                "label": r"\vec{F}(x, y) = \sin(xy)\hat{i} + \cos(x + y)\hat{j}",
                "color": [PURPLE, YELLOW],
            },
        ]
    
        # Create the initial vector field and label
        initial_field_data = functions_2D[0]
        vector_field_2D = ArrowVectorField(
            initial_field_data["func"],
            colors=initial_field_data["color"],
            x_range=[-3, 3],
            y_range=[-3, 3],
            length_func=lambda norm: 0.6,
        )
        label = MathTex(initial_field_data["label"]).move_to(RIGHT * 0 + UP * -4.0 + OUT * 0).set_color_by_gradient(*initial_field_data["color"])
        
#       self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, zoom = 0.75, run_time=0.1)
        # Add the first vector field and label to the scene
        self.play(Create(vector_field_2D))
        self.wait(2)

        # Iterate through the remaining fun vector field functions
        for field_data in functions_2D[1:]:
            new_vector_field_2D = ArrowVectorField(
                field_data["func"],
                colors=field_data["color"],
                x_range=[-3, 3],
                y_range=[-3, 3],
                length_func=lambda norm: 0.6
            )
            new_label = MathTex(field_data["label"]).move_to(RIGHT * 0 + UP * -4.0 + OUT * 0).set_color_by_gradient(*field_data["color"])

            self.play(
                Transform(vector_field_2D, new_vector_field_2D),
                Transform(label, new_label),
                run_time=3,
            )
            self.wait(2)

        self.play(Unwrite(axes_2D), Unwrite(x_label), Unwrite(label), Unwrite(new_label), Unwrite(y_label))
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, zoom = 0.75, run_time=1.5)
        # Transition to 3D Scene (Shift the Plane Upward and Rotate into 3D)
        self.play(vector_field_2D.animate.shift(OUT * 2))
        
        # Create a 3D axes_3D
        axes_3D = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            axis_config={
                "color": WHITE,
                "include_ticks": True,  # Enable ticks
                "include_tip": True,    # Add arrow tips
                "tip_length": 0.2       # Control arrow tip size
            },
        )
        x_label = always_redraw(lambda: MathTex("x").next_to(axes_3D.x_axis.get_end(), RIGHT, buff=0.2).rotate(PI/2, axis=RIGHT))
        y_label = always_redraw(lambda: MathTex("y").next_to(axes_3D.y_axis.get_end(), UP, buff=0.2).rotate(PI/2, axis=RIGHT))
        z_label = always_redraw(lambda: MathTex("z").next_to(axes_3D.z_axis.get_end(), UP*0.75, buff=0.2).rotate(PI/2, axis=RIGHT))
        
        # Create the axes and labels
        self.play(Create(axes_3D), Write(x_label), Write(y_label), Write(z_label), run_time=1.0, rate_func=smooth)
        
        # Vector Field 1: Rotation in 3D Space
        vector_field_1 = ArrowVectorField(
            lambda pos: np.array([-pos[1], pos[0], pos[2]]),
            colors=[RED, PURPLE],
            x_range=[-3, 3, 0.75],
            y_range=[-3, 3, 0.75],
            z_range=[-3, 3, 0.75],
            length_func=lambda norm: 0.6
        )
        
        # Vector Field 2: Sin-Cos Field in 3D
        vector_field_2 = ArrowVectorField(
            lambda pos: np.array([np.sin(pos[0]), np.cos(pos[1]), np.sin(pos[2])]),
            colors=[YELLOW, GREEN],
            x_range=[-3, 3, 0.75],
            y_range=[-3, 3, 0.75],
            z_range=[-3, 3, 0.75],
            length_func=lambda norm: 0.6
        )
        
        # Vector Field 3: Complex Scaling Field
        vector_field_3 = ArrowVectorField(
            lambda pos: np.array([pos[0] * np.sin(pos[1]), pos[1] * np.cos(pos[2]), pos[2] * np.sin(pos[0])]),
            colors=[BLUE, ORANGE],
            x_range=[-3, 3, 0.75],
            y_range=[-3, 3, 0.75],
            z_range=[-3, 3, 0.75],
            length_func=lambda norm: 0.6
        )
        
        # Vector Field 4: Gaussian Decay Field
        vector_field_4 = ArrowVectorField(
            lambda pos: np.array([np.exp(-pos[0]**2), np.exp(-pos[1]**2), np.exp(-pos[2]**2)]),
            colors=[GREEN, PINK],
            x_range=[-3, 3, 0.75],
            y_range=[-3, 3, 0.75],
            z_range=[-3, 3, 0.75],
            length_func=lambda norm: 0.6
        )
        
        # Vector Field 5: Tangent Field in 3D
        vector_field_5 = ArrowVectorField(
            lambda pos: np.array([np.tan(pos[0]), np.tan(pos[1]), np.tan(pos[2])]),
            colors=[PURPLE, YELLOW],
            x_range=[-3, 3, 0.75],
            y_range=[-3, 3, 0.75],
            z_range=[-3, 3, 0.75],
            length_func=lambda norm: 0.6
        )
        
        # Morph vector arrows from 2D to 3D, starting with vector_field_5
#       self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, zoom = 0.75, run_time=1.5)
        
        # Create vector_field_5 on the screen
        self.play(Transform(vector_field_2D, vector_field_5), run_time=2)
        
        # Create fixed-in-frame labels with animations
        def create_fixed_label(label):
#           self.play(Write(label), run_time=1.5, rate_func=smooth)
            self.add_fixed_in_frame_mobjects(label)
            
        # Define the labels
        label_1 = MathTex(r"\vec{F}(x, y, z) = -y\hat{i} + x\hat{j} + z\hat{k}").move_to(RIGHT * -3.0 + UP * 3.0 + OUT*0).set_color_by_gradient(RED, PURPLE).scale(0.7)
        label_2 = MathTex(r"\vec{F}(x, y, z) = \sin(x)\hat{i} + \cos(y)\hat{j} + \sin(z)\hat{k}").move_to(RIGHT * -3.0 + UP * 3.0 + OUT*0).set_color_by_gradient(YELLOW, GREEN).scale(0.7)
        label_3 = MathTex(r"\vec{F}(x, y, z) = x\sin(y)\hat{i} + y\cos(z)\hat{j} + z\sin(x)\hat{k}").move_to(RIGHT * -3.0 + UP * 3.0 + OUT*0).set_color_by_gradient(BLUE, ORANGE).scale(0.7)
        label_4 = MathTex(r"\vec{F}(x, y, z) = e^{-x^2}\hat{i} + e^{-y^2}\hat{j} + e^{-z^2}\hat{k}").move_to(RIGHT * -3.0 + UP * 3.0 + OUT*0).set_color_by_gradient(GREEN, PINK).scale(0.7)
        label_5 = MathTex(r"\vec{F}(x, y, z) = \tan(x)\hat{i} + \tan(y)\hat{j} + \tan(z)\hat{k}").move_to(RIGHT * -3.0 + UP * 3.0 + OUT*0).set_color_by_gradient(PURPLE, YELLOW).scale(0.7)
        
        # Add the labels as fixed frame mobjects with animation
        create_fixed_label(label_5)
        self.wait(1)
#       self.play(Transform(label_1, label_2), run_time=2)
#       create_fixed_label(label_2)
#       
#       self.wait(1)
#       self.play(Transform(label_2, label_3), run_time=2)
#       create_fixed_label(label_3)
#       
#       self.wait(1)
#       self.play(Transform(label_3, label_4), run_time=2)
#       create_fixed_label(label_4)
#       
#       self.wait(1)