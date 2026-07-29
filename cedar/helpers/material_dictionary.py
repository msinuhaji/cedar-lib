# cedar/helpers/materials.py

class MATERIALS:
    COPPER = {
        'DensityField': 8960,
        'ElectricalConductivityField': 5.8e7,
        'PermittivityField': 1.0,
        'ThermalConductivityField': 401,
        'HeatCapacityField': 385,
    }
    AIR = {
        'DensityField': 1.2,
        'ElectricalConductivityField': 0.0,
        'PermittivityField': 1.0006,
        'ThermalConductivityField': 0.026,
        'HeatCapacityField': 1005,
    }
    SILICON = {
        'DensityField': 2330,
        'ElectricalConductivityField': 1e-3,
        'PermittivityField': 11.7,
        'ThermalConductivityField': 150,
        'HeatCapacityField': 705,
    }
    ALUMINIUM = {
        'DensityField': 2700,
        'ElectricalConductivityField': 3.5e7,
        'PermittivityField': 1.0,
        'ThermalConductivityField': 237,
        'HeatCapacityField': 897,
    }
    GOLD = {
        'DensityField': 19300,
        'ElectricalConductivityField': 4.1e7,
        'PermittivityField': 1.0,
        'ThermalConductivityField': 314,
        'HeatCapacityField': 129,
    }
    SILICON_DIOXIDE = {  # common insulator/dielectric layer in chips
        'DensityField': 2650,
        'ElectricalConductivityField': 1e-14,
        'PermittivityField': 3.9,
        'ThermalConductivityField': 1.4,
        'HeatCapacityField': 703,
    }
    FR4 = {  # common PCB substrate material
        'DensityField': 1850,
        'ElectricalConductivityField': 1e-12,
        'PermittivityField': 4.5,
        'ThermalConductivityField': 0.3,
        'HeatCapacityField': 1150,
    }