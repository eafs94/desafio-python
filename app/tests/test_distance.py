from app.utils.distance import calcular_distancia

def test_distance_same_coordinates():
    d = calcular_distancia(-30.0, -51.0, -30.0, -51.0)
    assert round(d, 4) == 0
