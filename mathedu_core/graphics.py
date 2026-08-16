"""Digital Differential Analyzer (DDA) line-generation algorithm."""


def dda_line(x0, y0, x1, y1):
    """Generate the integer raster coordinates of the line from (x0, y0) to (x1, y1).

    Returns ``(x_coordinates, y_coordinates, x_increments, y_increments)``.
    """
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)
    steps = max(dx, dy)

    if steps == 0:
        return [round(x0)], [round(y0)], ["-"], ["-"]

    xinc = dx / steps
    yinc = dy / steps

    x = float(x0)
    y = float(y0)

    x_coordinates = [round(x)]
    y_coordinates = [round(y)]
    x_inc = []
    y_inc = []

    for _ in range(int(steps)):
        x = round(x, 2) + xinc
        y = round(y, 2) + yinc
        x_coordinates.append(round(x))
        y_coordinates.append(round(y))
        x_inc.append(round(x, 2))
        y_inc.append(round(y, 2))

    x_inc.append("-")
    y_inc.append("-")

    return x_coordinates, y_coordinates, x_inc, y_inc