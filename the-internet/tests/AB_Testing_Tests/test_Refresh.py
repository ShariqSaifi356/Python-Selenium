from pages.AB_Testing_Page.ab_testing_page import ABTestingPage

def test_checkout_flow(setup):
    driver = setup

    ab_page = ABTestingPage(driver)
    
    ab_page.openABTestingPage() 
    
    expected_variations =  ["A/B Test Control", "A/B Test Variation 1", "No A/B Test"]
    
    for _ in range(5):
        heading  = ab_page.headingOfABPage()
        print(heading)
        assert heading in expected_variations
        driver.refresh()