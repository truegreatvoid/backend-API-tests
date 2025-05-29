***Settings***
Resource  ../helpers/common-actions.robot
Resource  ../locators/options-page-locators.robot
Resource  ./global-page.robot

***Keywords***

Verify Number Of Options
    [Arguments]    ${number}
    Verify Element    ${containerOptions}
    ${count}=    Get Element Count    ${cardOption}
    Should Be Equal As Numbers    ${count}    ${number}

Go To Options Page
    Click Button Options
    Sleep  0.5s
    Verify Current URL  http://localhost:3000/options

Click Option Office
    Verify Element    ${optionOffice}
    Click Element    ${optionOffice}

Click Option Room
    Verify Element    ${optionRoom}
    Click Element    ${optionRoom}

Click Option Resource
    Verify Element    ${optionResource}
    Click Element    ${optionResource}

Click Option Reservation
    Verify Element    ${optionReservation}
    Click Element    ${optionReservation}