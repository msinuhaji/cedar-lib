import numpy as np
import scipy as sp

class Raster:
    def __init__ (self, **kwargs):
        self.kwargs = kwargs
        self.matrix = np.zeros([kwargs.get("width", 1), kwargs.get("length", 1)])
        self.cell_size = kwargs.get("cell_size", 1)
    
    def solve(self):
        return self.copy()
        
    def central_grad(self, neumann_border_conditions=True):
        if len(self.matrix.shape) != 2: raise ValueError("Raster is the wrong shape; cannot operate gradients!")
        
        padded = np.pad(self.matrix, 1, "reflect" if neumann_border_conditions else "constant")
        
        partial_x = sp.ndimage.correlate(
            padded,
            np.array([[-1, 0, 1]]) / (2 * self.cell_size)
        )
        partial_y = sp.ndimage.correlate(
            padded,
            np.array([[-1], [0], [1]]) / (2 * self.cell_size)
        )
        
        out = self.copy()
        out.matrix = np.stack((partial_x, partial_y), axis=-1)[1:-1, 1:-1]
        
        return out
    
    def divergence(self, neumann_border_conditions=True): # do not use to take laplacian or else second dir issues
        if len(self.matrix.shape) != 3: raise ValueError("Raster is the wrong shape; cannot operate divergence!")
        if self.matrix.shape[2] != 2: raise ValueError("Not a vector raster; cannot operate divergence!")
        
        padded = np.pad(self.matrix, ((1, 1), (1, 1), (0, 0)), "reflect" if neumann_border_conditions else "constant")
        f_x = padded[..., 0]
        f_y = padded[..., 1]
        
        f_x_wrt_x = sp.ndimage.correlate(
           f_x,
           np.array([[-1, 0, 1]]) / (2 * self.cell_size)
        )
        f_y_wrt_y = sp.ndimage.correlate(
            f_y,
            np.array([[-1], [0], [1]]) / (2 * self.cell_size)
        )
        
        out = self.copy()
        out.matrix = (f_x_wrt_x + f_y_wrt_y)[1:-1, 1:-1]
        
        return out
    
    def curl(self, neumann_border_conditions=True):
        if len(self.matrix.shape) != 3: raise ValueError("Raster is the wrong shape; cannot operate curl!")
        if self.matrix.shape[2] != 2: raise ValueError("Not a vector raster; cannot operate curl!")
        
        padded = np.pad(self.matrix, ((1, 1), (1, 1), (0, 0)), "reflect" if neumann_border_conditions else "constant")
        f_x = padded[..., 0]
        f_y = padded[..., 1]
        
        f_y_wrt_x = sp.ndimage.correlate(
            f_y,
            np.array([[-1, 0, 1]]) / (2 * self.cell_size)
        )
        f_x_wrt_y = sp.ndimage.correlate(
           f_x,
           np.array([[-1], [0], [1]]) / (2 * self.cell_size)
        )

        out = self.copy()
        out.matrix = (f_y_wrt_x - f_x_wrt_y)[1:-1, 1:-1]
        
        return out
    
    def copy(self):
        out = type(self)(**self.kwargs)
        out.matrix = self.matrix.copy()
        return out