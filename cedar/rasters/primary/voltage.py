from cedar.raster import Raster
from primary.charge_density import ChargeDensity
from rasters.secondary.architecture.permittivity import Permittivity

class Voltage(Raster):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def solve(self):
        pass