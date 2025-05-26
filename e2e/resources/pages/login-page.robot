***Settings***
Resource  ../locators/login-page-locators.robot
Resource  ../helpers/common-actions.robot

***Keywords***

Verify Login Page
    Verify Element  ${textHeaderLogin}
    Verify Element  ${inputUsername}
    Verify Element  ${inputPassword}
    Verify Element  ${buttonLogin}
    Verify Element Text      ${textHeaderLogin}  Swag Labs
    Verify Placeholder Text  ${inputUsername}    Username
    Verify Placeholder Text  ${inputPassword}    Password
    Verify Element Value     ${buttonLogin}      Login

Verify Login Page Failed
    Verify Element  ${textHeaderLogin}
    Verify Element  ${inputUsername}
    Verify Element  ${inputPassword}
    Verify Element  ${buttonLogin}
    Verify Element Text      ${textHeaderLogin}  Swag Labs
    Verify Placeholder Text  ${inputUsername}    Username
    Verify Placeholder Text  ${inputPassword}    Password
    Verify Element Value     ${buttonLogin}      Logins

Click Login button
    Click Element  ${buttonLogin}

Verify error on field Username
    Verify Element  ${iconErrorUsername}

Verify error on field Password
    Verify Element  ${iconErrorPassword}

Verify error "Username is required"
    Verify Element  ${textHeaderError}
    Verify Element  ${buttonError}
    Verify Element  ${iconButtonError}
    Verify Element Text  ${textHeaderError}  Epic sadface: Username is required

Input Username
    [Arguments]  ${text}
    Input Text to Element  ${inputUsername}    ${text}

Input Password
    [Arguments]  ${text}
    Input Text to Element  ${inputPassword}    ${text}

Verify error "Username and Password do not match"
    Verify Element  ${textHeaderError}
    Verify Element  ${buttonError}
    Verify Element  ${iconButtonError}
    Verify Element Text  ${textHeaderError}  Epic sadface: Username and password do not match any user in this service

Verify Login Page is not shown anymore
    Verify Element Not Available  ${textHeaderLogin}
    Verify Element Not Available  ${inputUsername}
    Verify Element Not Available  ${inputPassword}
    Verify Element Not Available  ${buttonLogin}