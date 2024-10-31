#!/usr/bin/env python3

from manim import *
import numpy as np

# Set background color
config.background_color = ManimColor("#030303")

class VectorCrossProductAB(ThreeDScene):
    def construct(self):
        MathTex.set_default(font_size=32)

        # Set initial camera orientation and create 3D axes
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        # Create 3D axes and shift to the right
        axes = ThreeDAxes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1], z_range=[-3, 3, 1],
            axis_config={"include_numbers": False, "include_ticks": True, "include_tip": True},
        )

        # Axis labels
        x_label = always_redraw(lambda: MathTex("x").next_to(axes.x_axis.get_end(), RIGHT, buff=0.2).rotate(PI/2, axis=RIGHT))
        y_label = always_redraw(lambda: MathTex("y").next_to(axes.y_axis.get_end(), UP, buff=0.2).rotate(PI/2, axis=RIGHT))
        z_label = always_redraw(lambda: MathTex("z").next_to(axes.z_axis.get_end(), UP, buff=0.2).rotate(PI/2, axis=RIGHT))
        
        # Create the semi-transparent xy-plane with colored gridlines
        xy_plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": WHITE},  # Keep the gridlines white as well
            background_line_style={
                "stroke_color": BLUE,  # Blue gridlines
                "stroke_width": 2,     # Thicker gridlines for visibility
                "stroke_opacity": 0.25,  # Semi-transparent gridlines
            }
        )
        # Set initial camera orientation
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait(1)
        
        # Apply blue fill color with low opacity
        xy_plane.set_fill(BLUE, opacity=0.2)  # Blue fill with 20% opacity
        
        # Functions to turn the plane on and off
        def plane_on():
            """Add the xy plane to the scene (turn it on)"""
            self.add(xy_plane)
            
        def plane_off():
            """Remove the xy plane from the scene (turn it off)"""
            self.remove(xy_plane)
        
        # Title of the scene
        title = MathTex(r"\text{Cross-Product in a glance!}").set_color_by_gradient(BLUE, GREEN).scale(1.35)
        # Create an underline with the same width as the title
        underline = Line(
            start=title.get_left(), 
            end=title.get_right(), 
            color=BLUE
        ).next_to(title, DOWN, buff=0.1)
        upper_right_group = VGroup(title,underline).to_corner(UP + RIGHT, buff=0.25)
        # First, add the mobject group to be fixed in the frame
        
        # Then, apply the Write animation to each element in the group individually
        for mobj in upper_right_group:
            self.play(Write(mobj), run_time=1.5, rate_func=smooth)
        self.add_fixed_in_frame_mobjects(upper_right_group)
        
        # Define vector coordinates
        vector_A_coord = np.array([1, 2, 1])
        vector_B_coord = np.array([-0.5, 1.5, 1])
        vector_C_coord = np.cross(vector_A_coord, vector_B_coord)  # Cross product

        # Create Arrow3D vectors
        vector_A = Arrow3D(ORIGIN, vector_A_coord, color=GOLD)
        vector_B = Arrow3D(ORIGIN, vector_B_coord, color=BLUE_E)
        vector_C = Arrow3D(ORIGIN, vector_C_coord, color=TEAL_D, thickness=0.01)

        # Unit vector \hat{\eta} along vector C direction
        unit_vector_eta = vector_C_coord / np.linalg.norm(vector_C_coord)
        vector_eta = Arrow3D(ORIGIN, unit_vector_eta, color=WHITE)

        # Vector labels
        label_A = always_redraw(lambda: MathTex(r"\vec{A}", color=GOLD).rotate(PI/2, axis=RIGHT).next_to(vector_A.get_end(), RIGHT + UP, buff=0.1))
        label_B = always_redraw(lambda: MathTex(r"\vec{B}", color=WHITE).rotate(PI/2, axis=RIGHT).next_to(vector_B.get_end(), LEFT + UP, buff=0.1))
        label_C = always_redraw(lambda: MathTex(r"\vec{C}", color=TEAL_D).rotate(PI/2, axis=RIGHT).next_to(vector_C.get_end(), RIGHT + UP, buff=0.1))
        label_eta = always_redraw(lambda: MathTex(r"\hat{\eta}", color=WHITE).rotate(PI/2, axis=RIGHT).next_to(vector_eta.get_end(), RIGHT, buff=0.1))
        #       
        #       Parallelogram formed by vectors A and B
        parallelogram = Polygon(
            ORIGIN,
            vector_A_coord,
            vector_A_coord + vector_B_coord,
            vector_B_coord,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.35, stroke_opacity=0.5
        )
        self.move_camera(phi=75 * DEGREES, theta=-90 * DEGREES, run_time=2)
        
        # A hack to correctly rotate the camera around shifted axes
        vector_grouped = VGroup(axes, x_label, y_label, z_label, vector_A, vector_B, vector_eta, vector_C, parallelogram, label_A, label_B, label_C, label_eta)
        
        # Display the vectors, labels, and parallelogram
        self.play(Create(vector_grouped), rate_func=smooth, run_time=1.5)
        # Initially show the plane
        plane_on()
        self.move_camera(phi=60 * DEGREES, theta=-135 * DEGREES, run_time=3)
        self.wait(3)
        self.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES, zoom=1.25, run_time=3)
        self.wait(3)
        self.move_camera(phi=75 * DEGREES, theta=-90 * DEGREES, zoom=0.85, run_time=2)
        self.wait(3)
        
        # Fixed text: Cross-product equation and explanations (on the left)
        cross_product_text = MathTex(
            r"\vec{A} \times \vec{B} = \hat{\eta} \, | \vec{A} | \, | \vec{B} | \, \sin \theta_{AB} = \vec{C}"
        ).set_color_by_gradient(RED, BLUE)
        
        length_text = MathTex(
            r"| \vec{C} | = | \vec{A} | \, | \vec{B} | \, \sin \theta_{AB} = C_{AB}"
        ).set_color_by_gradient(YELLOW, BLUE)
        
        upper_left_group = VGroup(cross_product_text, length_text).arrange(DOWN, aligned_edge=LEFT).to_corner(UP + LEFT, buff=0.5)
        
        where_text = MathTex(r"\text{where:}").set_color_by_gradient(WHITE, GRAY)
        where1_text = MathTex(
            r"\theta_{AB} \text{ is the angle between } \vec{A} \text{ and } \vec{B};"
        ).set_color_by_gradient(RED, BLUE)
        
        where2_text = MathTex(
            r"\hat{\eta} \text{ is the unit vector perpendicular to both } \vec{A} \text{ and } \vec{B};"
        ).set_color_by_gradient(LIGHT_BROWN, BLUE)
        
        where3_text = MathTex(
            r"C_{AB} \text{ is the area of the parallelogram formed by } \vec{A} \text{ and } \vec{B}."
        ).set_color_by_gradient(YELLOW, RED)
        
        lower_left_group = VGroup(where_text, where1_text, where2_text, where3_text).arrange(DOWN, aligned_edge=LEFT).to_corner(DOWN + LEFT, buff=0.5)
        
        # Animate the writing of each mobject individually using `UpdateFromAlphaFunc`
        for mobj in upper_left_group:
            self.play(Write(mobj), run_time=1.5, rate_func=smooth)
            
        for mobj in lower_left_group:
            self.play(Write(mobj), run_time=1.5, rate_func=smooth)
            
        # Add the fixed frame mobjects to the scene first
        self.add_fixed_in_frame_mobjects(upper_left_group, lower_left_group)
            
        self.set_camera_orientation(phi=75 * DEGREES, zoom=0.85, frame_center=axes.get_origin())
        self.wait(1)
        self.move_camera(phi=75 * DEGREES, theta=-450 * DEGREES, zoom=0.85, run_time=10)
        self.wait(2)
        
        # Unwrite all text mobjects (upper-left, lower-left, upper-right)
        for mobj in upper_left_group:
            self.play(Unwrite(mobj), run_time=0.1, rate_func=smooth)
            
        for mobj in lower_left_group:
            self.play(Unwrite(mobj), run_time=0.1, rate_func=smooth)
            
            # Unwrite axes, vectors, labels, parallelogram, and plane
        self.play(
            Unwrite(axes),
            Unwrite(x_label), Unwrite(y_label), Unwrite(z_label),
            Unwrite(vector_A), Unwrite(vector_B), Unwrite(vector_C), Unwrite(vector_eta),
            Unwrite(label_A), Unwrite(label_B), Unwrite(label_C), Unwrite(label_eta),
            Unwrite(parallelogram),
            Unwrite(xy_plane),
            run_time=1, rate_func=smooth
        )
        
        # Final pause to ensure the screen is empty
        self.wait(1)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, zoom=1.00, run_time=0.1)
        # Colors for vector components and unit vectors
        i_color = YELLOW
        j_color = GREEN
        k_color = BLUE
        A_x_color = RED
        A_y_color = ORANGE
        A_z_color = PINK
        B_x_color = TEAL
        B_y_color = PURPLE
        B_z_color = GOLD
        
        # Define vector A = A_x * i + A_y * j + A_z * k
        vector_A = MathTex(
            r"\vec{A} = ",
            r"A_x\hat{i} + A_y\hat{j} + A_z\hat{k}",
            substrings_to_isolate=["A_x", "A_y", "A_z", r"\hat{i}", r"\hat{j}", r"\hat{k}"]
        ).scale(1.25).move_to(RIGHT * 0.0 + UP * 1.25).set_color_by_tex_to_color_map({
            "A_x": A_x_color, "A_y": A_y_color, "A_z": A_z_color,
            r"\hat{i}": i_color, r"\hat{j}": j_color, r"\hat{k}": k_color
        })
        
        # Define vector B = B_x * i + B_y * j + B_z * k
        vector_B = MathTex(
            r"\vec{B} = ",
            r"B_x\hat{i} + B_y\hat{j} + B_z\hat{k}",
            substrings_to_isolate=["B_x", "B_y", "B_z", r"\hat{i}", r"\hat{j}", r"\hat{k}"]
        ).scale(1.25).move_to(RIGHT * 0.0 + UP * 0.25).set_color_by_tex_to_color_map({
            "B_x": B_x_color, "B_y": B_y_color, "B_z": B_z_color,
            r"\hat{i}": i_color, r"\hat{j}": j_color, r"\hat{k}": k_color
        })
        
        # Group the two vectors for vertical alignment
        vectors_group = VGroup(vector_A, vector_B).arrange(DOWN, buff=0.5)
        
        # Display the 3x3 determinant setup
        determinant = MathTex(
            r"\vec{A} \times \vec{B} = \begin{vmatrix}"
            r"\hat{i} & \hat{j} & \hat{k} \\[4pt]"
            r"A_x & A_y & A_z \\[4pt]"
            r"B_x & B_y & B_z"
            r"\end{vmatrix}"
        ).scale(1.25).move_to(RIGHT * 0.0 + UP * -0.5).set_color_by_tex_to_color_map({
            "A_x": A_x_color, "A_y": A_y_color, "A_z": A_z_color,
            "B_x": B_x_color, "B_y": B_y_color, "B_z": B_z_color,
            r"\hat{i}": i_color, r"\hat{j}": j_color, r"\hat{k}": k_color
        })
        
        # Place the determinant below the vectors
        determinant.next_to(vectors_group, DOWN, buff=0.8)
        
        # Define the cross-product equation with component-wise colors
        cross_product = MathTex(
            r"\vec{A} \times \vec{B} = ",
            r"\hat{i}(", r"A_y", r"B_z", r"-", r"A_z", r"B_y", r") - ",
            r"\hat{j}(", r"A_x", r"B_z", r"-", r"A_z", r"B_x", r") + ",
            r"\hat{k}(", r"A_x", r"B_y", r"-", r"A_y", r"B_x", r")"
        ).scale(1.25).move_to(RIGHT * 0.0 + UP * -0.5).set_color_by_tex_to_color_map({
            "A_x": A_x_color, "A_y": A_y_color, "A_z": A_z_color,
            "B_x": B_x_color, "B_y": B_y_color, "B_z": B_z_color,
            r"\hat{i}": i_color, r"\hat{j}": j_color, r"\hat{k}": k_color
        })
        
        # Place the cross-product result below the determinant
        cross_product.next_to(determinant, DOWN, buff=0.8)
        
        # Center everything on the screen
        content = VGroup(vectors_group, determinant, cross_product).arrange(DOWN, buff=1).move_to(ORIGIN)
        
        # Animate everything
        self.play(Write(vector_A), Write(vector_B))
        self.wait(1)
        self.play(Write(determinant))
        self.wait(1)
        self.play(Write(cross_product))
        self.wait(2)
        
        # Fade out everything at the end
        self.play(FadeOut(content), Unwrite(title), Uncreate(underline), rate_func = smooth, run_time = 1.0)
        for mobj in upper_right_group:
            self.play(Unwrite(mobj), run_time=0.5, rate_func=smooth)
        self.wait(1)