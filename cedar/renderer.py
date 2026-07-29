import numpy
from vispy import app, scene

app.use_app('pyqt6')

class Renderer:
    def __init__(self, simulation):
        if simulation is None:
            raise Exception('No Simulation given!')

        self.simulation = simulation
        self.canvas = scene.SceneCanvas(
            keys='interactive',
            show=True
        )
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = "panzoom"
        self.view.camera.set_range()

        self.displayingFields = {}
        self.displayingVisuals = {}

    def showField(self, fieldName):
        if fieldName not in self.simulation._fields:
            raise Exception('Field does not exist!')

        self.displayingFields[fieldName] = self.simulation._fields[fieldName] # NOTE: CREATE A FIELD BASE CLASS! THIS IS IMPORTANT!
        visual = scene.visuals.Image(
            self.displayingFields[fieldName].raster,
            cmap='hot',
            interpolation="linear",
            parent=self.view.scene,
            opacity=1/len(self.displayingFields)
        )
        self.displayingVisuals[fieldName] = visual

        raster = self.displayingFields[fieldName].raster
        if raster.ndim == 2:
            height, width = raster.shape
            self.view.camera.set_range(x=(0, width), y=(0, height), margin=0)

    def update(self):
        for name, visual in self.displayingVisuals.items():
            visual.set_data(
                self.simulation._fields[name].raster
            )