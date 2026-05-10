import requests
from pages.AB_Testing_Page.ab_testing_page import ABTestingPage

def test_checkout_flow(setup):
    driver = setup

    ab_page = ABTestingPage(driver)
    
    ab_page.openABTestingPage()
    
    assert ab_page.visibilityOfElement() == True    
    
    response = requests.get(ab_page.url())
    assert response.status_code == 200
    
    assert ab_page.url() == "https://the-internet.herokuapp.com/abtest"
    