# cedar/fields/voltage_field.py
import numpy
from cedar.helpers.raster_operations import tensor_centre_laplacian
from cedar.fields.base_field_class import BaseField

class VoltageField(BaseField):
    def __init__(self, simulation):
        super().__init__(simulation)

    def solve(self, dt):
        cell_size = self._simulation._cell_size
        conductivity_field = self._simulation._fields['ElectricalConductivityField']
        neighbour_conductivity_harmonic_mean = conductivity_field.get_neighbour_harmonic_mean()

        out = self.copy()
        return out