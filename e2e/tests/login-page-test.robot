***Settings***
Resource  ../config/browser-config.robot
Resource  ../resources/pages/login-page.robot
Resource  ../resources/global-variables.robot

Suite Setup     Open SauceDemo
Suite Teardown  Finish Test Suite

***Test Cases***

As a User, I will see Error when leave Username and Password field as empty and then click Login button
    [Documentation]  Click Login Button without filling Username and Password 
    ...              User should see error on Username, Password, and Login Button
    Click Login button
    Verify error on field Username
    Verify error on field Password
    Verify error "Username is required"

As a User, I will see Error when input incorrect Username and Password then click Login button
    [Documentation]  Click Login Button after filling Username and Password with incorrect value
    ...              User should see error on Username, Password, and Login Button
    Input Username    MyName
    Input Password    Unknown
    Click Login button
    Verify error on field Username
    Verify error on field Password
    Verify error "Username and Password do not match"

As a User, I will not see Login Page anymore when input correct Username and Password then click Login button
    [Documentation]  Click Login Button after filling Username and Password with correct value
    ...              User should not see Login Page anymore and redirected to Page 'https://www.saucedemo.com/inventory.html
    Input Username    ${validUsername}
    Input Password    ${validPassword}
    Click Login button
    Verify Login Page is not shown anymore
    Verify Current URL  https://www.saucedemo.com/inventory.html