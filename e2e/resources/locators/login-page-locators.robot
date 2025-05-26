*** Variables ***

# Main Input
${sectionForm}      xpath=//div[@class="login_wrapper"]
${textHeaderLogin}  xpath=//div[@class="login_logo"]
${inputUsername}    xpath=//input[@data-test="username"]
${inputPassword}    xpath=//input[@data-test="password"]
${buttonLogin}      xpath=//input[@data-test="login-button"]

# Errors
${iconErrorUsername}   xpath=//input[@data-test="username"]/following-sibling::*[name()="svg"][contains(@class, 'error_icon')]
${iconErrorPassword}   xpath=//input[@data-test="password"]/following-sibling::*[name()="svg"][contains(@class, 'error_icon')]
${textHeaderError}     xpath=//h3[@data-test="error"]
${buttonError}         xpath=//button[@data-test="error-button"]
${iconButtonError}     xpath=//button[@data-test="error-button"]/*[name()="svg"]