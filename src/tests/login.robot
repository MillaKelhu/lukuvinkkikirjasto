*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Reset Added User And Close Browser
Test Setup  Create User For Tests And Go To Login Page
*** Test Cases ***

User Can Log In
    Set Username  testiuser
    Set Password  123456
    Submit
    Main Page Should Be Open

User Can Not Log In With Wrong Password
    Set Username  testiuser
    Set Password  12345678
    Submit
    Login Should Fail

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

Create User For Tests And Go To Login Page
    Reset Adding User  testiuser  123456
    Create User  testiuser  123456
    Go To Login Page
    Login Page Should Be Open

Reset Added User And Close Browser
    Reset Adding User  testiuser  123456
    Close Browser