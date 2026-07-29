# cedar/fields/temperature_field.py
import numpy
from cedar.helpers.tensor_discrete_calculus import tensor_centre_laplacian
from cedar.fields.base_field_class import BaseField

class TemperatureField(BaseField):
    def __init__(self, simulation):
        super().__init__(simulation)

    def solve(self, dt):
        h = self._simulation._cell_size
        k = self._simulation._fields["ThermalConductivityField"].raster
        denominator = (
            self._simulation._fields["DensityField"].raster
            * self._simulation._fields["HeatCapacityField"].raster
        )

        diffusivity = numpy.divide(
            k, denominator,
            out=numpy.zeros_like(k),
            where=denominator > 0
        )

        laplacian = tensor_centre_laplacian(self.raster, h=h)

        out = self.copy()
        out.raster = self.raster + dt * diffusivity * laplacian
        return out