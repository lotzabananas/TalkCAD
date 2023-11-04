import vtk

# Create a sphere
sphere = vtk.vtkSphereSource()
sphere.SetRadius(5)
sphere.SetPhiResolution(50)
sphere.SetThetaResolution(50)
sphere.Update()

# Create a mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(sphere.GetOutputPort())

# Create an actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Add the actor to the scene
renderer.AddActor(actor)
renderer.SetBackground(0.1, 0.2, 0.3)  # Background color dark blue

# Render and interact
renderWindow.Render()
renderWindowInteractor.Start()

# Export to STL
stlWriter = vtk.vtkSTLWriter()
stlWriter.SetFileName("sphere.stl")
stlWriter.SetInputConnection(sphere.GetOutputPort())
stlWriter.Write()
