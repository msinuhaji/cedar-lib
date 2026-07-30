# cedar/fields/material_fields.py
import numpy
from cedar.fields.base_field_class import BaseField

class DensityField(BaseField):
    pass  # basefield default class, no changes needed!

class ElectricalConductivityField(BaseField):
    def get_neighbour_harmonic_mean(self):
        reciprocal_raster = 1 / self.raster
        padded_reciprocal = numpy.pad(reciprocal_raster, 1, mode="edge")
        trim = (slice(1, -1), slice(1, -1))

        def harmonic_mean_towards(shift, axis):
            neighbour_reciprocal = numpy.roll(padded_reciprocal, shift, axis=axis)
            return (1 / ((padded_reciprocal + neighbour_reciprocal) / 2))[trim]

        return {
            'up':    harmonic_mean_towards(shift=-1, axis=0),
            'down':  harmonic_mean_towards(shift=1,  axis=0),
            'left':  harmonic_mean_towards(shift=-1, axis=1),
            'right': harmonic_mean_towards(shift=1,  axis=1),
        }

class PermittivityField(BaseField):
    pass

class ThermalConductivityField(BaseField):
    pass

class HeatCapacityField(BaseField):
    pass