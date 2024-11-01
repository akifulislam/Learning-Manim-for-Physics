from manim import *
import numpy as np
from manim_physics import *
import time

# Set background color
config.background_color = ManimColor("#030303")

class UniformElectricField3D(ThreeDScene):
    MathTex.set_default(font_size=42)
    # Define create_description_box as a separate method of the class
    def create_description_box(self, text_content):
            # Create the text content
            description_text = MathTex(text_content)
            description_text.scale(0.75)
        
            # Create a rounded rectangle that automatically adjusts to the text size with buffer
            description_box = RoundedRectangle(
                corner_radius=0.2, 
                width=description_text.width + 0.5,  # Add width based on text and buffer
                height=description_text.height + 0.5  # Add height based on text and buffer
            )
            description_box.set_fill(GREY, opacity=0.2)
        
            # Center the text within the box
            description_text.move_to(description_box.get_center())
        
            # Group the box and text together
            description_group = VGroup(description_box, description_text)
        
            return description_group
        
    def construct(self):         
        # Create the description box with the desired text
        description1 = self.create_description_box(r"\text{Act 1: Produce a uniform field.}").scale(1.0)
        
        # Position the description box at the bottom of the frame
        description1.move_to(LEFT * 4.0 + UP * 3.25)
        
        # Add the description box as a fixed in frame object
        self.add_fixed_in_frame_mobjects(description1)
        
        # Animate the appearance of the description box
        self.play(FadeIn(description1))
    
        # Set field parameters
        x_range = np.arange(-3.0, 4.0, 1)  # x from -2 to 2 with Act size 1
        y_range = np.arange(-3.0, 3.0, 1)  # y from -3 to 3 with Act size 1
        z_range = np.arange(-1.0, 2.0, 1)  # z from -2 to 2 with Act size 1
        
        # Define the field direction along the y-axis
        field_direction = np.array([0, 1, 0])  # Along y-axis
        field_length = 1  # Length of each field vector
        
        # Set the camera orientation for better visibility
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # Colors for vector components and unit vectors
        j_color = GREEN
        v_color = TEAL
        E_y_color = BLUE
        a_color = RED
        t_color = YELLOW
        
        # Define field label with color mappings
        field_label = MathTex(
            r"\vec{E} = E_y\hat{j}",
            substrings_to_isolate=[r"E_y", r"\hat{j}"]
        ).move_to(LEFT * 5.5 + UP * 2.25).scale(1.0)
        field_label.set_color_by_tex_to_color_map({
            r"E_y": E_y_color, r"\hat{j}": j_color
        })
        
        # Define acceleration label with color mappings
        acceleration_label = MathTex(
            r"\vec{a} = \left(\frac{q}{m}\right)\vec{E}",
            substrings_to_isolate=[r"\vec{a}", r"\vec{E}"]
        ).move_to(RIGHT * 5.35 + UP * 3.0).scale(1.0)
        acceleration_label.set_color_by_tex_to_color_map({
            r"\vec{a}": a_color, r"\vec{E}": E_y_color
        })
        
        # Define velocity label with initial value of `t` as 0 and color mappings
        velocity_label = MathTex(
            r"\vec{v} = \underbrace{\vec{v}_0}_{=0} + \vec{a}t",
            substrings_to_isolate=[r"\vec{v}", r"\vec{a}", "t"]
        ).scale(1.0).move_to(RIGHT * 5.35 + UP * 1.65)
        velocity_label.set_color_by_tex_to_color_map({
            r"\vec{v}": v_color, r"\vec{a}": a_color, "t": t_color
        })
        
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
        self.wait(1)
        
        # Define the scale factor to simulate thickness
        scale_factor = 1.5  # Adjust to increase or decrease the thickness effect
        
        rectangle1 = Rectangle(height=3.5, width=7.5).set_fill(TEAL, opacity=0.5).set_stroke(width=2.0).rotate(PI/2, axis=RIGHT).move_to(DOWN * 3)
        rectangle2 = Rectangle(height=3.5, width=7.5).set_fill(RED, opacity=0.5).set_stroke(width=2.0).rotate(PI/2, axis=RIGHT).move_to(UP * 3)
        self.play(Write(rectangle1), Write(rectangle2), rate_func=smooth, run_time=1)
        
        # Define grid parameters for placing charges
        rows, cols = 7, 3
        spacing_x, spacing_y = 1, 1  # Spacing between charges
        
        # Generate and add plus charges to rectangle1
        plus_charges = VGroup()
        for i in range(rows):
            for j in range(cols):
                x_pos = (i - rows // 2) * spacing_x
                y_pos = (j - cols // 2) * spacing_y
                charge = Charge(1, add_glow=False).move_to(rectangle1.get_center() + x_pos * RIGHT + y_pos * OUT).rotate(PI/2, axis=RIGHT)
                plus_charges.add(charge)
        self.play(Create(plus_charges), rate_func=smooth, run_time=1)
        
        # Generate and add minus charges to rectangle2
        minus_charges = VGroup()
        for i in range(rows):
            for j in range(cols):
                x_pos = (i - rows // 2) * spacing_x
                y_pos = (j - cols // 2) * spacing_y
                charge = Charge(-1, add_glow=False).move_to(rectangle2.get_center() + x_pos * RIGHT + y_pos * OUT).rotate(PI/2, axis=RIGHT)
                minus_charges.add(charge)
        self.play(Create(minus_charges), rate_func=smooth, run_time=1)
        
        # Set the camera for a 3D view
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
        
        # Generate all field vectors in a VGroup for efficient rendering
        field_vectors = VGroup()
        for x in x_range:
            for y in y_range:
                for z in z_range:
                    start_point = np.array([x, y, z])
                    end_point = start_point + field_direction * field_length
                    field_vector = Arrow(start=start_point, end=end_point, color=WHITE).scale(scale_factor).rotate(PI/2, axis=UP)
                    field_vectors.add(field_vector)
                    
        self.play(Create(field_vectors), rate_func=smooth, run_time=1.5)
        self.wait(2)
        
        # Add fixed objects
        self.add_fixed_in_frame_mobjects(field_label)
        self.play(Create(field_label))
        
        # Move the camera
        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, rate_func=smooth, zoom = 0.9, run_time=1.5)
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, rate_func=smooth, zoom = 1.0, run_time=1.5)
        self.wait(2)
        
        # Start ambient camera rotation
        self.begin_ambient_camera_rotation(rate=2 * PI / 6)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.wait(3)
        # Unwrite objects and prepare for charge animation
        self.play(Unwrite(rectangle1), Unwrite(rectangle2), Unwrite(plus_charges), Unwrite(minus_charges))
        self.wait(2)
        # Animate the appearance of the description box
        self.play(FadeOut(description1))
        self.wait(1)
        # Create the plus charge at its starting position below the lower rectangle
        plus_charge = Charge(1).rotate(PI/2, axis=RIGHT)
        minus_charge = Charge(-1).rotate(PI/2, axis=RIGHT)
        
        # Create the description box with the desired text
        description2 = self.create_description_box(r"\text{Act 2: Release charged particles from \textit{rest}.").scale(0.9)
        
        # Position the description box at the bottom of the frame
        description2.move_to(LEFT * 3.45 + UP * 3.25)
        
        # Add the description box as a fixed in frame object
        self.add_fixed_in_frame_mobjects(description2)
        
        # Animate the appearance of the description box
        self.play(FadeIn(description2))
        
        # Morph the field vectors to the updated opacity and gradient colors
        self.play(
            field_vectors.animate.set_opacity(0.45).set_color_by_gradient(RED, ORANGE, TEAL),
            run_time=2  # Adjust run_time for the duration of the morphing effect
        )
        plus_charge.move_to(DOWN * 2.5)
        self.wait(2)
        # Add fixed objects
        # Add the labels as fixed in frame objects first
        self.add_fixed_in_frame_mobjects(acceleration_label, velocity_label)
        
        # Then animate their creation
        self.play(Create(acceleration_label), Create(velocity_label))
        self.wait(3)
        self.play(FadeIn(plus_charge), rate_func=smooth, run_time=1)
        
        # Animate the plus charge moving up to y = 3 (aligned with the upper rectangle)
        self.play(plus_charge.animate.move_to(UP * 3), run_time=2)
        
        self.wait(1)
        
        # Fade out the charge after it moves
        self.play(FadeOut(plus_charge), rate_func=smooth, run_time=1)

        minus_charge.move_to(UP * 2.5)
        self.play(FadeIn(minus_charge), rate_func = smooth, run_time=1)
        
        # Animate the minus charge moving down to y = -3 (aligned with the lower rectangle)
        self.play(minus_charge.animate.move_to(DOWN * 3), run_time=2)
        #       self.play()
        self.wait(2)
        self.play(FadeOut(minus_charge), rate_func = smooth, run_time=1)
        
        ### front-view
        # field_vectors.rotate(-PI/2, axis = UP)
        self.move_camera(phi=75 * DEGREES, theta=-90 * DEGREES)
        self.wait(2)
        
        # Add the charges to the scene
        plus_charge.move_to(DOWN * 2.5)
        self.play(FadeIn(plus_charge), rate_func = smooth, run_time=1)
        
        # Animate the plus charge moving up to y = 3 (aligned with the upper rectangle)
        self.play(plus_charge.animate.move_to(UP * 3), run_time=2)
        self.play(FadeOut(plus_charge), rate_func = smooth, run_time=1)
        minus_charge.move_to(UP * 2.5)
        self.play(FadeIn(minus_charge), rate_func = smooth, run_time=1)
        # Animate the minus charge moving down to y = -3 (aligned with the lower rectangle)
        self.play(minus_charge.animate.move_to(DOWN * 3), run_time=2)
        #       self.play()
        self.wait(2)
        self.play(FadeOut(minus_charge), rate_func = smooth, run_time=1)
        ### top-view
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait(2)
        
        # Add the charges to the scene
        plus_charge.move_to(DOWN * 2.5).rotate(PI/2, axis = RIGHT)
        self.play(FadeIn(plus_charge), rate_func = smooth, run_time=1)
        
        # Animate the plus charge moving up to y = 3 (aligned with the upper rectangle)
        self.play(plus_charge.animate.move_to(UP * 3), run_time=2)
        self.play(FadeOut(plus_charge), rate_func = smooth, run_time=1)
        minus_charge.move_to(UP * 2.5).rotate(PI/2, axis = RIGHT)
        self.play(FadeIn(minus_charge), rate_func = smooth, run_time=1)
        # Animate the minus charge moving down to y = -3 (aligned with the lower rectangle)
        self.play(minus_charge.animate.move_to(DOWN * 3), run_time=2)
        #       self.play()
        self.wait(2)
        self.play(FadeOut(minus_charge), rate_func = smooth, run_time=1)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
        
        # Separate vectorized and non-vectorized mobjects
        vectorized_mobjects = [mob for mob in self.mobjects if isinstance(mob, VMobject)]
        non_vectorized_mobjects = [mob for mob in self.mobjects if not isinstance(mob, VMobject)]
        
        # Apply Unwrite to vectorized objects and FadeOut to others
        self.play(
            *[Unwrite(mob) for mob in vectorized_mobjects],
            *[FadeOut(mob) for mob in non_vectorized_mobjects],
            run_time=0.5  # Adjust run_time as needed
        )
        self.wait(0.5)  # Brief wait to complete the effect