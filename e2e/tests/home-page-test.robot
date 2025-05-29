***Settings***
Resource  ../config/browser-config.robot
Resource  ../resources/pages/global-page.robot
Resource  ../resources/pages/home-page.robot

Suite Setup     Open WorkSpacePro
Suite Teardown  Finish Test Suite

***Test Cases***

Como um usuário, ao acessar a página principal, eu quero ver o nome e a descrição da plataforma
    [Documentation]  Acessando a página principal da aplicação
    ...  e veja o nome e a descrição da plataforma
    Verify Current URL  http://localhost:3000/
    Verify Title Home Page 
    Verify Description Home Page 

Como um usuário, ao clicar no botão de opções, eu quero ver a página de opções e quando clicar no botão "Voltar" quero ser redirecionado para a página inicial
    [Documentation]  Acessando a página principal da aplicação
    ...  clicando no botão "Testar Agora"
    ...  deve ser redirecionado para a rota "/options"
    ...  e quando clicar no botão "Voltar" deve ser redirecionado para a página inicial
    Click Button Options
    Sleep  0.5s
    Verify Current URL  http://localhost:3000/options
    Click Button Back
    Sleep  0.5s
    Verify Current URL  http://localhost:3000/