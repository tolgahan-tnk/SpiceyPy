import spiceypy as spice
import numpy as np

# Paths to the SPICE kernels needed for this example
kernel_list = [
    "/home/tt/corto/input/S07_Mars_Phobos_Deimos/kernels/naif0012.tls",
    "/home/tt/corto/input/S07_Mars_Phobos_Deimos/kernels/mar097.bsp",
    "/home/tt/corto/input/S07_Mars_Phobos_Deimos/kernels/pck00010.tpc",
]

for k in kernel_list:
    spice.furnsh(k)

spice_time = "2018-08-02T08:48:03.686"
et = spice.utc2et(spice_time)

# Positions relative to Mars
phobos_pos, _ = spice.spkpos("PHOBOS", et, "J2000", "NONE", "MARS BARYCENTER")
sun_pos, _ = spice.spkpos("SUN", et, "J2000", "NONE", "MARS BARYCENTER")

# Orientations from J2000 to body-fixed frames
mars_rot = spice.pxform("J2000", "IAU_MARS", et)
phobos_rot = spice.pxform("J2000", "IAU_PHOBOS", et)
sun_rot = spice.pxform("J2000", "IAU_SUN", et)

print("Phobos position (km):", phobos_pos)
print("Sun position (km):", sun_pos)
print("Mars rotation matrix:\n", mars_rot)
print("Phobos rotation matrix:\n", phobos_rot)
print("Sun rotation matrix:\n", sun_rot)

spice.kclear()
