#!/usr/bin/env python3

from manim import *  # Version 0.18.0
import numpy as np

# Set background color
config.background_color = ManimColor("#030303")

class VectorResolution(Scene):
    def construct(self):
        MathTex.set_default(font_size=32)
        # Create a number plane and shift it left
        plane = NumberPlane(
            x_range=(-4, 4, 1),
            y_range=(-3, 3, 1),
            axis_config={
                "include_numbers": True, 
                "include_ticks": True, 
                "include_tip": True
            },
            background_line_style={
                "stroke_opacity": 0.15, 
                "stroke_color": BLUE, 
                "stroke_width": 1
            },
        ).shift(LEFT * 2.5)
        
        # Title of the scene
        title = MathTex(r"\text{Vectors in a glance!}").move_to(
            RIGHT * 1.0 + UP * 3.5
        ).set_color_by_gradient(BLUE, GREEN).scale(1.5)
        # Create an underline with the same width as the title
        underline = Line(
            start=title.get_left(), 
            end=title.get_right(), 
            color=BLUE
        ).next_to(title, DOWN, buff=0.1)  # Adjust position slightly below the title
        self.play(Write(title), Create(underline), rate_func=smooth, run_time=1.5)
        
        # Axis labels with updaters to adjust their positions dynamically
        x_label = always_redraw(lambda: MathTex("x").next_to(plane.x_axis.get_end(), RIGHT, buff=0.2))
        y_label = always_redraw(lambda: MathTex("y").next_to(plane.y_axis.get_end(), UP, buff=0.2))
        
        # Vector B starts on the x-axis and will rotate clockwise
        vector_b_coords = np.array([2.0, 0, 0])
        vector_b = plane.get_vector(vector_b_coords, color=BLUE)
        vector_b_label = MathTex(r"\vec{B}", color=BLUE).next_to(vector_b, direction=RIGHT + UP * 0.25, buff=0.1)
        
        # Create vertical and horizontal lines from the end of vector B
        vector_b_vertical_line = plane.get_vertical_line(vector_b.get_end(), color=YELLOW)
        vector_b_horizontal_line = plane.get_horizontal_line(vector_b.get_end(), color=YELLOW)

        # Create labels for the horizontal and vertical lines
        B_x_label = MathTex("B_x", color=YELLOW).next_to(vector_b_horizontal_line, DOWN, buff=0.2)
        B_y_label = MathTex("B_y", color=YELLOW).next_to(vector_b_vertical_line, RIGHT, buff=0.2)

        theta_tracker = ValueTracker(0)
        # Headers and dynamically updated mathematical notations
        header_vector = MathTex(r"\text{Vector Notation}").to_corner(UP + RIGHT, buff=1)
        vector_component_text = always_redraw(lambda: MathTex(
            r"\vec{B} = "
            + f"{round(2.0 * np.cos(theta_tracker.get_value() * DEGREES), 2)} \\hat{{i}} + "
            + f"{round(2.0 * np.sin(theta_tracker.get_value() * DEGREES), 2)} \\hat{{j}}"
        ).next_to(header_vector, DOWN, aligned_edge=LEFT).set_color_by_gradient(BLUE, GREEN))

        header_components = MathTex(r"\text{Components}").next_to(vector_component_text, DOWN, buff=0.4)
        bx_by_text = always_redraw(lambda: VGroup(
            MathTex(
                r"B_x = |\vec{B}|\cos\theta = "
                + f"{round(2.0 * np.cos(theta_tracker.get_value() * DEGREES), 2)}"
            ),
            MathTex(
                r"B_y = |\vec{B}|\sin\theta = "
                + f"{round(2.0 * np.sin(theta_tracker.get_value() * DEGREES), 2)}"
            )
        ).arrange(DOWN, aligned_edge=LEFT).next_to(header_components, DOWN, buff=0.4).set_color_by_gradient(YELLOW, ORANGE))

        header_magnitude = MathTex(r"\text{Magnitude}").next_to(bx_by_text, DOWN, buff=0.4)
        magnitude_text = always_redraw(lambda: MathTex(
            r"|\vec{B}| = \sqrt{B_x^2 + B_y^2} = "
            + f"{round(np.sqrt((2.0 * np.cos(theta_tracker.get_value() * DEGREES))**2 + (2.0 * np.sin(theta_tracker.get_value() * DEGREES))**2), 2)}"
        ).next_to(header_magnitude, DOWN, buff=0.4).set_color_by_gradient(GREEN, BLUE))

        header_unit_vector = MathTex(r"\text{Unit Vector}").next_to(magnitude_text, DOWN, buff=0.4)
        unit_vector_text = always_redraw(lambda: MathTex(
            r"\hat{n}_B = \frac{\vec{B}}{|\vec{B}|} = "
            + f"{round(np.cos(theta_tracker.get_value() * DEGREES) / np.linalg.norm([np.cos(theta_tracker.get_value() * DEGREES), np.sin(theta_tracker.get_value() * DEGREES)]), 2)} \\hat{{i}} + "
            + f"{round(np.sin(theta_tracker.get_value() * DEGREES) / np.linalg.norm([np.cos(theta_tracker.get_value() * DEGREES), np.sin(theta_tracker.get_value() * DEGREES)]), 2)} \\hat{{j}}"
        ).next_to(header_unit_vector, DOWN, buff=0.4).set_color_by_gradient(RED, YELLOW))

        # Theta text 1: 0 to 90 degrees
        theta_text_1 = always_redraw(lambda: MathTex(
            r"\theta = \tan^{-1}\frac{|B_y|}{|B_x|} = "
            + f"{round(np.degrees(np.arctan(abs(np.sin(theta_tracker.get_value() * DEGREES)) / abs(np.cos(theta_tracker.get_value() * DEGREES)))), 2)}^\circ"
        ).move_to(RIGHT * 0 + UP * 2.5 + OUT * 0).set_color_by_gradient(RED, ORANGE))
        
        # Theta text 2: π - arctan(...) = result
        theta_text_2 = always_redraw(lambda: MathTex(
            r"\theta = \pi - \tan^{-1}\frac{|B_y|}{|B_x|} = "
            + f"{round(180 - abs(np.degrees(np.arctan(np.sin(theta_tracker.get_value() * DEGREES) / np.cos(theta_tracker.get_value() * DEGREES)))), 2)}^\circ"
        ).move_to(RIGHT * -4.85 + UP * 3.0 + OUT * 0).set_color_by_gradient(BLUE, PURPLE))
        
        # Theta text 3: π + arctan(...) = result
        theta_text_3 = always_redraw(lambda: MathTex(
            r"\theta = \pi + \tan^{-1}\frac{|B_y|}{|B_x|} = "
            + f"{round(180 + abs(np.degrees(np.arctan(np.sin(theta_tracker.get_value() * DEGREES) / np.cos(theta_tracker.get_value() * DEGREES)))), 2)}^\circ"
        ).move_to(RIGHT * -4.85 + UP * -3.0 + OUT * 0).set_color_by_gradient(GREEN, YELLOW))
        
        # Theta text 4: 2π - arctan(...) = result
        theta_text_4 = always_redraw(lambda: MathTex(
            r"\theta = 2\pi - \tan^{-1}\frac{|B_y|}{|B_x|} = "
            + f"{round(360 - abs(np.degrees(np.arctan(np.sin(theta_tracker.get_value() * DEGREES) / np.cos(theta_tracker.get_value() * DEGREES)))), 2)}^\circ"
        ).move_to(RIGHT * 0.5 + UP * -3.25 + OUT * 0).set_color_by_gradient(GRAY_A, YELLOW_C))
        # Add elements to the scene
        self.play(Create(plane), Write(x_label), Write(y_label), rate_func=exponential_decay, run_time=1.5)
        self.play(
            Write(vector_b), Write(vector_b_label),
            Write(header_vector), Write(vector_component_text),
            Write(header_components), Write(bx_by_text),
            Write(header_magnitude), Write(magnitude_text),
            Write(header_unit_vector), Write(unit_vector_text),
            Write(vector_b_horizontal_line), Write(vector_b_vertical_line),
            Write(B_x_label), Write(B_y_label),
            rate_func=smooth, run_time=2
        )
        self.wait(2)

        # Smoothly rotate vector B using a ValueTracker
        vector_b_copy = vector_b.copy()
        vector_b_label_copy = vector_b_label.copy()

        vector_b.add_updater(lambda vec: vec.become(
            vector_b_copy.copy().rotate(theta_tracker.get_value() * DEGREES, about_point=plane.get_origin())
        ))
        vector_b_label.add_updater(lambda lbl: lbl.become(
            vector_b_label_copy.copy().rotate(theta_tracker.get_value() * DEGREES, about_point=plane.get_origin())
            .rotate(-theta_tracker.get_value() * DEGREES)
        ))

        # Updaters to keep the vertical and horizontal lines in sync
        vector_b_vertical_line.add_updater(lambda line: line.become(
            plane.get_vertical_line(vector_b.get_end(), color=YELLOW)
        ))
        vector_b_horizontal_line.add_updater(lambda line: line.become(
            plane.get_horizontal_line(vector_b.get_end(), color=YELLOW)
        ))

        # Updaters to keep the labels in sync with their lines
        B_x_label.add_updater(lambda lbl: lbl.next_to(vector_b_horizontal_line, DOWN, buff=0.2))
        B_y_label.add_updater(lambda lbl: lbl.next_to(vector_b_vertical_line, RIGHT, buff=0.2))
        
        # Animate the rotation of vector B
        self.add(theta_text_1)
        self.play(theta_tracker.animate(run_time=5, rate_func=smooth).set_value(90))
        self.wait(1.0)
        self.remove(theta_text_1)
        self.add(theta_text_2)
        self.play(theta_tracker.animate(run_time=5, rate_func=smooth).set_value(180))
        self.wait(1.0)
        self.remove(theta_text_2)
        self.add(theta_text_3)
        self.play(theta_tracker.animate(run_time=5, rate_func=smooth).set_value(270))
        self.wait(1.0)
        self.remove(theta_text_3)
        self.add(theta_text_4)
        self.play(theta_tracker.animate(run_time=5, rate_func=smooth).set_value(360))
        self.wait(1.0)
        self.remove(theta_text_4)
        
        # Unwrite the plane, labels, vectors, and all other elements in reverse order
        self.play(
            Unwrite(theta_text_4), Unwrite(theta_text_3), Unwrite(theta_text_2), Unwrite(theta_text_1),
            Unwrite(unit_vector_text), Unwrite(header_unit_vector),
            Unwrite(magnitude_text), Unwrite(header_magnitude),
            Unwrite(bx_by_text), Unwrite(header_components),
            Unwrite(vector_component_text), Unwrite(header_vector),
            Unwrite(B_x_label), Unwrite(B_y_label),
            Unwrite(vector_b_horizontal_line), Unwrite(vector_b_vertical_line),
            Unwrite(vector_b_label), Unwrite(vector_b),
            Unwrite(x_label), Unwrite(y_label), 
            Uncreate(plane), Unwrite(title), Uncreate(underline),
            run_time=1, rate_func=smooth
        )
        self.wait(1)