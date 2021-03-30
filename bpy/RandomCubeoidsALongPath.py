import bpy
import random

######################## FUNCTIONS ############################
def select(objName, additive=False):
    # By default, clear other selections
    if not additive:
        bpy.ops.object.select_all(action='DESELECT')
    # Set the 'select' property of the datablock to True
    bpy.data.objects[objName].select_set(True)

def myActivator(objName):
    # Pass bpy.data.objects datablock to scene class
    bpy.context.view_layer.objects.active = bpy.data.objects[objName]

################### INPUT VALUES ################
#side a and b
locationcount = 8
width = 6
ballcount = 13

#Objectparameter
objectLength = 1
objectWidth = 0.1

#Set max cap for balls
if (ballcount > width) or (ballcount > locationcount):
    ballcount = min([locationcount,width])

######################## Predefined Parameters for Calculation #############
#Defines MIN Space between 2 Objects
maxBallsize = objectWidth 
bigger = max([locationcount,width])

distance = objectLength + 2*objectWidth
sizePlane = bigger*distance 

x = -(locationcount-1)*distance/2 #Build Objects centered
for i in range(locationcount):
    move = -(width-1)*distance/2
    for j in range(width):
        #Create Object at location
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(move, x, 0), scale=(objectWidth, objectLength, objectWidth))
        # Rotate on a random angle
        rotate = random.randrange(0, 63, 1)/10
        bpy.ops.transform.rotate(value=rotate, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
        #Change Physics to rigid Body -> PASSIVE
        objName, objLocation = bpy.context.object.name,bpy.context.object.location
        select(objName)
        bpy.ops.rigidbody.object_add(type='PASSIVE')
        move += distance
    x+=distance

######################## Create and adjust Plane beneath #####################
bpy.ops.mesh.primitive_plane_add(size=sizePlane, enter_editmode=False, align='WORLD', location=(0, 0, -objectWidth/2), scale=(1, 1, 1))
#Scale Down to Size
if locationcount > width:
    bpy.ops.transform.resize(value=(width/locationcount, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
elif locationcount < width:
    bpy.ops.transform.resize(value=(1, locationcount/width, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)


#Change Physics to rigid Body -> PASSIVE
objName, objLocation = bpy.context.object.name,bpy.context.object.location
select(objName)
bpy.ops.rigidbody.object_add(type='PASSIVE')
    


####################### Create Balls ########################

ballXLoc = -width/2 + width/ballcount
for ball in range(ballcount):
    ballsize = random.randrange(0,maxBallsize*100,1)/100
    bpy.ops.mesh.primitive_uv_sphere_add(radius=ballsize, enter_editmode=False, align='WORLD', location=(ballXLoc, locationcount*distance/2, 0), scale=(1, 1, 1))
    bpy.ops.rigidbody.object_add(type='ACTIVE')
    ballXLoc += width/ballcount
    
    
    
    