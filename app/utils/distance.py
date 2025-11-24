import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371  # raio da Terra
    
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    d_lat = lat2 - lat1
    d_lon = lon2 - lon1

    a = (
        math.sin(d_lat / 2)**2
        + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2)**2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c
