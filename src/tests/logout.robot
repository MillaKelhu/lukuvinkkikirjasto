*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Reset Added User And Close Browser
Test Setup  Create User For Tests And Log In
*** Test Cases ***

User Can Log Out
    User Should Be Logged In
    Click Button  Kirjaudu ulos
    User Should Be Logged Out

*** Keywords ***
Set Username
    [Arguments]  ${title}
    Input Text  username  ${title}

Set Password
    [Arguments]  ${link_url}
    Input Text  password  ${link_url}

Login Should Fail
    Login Page Should Be Open
    Page Should Contain  Virheellinen käyttäjänimi tai salasana.

Submit
    Click Button  login button

Create User For Tests And Log In
    Reset Adding User  testiuser  123456
    Create User  testiuser  123456
    Go To Login Page
    Login Page Should Be Open
    Set Username  testiuser
    Set Password  123456
    Submit
    Main Page Should Be Open

Reset Added User And Close Browser
    Reset Adding User  testiuser  123456
    Close Browser