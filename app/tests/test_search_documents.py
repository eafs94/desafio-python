def test_search_documents_found(client):
    # cria documento para testar busca
    client.post("/documentos", json={
        "titulo": "Era da Informação",
        "autor": "Autor X",
        "conteudo": "Informação importante",
        "data": "2025-01-01"
    })

    response = client.get("/documentos?palavraChave=informa")
    assert response.status_code == 200

    results = response.json()
    assert len(results) == 1
    assert results[0]["titulo"] == "Era da Informação"


def test_search_documents_not_found(client):
    response = client.get("/documentos?palavraChave=naoexiste")
    assert response.status_code == 200
    assert response.json() == []


def test_search_empty_keyword(client):
    response = client.get("/documentos?palavraChave=")
    assert response.status_code == 400
    assert response.json()["detail"] == "A palavra-chave nao pode ser vazia."
