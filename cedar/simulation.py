# cedar/simulation.py
from cedar.fields.material_field import MaterialField
from cedar.fields.temperature_field import TemperatureField


class Simulation:
    def __init__(self, resolution: list, configs: dict):
        self._time = 0.0
        self._resolution = resolution
        self._fields = {
            "MaterialField": MaterialField(self),
            "TemperatureField": TemperatureField(self),
        }

        self._cell_size = configs["cell_size"] or 1.0
        self._step_size = self._cell_size**2  # per unit seconds

    def step(self, dt):

        out_fields = {}

        # solve all fields before setting time

        for name, field in self._fields.items():
            out_fields[name] = field.solve(dt)

        self._time += dt
        self._fields = out_fields

    def render(self):
        pass
