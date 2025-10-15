def find_farthest_orbit(orbits):
    return max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1])