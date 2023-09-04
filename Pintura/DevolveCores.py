import colorgram

colors = colorgram.extract('Projeto 18\imagem2.jpg', 15)
cores_rgb = []
for cor in colors:
    r = cor.rgb.r
    g = cor.rgb.g
    b = cor.rgb.b
    nova_cor = (r,g,b)
    cores_rgb.append(nova_cor)
print(cores_rgb)