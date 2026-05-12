from pages.AB_Testing_Page.ab_testing_page import ABTestingPage

def test_checkout_flow(setup):
    driver = setup

    ab_page = ABTestingPage(driver)
    
    ab_page.openABTestingPage()    
    assert ab_page.headingOfABPage() in ["A/B Test Control", "A/B Test Variation 1", "No A/B Test"]