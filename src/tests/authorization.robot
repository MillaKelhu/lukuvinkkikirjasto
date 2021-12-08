*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
*** Test Cases ***

User Can Register
    Go To Register Page
    Set Username  testiuser
    Set Password  123456
    Submit
    Page Should Contain  Lukuvinkidadat

User Can Log In
    Go To Login Page
    Set Username  testiuser
    Set Password  123456
    Submit
    Wait Until Keyword Succeeds  30s  3s  Page Should Contain  Lukuvinkidadat

User Cannot Log In With Wrong Password
    Go To Login Page
    Set Username  testiuser2
    Set Password  12341
    Submit
    Page Should Contain  Incorrect username or password

User Cannot Register With Existing Username
    Go To Register Page
    Set Username  testiuser
    Set Password  uusisalasana
    Page Should Contain  Käyttäjänimi on jo käytössä

*** Keywords ***
Set Username
    [Arguments]  ${title}
    Input Text  username  ${title}

Set Password
    [Arguments]  ${link_url}
    Input Text  password  ${link_url}

Submit
    Click Button  Kirjaudu sisään