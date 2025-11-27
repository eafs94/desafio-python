def test_search_plural_singular(client):
    client.post("/documentos", json={
        "titulo": "Informações sobre grandes cidades",
        "autor": "Autor",
        "conteudo": "As cidades brasileiras são diversas.",
        "data": "2025-01-01",
        "latitude": -30.0,
        "longitude": -51.0
    })

    response = client.get("/documentos?palavraChave=diversa")

    assert response.status_code == 200
    results = response.json()

    assert len(results) == 1
    assert results[0]["titulo"] == "Informações sobre grandes cidades"
