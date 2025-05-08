# SeleniumBase e CapSolver

O SeleniumBase é uma poderosa biblioteca Python que estende o Selenium tradicional, oferecendo uma sintaxe mais simples e funcionalidades avançadas como suporte integrado ao undetected-chromedriver (uc), asserts automáticos, geração de relatórios visuais e execução de testes com comandos amigáveis. Sua versatilidade o torna ideal não apenas para testes, mas também para automação de tarefas e scraping avançado.

Entretanto, ao automatizar sites que utilizam reCAPTCHA ou outros mecanismos anti-bot, é comum esbarrar em barreiras que impedem o carregamento ou envio de formulários automaticamente. É aí que entra o CapSolver, uma solução especializada em resolver CAPTCHAs em tempo real via API ou extensão de navegador.

Ao integrar o CapSolver com SeleniumBase, é possível resolver CAPTCHAs automaticamente sem necessidade de interação manual. A abordagem mais prática é utilizar a extensão oficial da CapSolver, que pode ser carregada diretamente no navegador do SeleniumBase.

Essa extensão atua diretamente no navegador, detectando e resolvendo reCAPTCHAs visualmente como um usuário humano faria. Após a resolução, basta aguardar a resposta ser preenchida no campo invisível #g-recaptcha-response e enviar o formulário.

Essa combinação permite automatizar fluxos completos de scraping mesmo em páginas protegidas com CAPTCHA, mantendo o navegador em modo visual ou headless. É uma solução robusta, confiável e altamente recomendada para desenvolvedores que precisam contornar bloqueios em páginas protegidas.

Aqui uma implementação simples que você pode ajustar para seu usos específicos.

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