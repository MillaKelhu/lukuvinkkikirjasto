*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://localhost:5000
${ADDLINK URL}  http://localhost:5000/addlink

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

Add Link Page Should Be Open
    Page Should Contain  Syötä lukuvinkkisi nimi ja osoite