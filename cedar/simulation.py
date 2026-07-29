# cedar/simulation.py
from cedar.renderer import Renderer

from cedar.fields.base_field_class import BaseField
from cedar.fields.temperature_field import TemperatureField
from cedar.fields.material_fields import DensityField, ElectricalConductivityField, PermittivityField, ThermalConductivityField, HeatCapacityField

class Simulation:
    def __init__(self, resolution: list, configs: dict = None):
        configs = configs or {}
        self._time = 0.0
        self._resolution = resolution
        self._fields = {
            "DensityField": DensityField(self),
            "ElectricalConductivityField": ElectricalConductivityField(self),
            "PermittivityField": PermittivityField(self),
            "ThermalConductivityField": ThermalConductivityField(self),
            "HeatCapacityField": HeatCapacityField(self),
            "TemperatureField": TemperatureField(self),
        }

        self._cell_size = configs.get("cell_size", 1.0) # per unit metres
        self._step_size = self._cell_size**2  # per unit seconds

        self.renderer = Renderer(self)

    def step(self, dt):

        out_fields = {}

        # solve all fields before setting time

        for name, field in self._fields.items():
            out_fields[name] = field.solve(dt)

        self._time += dt
        self._fields = out_fields

        self.renderer.update()

    def showField(self, field_name):
        self.renderer.showField(field_name)

    def drawRect(self, field_name: str, value: float, top_left_corner: tuple, bottom_right_corner: tuple):
        if field_name is None or value is None or top_left_corner is None or bottom_right_corner is None:
            raise Exception('Params undefined!')

        if not field_name in self._fields:
            raise Exception('Field does not exist!')

        x1, y1 = top_left_corner
        x2, y2 = bottom_right_corner
        self._fields[field_name].raster[y1:y2, x1:x2] = value

    def drawFill(self, field_name: str, value: float):
        if field_name is None or value is None:
            raise Exception('Params undefined!')

        if not field_name in self._fields:
            raise Exception('Field does not exist!')

        self._fields[field_name].raster[:, :] = value

    def drawRectFromMaterial(self, field_value_dict: dict, top_left_corner: tuple, bottom_right_corner: tuple):
        if field_value_dict is None or top_left_corner is None or bottom_right_corner is None:
            raise Exception('Params undefined!')

        x1, y1 = top_left_corner
        x2, y2 = bottom_right_corner

        for field in field_value_dict:
            self._fields[field].raster[y1:y2, x1:x2] = field_value_dict[field]

    def drawFillFromMaterial(self, field_value_dict: dict):
            if field_value_dict is None:
                raise Exception('Params undefined!')

            for field in field_value_dict:
                self._fields[field].raster[:, :] = field_value_dict[field]
        