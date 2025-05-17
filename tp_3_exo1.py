from Mathy import (
    Vector3,
    TranslationMatrix3x3,
    RotationMatrix3x3,
    HomothetyMatrix3x3
)

# --- Question 1 ---
# Create a translation matrix to move the character to position (1, 2)
translation = TranslationMatrix3x3(1, 2)
print("Question 1 - Translation matrix (to position (1, 2)):")
print(translation)

# --- Question 2 ---
# Create a rotation matrix for a 45° counterclockwise rotation
rotation = RotationMatrix3x3(45)
print("\nQuestion 2 - Rotation matrix (45° counterclockwise):")
print(rotation)

# --- Question 3 ---
# Create a homothety matrix with a scale factor of 2
homothety = HomothetyMatrix3x3(2)
print("\nQuestion 3 - Homothety matrix (scaling by factor of 2):")
print(homothety)

# --- Question 4 ---
# Compose the global transformation (translation * rotation * homothety)
global_transform = translation.prod(rotation).prod(homothety)
print("\nComposed global transformation matrix (Translation * Rotation * Homothety):")  # noqa: E501
print(global_transform)

# Define the local transformation of the sword
sword_translation = TranslationMatrix3x3(0.5, -0.5)
sword_rotation = RotationMatrix3x3(180)
local_sword_transform = sword_translation.prod(sword_rotation)
print("\nQuestion 4 - Local sword transformation matrix (Translation(0.5, -0.5) * Rotation(180°)):")  # noqa: E501
print(local_sword_transform)

# --- Question 5 ---
# Apply the full transformation to the sword's local position
final_transform = global_transform.prod(local_sword_transform)
print("\nQuestion 5 - Final transformation matrix:")
print(final_transform)

# Apply the final transformation to the origin of the sword's local frame 
# to get its position in world coordinates
sword_world_position = Vector3(0, 0, 1).multiply_by_matrix(final_transform)
print("\nSword world coordinates after full transformation:")
print(sword_world_position)
