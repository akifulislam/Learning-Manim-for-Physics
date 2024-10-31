#!/usr/bin/env python3

from manim import *
import numpy as np

# Set background color
config.background_color = ManimColor("#030303")

class VectorCrossProductComparison(ThreeDScene):
    def construct(self):
        MathTex.set_default(font_size=32)

        # Set initial camera orientation and create 3D axes
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Create and format 3D axes for the left diagram
        axes_left = ThreeDAxes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1], z_range=[-3, 3, 1]
        )
        x_label_left = always_redraw(lambda: MathTex("x").next_to(axes_left.x_axis.get_end(), UP, buff=0.2).rotate(PI / 2, axis=RIGHT))
        y_label_left = always_redraw(lambda: MathTex("y").next_to(axes_left.y_axis.get_end(), UP, buff=0.2).rotate(PI / 2, axis=RIGHT))
        z_label_left = always_redraw(lambda: MathTex("z").next_to(axes_left.z_axis.get_end(), UP, buff=0.2).rotate(PI / 2, axis=RIGHT))
        
        # Create and format 3D axes for the right diagram
        axes_right = ThreeDAxes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1], z_range=[-3, 3, 1]
        )
        x_label_right = always_redraw(lambda: MathTex("x").next_to(axes_right.x_axis.get_end(), UP, buff=0.2).rotate(PI / 2, axis=RIGHT))
        y_label_right = always_redraw(lambda: MathTex("y").next_to(axes_right.y_axis.get_end(), UP, buff=0.2).rotate(PI / 2, axis=RIGHT))
        z_label_right = always_redraw(lambda: MathTex("z").next_to(axes_right.z_axis.get_end(), UP, buff=0.2).rotate(PI / 2, axis=RIGHT))
        
        self.wait(1)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, rate_func = smooth, run_time=2)
        self.wait(2)
        # ---------------- Diagram 1: A x B ---------------- #
        vector_A_coord_1 = np.array([1, 2, 1])
        vector_B_coord_1 = np.array([-0.5, 1.5, 1])
        vector_D_coord = -np.cross(vector_A_coord_1, vector_B_coord_1)  # Cross product
        
        # Unit vector \hat{\eta} along vector C direction
        unit_vector_eta1 = vector_D_coord / np.linalg.norm(vector_D_coord)
        vector_eta1 = Arrow3D(ORIGIN, unit_vector_eta1, color=WHITE)
        
        vector_A_1 = Arrow3D(ORIGIN, vector_A_coord_1, color=GOLD)
        vector_B_1 = Arrow3D(ORIGIN, vector_B_coord_1, color=WHITE)
        vector_D = Arrow3D(ORIGIN, vector_D_coord, color=TEAL_D, thickness=0.01)

        label_A_1 = MathTex(r"\vec{A}", color=GOLD).rotate(PI/2, axis=RIGHT).next_to(vector_A_1.get_end(), RIGHT + UP, buff=0.1)
        label_B_1 = MathTex(r"\vec{B}", color=BLUE_E).rotate(PI/2, axis=RIGHT).next_to(vector_B_1.get_end(), LEFT + UP, buff=0.1)
        label_D = MathTex(r"\vec{D}", color=TEAL_D).rotate(PI/2, axis=RIGHT).next_to(vector_D.get_end(), RIGHT + UP, buff=0.1)
#       label_eta1 = always_redraw(lambda: MathTex(r"\hat{\eta}_1", color=WHITE)
#                                           .rotate(PI / 2, axis=RIGHT)
#                                           .next_to(vector_eta1.get_end(), buff=0.1))

        parallelogram_1 = Polygon(
            ORIGIN,
            vector_A_coord_1,
            vector_A_coord_1 + vector_B_coord_1,
            vector_B_coord_1,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.35
        )

        group_1 = VGroup(
            axes_left, x_label_left, y_label_left, z_label_left, vector_A_1, vector_B_1, vector_D,
            label_A_1, label_B_1, label_D, parallelogram_1
        ).shift(LEFT * 4).scale(0.75)

        # ---------------- Diagram 2: B x A ---------------- #
        vector_A_coord_2 = np.array([1, 2, 1])
        vector_B_coord_2 = np.array([-0.5, 1.5, 1])
        vector_C_coord = np.cross(vector_A_coord_2, vector_B_coord_2)  # Cross product

        vector_A_2 = Arrow3D(ORIGIN, vector_A_coord_2, color=GOLD)
        vector_B_2 = Arrow3D(ORIGIN, vector_B_coord_2, color=WHITE)
        vector_C = Arrow3D(ORIGIN, vector_C_coord, color=TEAL_D, thickness=0.01)
        # Unit vector \hat{\eta} along vector C direction
        unit_vector_eta2 = vector_C_coord / np.linalg.norm(vector_C_coord)
        vector_eta2 = Arrow3D(ORIGIN, unit_vector_eta2, color=WHITE)

        label_A_2 = MathTex(r"\vec{A}", color=GOLD).rotate(PI/2, axis=RIGHT).next_to(vector_A_2.get_end(), RIGHT + UP, buff=0.1)
        label_B_2 = MathTex(r"\vec{B}", color=BLUE_E).rotate(PI/2, axis=RIGHT).next_to(vector_B_2.get_end(), LEFT + UP, buff=0.1)
        label_C = MathTex(r"\vec{C}", color=TEAL_D).rotate(PI/2, axis=RIGHT).next_to(vector_C.get_end(), RIGHT + UP, buff=0.1)
#       label_eta2 = always_redraw(lambda: MathTex(r"\hat{\eta}_2", color=WHITE)
#                                           .rotate(PI / 2, axis=RIGHT)
#                                           .next_to(vector_eta2.get_end(), buff=0.1))

        parallelogram_2 = Polygon(
            ORIGIN,
            vector_A_coord_2,
            vector_A_coord_2 + vector_B_coord_2,
            vector_B_coord_2,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.35
        )

        group_2 = VGroup(
            axes_right, x_label_right, y_label_right, z_label_right, vector_A_2, vector_B_2, vector_C,
            label_A_2, label_B_2, label_C, parallelogram_2
        ).shift(RIGHT * 4).scale(0.75)

        # ---------------- Add both groups to the scene ---------------- #
        self.play(Create(group_1), Create(group_2), run_time=2)
        self.wait(2)

        # Rotate the camera around the combined scene
        self.move_camera(phi=75 * DEGREES, theta=-450 * DEGREES, run_time=10)
        self.wait(2)

        # Fade out both diagrams
        self.play(FadeOut(group_1), FadeOut(group_2), run_time=1)
        self.wait(1)