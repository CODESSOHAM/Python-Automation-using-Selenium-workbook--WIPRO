*** Settings ***
Library    SeleniumLibrary

Test Setup       Open Test Browser
Test Teardown    Close Browser


*** Variables ***
${URL}        https://demowebshop.tricentis.com/
${BROWSER}    chrome


*** Test Cases ***
Verify E-Commerce Website

    Page Should Contain    Demo Web Shop
    Title Should Be    Demo Web Shop

Verify Search Functionality

    Input Text    id=small-searchterms    laptop
    Click Button    xpath=//input[@value='Search']
    Page Should Contain    Search
    Capture Page Screenshot    screenshots/search_result.png


*** Keywords ***
Open Test Browser

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
