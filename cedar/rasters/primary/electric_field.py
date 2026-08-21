from cedar.raster import Raster

class ElectricField(Raster):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def solve(self):
        pass