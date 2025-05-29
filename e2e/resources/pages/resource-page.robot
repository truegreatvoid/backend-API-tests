***Settings***
Library    ../../../venv/lib/python3.12/site-packages/robot/libraries/XML.py
Resource  ../helpers/common-actions.robot
Resource  ../locators/resources-page-locators.robot
Resource  ./global-page.robot
Resource  ./options-page.robot

***Keywords***

Go To Resources Page
    Click Button Options
    Sleep  0.5s
    Click Option Resource
    Sleep  0.5s
    Verify Current URL  http://localhost:3000/resources

Open Resource Form
    Verify Element    ${buttonCreateResource}
    Click Element    ${buttonCreateResource}
    Verify Element    ${formResource}

Input Resource Name
    [Arguments]  ${text}
    Input Text to Element  ${inputNameResource}    ${text}

Input Resource Description 
    [Arguments]  ${text}
    Input Text to Element  ${inputDescriptionResource}    ${text}

Input Resource Search
    [Arguments]  ${text}
    Input Text to Element  ${inputResourceSearch}    ${text}

Click Save Resource
    Verify Element    ${buttonSaveResource}
    Click Element    ${buttonSaveResource}

Check Item In Table
    [Arguments]    ${name}    ${description}
    Wait For Elements State     ${tableResources}     stable
    ${nameLocator}=    Set Variable    //div[contains(@class, "capitalize") and text()="${name}"]
    Verify Element Text     ${nameLocator}    ${name}
    ${descriptionLocator}=    Set Variable    //div[text()="${description}"]
    Verify Element Text    ${descriptionLocator}    ${description}