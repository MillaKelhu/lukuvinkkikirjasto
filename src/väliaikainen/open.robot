*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***

Site Can Be Opened
    Go To Main Page
    Main Page Should Be Open
