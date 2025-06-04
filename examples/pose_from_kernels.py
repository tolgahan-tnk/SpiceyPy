import spiceypy as spice
import numpy as np

# List of kernel paths
# Local paths to the SPICE kernels needed for this example.  The ``mar097.bsp``
# kernel contains ephemerides for Mars and its satellites (Phobos and Deimos)
# from 1997 through 2050, which includes the example epoch below.  The
# ``pck00010.tpc`` file provides planetary orientation data.
kernel_list = [
    "/home/tt/corto/input/S07_Mars_Phobos_Deimos/kernels/naif0012.tls",
    "/home/tt/corto/input/S07_Mars_Phobos_Deimos/kernels/mar097.bsp",
    "/home/tt/corto/input/S07_Mars_Phobos_Deimos/kernels/pck00010.tpc",
]

# Load kernels
for k in kernel_list:
    spice.furnsh(k)

# Convert UTC to ET
spice_time = "2018-08-02T08:48:03.686"
et = spice.utc2et(spice_time)

# Example: position of Phobos relative to Mars at the epoch
pos, lt = spice.spkpos("PHOBOS", et, "J2000", "NONE", "MARS BARYCENTER")

# Orientation matrix from J2000 to Mars body-fixed frame
rot = spice.pxform("J2000", "IAU_MARS", et)

print("Phobos position (km):", pos)
print("Mars rotation matrix:")
print(rot)

# Always unload kernels when done
spice.kclear()
