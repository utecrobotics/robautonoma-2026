# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import pcl

# Cargar la nube de puntos
cloud = pcl.load_XYZRGB('mesa_downsampled.pcd')

# Crear un filtro PassThrough
passthrough = cloud.make_passthrough_filter()

# Assignar el eje y el rango para el filtro.
filter_axis = 'y'
passthrough.set_filter_field_name(filter_axis)
min_val = 0.5
max_val = 1.5
passthrough.set_filter_limits(min_val, max_val)

# Usar el filtro para obtener la nube de puntos resultante
cloud_filtered = passthrough.filter()

# Grabar el resultado en disco
filename = 'mesa_pass.pcd'
pcl.save(cloud_filtered, filename)