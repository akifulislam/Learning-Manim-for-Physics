#!/usr/bin/env python3

from manim import *
import numpy as np

# Set background color
config.background_color = ManimColor("#030303")

class VectorField3DTransform(ThreeDScene):
	def construct(self):
		self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, zoom = 0.75)
		
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
			self.add_fixed_in_frame_mobjects(upper_right_group)
			
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
		
		# Create fixed-in-frame labels with animations
		def create_fixed_label(label):
#           self.play(Write(label), run_time=1.5, rate_func=smooth)
			self.add_fixed_in_frame_mobjects(label)
			
		# Define the labels
		label_1 = MathTex(r"\vec{F}(x, y, z) = -y\hat{i} + x\hat{j} + z\hat{k}") \
			.move_to(RIGHT * -3.0 + UP * 3.0 + OUT * 0) \
			.set_color_by_gradient(RED, PURPLE).scale(0.75)
		
		label_2 = MathTex(r"\vec{F}(x, y, z) = \sin(x)\hat{i} + \cos(y)\hat{j} + \sin(z)\hat{k}") \
			.move_to(RIGHT * -3.0 + UP * 3.0 + OUT * 0) \
			.set_color_by_gradient(YELLOW, GREEN).scale(0.75)
		
		label_3 = MathTex(r"\vec{F}\left(x, y, z\right) = x\sin\left(y\right)\hat{i} + y\cos\left(z\right)\hat{j} + z\sin\left(x\right)\hat{k}") \
			.move_to(RIGHT * -2.75 + UP * 3.0 + OUT * 0) \
			.set_color_by_gradient(BLUE, ORANGE).scale(0.75)
		
		label_4 = MathTex(r"\vec{F}(x, y, z) = e^{-x^2}\hat{i} + e^{-y^2}\hat{j} + e^{-z^2}\hat{k}") \
			.move_to(RIGHT * -3.0 + UP * 3.0 + OUT * 0) \
			.set_color_by_gradient(GREEN, PINK).scale(0.75)
		
		label_5 = MathTex(r"\vec{F}(x, y, z) = \tan(x)\hat{i} + \tan(y)\hat{j} + \tan(z)\hat{k}") \
			.move_to(RIGHT * -3.0 + UP * 3.0 + OUT * 0) \
			.set_color_by_gradient(PURPLE, YELLOW).scale(0.75)
		
		# Morph vector arrows from 2D to 3D, starting with vector_field_5
#       self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, zoom = 0.75, run_time=1.5)
		
		# Add all the elements to the scene in a single line
		self.add(
			axes_3D, x_label, y_label, z_label,  # 3D Axes and labels
			vector_field_5  # Vector field 5
		)
		create_fixed_label(label_5)
		
		self.play(
			Transform(vector_field_5, vector_field_4),
			Transform(label_5, label_4),
			run_time=2
		)
		self.wait(2)
		
		self.play(
			Transform(vector_field_5, vector_field_3),
			Transform(label_5, label_3),
			run_time=2
		)
		self.wait(2)
		
		self.play(
			Transform(vector_field_5, vector_field_2),
			Transform(label_5, label_2),
			run_time=2
		)
		self.wait(2)
		
		self.play(
			Transform(vector_field_5, vector_field_1),
			Transform(label_5, label_1),
			run_time=2
		)
		self.wait(2)
		
		self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=1.5)
		self.move_camera(phi=75 * DEGREES, theta=315 * DEGREES, run_time=6)
		self.wait(2)
		self.move_camera(phi=90 * DEGREES, theta=270 * DEGREES, run_time=1.5)
		self.wait(1)
		self.move_camera(phi=90 * DEGREES, theta=180 * DEGREES, run_time=1.5)
		self.wait(1)
		self.move_camera(phi=90 * DEGREES, theta=90 * DEGREES, run_time=1.5)
		self.wait(1)
		self.move_camera(phi=90 * DEGREES, theta=0* DEGREES, run_time=1.5)
		self.wait(1)
		self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, run_time=1.5)
		
		# Speed up Unwrite and Uncreate everything from the scene
		self.play(
			Unwrite(x_label, run_time=0.5), 
			Unwrite(y_label, run_time=0.5), 
			Unwrite(z_label, run_time=0.5),
			Uncreate(axes_3D, run_time=0.5)
		)
		# Unwrite the final vector field and label
		self.play(Unwrite(vector_field_1), Unwrite(label_5), run_time=0.005)
		self.wait(1)
		
		# Unwrite the title and underline
		for mobj in upper_right_group:
			self.play(Unwrite(mobj), run_time=0.5, rate_func=smooth)