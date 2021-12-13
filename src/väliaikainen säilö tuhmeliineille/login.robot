*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User For Tests And Go To Login Page
*** Test Cases ***

User Can Log In
    Set Username  testiuser
    Set Password  123456
    Submit
    Page Should Contain  Lukuvinkidadat

User Can Not Log In With Incorrect Password
    Set Username  testiuser
    Set Password  1234568
    Submit
    Page Should Contain  Incorrect username or password

*** Keywords ***
Set Username
    [Arguments]  ${title}
    Input Text  username  ${title}

Set Password
    [Arguments]  ${link_url}
    Input Text  password  ${link_url}

Submit
    Click Button  Kirjaudu sisään

Create User For Tests And Go To Login Page
    Go To Register Page
    Set Username  testiuser
    Set Password  123456
    Submit
    Go To Login Page