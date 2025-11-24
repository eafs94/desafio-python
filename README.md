# **Microsserviço de Busca de Documentos**

Este projeto implementa um microsserviço em **Python + FastAPI** para criação e busca de documentos, conforme a especificação do desafio técnico.

O objetivo é entregar uma solução **simples**, **organizada**, **testada** e **de fácil manutenção**, seguindo boas práticas de arquitetura.

---

## **Tecnologias utilizadas**

* **FastAPI** – API REST leve, moderna e performática
* **SQLite + SQLAlchemy** – banco local persistente e ORM robusto
* **Pydantic** – validação e serialização de dados
* **Pytest** – testes automatizados
* **Logging nativo do Python** – rastreamento de operações e erros

---

## **Arquitetura do projeto**

Organizado em camadas para facilitar manutenção e clareza:

```
app/
 ├── api/               → rotas da API (FastAPI Router)
 ├── core/              → banco de dados e configurações
 ├── models/            → modelos SQLAlchemy (tabelas)
 ├── repositories/      → camada de acesso ao banco (CRUD)
 ├── schemas/           → contratos e validações Pydantic
 ├── services/          → regras de negócio
 ├── utils/             → utilitários (logger, cálculo de distância)
 ├── tests/             → testes unitários com pytest
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
* validação de erros
* fluxo completo dos endpoints principais

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
    "data": "2025-01-01",
    "latitude": -30.03,
    "longitude": -51.23
}
```

Retorno: **201 CREATED**

---

### **2. Buscar documentos por palavra-chave**

`GET /documentos`

Parâmetros disponíveis:

| Parâmetro      | Tipo   | Descrição                                        |
| -------------- | ------ | ------------------------------------------------ |
| `palavraChave` | string | Busca tradicional por palavra-chave              |
| `busca`        | string | **Busca por frase completa (bônus)**             |
| `latitude`     | float  | **Ordenação por proximidade geográfica (bônus)** |
| `longitude`    | float  | **Ordenação por proximidade geográfica (bônus)** |

---

### **2.1. Busca por palavra-chave**

```
GET /documentos?palavraChave=informação
```

Retorno:

* lista com documentos encontrados
* lista vazia se não encontrar
* erro 400 se palavra estiver vazia

---

### **2.2. Busca por frase (bônus)**

```
GET /documentos?busca=informações importantes sobre a cidade
```

A busca por frase verifica a ocorrência da frase completa no título, autor ou conteúdo.

---

### **2.3. Ordenação por geolocalização (bônus)**

Se latitude + longitude forem enviados, o resultado é ordenado automaticamente pela distância do ponto informado.

Exemplo:

```
GET /documentos?palavraChave=cidade&latitude=-30.03&longitude=-51.23
```

---

## **Logs**

A aplicação registra:

* criação de documentos
* buscas realizadas
* exceções e validações
* operações de ordenação geográfica

Os logs utilizam `logging` do Python via `utils/logger.py`.

---

## **Decisões Técnicas**

* **FastAPI** pela simplicidade e documentação automática.
* **SQLite** por ser leve e suficiente para o escopo do desafio.
* **SQLAlchemy** para um CRUD mais limpo e organizado.
* **Arquitetura em camadas** para separar responsabilidades.
* **Testes automatizados** para garantir funcionamento e cumprir critérios de avaliação.

---

## **Observações**

* A busca por frase utiliza comparação “contém” (`LIKE "%frase%"`).
* A busca por palavra-chave mantém o comportamento mais restritivo definido inicialmente.
* Latitude/longitude são opcionais e utilizadas apenas para ordenação.
* A aplicação está pronta para expansão futura caso necessário.
