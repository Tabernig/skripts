import bpy
import numpy as np
import re
import time

def select(objName, additive=False):
    # By default, clear other selections
    if not additive:
        bpy.ops.object.select_all(action='DESELECT')
    # Set the 'select' property of the datablock to True
    bpy.data.objects[objName].select_set(True)

def myActivator(objName):
    # Pass bpy.data.objects datablock to scene class
    bpy.context.view_layer.objects.active = bpy.data.objects[objName]
    
def createGrid(Gridname,VerticesAsTuplesInList): 
    name = Gridname
    verts = VerticesAsTuplesInList
    faces = []
    #################Create Mesh Datablock
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts,[],faces)

    ################Create Object and link to scene
    obj = bpy.data.objects.new(name,mesh)
    bpy.context.collection.objects.link(obj)  #scene has been replaced by context

    ##########################Select the object:
    bpy.context.view_layer.objects.active = obj
    objName = bpy.context.object.name
    select(objName)

    

########## Paths ############
#Files:
#D:\_Programmieren\VU_Automatisierung_Daten\Daten\echoratio
begin = time.time()
echoratio = open("D:/_Programmieren/VU_Automatisierung_Daten/Daten/pointcloud1_small.txt")

###########generates Cubes at each point. Slow at large point numbers #################
#coordlist = []
#i = 0

#for line in echoratio:
#    line = line.strip()
#    getrennte_Line = re.split(";",line)
#    x= float(getrennte_Line[0])
#    y= float(getrennte_Line[1])
#    z= float(getrennte_Line[2])
#    coordlist.append([x,y,z])
##    if i < 10:
##        bpy.ops.mesh.primitive_cube_add(size=0.01, location=(x-680500.00, y-5237200.00, z-600))
##    i+=1
#coordArray = np.array(coordlist)

#############################################################################################################


############## 2D Gird creation ####################
name = "GRID"
name2D = "GRID2D"
rows = 10
columns = 20

verts = []
verts2D = []
listofx = []
listofy = []
listofz = []
counter = 0
for line in echoratio:
    line = line.strip()
    getrennte_Line = re.split("\t",line)
    x = float(getrennte_Line[0])
    y = float(getrennte_Line[1])
    z = float(getrennte_Line[2])
    listofx.append(x)
    listofy.append(y)
    listofz.append(z)
    
    verts2D.append((x,y,0))
    verts.append((x,y,z))


####### Gives the Volume for a cuboid containing all points ########
xmax,xmin = max(listofx),min(listofx)
ymax,ymin = max(listofy),min(listofy)
zmax,zmin = max(listofz),min(listofz)

xdiff = xmax - xmin
ydiff = ymax - ymin
zdiff = zmax - zmin
diffList = [xdiff,ydiff,zdiff]


############# Create the GRID at the Centre ################
centreGrid = "GRID CENTRE"
vertsCentred = []

for coords in verts:
    xC = coords[0]-xmin
    yC = coords[1]-ymin
    zC = coords[2]-zmin
    vertsCentred.append((xC,yC,zC))

#Optional
faces = []

createGrid(name,verts)
createGrid(name2D,verts2D)
createGrid(centreGrid, vertsCentred)

# SCALES by 30
#bpy.ops.transform.resize(value=(30, 30, 30), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, True, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)

bpy.ops.object.select_all(action='DESELECT')
#print(diffList)

####################### SCALE 10by10by10 #######################
#bpy.ops.transform.resize(value=(10, 10, 10), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, True, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)



#############################################################################################################

#print(coordArray)
########### creating some cubes
#rng = 9
#i = 0
#for k in range(rng):
#    for j in range(rng):
#        for i in range(rng):
#            bpy.ops.mesh.primitive_cube_add(size=1, location=(i, j, k))
#            if i%2== 0:
#                bpy.ops.mesh.primitive_cube_add(size=0.5, location=(i, j, k))
#            elif i%3 == 0:
#                bpy.ops.mesh.primitive_cube_add(size=0.4, location=(i, j, k))
            

########## Activating Objects ############
# Activate the object named 'Sphere'
#myActivator('Cube.124')
# Verify the 'Sphere' was activated
#print("Active object:", bpy.context.object.name)
# Selected objects were unaffected
#print("Selected objects:", bpy.context.selected_objects)


################ Selecting Objects ###############

# Select only 'Cube'
#mySelector('Cube.005')
#objName, objLocation = bpy.context.object.name,bpy.context.object.location

#print(objName,objLocation)
# Select 'Sphere', keeping other selections
#mySelector('Sphere', additive=True)
# Translate selected objects 1 unit along the x-axis
#bpy.ops.transform.translate(value=(1, 0, 0))













#Output Objekt datablock
#bpy.context.selected_objects

# Return the names of selected objects
#[k.name for k in bpy.context.selected_objects]
# Return the locations of selected objects
# (location of origin assuming no pending transformations)
#[k.location for k in bpy.context.selected_objects]

print("Done, took:"+str(time.time()-begin)+"seconds")


