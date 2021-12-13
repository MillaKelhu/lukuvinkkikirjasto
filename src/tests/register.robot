*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Reset Register And Close Browser
Test Setup  Open Register Page
*** Test Cases ***

User Can Register
    Set Username  testiuser
    Set Password  123456
    Submit
    Login Page Should Be Open

*** Keywords ***
Set Username
    [Arguments]  ${title}
    Input Text  username  ${title}

Set Password
    [Arguments]  ${link_url}
    Input Text  password  ${link_url}

Submit
    Click Button  Luo

Open Register Page
    Go To Register Page
    Register Page Should Be Open

Reset Register And Close Browser
    Reset Adding User  testiuser  123456
    Close Browser
