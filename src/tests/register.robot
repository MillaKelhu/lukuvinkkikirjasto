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
    Main Page Should Be Open

User Can Not Register With Existing Username
    Create Existing User
    Set Username  existinguser
    Set Password  123456
    Submit
    Register Should Fail

*** Keywords ***
Set Username
    [Arguments]  ${title}
    Input Text  username  ${title}

Set Password
    [Arguments]  ${link_url}
    Input Text  password  ${link_url}

Submit
    Click Button  Luo

Register Should Fail
    Register Page Should Be Open
    Page Should Contain  Käyttäjänimi on jo käytössä

Create Existing User
    Reset Adding User  existinguser  123456
    Create User  existinguser  123456

Open Register Page
    Go To Register Page
    Register Page Should Be Open

Reset Register And Close Browser
    Reset Adding User  existinguser  123456
    Reset Adding User  testiuser  123456
    Close Browser
