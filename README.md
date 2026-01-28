# Python API 

Esse repositório contém um projeto em Python com exemplo de API simples e integração com processamento de dados (como envio de JSON para S3).
É um projeto para estudos, portfólio e serve como base para APIs maiores.

## 📁 Estrutura do projeto

A estrutura principal é:

├── .gitignore
├── main.py
└── json_to_s3/
├── main.ipynb
└── venv/

- `main.py`: ponto de entrada da API  
- `json_to_s3/main.ipynb`: notebook com lógica de manipulação de JSON e upload para S3  
- `.gitignore`: ignora arquivos que **não devem** ir para o Git (como credenciais e chaves)  


## O que esse projeto faz

-  **API em Python** — com endpoints simples para iniciar seu backend REST em Python  
-  **Processamento de JSON** — exemplo de leitura de arquivo `amazon_data.json`  
-  **Upload para Amazon S3** — lógica de envio de dados para AWS S3 (em notebook) *(se configurado)*  

## 🚀 Como usar

### 1. Clone o projeto

```bash
git clone https://github.com/mel-ferreira/python_api.git
cd python_api

### 2. Criar e ativar o ambiente virtual
python -m venv venv

### 3. Instalar dependências
pip install fastapi uvicorn boto3 jupyter


