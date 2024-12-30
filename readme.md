
# Transcrição de Áudio com API Groq

Este é um projeto em Python utilizando o Streamlit para criar uma interface web interativa que permite enviar arquivos de áudio e transcrevê-los usando a API Groq. O projeto suporta arquivos de áudio nos formatos `.mp3` e `.wav` e fornece uma opção para baixar a transcrição gerada.

## Funcionalidades

- Upload de arquivos de áudio nos formatos `.mp3`, `.wav`, entre outros.
- Transcrição automática do áudio usando a API Groq.
- Exibição da transcrição gerada na interface web.
- Opção para baixar a transcrição gerada em formato `.txt`.

## Pré-requisitos

- Python 3.7 ou superior.
- Conta na API Groq com uma chave de API válida.

## Instalação

### Passo 1: Clonar o repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### Passo 2: Criar um ambiente virtual (opcional)

Recomenda-se criar um ambiente virtual para instalar as dependências isoladamente:

```bash
python -m venv venv
source venv/bin/activate  # No Linux/macOS
venv\Scripts\activate     # No Windows
```

### Passo 3: Instalar as dependências

Instale as dependências do projeto utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Como Executar

Para rodar o aplicativo Streamlit, use o seguinte comando:

```bash
streamlit run app.py
```
No Windows:
```bash
python -m streamlit run .\app.py
```

Após executar o comando, acesse a interface no navegador através do link exibido no terminal (normalmente `http://localhost:8501`).

## Como Usar

1. **Envio de Áudio**: Faça o upload de um arquivo de áudio no formato `.mp3` ou `.wav` através da interface.
2. **Transcrição**: Após o envio do arquivo, clique no botão "Transcrever áudio" para que o áudio seja transcrito.
3. **Baixar a Transcrição**: Após a transcrição ser exibida, você pode clicar no botão "Baixar Transcrição" para baixar a transcrição em formato `.txt`.

## Contribuições

Contribuições são bem-vindas! Se você tem sugestões ou melhorias para o projeto, sinta-se à vontade para abrir um **pull request**.

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
