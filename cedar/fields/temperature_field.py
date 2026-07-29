# cedar/fields/temperature_field.py
import numpy
from cedar.helpers.tensor_discrete_calculus import tensor_centre_laplacian

class TemperatureField:
    def __init__(self, simulation):
        if not simulation:
            raise Exception('No Simulation given!')
        self._simulation = simulation
        self.raster = numpy.zeros(simulation._resolution) # temperature field, in kelvin

    def solve(self, dt):

        # heat distribution: pd temp wrt time = diffusivity * laplacian temp wrt space

        diffusivity = 0.3  # placeholder until MaterialField is wired in
        h = self._simulation._cell_size
    
        laplacian = tensor_centre_laplacian(self.raster, h=h)

        out = self.copy()
        out.raster = self.raster + dt * diffusivity * laplacian
        
        return out

    def copy(self):
        out = TemperatureField(self._simulation)
        out.raster = self.raster.copy()
        return out