import bpy
import random



locationcount = 50
width = 50





x = 0
for i in range(locationcount):
    move = -0.5
    for j in range(width):
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(move, x, 0), scale=(0.1, 0.3, 0.1))
        rotate = random.randrange(0, 63, 1)/10
        bpy.ops.transform.rotate(value=rotate, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
        move += 0.5
    x+=0.5
