import numpy
from vispy import app, scene
from vispy.color import Colormap

app.use_app('pyqt6')

# a small palette of single-hue colormaps (transparent -> solid colour),
# cycled through as fields are added, so each layer is visually distinct
_PALETTE = [
    
    Colormap([(0, 1, 0, 0), (0, 1, 0, 1)]),   # green
    Colormap([(1, 0, 0, 0), (1, 0, 0, 1)]),   # red
    
    Colormap([(0, 0.4, 1, 0), (0, 0.4, 1, 1)]),  # blue
    Colormap([(1, 1, 0, 0), (1, 1, 0, 1)]),   # yellow
    Colormap([(1, 0, 1, 0), (1, 0, 1, 1)]),   # magenta
    Colormap([(0, 1, 1, 0), (0, 1, 1, 1)]),   # cyan
]


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
        self.view.camera.interactive = False

        self.displayingFields = {}
        self.displayingVisuals = {}

    def showField(self, fieldName):
        if fieldName not in self.simulation._fields:
            raise Exception('Field does not exist!')

        self.displayingFields[fieldName] = self.simulation._fields[fieldName]

        colormap = _PALETTE[len(self.displayingVisuals) % len(_PALETTE)]

        visual = scene.visuals.Image(
            self.displayingFields[fieldName].raster,
            cmap=colormap,
            interpolation="linear",
            parent=self.view.scene,
        )
        visual.set_gl_state('translucent', depth_test=False)  # allow proper alpha blending between layers
        self.displayingVisuals[fieldName] = visual

        # # re-normalize opacity across ALL currently displayed fields, not just the new one
        # new_opacity = 1 / len(self.displayingVisuals) + 0.2
        # for v in self.displayingVisuals.values():
        #     v.opacity = new_opacity

        raster = self.displayingFields[fieldName].raster
        if raster.ndim == 2:
            height, width = raster.shape
            self.view.camera.set_range(x=(0, width), y=(0, height), margin=0)

    def update(self):
        for name, visual in self.displayingVisuals.items():
            visual.set_data(
                self.simulation._fields[name].raster
            )