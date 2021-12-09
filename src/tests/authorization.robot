*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Login Browser
Suite Teardown  Close Browser
*** Test Cases ***

User Can Register
    Go To Register Page
    Set Username  testiuser
    Set Password  123456
    Submit
    Page Should Contain  Eikö sinulla ole käyttäjää?

User Can Log In
    Go To Login Page
    Set Username  testiuser
    Set Password  123456
    Submit
    Page Should Contain  lukuvinkikki

User Can Not Log In With Incorrect Password
    Go To Login Page
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

Open And Configure Login BROWSER
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To Register Page
    Set Username  testiuser
    Set Password  123456
    Submit