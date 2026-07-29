# cedar/fields/material_field.py
import numpy

class MaterialField:
    def __init__(self, simulation):
        if simulation is None:
            raise Exception('No Simulation given!')
        self._simulation = simulation

        # The following raster is [density, electrical_conductivity, permittivity, thermal_conductivity, heat_capacity]
        self.raster = numpy.full((*simulation._resolution, 5), 0.0) 

    def solve(self, dt):
        return self.copy()

    def copy(self):
        out = MaterialField(self._simulation)
        out.raster = self.raster.copy()
        return out