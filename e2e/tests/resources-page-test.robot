***Settings***
Resource  ../config/browser-config.robot
Resource  ../resources/pages/resource-page.robot

Suite Setup     Open WorkSpacePro
Suite Teardown  Finish Test Suite

***Test Cases***

Como um usuário, eu devo conseguir criar um novo recurso
    [Documentation]    Acesso a página de recursos
    ...    Abro o formulário de criação de recurso
    ...    Preencho todos os campos e clico no botão salvar
    ${timestamp}=     Get Time    epoch
    ${nameResource}=  Set Variable    Nome ${timestamp}
    ${descriptionResource}=  Set Variable    Descrição ${timestamp}
    Go To Resources Page
    Open Resource Form
    Input Resource Name    ${nameResource}
    Input Resource Description    ${descriptionResource}
    Click Save Resource
    Check Item In Table    ${nameResource}    ${descriptionResource}


Como um usuário, eu devo conseguir pesquisar um recurso pelo nome usando a barra de pesquisa
    [Documentation]    Acesso a página de recursos
    ...    escrevo o nome do recurso na barra de pesquisa
    ...    deve visualizar o recurso existente 
    ${timestamp}=     Get Time    epoch
    ${nameResource}=  Set Variable    Nome ${timestamp}
    ${descriptionResource}=  Set Variable    Descrição ${timestamp}
    Open Resource Form
    Input Resource Name    ${nameResource}
    Input Resource Description    ${descriptionResource}
    Click Save Resource
    Sleep    0.5s
    Input Resource Search    ${nameResource}
    Check Item In Table    ${nameResource}    ${descriptionResource}
