# **Microsserviço de Busca de Documentos**

Este projeto implementa um microsserviço em **Python + FastAPI** para criação e busca de documentos a partir de uma palavra-chave, conforme a especificação do desafio técnico.
O foco é uma solução simples, organizada, funcional e fácil de manter.

---

## **🔧 Tecnologias utilizadas**

* **FastAPI** (API REST simples e performática)
* **SQLite + SQLAlchemy** (banco leve, persistente e com ORM)
* **Pydantic** (validação de dados)
* **Pytest** (testes automatizados)
* **Logging nativo do Python**

---

## **Arquitetura do projeto**

Organizado em camadas para facilitar manutenção e clareza:

```
app/
 ├── api/               → rotas da API (FastAPI Router)
 ├── core/              → banco de dados e configurações gerais
 ├── models/            → modelos SQLAlchemy (tabelas)
 ├── repositories/      → camada de acesso ao banco (CRUD)
 ├── schemas/           → validações e contratos Pydantic
 ├── services/          → regras de negócio
 ├── utils/             → utilitários e logger
 ├── tests/             → testes unitários (pytest)
 └── main.py            → ponto de entrada da aplicação
```

---

## **Como executar o projeto**

### 1. Instalar dependências

```
pip install -r requirements.txt
```

### 2. Rodar a aplicação

```
uvicorn app.main:app --reload
```

### 3. Documentação automática

Acesse:

```
http://127.0.0.1:8000/docs
```

---

## **Como executar os testes**

```
pytest -q
```

Os testes cobrem:

* criação de documento
* busca por palavra-chave
* cenários de erro para entradas inválidas

---

## **Endpoints**

### **1. Criar documento**

`POST /documentos`

Exemplo:

```json
{
    "titulo": "Meu Documento",
    "autor": "Eric",
    "conteudo": "Texto simples",
    "data": "2025-01-01"
}
```

Retorno: **201 CREATED**

---

### **2. Buscar documentos por palavra-chave**

`GET /documentos?palavraChave=info`

Exemplo:

```
GET /documentos?palavraChave=Informação
```

Exemplo de retorno:

```json
[
  {
    "id": 1,
    "titulo": "Era da Informação",
    "autor": "Autor X",
    "conteudo": "Informação importante",
    "data": "2025-01-01"
  }
]
```

Regras:

* palavra inexistente → lista vazia
* palavra vazia → erro 400

---

## **Logs**

A aplicação registra:

* criação de documentos
* buscas realizadas
* erros de validação

Os logs utilizam `logging` do Python e são gerenciados pelo utilitário `utils/logger.py`.

---

## **Decisões Técnicas**

* **FastAPI** pela simplicidade e documentação automática.
* **SQLite** por ser leve e suficiente para o escopo do desafio.
* **SQLAlchemy** para um CRUD mais limpo e organizado.
* **Arquitetura em camadas** para separar responsabilidades.
* **Testes automatizados** para garantir funcionamento e cumprir critérios de avaliação.

---

## **Observações**

* O escopo principal foi implementado conforme solicitado.
* A estrutura está preparada para possíveis expansões (ex.: ordenação por geolocalização e busca por frase).
