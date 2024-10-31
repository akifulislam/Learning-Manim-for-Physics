from manim import *
import numpy as np

# Set background color
config.background_color = ManimColor("#030303")

class VectorsIn2D(Scene):
    MathTex.set_default(font_size=32)
    def construct(self):
        # Create a number plane
        plane = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-3.5, 3.5, 0.5),
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

        # Title and underline
        title = MathTex(r"\text{Vector Addition in a glance!}").move_to(RIGHT * 3.5 + UP * 3.5).set_color_by_gradient(BLUE, GREEN).scale(1.25)
        underline = Line(start=title.get_left(), end=title.get_right(), color=BLUE).next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline), rate_func=smooth, run_time=1.5)

        # Axis labels with updaters
        x_label = always_redraw(lambda: MathTex("x").next_to(plane.x_axis.get_end(), RIGHT, buff=0.2))
        y_label = always_redraw(lambda: MathTex("y").next_to(plane.y_axis.get_end(), LEFT, buff=0.2))

        # Display plane and labels
        self.play(Create(plane), Write(x_label), Write(y_label), run_time=1.5)

        # Define vectors with only coordinates and colors
        vectors = [
                    {"coord": np.array([2, 2, 0]), "color": RED},
                    {"coord": np.array([-4, 2.5, 0]), "color": GREEN},
                    {"coord": np.array([-3, -2, 0]), "color": YELLOW},
                    {"coord": np.array([3, -3, 0]), "color": PURPLE},
                ]
        

        vector_mobjects = VGroup()
        projection_mobjects = VGroup()

        # Draw each vector and its projections
        for vector in vectors:
            arrow = Arrow(ORIGIN, vector["coord"], buff=0, color=vector["color"])
            x_proj = DashedLine([vector["coord"][0], 0, 0], vector["coord"], color=vector["color"])
            y_proj = DashedLine([0, vector["coord"][1], 0], vector["coord"], color=vector["color"])
            
            # Add to mobjects group
            vector_mobjects.add(arrow)
            projection_mobjects.add(x_proj, y_proj)
            
            # Play animations
            self.play(FadeIn(arrow), run_time=1.0)
            self.play(Create(x_proj), Create(y_proj), run_time=1.0)

        # Helper function to compute the magnitude of a vector
        def magnitude(vec):
            return np.linalg.norm(vec)
        
        # Calculate vector components and magnitudes
        A = vectors[0]["coord"]
        B = vectors[1]["coord"]
        C = vectors[2]["coord"]
        D = vectors[3]["coord"]
        
        # Create labels for coordinates, components, and magnitudes
        coord_labels = VGroup(
            MathTex(rf"\vec{{A}} = {A[0]} \hat{{i}} + {A[1]} \hat{{j}}").set_color(RED).move_to([2, 2.5, 0]),
            MathTex(rf"\vec{{B}} = {B[0]} \hat{{i}} + {B[1]} \hat{{j}}").set_color(GREEN).move_to([-4.75, 2.85, 0]),
            MathTex(rf"\vec{{C}} = {C[0]} \hat{{i}} + {C[1]} \hat{{j}}").set_color(YELLOW).move_to([-4, -2.25, 0]),
            MathTex(rf"\vec{{D}} = {D[0]} \hat{{i}} + {D[1]} \hat{{j}}").set_color(PURPLE).move_to([4.25, -3.0, 0])
        )

        angle_labels = VGroup(
            MathTex(r"\theta = \tan^{-1}\frac{|A_y|}{|A_x|}").set_color_by_gradient(BLUE, GREEN).move_to([4.5, 1.9, 0]),
            MathTex(r"\theta = \pi - \tan^{-1}\frac{|B_y|}{|B_x|}").set_color_by_gradient(BLUE, GREEN).move_to([-1.5, 2, 0]),
            MathTex(r"\theta = \pi + \tan^{-1}\frac{|C_y|}{|C_x|}").set_color_by_gradient(BLUE, GREEN).move_to([-5, -1.55, 0]),
            MathTex(r"\theta = 2\pi - \tan^{-1}\frac{|D_y|}{|D_x|}").set_color_by_gradient(BLUE, GREEN).move_to([5, -2, 0])
        )

        component_labels = VGroup(
                    MathTex(rf"A_x = {A[0]}").set_color(RED).move_to([0.85, 1.75, 0]),
                    MathTex(rf"A_y = {A[1]}").set_color(RED).move_to([2.75, 1.0, 0]),
                    MathTex(rf"B_x = {B[0]}").set_color(GREEN).move_to([-2, 3.0, 0]),
                    MathTex(rf"B_y = {B[1]}").set_color(GREEN).move_to([-4.75, 1.25, 0]),
                    MathTex(rf"C_x = {C[0]}").set_color(YELLOW).move_to([-1.5, -2.5, 0]),
                    MathTex(rf"C_y = {C[1]}").set_color(YELLOW).move_to([-3.85, -0.85, 0]),
                    MathTex(rf"D_x = {D[0]}").set_color(PURPLE).move_to([1.5, -3.5, 0]),
                    MathTex(rf"D_y = {D[1]}").set_color(PURPLE).move_to([4.0, -1.0, 0])
                )
        
        magnitude_labels = VGroup(
            MathTex(rf"|\vec{{A}}| = {magnitude(A):.2f}").set_color(RED).rotate(PI / 4).move_to([1.25, 0.75, 0]),
            MathTex(rf"|\vec{{B}}| = {magnitude(B):.2f}").set_color(GREEN).rotate(-33.69 * DEGREES).move_to([-1, 1.0, 0]),
            MathTex(rf"|\vec{{C}}| = {magnitude(C):.2f}").set_color(YELLOW).rotate(33.69 * DEGREES).move_to([-1.9, -0.85, 0]),
            MathTex(rf"|\vec{{D}}| = {magnitude(D):.2f}").set_color(PURPLE).rotate(-PI / 4).move_to([1.75, -1.25, 0])
        )

        # Animate the labels
        self.play(Write(coord_labels), Write(angle_labels), Write(component_labels), Write(magnitude_labels), run_time=2)

        # Wait and fade out everything
        self.wait(2)
        self.play(
            FadeOut(vector_mobjects), 
            FadeOut(projection_mobjects), 
            FadeOut(coord_labels), 
            FadeOut(angle_labels), 
            FadeOut(component_labels), 
            FadeOut(magnitude_labels), 
            Uncreate(plane), Unwrite(x_label), Unwrite(y_label),
            rate_func=smooth, run_time=2
        )
        # Colors for unit vectors and vector components
        I_COLOR = TEAL
        J_COLOR = ORANGE
        A_x_color = RED
        B_x_color = GREEN
        C_x_color = YELLOW
        D_x_color = PURPLE
        
        A_y_color = RED
        B_y_color = GREEN
        C_y_color = YELLOW
        D_y_color = PURPLE
        
        # Extract x and y components from the vectors
        A_x, A_y = vectors[0]["coord"][:2]
        B_x, B_y = vectors[1]["coord"][:2]
        C_x, C_y = vectors[2]["coord"][:2]
        D_x, D_y = vectors[3]["coord"][:2]
        
        # Calculate the resultant components R_x and R_y
        R_x = A_x + B_x + C_x + D_x
        R_y = A_y + B_y + C_y + D_y
        
        # Create the resultant vector labels with appropriate color mapping
        resultant_labels = VGroup(
            MathTex(
                r"\text{Resultant Vector } \vec{R} = \vec{A} + \vec{B} + \vec{C} + \vec{D} = R_x\hat{i} + R_y\hat{j}",
                substrings_to_isolate=[r"\vec{A}", r"\vec{B}", r"\vec{C}", r"\vec{D}", r"\hat{i}", r"\hat{j}"]
            ).set_color_by_tex_to_color_map({
                r"\vec{A}": A_x_color, r"\vec{B}": B_x_color, r"\vec{C}": C_x_color, r"\vec{D}": D_x_color,
                r"\hat{i}": I_COLOR, r"\hat{j}": J_COLOR
            }).move_to([0, 2, 0]).scale(1.25),
            
            MathTex(
                rf"R_x = A_x + B_x + C_x + D_x = {A_x} + ({B_x}) + ({C_x}) + {D_x} = {R_x}",
                substrings_to_isolate=["A_x", "B_x", "C_x", "D_x"]
            ).set_color_by_tex_to_color_map({
                "A_x": A_x_color, "B_x": B_x_color, "C_x": C_x_color, "D_x": D_x_color
            }).move_to([0, 1, 0]).scale(1.25),
            
            MathTex(
                rf"R_y = A_y + B_y + C_y + D_y = {A_y} + {B_y} + ({C_y}) + ({D_y}) = {R_y}",
                substrings_to_isolate=["A_y", "B_y", "C_y", "D_y"]
            ).set_color_by_tex_to_color_map({
                "A_y": A_y_color, "B_y": B_y_color, "C_y": C_y_color, "D_y": D_y_color
            }).move_to([0, 0, 0]).scale(1.25),
            
            MathTex(
                rf"\vec{{R}} = ({R_x})\hat{{i}} + ({R_y})\hat{{j}}",
                substrings_to_isolate=[r"\hat{i}", r"\hat{j}"]
            ).set_color_by_tex_to_color_map({
                r"\hat{i}": I_COLOR, r"\hat{j}": J_COLOR
            }).move_to([0, -1.0, 0]).scale(1.25),
            
            MathTex(
                r"\text{Find the angle by checking the quadrant.}",
                substrings_to_isolate=[r"\hat{i}", r"\hat{j}"]
            ).set_color_by_tex_to_color_map({
                r"\hat{i}": I_COLOR, r"\hat{j}": J_COLOR
            }).move_to([0, -2.0, 0]).scale(1.25)
        )
        # Animate the display of the resultant vector labels
        self.play(Write(resultant_labels), run_time=2)
        self.wait(3)
        self.play(Unwrite(resultant_labels), Unwrite(title), Uncreate(underline), run_time=1.5)
        self.wait(1)