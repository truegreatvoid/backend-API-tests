***Settings***
Resource  ../locators/global-page-locators.robot
Resource  ../helpers/common-actions.robot

***Keywords***

Click Button Back
    Verify Element  ${buttonBack}
    Click Element   ${buttonBack}

Click Button Options
    Verify Element  ${buttonOptions}
    Click Element   ${buttonOptions}