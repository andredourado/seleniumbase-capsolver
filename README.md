# SeleniumBase e CapSolver

## Criando sua conta no CapSolver

1. Crie uma conta no site do CapSolver para conseguir a chave da API. Clique aqui: [https://dashboard.capsolver.com/passport/register](https://dashboard.capsolver.com/passport/register?inviteCode=A-MrvSbq8WsM)

## Baixando a extensão do CapSolver

1. Baixe a última versão da extensão do CapSolver em ["https://github.com/capsolver/capsolver-browser-extension/releases"](https://github.com/capsolver/capsolver-browser-extension/releases/download/v1.15.6/CapSolver.Browser.Extension-v1.15.6.zip)

2. Extraia o conteúdo do arquivo ".zip" na raiz do seu projeto. Renomeie o diretório para "capsolver_extension" para simplificar o acesso.

## Configurando a extensão do CapSolver

1. Edite o arquivo "capsolver_extension/assets/config.js" e insira a chave da API em "apiKey":

## Executando a rotina

1. Execute o script "seleniumbase_capsolver.py" com o seguinte comando:

    ```bash
      python3 seleniumbase_capsolver.py
    ```