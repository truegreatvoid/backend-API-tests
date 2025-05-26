*** Settings ***
Library    Browser


***Keywords***
Verify Element
    [Arguments]     ${element}
    [Documentation]     Wait Element until it is stable at the DOM
    Wait For Elements State     ${element}     stable

Verify Element With Timeout
    [Arguments]     ${element}    ${timeout}
    [Documentation]     Wait Element until it is stable at the DOM before passing timeout duration
    Wait For Elements State     ${element}     stable    ${timeout}

Verify Element Not Available
    [Arguments]     ${element}
    [Documentation]     Wait Element until it is not available at the DOM
    Wait For Elements State     ${element}     hidden

Verify Element Text
    [Arguments]     ${element}  ${text}
    [Documentation]     Validate Element have specific Text
    Verify Element      ${element}\[.="${text}"]

Verify Element Text With Timeout
    [Arguments]     ${element}    ${text}    ${timeout}
    [Documentation]     Validate Element have specific Text before passing timeout duration
    Verify Element With Timeout    ${element}\[.="${text}"]    ${timeout}

Verify Element Value
    [Arguments]     ${element}      ${value}
    [Documentation]     Validate Element have specific attribute value
    Verify Element      ${element}\[@value="${value}"]

Verify Placeholder Text
    [Arguments]     ${element}      ${text}
    [Documentation]     Validate Text shown on placeholder
    ${value}=        Get Attribute    ${element}    placeholder
    Should Be Equal As Strings      ${text}     ${value}

Click Element
    [Arguments]     ${element}
    [Documentation]     Do Click action only when element is ready to click.
    ...     Reference : https://playwright.dev/docs/actionability
    Click   ${element}

Click Element with Text
    [Arguments]     ${element}      ${text}
    [Documentation]     Do Click action to an element have specific text.
    Click   ${element}\[.="${text}"]

Input Text to Element
    [Arguments]     ${element}      ${value}
    [Documentation]     Clear and Input a text to Input Field
    ...     only when element is ready at DOM.
    Verify Element  ${element}
    Type Text   ${element}      ${value}

Input Text with Delay
    [Arguments]     ${element}      ${value}    ${delay}=1ms
    [Documentation]     Clear and Input a text to Input Field
    ...     only when element is ready at DOM.
    Verify Element  ${element}
    Type Text   ${element}      ${value}    ${delay}

Input Password to Element
    [Documentation]     Clear and Input a text to Input Field without log the credential value
    ...     only when element is ready at DOM.
    [Arguments]     ${element}      ${value}
    Verify Element  ${element}
    Type Secret   ${element}      $value

Verify Checkbox State by Value
    [Documentation]     Verify state of checkbox where element have specific attribute value
    [Arguments]     ${element}      ${value}    ${state}
    Get Checkbox State      ${element}\[@value="${value}"]      ==      ${state}

Get Text Element by Index
    [Documentation]     Return the text of an element from specific index
    [Arguments]     ${element}  ${index}
    ${text}=        Get Text       ${element}\[${index}]

    RETURN    ${text}

Verify Search Query Paramater Value
    [Documentation]     Validate value of an url paramater
    [Arguments]     ${param}    ${text}
    ${value}=       Get Value of URL Paramater      ${param}
    Should Be Equal As Strings      ${text}     ${value}

Verify Current URL
    [Documentation]
    [Arguments]    ${text}
    ${currentUrl}=  Get Url
    Should Be Equal As Strings      ${text}     ${currentUrl}