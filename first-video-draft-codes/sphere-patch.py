from manim import *

class SphereWithPatch(ThreeDScene):
    # Function to create and add patches with normal vectors
    def add_patch_with_normal(self, u_idx_start, u_idx_end, v_idx_start, v_idx_end, color=YELLOW):
        # Parameters inside the function
        radius = 2  # Or use self.radius if defined elsewhere
        phi_slices = 10
        theta_slices = 20
        # Calculate actual u and v values
        u_start = u_idx_start * PI / phi_slices
        u_end = u_idx_end * PI / phi_slices
        v_start = v_idx_start * (-TAU / theta_slices)
        v_end = v_idx_end * (-TAU / theta_slices)
        # Create the patch
        patch = Surface(
            lambda u, v: radius * np.array([
                np.sin(u) * np.cos(v),
                np.sin(u) * np.sin(v),
                np.cos(u)
            ]),
            u_range=[u_start, u_end],
            v_range=[v_start, v_end],
            resolution=(1, 1),
            fill_color=color,
            fill_opacity=1,
            stroke_color=RED,
            stroke_width=5,
        )
        # Calculate the center point of the patch
        u_center = (u_start + u_end) / 2
        v_center = (v_start + v_end) / 2
        # Position vector at the center of the patch
        position = radius * np.array([
            np.sin(u_center) * np.cos(v_center),
            np.sin(u_center) * np.sin(v_center),
            np.cos(u_center)
        ])
        # Normal vector at the center
        normal_vector = position / np.linalg.norm(position)
        
        # Create the normal vector arrow
        normal_arrow = Arrow3D( # Toggle on for 3D arrow
            start=position,
            end=position + normal_vector * radius * 0.5,
            color=RED,
            stroke_width=0.5
        )
        
#       normal_arrow = Arrow( # Toggle on for 2D arrow
#           start=position,
#           end=position + normal_vector * radius * 0.75,
#           color=RED,
#           stroke_width=5
#       )
        
        # Create the label for the normal vector
        label = MathTex(r"\vec{dA}", color=RED).rotate(PI / 2, axis=RIGHT)
        label.scale(0.7)
        label.move_to(position + normal_vector * radius * 0.75)
        # Add patch, arrow, and label to the scene
#       self.add(patch, normal_arrow, label) # Toggle on for patch, arrow, label draw
        self.play(Create(patch), Create(normal_arrow))

    def construct(self):
        # Control parameters
        radius = 2.0  # Adjust the radius of the sphere
        phi_slices = 10  # Number of slices along phi (vertical)
        theta_slices = 20  # Number of slices along theta (horizontal)

        # Create the sphere
        sphere = Surface(
            lambda u, v: radius * np.array([
                np.sin(u) * np.cos(v),
                np.sin(u) * np.sin(v),
                np.cos(u)
            ]),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU],
            resolution=(phi_slices, theta_slices),
            fill_opacity=0.45,
            checkerboard_colors=[BLUE_E, BLUE_E],
            stroke_color=WHITE,
            stroke_width=0.75,
        )

        # Set up the camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, zoom=1.0)

        # Add the sphere to the scene
        self.add(sphere)

        # Use the function to add multiple patches with normal vectors

        self.add_patch_with_normal(u_idx_start=3, u_idx_end=4, v_idx_start=0, v_idx_end=1, color=YELLOW)
        self.add_patch_with_normal(u_idx_start=3, u_idx_end=4, v_idx_start=1, v_idx_end=2, color=YELLOW)
        self.add_patch_with_normal(u_idx_start=3, u_idx_end=4, v_idx_start=2, v_idx_end=3, color=YELLOW)
        self.add_patch_with_normal(u_idx_start=3, u_idx_end=4, v_idx_start=3, v_idx_end=4, color=YELLOW)
        self.add_patch_with_normal(u_idx_start=3, u_idx_end=4, v_idx_start=4, v_idx_end=5, color=YELLOW)
        self.add_patch_with_normal(u_idx_start=3, u_idx_end=4, v_idx_start=5, v_idx_end=6, color=YELLOW)
        self.add_patch_with_normal(u_idx_start=2, u_idx_end=3, v_idx_start=2, v_idx_end=3, color=YELLOW)
        self.add_patch_with_normal(u_idx_start=3, u_idx_end=4, v_idx_start=7, v_idx_end=8, color=YELLOW)
        
#       # Loop through all possible patches
#       for u_idx in range(phi_slices):
#           for v_idx in range(theta_slices):
#               u_idx_start = u_idx
#               u_idx_end = u_idx + 1
#               v_idx_start = v_idx
#               v_idx_end = v_idx + 1
#               self.add_patch_with_normal(u_idx_start, u_idx_end, v_idx_start, v_idx_end)

        self.wait(5)