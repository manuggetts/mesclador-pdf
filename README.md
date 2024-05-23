# Mesclador de PDFs

Este script Python mescla arquivos PDF em um único arquivo.pdf. Ele percorre, em ordem alfabética, todos os arquivos PDF em uma pasta especificada, mescla-os e salva o resultado em um novo arquivo PDF.

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Como Usar](#como-usar)
  - [Usando o executável](#usando-o-executável)
    - [Download e Estrutura de Diretórios](#download-e-estrutura-de-diretórios)
    - [Executar o Executável](#executar-o-executável)
  - [Clonando o Repositório](#clonando-o-repositório)
    - [Estrutura de Diretórios](#estrutura-de-diretórios)
    - [Customização dos Caminhos](#customização-dos-caminhos)
    - [Executar o Script](#executar-o-script)
    - [Verificar o Arquivo Mesclado](#verificar-o-arquivo-mesclado)
- [Código Fonte](#código-fonte)
- [Contribuição](#contribuição)

---

## 🚀 Como Usar

### Usando o executável 👾

#### Download e Estrutura de Diretórios

Para os que preferem uma solução sem necessidade de configurar um ambiente Python, deixei este executável disponível para download. Você pode baixar o executável e a estrutura de diretórios necessária no seguinte link:

- [Download do Executável](https://github.com/manuggetts/mesclador-pdf/blob/main/dist/main.exe)

#### Estrutura de Diretórios

Certifique-se de que seus arquivos PDF a serem mesclados estão na pasta `arquivos`. O script percorrerá os arquivos PDF na ordem alfabética dos nomes dos arquivos. Se você deseja mesclar os arquivos em uma ordem específica, você pode renomear os arquivos para que a ordem alfabética corresponda à ordem desejada. Por exemplo:

```
mesclador-pdf/
├── main.py
├── arquivos/
│ ├── 01_arquivo.pdf
│ ├── 02_arquivo.pdf
│ ├── 03_arquivo.pdf
│ └── (outros PDFs)
```

Neste exemplo, os arquivos serão mesclados na ordem `01_arquivo.pdf`, `02_arquivo.pdf`, `03_arquivo.pdf`, etc.

#### Executar o Executável

Para executar o programa, basta dar um duplo clique no arquivo `mesclador-pdf.exe` e pronto, o arquivo merged.pdf será criado na pasta `arquivos` contendo todos os PDFs mesclados. Bom proveito!

---

### Clonando o Repositório 🤖

#### Pré-requisitos

Certifique-se de ter o Python instalado. Este script foi testado com Python 3.8.

Você também precisará instalar a biblioteca `PyPDF2`. Para instalá-la, execute o seguinte comando no seu terminal:

```
pip install PyPDF2
```

Agora, clone o repositório para a sua máquina:

```
git clone https://github.com/manuggetts/mesclador-pdf.git
```
Vá até o diretório:
```
cd mesclador-pdf
```

#### Estrutura de Diretórios

Certifique-se de que seus arquivos PDF a serem mesclados estão na pasta `arquivos`. O script percorrerá os arquivos PDF na ordem alfabética dos nomes dos arquivos. Se você deseja mesclar os arquivos em uma ordem específica, você pode renomear os arquivos para que a ordem alfabética corresponda à ordem desejada. Por exemplo:

```
mesclador-pdf/
├── main.py
├── arquivos/
│ ├── 01_arquivo.pdf
│ ├── 02_arquivo.pdf
│ ├── 03_arquivo.pdf
│ └── (outros PDFs)
```

Neste exemplo, os arquivos serão mesclados na ordem `01_arquivo.pdf`, `02_arquivo.pdf`, `03_arquivo.pdf`, etc.

#### Customização dos Caminhos

No script main.py, as variáveis input_folder e output_file são configuradas para usar caminhos relativos, sendo 'arquivos' a pasta que estará seus arquivos e 'merged.pdf' o nome do arquivo mesclado.
Certifique-se de que os caminhos fornecidos sejam relativos ao diretório onde você está executando o script ou sejam caminhos absolutos corretos.
Você pode ajustar conforme necessário:

1. Entrada: `input_folder = os.path.join('arquivos')`
2. Saída: `output_file = os.path.join('arquivos', 'merged.pdf')`

#### Executar o Script

Abra o terminal, navegue até o diretório onde está o script main.py e execute:
```
python main.py
```

#### Verificar o Arquivo Mesclado

Após a execução do script, o arquivo 'merged.pdf' deve ser criado na pasta arquivos. Verifique se o arquivo 'merged.pdf' contém todos os PDFs mesclados conforme esperado.

---

## 🛠️ Código Fonte

- [main.py](https://github.com/manuggetts/mesclador-pdf/blob/main/main.py)

## Contribuição 🤝
Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, por favor, abra uma [issue](https://github.com/manuggetts/mesclador-pdf/issues) ou envie um [pull request](https://github.com/manuggetts/mesclador-pdf/pulls).
