from manim import *
import numpy as np
from manim_physics import *
import time

# Set background color
config.background_color = ManimColor("#030303")

class ParabolicPathElectricField3D(ThreeDScene):
    MathTex.set_default(font_size=42)
    
    def create_description_box(self, text_content):
        description_text = MathTex(text_content)
        description_text.scale(0.75)
        description_box = RoundedRectangle(
            corner_radius=0.2, 
            width=description_text.width + 0.5,
            height=description_text.height + 0.5
        )
        description_box.set_fill(GREY, opacity=0.5)
        description_text.move_to(description_box.get_center())
        description_group = VGroup(description_box, description_text)
        return description_group
        
    def construct(self):         
        description1 = self.create_description_box(r"\text{Act 1: Produce a uniform field}").scale(1.0)
        description1.move_to(LEFT * 4.0 + UP * 3.25)
        self.add_fixed_in_frame_mobjects(description1)
        self.play(FadeIn(description1))
    
        x_range = np.arange(-3.0, 3.0, 1)
        y_range = np.arange(-3.0, 4.0, 1)
        z_range = np.arange(-1.0, 2.0, 1)
        
        # Define the field along the x-axis
        field_direction = np.array([1, 0, 0])  # Along x-axis
        field_length = 1  
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # Colors for vector components and unit vectors
        i_color = GREEN
        v_color = TEAL
        E_x_color = BLUE
        a_color = RED
        E_vector_color = ORANGE
        t_color = YELLOW
        
        # Define field label with new direction (x-axis)
        field_label = MathTex(
            r"\vec{E} = E_x\hat{i}",
            substrings_to_isolate=[r"\vec{E}", r"E_x", r"\hat{i}"]
        ).move_to(LEFT * 5.5 + UP * 2.10).scale(1.0)
        field_label.set_color_by_tex_to_color_map({
            r"\vec{E}": E_vector_color, r"E_x": E_x_color, r"\hat{i}": i_color
        })
        
        # Define acceleration label with new field direction
        acceleration_label = MathTex(
            r"\vec{a} = \left(\frac{q}{m}\right)\vec{E}",
            substrings_to_isolate=[r"\vec{E}", r"\vec{a}", r"E_x", r"\hat{i}"]
        ).move_to(RIGHT * 5.25 + UP * 3.0).scale(1.0)
        acceleration_label.set_color_by_tex_to_color_map({
            r"\vec{E}": E_vector_color, r"\vec{a}": a_color, r"E_x": E_x_color, r"\hat{i}": i_color
        })
# Define the speed label for the y-component: v_y = v_{0y}
        acceleration_label_y = MathTex(
            r"a_y = 0",
            substrings_to_isolate=["v_y", "v_{0y}"]
        ).scale(1.0).next_to(acceleration_label, DOWN, buff=0.4)
        acceleration_label_y.set_color_by_tex_to_color_map({
            "v_y": t_color, "v_{0y}": t_color
        })
        
        # Define the speed label for the x-component: v_x = v_{0x} + a_x t
        acceletation_label_x = MathTex(
            r"a_x = \frac{q}{m}E_x",
            substrings_to_isolate=[r"E_x", "v_x", "v_{0x}", "a_x", "t"]
        ).scale(1.0).next_to(acceleration_label_y, DOWN, buff=0.3)
        acceletation_label_x.set_color_by_tex_to_color_map({
            r"E_x": E_x_color, "v_x": a_color, "v_{0x}": t_color, "a_x": a_color, "t": t_color
        })
        
        # Define velocity label with initial `v_y` and new `v_x` inside the field
        velocity_label = MathTex(
            r"\vec{v} = v_y\hat{j} + v_x\hat{i}",
            substrings_to_isolate=[r"\vec{v}", r"v_y", r"v_x", r"\hat{j}", r"\hat{i}"]
        ).scale(1.0).move_to(RIGHT * 5.25 + DOWN * 1.0)
        velocity_label.set_color_by_tex_to_color_map({
            r"\vec{v}": v_color, r"v_y": t_color, r"v_x": a_color, r"\hat{j}": i_color, r"\hat{i}": i_color
        })
        # Define the speed label for the y-component: v_y = v_{0y}
        speed_label_y = MathTex(
            r"v_y = v_{0y}",
            substrings_to_isolate=["v_y", "v_{0y}"]
        ).scale(1.0).next_to(velocity_label, DOWN, buff=0.4)
        speed_label_y.set_color_by_tex_to_color_map({
            "v_y": t_color, "v_{0y}": t_color
        })
        
        # Define the speed label for the x-component: v_x = v_{0x} + a_x t
        speed_label_x = MathTex(
            r"v_x = \underbrace{v_{0x}}_{=0} + a_x t",
            substrings_to_isolate=["v_x", "v_{0x}", "a_x", "t"]
        ).scale(1.0).next_to(speed_label_y, DOWN, buff=0.3)
        speed_label_x.set_color_by_tex_to_color_map({
            "v_x": a_color, "v_{0x}": t_color, "a_x": a_color, "t": t_color
        })
        
        # Create a 3D axes
        axes_3D = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            axis_config={
                "color": WHITE,
                "include_ticks": True,
                "include_tip": True,
                "tip_length": 0.2
            },
        )
        x_label = always_redraw(lambda: MathTex("x").next_to(axes_3D.x_axis.get_end(), RIGHT, buff=0.2).rotate(PI/2, axis=RIGHT))
        y_label = always_redraw(lambda: MathTex("y").next_to(axes_3D.y_axis.get_end(), UP, buff=0.2).rotate(PI/2, axis=RIGHT))
        z_label = always_redraw(lambda: MathTex("z").next_to(axes_3D.z_axis.get_end(), UP*0.75, buff=0.2).rotate(PI/2, axis=RIGHT))
        
        # Create the axes and labels
        self.play(Create(axes_3D), Write(x_label), Write(y_label), Write(z_label), run_time=1.0, rate_func=smooth)
        self.wait(1)
        
        axes_labels = VGroup(x_label, y_label, z_label)
        
        scale_factor = 1.5  
        
        rectangle1 = Rectangle(height=7.5, width=3.5).set_fill(TEAL, opacity=0.5).set_stroke(width=2.0).rotate(PI/2, axis=UP).move_to(LEFT * 3)
        rectangle2 = Rectangle(height=7.5, width=3.5).set_fill(RED, opacity=0.5).set_stroke(width=2.0).rotate(PI/2, axis=UP).move_to(RIGHT * 3)
        self.play(Write(rectangle1), Write(rectangle2), rate_func=smooth, run_time=1)
        
        rows, cols = 7, 3
        spacing_x, spacing_y = 1, 1  
        
        # Place charges on the rectangles
        plus_charges = VGroup()
        minus_charges = VGroup()
        for i in range(rows):
            for j in range(cols):
                x_pos = (i - (rows - 1) / 2) * spacing_x  # Centering along the rectangle's height
                y_pos = (j - (cols - 1) / 2) * spacing_y  # Centering along the rectangle's width
                plus_charge = Charge(1, add_glow=False).move_to(rectangle1.get_center() + x_pos * UP + y_pos * OUT).rotate(PI/2, axis=UP)
                minus_charge = Charge(-1, add_glow=False).move_to(rectangle2.get_center() + x_pos * UP + y_pos * OUT).rotate(PI/2, axis=UP)
                plus_charges.add(plus_charge)
                minus_charges.add(minus_charge)
            
        # Animate the appearance of the charges on each rectangle
        self.play(Create(plus_charges), Create(minus_charges), rate_func=smooth, run_time=1)
        
        # Set the camera for a 3D view
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
        
        # Generate field vectors along the x-axis
        field_vectors = VGroup()
        for x in x_range:
            for y in y_range:
                for z in z_range:
                    start_point = np.array([x, y, z])
                    end_point = start_point + field_direction * field_length
                    field_vector = Arrow(start=start_point, end=end_point, color=WHITE).scale(scale_factor).rotate(PI/2, axis=RIGHT)
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
        self.play(Unwrite(rectangle1), Unwrite(rectangle2), Unwrite(plus_charges), Unwrite(minus_charges))
        self.wait(2)
        self.play(FadeOut(description1))
        self.wait(1)
        
        self.move_camera(phi=75 * DEGREES, theta=-90 * DEGREES, rate_func=smooth, run_time=1.5)
        
        # Define parameters for initial velocity and acceleration inside the field
        initial_velocity_y = 1.5  # Initial velocity in y-direction
        acceleration_x = 0.35     # Acceleration in x-direction inside the field
        
        # Place the plus charge initially at DOWN * 5 outside the field region
        plus_charge1 = Charge(1).rotate(PI/2, axis = RIGHT)
        minus_charge1 = Charge(-1).rotate(PI/2, axis = RIGHT)
        plus_charge2 = Charge(1)
        minus_charge2 = Charge(-1)
        self.play(
            field_vectors.animate.set_opacity(0.45).set_color_by_gradient(RED, ORANGE, TEAL),
            run_time=2  # Adjust run_time for the duration of the morphing effect
        )
        
        disclaimer = self.create_description_box(r"^*\text{Field opacity decreased with gradient colors}\\\text{to show particle's motion clearly.}").scale(0.75)
        disclaimer.move_to(LEFT * 4.0 + DOWN * 3.25)
        self.add_fixed_in_frame_mobjects(disclaimer)
        self.play(FadeIn(disclaimer))
        self.wait(3)
        # Create the description box with the desired text
        description2 = self.create_description_box(r"\text{Act 2: Fire charged particles perpendicular} \\ \text{to the field with \textit{uniform} velocity.").scale(0.9)
        
        # Position the description box at the bottom of the frame
        description2.move_to(LEFT * 3.5 + UP * 3.25)
        
        # Add the description box as a fixed in frame object
        self.add_fixed_in_frame_mobjects(description2)
        
        # Animate the appearance of the description box
        self.play(FadeIn(description2), FadeOut(disclaimer))
        self.wait(3)
        # Add the labels as fixed in frame objects first
        # Add the labels as fixed in-frame objects first
        self.add_fixed_in_frame_mobjects(acceleration_label, acceletation_label_x, acceleration_label_y, 
                                                                            velocity_label, speed_label_x, speed_label_y)
        
        # Play the Create animation for each label
        self.play(
                Create(acceleration_label),
                Create(acceletation_label_x),
                Create(acceleration_label_y),
                Create(velocity_label),
                Create(speed_label_x),
                Create(speed_label_y),
                run_time=2  # Adjust run time as needed
        )
        self.wait(2)
        plus_charge1.move_to(DOWN * 5 + LEFT * 1.5)  # Starting position outside the field
        
#       # First velocity vector along the y-axis
#       velocity_vector_y = Arrow(
#           start=plus_charge.get_center(),
#           end=plus_charge.get_center() + initial_velocity_y * UP,
#           color=YELLOW
#       )
#       
#       # Updater for the y-axis velocity vector to follow the charge’s position
#       def update_velocity_vector_y(arrow):
#           # Update the start and end points of the arrow to follow the charge
#           start = plus_charge.get_center()
#           end = start + initial_velocity_y * UP
#           arrow.put_start_and_end_on(start, end)
#           
#       velocity_vector_y.add_updater(update_velocity_vector_y)
#       
#       # Second velocity vector along the x-axis, initially with zero length
#       velocity_vector_x = Arrow(
#           start=plus_charge.get_center(),
#           end=plus_charge.get_center(),  # Initially zero length
#           color=RED
#       )
#       
#       # Updater for the x-axis velocity vector that scales based on `acceleration_x * t`
#       def update_velocity_vector_x(arrow, dt):
#           # Initialize the time_elapsed attribute if it does not exist
#           if not hasattr(arrow, "time_elapsed"):
#               arrow.time_elapsed = 0
#           # Increment the elapsed time
#           arrow.time_elapsed += dt
#           # Start and end points based on the charge's position and updated x-component of velocity
#           start = plus_charge.get_center()
#           end = start + acceleration_x * arrow.time_elapsed * RIGHT
#           arrow.put_start_and_end_on(start, end)
#           
        # Add the updater to velocity_vector_x
#       velocity_vector_x.add_updater(update_velocity_vector_x)
        
        # Animate the appearance of the plus charge and its initial y-axis velocity vector
        self.play(FadeIn(plus_charge1), 
#           FadeIn(velocity_vector_y), 
            run_time=1)
        
        # Move the charge straight to DOWN * 3 before it enters the field region
        self.play(plus_charge1.animate.move_to(DOWN * 3 + LEFT * 1.5), run_time=1.5, rate_func=smooth)
        
        # Fade in the x-axis velocity vector as it enters the field region
#       self.play(FadeIn(velocity_vector_x), run_time=1)
        
        # Define the parabolic path for the charge starting from DOWN * 3
        parabolic_path1 = ParametricFunction(
            lambda t: np.array([
                0.5 * acceleration_x * t**2,   # Parabolic x-component due to acceleration_x
                initial_velocity_y * t,        # Linear y-component due to initial v_y
                0                              # z-component remains zero
            ]),
            t_range=(0, 5),  # Define the range for the parabolic path using a tuple
            color=YELLOW
        ).shift(DOWN * 3 + LEFT * 1.5)  # Start the parabolic path from DOWN * 3
        
        # Animate the plus charge moving along the parabolic path with the x-axis velocity vector increasing
        self.play(MoveAlongPath(plus_charge1, parabolic_path1), run_time=4, rate_func=smooth)
        
        # Remove the x-axis updater after the path completes
#       velocity_vector_x.remove_updater(update_velocity_vector_x)
        
        # Fade out the charge and both velocity vectors after the path completes
        self.play(FadeOut(plus_charge1), 
#           FadeOut(velocity_vector_y), 
#           FadeOut(velocity_vector_x), 
            run_time=1)
        self.wait(1)
        
        minus_charge1.move_to(DOWN * 5 + RIGHT * 1.5)  # Starting position outside the field
        # Animate the appearance of the plus charge and its initial y-axis velocity vector
        self.play(FadeIn(minus_charge1), 
#           FadeIn(velocity_vector_y), 
            run_time=1)
        
        # Move the charge straight to DOWN * 3 before it enters the field region
        self.play(minus_charge1.animate.move_to(DOWN * 3 + RIGHT * 1.5), run_time=1.5, rate_func=smooth)
        
        # Define the parabolic path for the charge starting from DOWN * 3
        parabolic_path2 = ParametricFunction(
            lambda t: np.array([
                0.5 * -acceleration_x * t**2,   # Parabolic x-component due to acceleration_x
                initial_velocity_y * t,        # Linear y-component due to initial v_y
                0                              # z-component remains zero
            ]),
            t_range=(0, 5),  # Define the range for the parabolic path using a tuple
            color=YELLOW
        ).shift(DOWN * 3 + RIGHT * 1.5)  # Start the parabolic path from DOWN * 3
        
        # Animate the plus charge moving along the parabolic path with the x-axis velocity vector increasing
        self.play(MoveAlongPath(minus_charge1, parabolic_path2), run_time=4, rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(minus_charge1), run_time=1)
        
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, rate_func=smooth, zoom = 0.75, run_time=1.5)
#       self.play(
#           axes_labels.animate.rotate(-PI/2, axis = RIGHT),
#           run_time=1  # Adjust run_time for the duration of the morphing effect
#       )
        self.wait(1.5)
        plus_charge2.move_to(DOWN * 5 + LEFT * 1.5)
        self.play(FadeIn(plus_charge2), run_time=1)
        self.play(plus_charge2.animate.move_to(DOWN * 3 + LEFT * 1.5), run_time=1.5, rate_func=smooth)
        self.play(MoveAlongPath(plus_charge2, parabolic_path1), run_time=4, rate_func=smooth)
        self.play(FadeOut(plus_charge2), run_time=1)
        self.wait(1)
        
        minus_charge2.move_to(DOWN * 5 + RIGHT * 1.5)
        self.play(FadeIn(minus_charge2), run_time=1)
        self.play(minus_charge2.animate.move_to(DOWN * 3 + RIGHT * 1.5), run_time=1.5, rate_func=smooth)
        self.play(MoveAlongPath(minus_charge2, parabolic_path2), run_time=4, rate_func=smooth)
        self.play(FadeOut(minus_charge2), run_time=1)
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, rate_func=smooth, zoom = 1.0, run_time=1.5)
        self.wait(1)
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