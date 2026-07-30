# cedar/fields/temperature_field.py
import numpy
from cedar.helpers.raster_operations import tensor_centre_laplacian
from cedar.fields.base_field_class import BaseField

class TemperatureField(BaseField):

    def solve(self, dt):
        cell_size = self._simulation._cell_size
        thermal_conductivity = self._simulation._fields["ThermalConductivityField"].raster
        density_times_heat_capacity = (
            self._simulation._fields["DensityField"].raster
            * self._simulation._fields["HeatCapacityField"].raster
        )

        diffusivity = numpy.divide(
            thermal_conductivity, density_times_heat_capacity,
            out=numpy.zeros_like(thermal_conductivity),
            where=density_times_heat_capacity > 0
        )

        laplacian = tensor_centre_laplacian(self.raster, h=cell_size)

        out = self.copy()
        out.raster = self.raster + dt * diffusivity * laplacian
        return out