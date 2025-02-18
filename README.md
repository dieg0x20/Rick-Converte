# Rick-Converte 
## PDF to PNG

Este repositório contém uma aplicação web simples desenvolvida em Python utilizando o framework Flask, com a funcionalidade de converter arquivos PDF para imagens PNG. A aplicação também foi configurada para rodar dentro de um container Docker, facilitando o processo de deploy e garantindo um ambiente de execução consistente.

## Funcionalidades

- **Conversão de PDF para PNG**: A aplicação recebe um arquivo PDF, converte suas páginas em imagens PNG e as retorna ao usuário.
- **Interface Web**: Interface simples para o upload de arquivos PDF e download das imagens convertidas.
- **Docker**: A aplicação pode ser facilmente executada dentro de um container Docker, garantindo portabilidade e facilidade de deploy.

## Tecnologias

- **Python** 3.9
- **Flask**: Framework para construção da API web.
- **Pillow**: Biblioteca para manipulação de imagens.
- **pdf2image**: Biblioteca para conversão de PDF para imagem.
- **Docker**: Para containerização da aplicação.

## Como Rodar a Aplicação

### Pré-requisitos

1. **Python** (se não for usar Docker)
2. **Docker** (caso queira rodar em container)

### Rodando a Aplicação Sem Docker

1. Clone este repositório:

   ```bash
   git clone https://github.com/dieg0x20/Rick-Converte.git
   cd Rick-Converte
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Rode a aplicação:

   ```bash
   flask run
   ```

   A aplicação estará disponível em `http://127.0.0.1:5000`.

### Rodando a Aplicação Com Docker

1. Clone o repositório:

   ```bash
   git clone https://github.com/dieg0x20/Rick-Converte.git
   cd Rick-Converte

2. Construa a imagem Docker:

   ```bash
   docker compose up -d --build .
   ```
   A aplicação estará disponível em `http://127.0.0.1:5000`.

### Dependências

```plaintext
Flask==2.0.1
pdf2image==1.16.0
Pillow==8.3.2
```

## Contribuindo

1. Fork este repositório.
2. Crie uma nova branch para sua feature (`git checkout -b feature/xyz`).
3. Faça suas alterações e commit (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/xyz`).
5. Abra um Pull Request.
