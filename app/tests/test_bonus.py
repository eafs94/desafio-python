def test_search_by_phrase(client):
    # Criar documento para o teste
    client.post("/documentos", json={
        "titulo": "Guia da Cidade",
        "autor": "Autor Y",
        "conteudo": "Informações importantes sobre a cidade.",
        "data": "2025-01-01"
    })

    # Busca por frase
    response = client.get("/documentos?busca=sobre a cidade")

    assert response.status_code == 200
    results = response.json()

    assert len(results) == 1
    assert results[0]["titulo"] == "Guia da Cidade"


def test_search_sorted_by_distance(client):
    # Documento mais próximo
    client.post("/documentos", json={
        "titulo": "Doc Perto",
        "autor": "Autor 1",
        "conteudo": "Teste de local",
        "data": "2025-01-01",
        "latitude": -30.03,
        "longitude": -51.23
    })

    # Documento mais distante
    client.post("/documentos", json={
        "titulo": "Doc Longe",
        "autor": "Autor 2",
        "conteudo": "Teste distante",
        "data": "2025-01-01",
        "latitude": -20.00,
        "longitude": -40.00
    })

    # Busca que retorna ambos, com coordenadas do ponto próximo
    response = client.get(
        "/documentos?busca=Teste&latitude=-30.03&longitude=-51.23"
    )

    assert response.status_code == 200
    results = response.json()

    # O mais próximo deve vir primeiro
    assert results[0]["titulo"] == "Doc Perto"
