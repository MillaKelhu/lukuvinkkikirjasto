*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.1 seconds
${HOME URL}  http://${SERVER}
${ADDLINK URL}  http://${SERVER}/addlink
${REGISTER PAGE}  http://${SERVER}/register
${LOGIN PAGE}  http://${SERVER}/login

*** Keywords ***
Open And Configure BROWSER
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Main Page
    Go To  ${HOME URL}

Main Page Should Be Open
    Page Should Contain  Lukuvinkidadat

Go To Add Link Page
    Go To  ${ADDLINK URL}

Go To Register Page
    Go To  ${REGISTER PAGE}

Go To Login Page
    Go To  ${LOGIN PAGE}

Add Link Page Should Be Open
    Page Should Contain  Syötä lukuvinkkisi nimi ja osoite

Register Page Should Be Open
    Page Should Contain  Onko sinulla jo käyttäjä? Kirjaudu sisään

Login Page Should Be Open
    Page Should Contain  Eikö sinulla ole käyttäjää? Luo uusi käyttäjä

User Should Not Be Logged In
    Page Should Contain  Kirjaudu sisään

User Should Be Logged In

Authenticate
    Create User  testiuser  12345
    Go To Login Page
    Set Username  testiuser
    Set Password  12345
    Click Button  login button

Set Username
    [Arguments]  ${title}
    Input Text  username  ${title}

Set Password
    [Arguments]  ${link_url}
    Input Text  password  ${link_url}