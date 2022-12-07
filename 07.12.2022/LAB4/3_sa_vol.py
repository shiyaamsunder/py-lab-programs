import math
def calculate_sa_vol(r):
    sa = 4 * math.pi * r ** 2
    vol = (4 / 3) * math.pi * r ** 3
    return [sa, vol]
radius = float(input("Enter the radius of sphere: "))

[sa, vol] = calculate_sa_vol(radius)

print(f"Surface area of the circle: %.2f\nVolume of the sphere: %.2f" % (sa, vol))
