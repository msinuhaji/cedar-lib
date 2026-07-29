# NOTE: NEXT UPDATE ABSTRACTS SIGNIFICANTLY
# TODO TOMORROW: CREATE BASE FIELD CLASS, IMPROVE RENDERING, MAKE MATERIAL FIELD WORK!

from vispy import app
from cedar.simulation import Simulation
from cedar.helpers.material_dictionary import MATERIALS
import traceback

sim = Simulation([70, 50], {"cell_size": 0.008})

sim.drawFillFromMaterial(MATERIALS.AIR)
sim.drawRectFromMaterial(MATERIALS.COPPER, [0, 10], [70, 20])
sim.drawRectFromMaterial(MATERIALS.COPPER, [0, 0], [10, 40])
sim.drawRect('TemperatureField', 400, [0, 0], [10, 40])

sim.showField('TemperatureField')
# sim.showField('DensityField')

def update(event):
    try:
        sim.step(0.1)
    except Exception:
        traceback.print_exc()
        timer.stop()   # stop retrying once we've seen the real error

timer = app.Timer(interval=0.01)
timer.connect(update)
timer.start()

app.run()