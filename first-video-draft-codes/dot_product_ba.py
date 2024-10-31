#!/usr/bin/env python3

from manim import *  # 0.18.0
import numpy as np

# Set background color
config.background_color = ManimColor("#030303")

class VectorDotProduct(Scene):
    def construct(self):
        # Defaults
        MathTex.set_default(font_size=32)
        
        # Title and underline
        title = MathTex(r"\text{Dot/Scalar Product in a glance!}").move_to(RIGHT * 0.0 + UP * 3.5).set_color_by_gradient(BLUE, GREEN).scale(1.25)
        underline = Line(start=title.get_left(), end=title.get_right(), color=BLUE).next_to(title, DOWN, buff=0.1)
        self.play(Write(title), Create(underline), rate_func=smooth, run_time=1.5)
        
        # Create the plane
        plane = NumberPlane(
            x_range=(-4, 4, 1),
            y_range=(-2.5, 2.5, 1),
            axis_config={"include_numbers": True, "include_ticks": True, "include_tip": True},
            background_line_style={"stroke_opacity": 0},
        )
        # Add axis labels with tips on axes
        x_label = always_redraw(lambda: MathTex("x").next_to(plane.x_axis.get_end(), RIGHT * 1, buff=0.2))
        y_label = always_redraw(lambda: MathTex("y").next_to(plane.y_axis.get_end(), UP + RIGHT * 0.5, buff=0.2))
        
        # Create the semi-transparent xy-plane with colored gridlines
        xy_plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": WHITE},
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1.0,
                "stroke_opacity": 0.15,
            }
        ).set_fill(BLUE, opacity=0.2)  # Apply blue fill with 20% opacity

        # Functions to turn the plane on and off
        def plane_on():
            self.add(xy_plane)

        def plane_off():
            self.remove(xy_plane)

        # Vector A fixed along the y-axis
        vector_a_coords = np.array([0, 2, 0])
        vector_a = plane.get_vector(vector_a_coords, color=RED)
        vector_a_label = MathTex(r"\vec{A}", color=RED).next_to(vector_a, direction=LEFT*0.25+UP*0.25, buff=0.1)

        # Vector B starts on the x-axis and will rotate clockwise
        vector_b_coords = np.array([0, 1.5, 0])
        vector_b = plane.get_vector(vector_b_coords, color=BLUE)
        vector_b_label = MathTex(r"\vec{B}", color=BLUE).next_to(vector_b, direction=RIGHT+UP*0.25, buff=0.1)
        self.wait(1.5)
        # Theta tracker for updating the angle
        theta_tracker = ValueTracker(0)
  
        # Display the dot product formula with cos(theta)
        math_text = MathTex(
          r"\text{Geometrical}: \vec{B} \cdot \vec{A} = |\vec{B}| * |\vec{A}| * \cos\theta =  1.5 * 2.0 * \cos("
          + str(round(theta_tracker.get_value()))
          + r"^{\circ}) = "
          + str(round(1.5 * 2.0 * np.cos(theta_tracker.get_value() * DEGREES), 2))
        ).move_to(RIGHT * 0.0 + UP * -2.9)
        math_text.set_color_by_gradient(BLUE, GREEN)
        
        # Math text displaying the dot product in component form
        component_text = MathTex(
          r"\text{Analytical}: \vec{B} \cdot \vec{A} = B_x A_x + B_y A_y = "
          + str(round(vector_b.get_end()[0], 2))
          + r" \cdot 0 + "
          + str(round(vector_b.get_end()[1], 2))
          + r" \cdot 2"
          + r" = "
          + str(round(vector_b.get_end()[1] * 2, 2))
        ).move_to(RIGHT * 0.0 + UP * -3.5)
        component_text.set_color_by_gradient(YELLOW, ORANGE)
#       
#       # Add initial vectors, labels, and plane
        self.play(Write(vector_a), Write(vector_b), 
          Write(vector_a_label), Write(vector_b_label), run_time=1.0, rate_func=smooth)
        self.play(Create(plane), Write(x_label), Write(y_label), run_time=1.0, rate_func=smooth)
#       
        plane_on()
        self.wait(1.5)
        # Projections of vector B onto the x and y axes
        proj_b_x = plane.get_vector([vector_b_coords[0], 0, 0], color=YELLOW).set_opacity(0.6)
        proj_b_y = plane.get_vector([0, vector_b_coords[1], 0], color=YELLOW).set_opacity(0.6)
        
        # Perpendicular dashed lines from vector B to x and y axes
        perp_line_x = DashedLine(
          start=vector_b.get_end(),
          end=[vector_b.get_end()[0], 0, 0],  # Projection onto x-axis
          color=ORANGE, stroke_width=2, dash_length=0.1
        )
        perp_line_y = DashedLine(
          start=vector_b.get_end(),
          end=[0, vector_b.get_end()[1], 0],  # Projection onto y-axis
          color=ORANGE, stroke_width=2, dash_length=0.1
        )
        
        # Add the initial projections
        self.add(proj_b_y, perp_line_y)
        self.play(Write(math_text), Write (component_text), run_time=1.0, rate_func=smooth)
        # Copy the vectors for smooth updates
        vector_b_copy = vector_b.copy()
        vector_b_label_copy = vector_b_label.copy()
  
        # Updater to rotate vector B and keep the label oriented
        vector_b.add_updater(
          lambda vec: vec.become(
            vector_b_copy.copy().rotate(theta_tracker.get_value() * DEGREES, about_point=plane.get_origin())
          )
        )
        vector_b_label.add_updater(
          lambda lbl: lbl.become(
            vector_b_label_copy.copy()
            .rotate(theta_tracker.get_value() * DEGREES, about_point=plane.get_origin())
            .rotate(-theta_tracker.get_value() * DEGREES)  # Maintain label orientation
          )
        )
        
        # Updater for the x-axis projection
        #       proj_b_x.add_updater(
        #         lambda p: p.become(
        #           plane.get_vector([vector_b.get_end()[0], 0, 0], color=YELLOW).set_opacity(0.6)
        #         )
        #       )
        
        # Updater for the y-axis projection
        proj_b_y.add_updater(
          lambda p: p.become(
            plane.get_vector([0, vector_b.get_end()[1], 0], color=YELLOW).set_opacity(0.6)
          )
        )
        # Updaters for the perpendicular lines
        #       perp_line_x.add_updater(
        #         lambda line: line.become(
        #           DashedLine(
        #             start=vector_b.get_end(),
        #             end=[vector_b.get_end()[0], 0, 0],  # Update projection onto x-axis
        #             color=ORANGE, stroke_width=2, dash_length=0.1
        #           )
        #         )
        #       )
        perp_line_y.add_updater(
          lambda line: line.become(
            DashedLine(
              start=vector_b.get_end(),
              end=[0, vector_b.get_end()[1], 0],  # Update projection onto y-axis
              color=ORANGE, stroke_width=2, dash_length=0.1
            )
          )
        )
  
        # Updater for math text to track the angle and dot product
        math_text.add_updater(
          lambda txt: txt.become(
            MathTex(
              r"\text{Geometrical}: \vec{B} \cdot \vec{A} = |\vec{B}| * |\vec{A}| * \cos\theta =  1.5 * 2.0 * \cos("
              + str(round(theta_tracker.get_value()))
              + r"^{\circ}) = "
              + str(round(1.5 * 2.0 * np.cos(theta_tracker.get_value() * DEGREES), 2))
            ).move_to(RIGHT * 0.0 + UP * -2.9).set_color_by_gradient(BLUE, GREEN)  # Apply gradient in the updater
          )
        )
        
        # Updater for the component form dot product text
        component_text.add_updater(
          lambda txt: txt.become(
            MathTex(
              r"\text{Analytical}: \vec{B} \cdot \vec{A} = B_x A_x + B_y A_y = "
              + str(round(vector_b.get_end()[0], 2))
              + r" \cdot 0 + "
              + str(round(vector_b.get_end()[1], 2))
              + r" \cdot 2"
              + r" = "
              + str(round(vector_b.get_end()[1] * 2, 2))
            ).move_to(RIGHT * 0.0 + UP * -3.50).set_color_by_gradient(YELLOW, ORANGE)  # Apply gradient in the updater
          )
        )
        theta = Angle.from_three_points(
          vector_a.get_end(), plane.get_origin(), vector_b.get_end(),
          other_angle=False, color=YELLOW
        )
        self.add(theta)
        
        theta.add_updater(
          lambda x: x.become(
            Angle.from_three_points(
              vector_a.get_end(),
              # A hack with the middle point, because it doesn't want to create angles for 180
              plane.coords_to_point(0, -0.001),
              vector_b.get_end(),
              other_angle=False
            )
          )
        )
        # Animate the rotation and tracking of the angle
        self.play(theta_tracker.animate(run_time=2, rate_func=smooth).set_value(90))
        self.wait(0.5)
        self.play(theta_tracker.animate(run_time=2, rate_func=smooth).set_value(180))
        self.wait(0.5)
        self.play(theta_tracker.animate(run_time=2, rate_func=smooth).set_value(270))
        self.wait(0.5)
        self.play(theta_tracker.animate(run_time=3, rate_func=smooth).set_value(360))
        self.wait(0.5)
        # Unwrite and uncreate everything from the scene
        self.play(
          Unwrite(vector_a), Unwrite(vector_b), 
          Unwrite(vector_a_label), Unwrite(vector_b_label),
          Unwrite(math_text), Unwrite(component_text),
          Uncreate(plane), Unwrite(x_label), Unwrite(y_label),
          Uncreate(xy_plane),
          Uncreate(proj_b_y), Uncreate(perp_line_y),
          Uncreate(theta), rate_func = smooth, run_time = 1.0)
        self.wait(1)
        
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
        ).scale(1.35).set_color_by_tex_to_color_map({
          "A_x": A_x_color, "A_y": A_y_color, "A_z": A_z_color,
          r"\hat{i}": i_color, r"\hat{j}": j_color, r"\hat{k}": k_color
        })
      
        # Define vector B = B_x * i + B_y * j + B_z * k
        vector_B = MathTex(
          r"\vec{B} = ",
          r"B_x\hat{i} + B_y\hat{j} + B_z\hat{k}",
          substrings_to_isolate=["B_x", "B_y", "B_z", r"\hat{i}", r"\hat{j}", r"\hat{k}"]
        ).scale(1.35).set_color_by_tex_to_color_map({
          "B_x": B_x_color, "B_y": B_y_color, "B_z": B_z_color,
          r"\hat{i}": i_color, r"\hat{j}": j_color, r"\hat{k}": k_color
        })
      
        # Group the two vectors for vertical alignment
        vectors_group = VGroup(vector_A, vector_B).arrange(DOWN, buff=0.5)
      
        # Display the expanded dot product equation with full component breakdown
        dot_product_equation = MathTex(
          r"\vec{A} \cdot \vec{B} = ",
          r"(A_x\hat{i} + A_y\hat{j} + A_z\hat{k})",
          r"\cdot",
          r"(B_x\hat{i} + B_y\hat{j} + B_z\hat{k})"
        ).scale(1.35).set_color_by_tex_to_color_map({
          "A_x": A_x_color, "A_y": A_y_color, "A_z": A_z_color,
          "B_x": B_x_color, "B_y": B_y_color, "B_z": B_z_color,
          r"\hat{i}": i_color, r"\hat{j}": j_color, r"\hat{k}": k_color
        })
      
        # Place the dot product equation below the vectors
        dot_product_equation.next_to(vectors_group, DOWN, buff=0.8)
      
        # Define the simplified dot product result with matching component colors
        expanded_dot_product = MathTex(
          r"\vec{A} \cdot \vec{B} = ",
          r"A_x", r"B_x", r"+",
          r"A_y", r"B_y", r"+",
          r"A_z", r"B_z"
        ).scale(1.35).set_color_by_tex_to_color_map({
          "A_x": A_x_color, "A_y": A_y_color, "A_z": A_z_color,
          "B_x": B_x_color, "B_y": B_y_color, "B_z": B_z_color
        })
      
        # Place the expanded equation below the full dot product equation
        expanded_dot_product.next_to(dot_product_equation, DOWN, buff=0.8)
      
        # Center everything on the screen
        content = VGroup(vectors_group, dot_product_equation, expanded_dot_product).arrange(DOWN, buff=1).move_to(ORIGIN)
      
        # Animate everything
        self.play(Write(vector_A), Write(vector_B))
        self.wait(1)
        self.play(Write(dot_product_equation))
        self.wait(1)
        self.play(Write(expanded_dot_product))
        self.wait(2)
      
        # Fade out everything at the end
        self.play(FadeOut(content), Unwrite(title), Uncreate(underline), rate_func = smooth, run_time = 1.0)
        self.wait(1)