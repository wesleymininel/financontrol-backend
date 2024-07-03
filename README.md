
# Controle Financeiro Mensal - BackEnd

Este projeto é o Backend do Controle Financeiro Mensal e faz parte do MVP do curso de Pós-Graduação em Engenharia de Software na disciplina de Desenvolvimento Full Stack Básico.

## Descrição do Projeto

O backend deste projeto fornece uma API RESTful para gerenciar dados financeiros, incluindo faturas. Ele interage com um frontend para permitir a adição, visualização e remoção de faturas, oferecendo um controle eficiente sobre gastos mensais.

## Tecnologias Utilizadas

- **Python**
- **Flask**
- **SQLAlchemy**
- **SQLite**


## Requisitos

Para executar este projeto, você precisará do frontend correspondente, disponível no seguinte repositório:

- [financontrol-frontend](https://github.com/wesleymininel/financontrol-frontend.git)

Certifique-se de ter o Python e o Flask instalados em seu ambiente de desenvolvimento.

## Como Executar o Projeto

### 1. Configuração do Backend

1. Clone o repositório do backend:
   ```sh
   git clone https://github.com/wesleymininel/financontrol-backend.git
   ```

2. Navegue até o diretório do backend:
   ```sh
   cd financontrol-backend
   ```

3. Criando o Ambiente ENV via Terminal PowerShell no ambiente Windows:
   ```sh
   python.exe -m venv env
   ```

4. Iniciando o Ambiente ENV via Terminal PowerShell no ambiente Windows:
   ```sh
   .\env\Scripts\Activate.ps1
   ```

5. Instale as dependências necessárias:
   ```sh
   pip install -r requirements.txt
   ```

5. Inicie o servidor Flask:
   ```sh
   flask run --host 0.0.0.0 --port 5000
   ```

   O backend estará disponível em `http://127.0.0.1:5000`.

### 2. Configuração do Frontend

1. Clone este repositório do frontend:
   ```sh
   git clone https://github.com/wesleymininel/financontrol-frontend.git
   ```

2. Navegue até o diretório do frontend:
   ```sh
   cd financontrol-frontend
   ```

3. Abra o arquivo `index.html` no seu navegador preferido.

## Estrutura do Projeto

A estrutura do projeto backend é a seguinte:

```
financontrol-backend/
├── model/
│   └── __init__.py
│   └── base.py
│   └── fatura.py
├── schemas/
│   └── __init__.py
│   └── error.py
│   └── fatura.jpg
├── app.py
├── logger.py
├── README.md
└── requirements.txt

## Funcionalidades

- **Adicionar Fatura**: Insira os detalhes da fatura, incluindo beneficiário, pagador, valor e data de vencimento.
- **Listar Faturas**: Visualize todas as faturas adicionadas em uma tabela.
- **Pesquisar Faturas**: Pesquisar fatura usando o beneficiario como referencia.
- **Remover Fatura**: Remova faturas pagas da lista.

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Você pode abrir issues ou enviar pull requests para melhorias e correções de bugs.

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
