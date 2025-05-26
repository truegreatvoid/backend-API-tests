*** Variables ***
${BROWSER}              chromium
${HEADLESS}             True  # False caso queira ver o navegador
${KEYWORD_TIMEOUT}      5s
${BROWSER_TIMEOUT}      5s
${SauceDemo_URL}        https://www.saucedemo.com/
${SCREENSHOT_DIR}    ${EXECDIR}/results/screenshots
${LOGS_DIR}          ${EXECDIR}/results/logs
${TIMESTAMP}         ${EMPTY}

*** Settings ***
Library     Browser      auto_closing_level=TEST    run_on_failure=Log And Capture Error    timeout=${BROWSER_TIMEOUT}
Library          OperatingSystem
Library          DateTime


*** Keywords ***
Log And Capture Error
    ${current_date}=    Get Current Date    result_format=%Y%m%d_%H%M%S
    Take Screenshot    filename=${EXECDIR}/error_${current_date}
    ${source}=    Get Page Source
    Create File    ${EXECDIR}/page_source_${current_date}.html    ${source}
    Log    ${source}

Open New Browser
    [Arguments]     ${url}
    New Browser     ${BROWSER}      headless=${HEADLESS}
    ${context}=    Get Device    Desktop Chrome
    New Context   &{context}
    New Page  ${url}
    Set Browser Timeout     ${KEYWORD_TIMEOUT}

Open SauceDemo
    Open New Browser    ${SauceDemo_URL}

Finish Test Suite
    ${current_date}=    Get Current Date    result_format=%Y%m%d_%H%M%S
    Set Suite Variable    ${TIMESTAMP}    ${current_date}
    Create Directory    ${SCREENSHOT_DIR}/${TIMESTAMP}
    Create Directory    ${LOGS_DIR}/${TIMESTAMP}
    Move Files    ${EXECDIR}/*.png    ${SCREENSHOT_DIR}/${TIMESTAMP}/
    Close Browser    ALL