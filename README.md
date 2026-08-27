# API de Gerenciamento de Usuários

## 1. API REST

**API de Gerenciamento de Usuários**

Uma API REST desenvolvida em Python utilizando Flask para realizar operações básicas de cadastro, consulta e alteração de usuários.

---

### 2. Objetivo da API

O objetivo desta API é disponibilizar uma estrutura simples para o **gerenciamento de usuários**, permitindo realizar operações de criação, consulta e atualização de dados.

A API utiliza requisições HTTP e trabalha com dados no formato **JSON**.

Entre as principais funcionalidades estão:

* Listar todos os usuários;
* Buscar um usuário através do seu ID;
* Cadastrar um novo usuário;
* Alterar informações de um usuário;
* Validar dados obrigatórios durante o cadastro;
* Retornar códigos HTTP apropriados para cada situação.

A API também possui tratamento de erros para situações como:

* Usuário não encontrado (`404 Not Found`);
* Cadastro sem o campo obrigatório `email` (`400 Bad Request`).

---

## 3. Tecnologias utilizadas

| Tecnologia    | Utilização                                               |
| ------------- | -------------------------------------------------------- |
| **Python**    | Linguagem de programação                                 |
| **Flask**     | Framework utilizado para desenvolvimento da API          |
| **JSON**      | Formato de comunicação e armazenamento dos dados         |
| **HTTP/REST** | Padrão utilizado na comunicação entre cliente e servidor |
| **VS Code**   | Editor de código recomendado                             |
| **Postman**   | Ferramenta recomendada para testar os endpoints          |

---

## 4. Estrutura do projeto

A estrutura básica do projeto é:

```text
projeto/
│
├── app.py
├── bd.py
└── venv/
```

### `app.py`

Contém a aplicação Flask e os endpoints responsáveis pelas operações da API.

### `bd.py`

Contém a estrutura de memória utilizada para armazenar os usuários.

Exemplo:

```python
usuarios = [
    {
        "id": 1,
        "nome": "João",
        "email": "joao@email.com"
    },
    {
        "id": 2,
        "nome": "Maria",
        "email": "maria@email.com"
    }
]
```

### `venv/`

Ambiente virtual utilizado para isolar as dependências do projeto.

---

# 5. Execução local

## 5.1 Pré-requisitos

Antes de executar o projeto, é necessário possuir:

* Python instalado;
* Editor de código;
* Terminal;
* Opcionalmente, Postman para realização dos testes.

---

## 5.2 Criar o ambiente virtual

No terminal, dentro da pasta do projeto, execute:

```bash
python -m venv venv
```

---

## 5.3 Ativar o ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

Caso esteja utilizando PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Após a ativação, o terminal deverá apresentar algo semelhante a:

```text
(venv)
```

---

## 5.4 Instalar o Flask

Com o ambiente virtual ativado:

```bash
pip install flask
```

---

## 5.5 Executar a aplicação

Execute:

```bash
python app.py
```

Se a aplicação estiver configurada para utilizar a porta padrão do Flask, o servidor estará disponível em:

```text
http://127.0.0.1:5000
```

ou:

```text
http://localhost:5000
```

---

# 6. Endpoints da API

A API disponibiliza os seguintes endpoints:

| Método | Endpoint         | Objetivo               | Status principal |
| ------ | ---------------- | ---------------------- | ---------------- |
| `GET`  | `/usuarios`      | Listar usuários        | `200`            |
| `POST` | `/usuarios`      | Criar usuário          | `201`            |
| `GET`  | `/usuarios/<id>` | Buscar usuário por ID  | `200` / `404`    |
| `PUT`  | `/usuarios/<id>` | Alterar usuário por ID | `200` / `404`    |

---

# 7. Exemplos de utilização

## 7.1 Listar usuários

### Requisição

```http
GET /usuarios
```

### Exemplo completo

```text
GET http://127.0.0.1:5000/usuarios
```

### Resposta

**Status:** `200 OK`

```json
[
    {
        "id": 1,
        "nome": "João",
        "email": "joao@email.com"
    },
    {
        "id": 2,
        "nome": "Maria",
        "email": "maria@email.com"
    }
]
```

---

# 8. Criar usuário

## Endpoint

```http
POST /usuarios
```

## Corpo da requisição

A API espera um objeto JSON contendo, no mínimo, o campo `email`.

### Exemplo válido

```json
{
    "id": 3,
    "nome": "Carlos",
    "email": "carlos@email.com"
}
```

### Resposta

**Status:** `201 Created`

```json
{
    "id": 3,
    "nome": "Carlos",
    "email": "carlos@email.com"
}
```

---

# 9. Validação do cadastro

O campo `email` é obrigatório durante o cadastro.

Caso seja enviada uma requisição sem esse campo:

### Requisição

```http
POST /usuarios
```

```json
{
    "id": 4,
    "nome": "Pedro"
}
```

### Resposta

**Status:** `400 Bad Request`

```json
{
    "erro": "O campo email é obrigatório"
}
```

Essa validação impede que usuários sejam cadastrados sem uma informação essencial.

---

# 10. Buscar usuário por ID

## Endpoint

```http
GET /usuarios/<id>
```

### Exemplo

```http
GET /usuarios/1
```

### Resposta

**Status:** `200 OK`

```json
{
    "id": 1,
    "nome": "João",
    "email": "joao@email.com"
}
```

---

# 11. Usuário não encontrado

Caso seja realizada uma busca utilizando um ID que não existe na estrutura de usuários:

### Requisição

```http
GET /usuarios/999
```

### Resposta

**Status:** `404 Not Found`

```json
{
    "erro": "Usuário não encontrado"
}
```

Esse comportamento informa ao cliente que a requisição foi processada corretamente, porém o recurso solicitado não existe.

---

# 12. Alterar usuário

## Endpoint

```http
PUT /usuarios/<id>
```

### Exemplo

```http
PUT /usuarios/1
```

### Corpo da requisição

```json
{
    "nome": "João Silva",
    "email": "joaosilva@email.com"
}
```

### Resposta

**Status:** `200 OK`

```json
{
    "id": 1,
    "nome": "João Silva",
    "email": "joaosilva@email.com"
}
```

---

# 13. Alteração de usuário inexistente

Caso seja realizada uma tentativa de alteração utilizando um ID que não existe:

### Requisição

```http
PUT /usuarios/999
```

### Resposta

**Status:** `404 Not Found`

```json
{
    "erro": "Usuário não encontrado"
}
```

---

# 14. Códigos de status HTTP utilizados

| Código            | Significado                       | Situação                        |
| ----------------- | --------------------------------- | ------------------------------- |
| `200 OK`          | Requisição realizada com sucesso  | Consulta ou alteração realizada |
| `201 Created`     | Recurso criado com sucesso        | Cadastro de usuário             |
| `400 Bad Request` | Dados da requisição são inválidos | Cadastro sem `email`            |
| `404 Not Found`   | Recurso não encontrado            | ID inexistente                  |

---

# 15. Resumo dos testes

Para validar o funcionamento da API, podem ser realizados os seguintes testes:

### Teste 1 — Listagem

```http
GET /usuarios
```

**Esperado:** `200 OK`

---

### Teste 2 — Cadastro válido

```http
POST /usuarios
```

Com:

```json
{
    "id": 3,
    "nome": "Carlos",
    "email": "carlos@email.com"
}
```

**Esperado:** `201 Created`

---

### Teste 3 — Cadastro sem e-mail

```http
POST /usuarios
```

Com:

```json
{
    "id": 4,
    "nome": "Pedro"
}
```

**Esperado:** `400 Bad Request`

---

### Teste 4 — Busca por ID existente

```http
GET /usuarios/1
```

**Esperado:** `200 OK`

---

### Teste 5 — Busca por ID inexistente

```http
GET /usuarios/999
```

**Esperado:** `404 Not Found`

---

### Teste 6 — Alteração

```http
PUT /usuarios/1
```

**Esperado:** `200 OK`

---

### Teste 7 — Alteração de ID inexistente

```http
PUT /usuarios/999
```

**Esperado:** `404 Not Found`

---

## 16. Conclusão

A API implementa uma estrutura básica de gerenciamento de usuários utilizando os princípios de uma API REST. A comunicação ocorre através do protocolo HTTP, utilizando JSON para transferência dos dados.

Além das operações básicas de consulta, criação e alteração, a aplicação possui validações e tratamento de erros, garantindo respostas adequadas para situações de dados inválidos ou recursos inexistentes.
