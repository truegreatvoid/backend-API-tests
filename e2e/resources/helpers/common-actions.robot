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

Click Element
    [Arguments]     ${element}
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

Verify Current URL
    [Documentation]
    [Arguments]    ${text}
    ${currentUrl}=  Get Url
    Should Be Equal As Strings      ${text}     ${currentUrl}