def test_create_document_success(client):
    payload = {
        "titulo": "Meu Documento",
        "autor": "Eric",
        "conteudo": "Texto simples",
        "data": "2025-01-01",
        "latitude": -30.0,
        "longitude": -51.0
    }

    response = client.post("/documentos", json=payload)

    assert response.status_code == 201
    result = response.json()

    assert result["titulo"] == "Meu Documento"
    assert result["autor"] == "Eric"
    assert "id" in result


def test_create_document_empty_title(client):
    payload = {
        "titulo": "",
        "autor": "Eric",
        "conteudo": "Texto qualquer",
        "data": "2025-01-01"
    }

    response = client.post("/documentos", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "O titulo do documento nao pode ser vazio."


def test_create_document_without_coordinates(client):
    payload = {
        "titulo": "Doc sem coords",
        "autor": "Autor",
        "conteudo": "Teste",
        "data": "2025-01-01"
    }

    response = client.post("/documentos", json=payload)

    assert response.status_code == 422  # erro de validação pydantic


def test_create_document_without_longitude(client):
    payload = {
        "titulo": "Doc inválido",
        "autor": "Autor",
        "conteudo": "Teste",
        "data": "2025-01-01",
        "latitude": -30.0
    }

    response = client.post("/documentos", json=payload)
    assert response.status_code == 422
