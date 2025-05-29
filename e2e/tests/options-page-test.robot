***Settings***
Resource  ../config/browser-config.robot
Resource  ../resources/pages/global-page.robot
Resource  ../resources/pages/options-page.robot

Suite Setup     Open WorkSpacePro
Suite Teardown  Finish Test Suite

***Test Cases***

Como um usuário, ao acessar a página de opções, eu quero ver as 4 opções disponíveis na plataforma
    Go To Options Page
    Verify Number Of Options  4

Como um usuário, ao clicar no botão "Escritórios", eu quero ver a página de CRUD dos escritórios
    Click Option Office
    Sleep  1s
    Verify Current URL  http://localhost:3000/offices
    Click Button Back
    Verify Current URL  http://localhost:3000/options    

Como um usuário, ao clicar no botão "Salas", eu quero ver a página de CRUD das salas
    Click Option Room
    Sleep  1s
    Verify Current URL  http://localhost:3000/rooms
    Click Button Back
    Verify Current URL  http://localhost:3000/options

Como um usuário, ao clicar no botão "Recursos", eu quero ver a página de CRUD dos recursos
    Click Option Resource
    Sleep  1s
    Verify Current URL  http://localhost:3000/resources
    Click Button Back
    Verify Current URL  http://localhost:3000/options 

Como um usuário, ao clicar no botão "Reservas", eu quero ver a página de CRUD das reservas
    Click Option Reservation
    Sleep  1s
    Verify Current URL  http://localhost:3000/reservations
    Click Button Back
    Verify Current URL  http://localhost:3000/options   