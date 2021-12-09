*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.1 seconds
${HOME URL}  http://localhost:5000
${ADDLINK URL}  http://localhost:5000/addlink
${REGISTER PAGE}  http://localhost:5000/register
${LOGIN PAGE}  http://localhost:5000/login

*** Keywords ***
Open And Configure BROWSER
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Main Page
    Go To  ${HOME URL}

Main Page Should Be Open
    Title Should Be  Lukuvinkit

Go To Add Link Page
    Go To  ${ADDLINK URL}

Go To Register Page
    Go To  ${REGISTER PAGE}
Go To Login Page
    Go To  ${LOGIN PAGE}
Add Link Page Should Be Open
    Page Should Contain  Syötä lukuvinkkisi nimi ja osoite

Authenticate
    Go To Register Page
    Set Username  testiuser
    Set Password  12345
    Click Button  Luo
    Go To Login Page
    Set Username  testiuser
    Set Password  12345
    Click Button  Kirjaudu sisään


Set Username
    [Arguments]  ${title}
    Input Text  username  ${title}

Set Password
    [Arguments]  ${link_url}
    Input Text  password  ${link_url}