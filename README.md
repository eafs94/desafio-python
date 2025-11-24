# **Microsserviço de Busca de Documentos**

Este projeto implementa um microsserviço em **Python + FastAPI** para criação e busca de documentos a partir de uma palavra-chave, conforme especificação do desafio técnico.
O foco é uma solução simples, organizada, funcional e fácil de manter.

---

## **🔧 Tecnologias utilizadas**

* **FastAPI** (API REST simples e performática)
* **SQLite + SQLAlchemy** (banco leve, não-volátil e com ORM)
* **Pydantic** (validação de dados)
* **Pytest** (testes automatizados)
* **Logging nativo do Python**

---

## **Arquitetura do projeto**

Organização em camadas para facilitar manutenção:

```
app/
 ├── core/           → conexão com banco e configurações
 ├── models/         → modelos SQLAlchemy
 ├── schemas/        → schemas Pydantic
 ├── repositories/   → acesso ao banco
 ├── services/       → regras de negócio
 ├── routers/        → rotas da API
 ├── logs/           → configuração de logs
 └── tests/          → testes unitários
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

Testes simples cobrindo criação e busca de documentos:

```
pytest -q
```

---

## **Endpoints**

### **1. Criar documento**

**POST /documentos**

Exemplo de corpo JSON:

```json
{
    "titulo": "Meu Documento",
    "autor": "Eric",
    "conteudo": "Texto simples",
    "data": "2025-01-01"
}
```

Retorno esperado:
201 CREATED com os dados gravados.

---

### **2. Buscar documentos por palavra-chave**

**GET /documentos?palavraChave=info**

Retorna lista de documentos cujo título ou conteúdo contenham a palavra informada.

Exemplo:

```
GET /documentos?palavraChave=Informação
```

Retorno:

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

Para palavra inexistente → retorna lista vazia.
Para palavra vazia → retorna erro **400**.

---

## **Logs**

A aplicação registra:

* criação de documentos
* buscas realizadas
* erros de validação

Os logs utilizam o **logging padrão do Python** e ficam acessíveis no console ou no handler configurado.

---

## **Decisões Técnicas**

* **FastAPI** → rápido, moderno e oferece documentação automática.
* **SQLite** → leve, persistente e suficiente para o escopo do desafio.
* **SQLAlchemy** → ORM consolidado, facilita CRUD e manutenção.
* **Arquitetura em camadas** → deixa o código limpo, isolado e fácil de evoluir.
* **Testes automatizados** → garantem que a API funciona e atendem ao critério da banca.

---

## **Observações**

* Apenas o escopo principal foi implementado conforme solicitado.
* Estrutura preparada para expansão (ex.: ordenação por geolocalização e busca por frases).
