from pages.AB_Testing_Page.ab_testing_page import ABTestingPage

def test_checkout_flow(setup):
    driver = setup

    ab_page = ABTestingPage(driver)
    
    ab_page.openABTestingPage()    
    assert ab_page.paragraphOfABPage()
    assert ab_page.getParagraphTextofABPage() != ""
    
    expected_keywords = ["testing", "businesses", "simultaneously", "versions", "desired"]
    for keyword in expected_keywords:
        assert keyword in ab_page.containsExpectedKeywords()