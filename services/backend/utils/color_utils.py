def generate_pastel_colormap(num_colors):
    colormap = []

    for i in range(num_colors):
        hue = i / num_colors
        saturation = 0.3
        value = 0.9

        h_i = int(hue * 6)
        f = hue * 6 - h_i
        p = value * (1 - saturation)
        q = value * (1 - f * saturation)
        t = value * (1 - (1 - f) * saturation)

        r, g, b = 0, 0, 0

        if h_i == 0:
            r, g, b = value, t, p
        elif h_i == 1:
            r, g, b = q, value, p
        elif h_i == 2:
            r, g, b = p, value, t
        elif h_i == 3:
            r, g, b = p, q, value
        elif h_i == 4:
            r, g, b = t, p, value
        elif h_i == 5:
            r, g, b = value, p, q

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
        colormap.append(hex_color)

    return colormap
