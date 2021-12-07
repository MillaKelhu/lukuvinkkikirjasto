*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
*** Test Cases ***

Open Link Form Page
    Go To Add Link Page
    Add Link Page Should Be Open

Add Link Correctly
    Set Title  Wikipedia
    Set Url  wikipedia.com
    Submit Link
    Page Should Contain  Lukuvinkit

*** Keywords ***
Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Url
    [Arguments]  ${link_url}
    Input Text  link_url  ${link_url}

Submit Link
    Click Button  Lisää Lukuvinkki