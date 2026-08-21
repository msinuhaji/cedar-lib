from cedar.raster import Raster

class ChargeDensity(Raster):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def solve(self):
        pass