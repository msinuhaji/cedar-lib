# cedar/fields/temperature_field.py
import numpy

class BaseField:
    def __init__(self, simulation):
        if not simulation:
            raise Exception('No Simulation given!')
        self._simulation = simulation
        self.raster = numpy.zeros(simulation._resolution) # default zeroes res. the only thing here is that there HAS to be a raster

    def solve(self, dt):
        return self.copy()

    def copy(self):
        out = type(self)(self._simulation)
        out.raster = self.raster.copy()
        return out