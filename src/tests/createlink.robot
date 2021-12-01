*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
*** Test Cases ***

Open Link Form Page
    Go To Add Link Page
    Add Link Page Should Be Open