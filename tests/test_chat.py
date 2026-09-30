import time

import pytest
from lingua.lingua import LanguageDetectorBuilder, Language

from pages.Gemini_pages import Gemini_Page
@pytest.mark.regression
@pytest.mark.smoke
def test_enter_prompt(driver):
    driver.get("https://gemini.google.com/app?hl=tr")

    gemini_page = Gemini_Page(driver)
    start_time = time.time()
    prompt ="Bana Türkiyenin başkentini söyle"
    gemini_page.enter_prompt(prompt)
    gemini_page.enter_send()
    get_response_element = gemini_page.get_response()
    detector = detector = LanguageDetectorBuilder.from_languages(
    Language.TURKISH,
    Language.ENGLISH,
    Language.GERMAN,
    Language.FRENCH,
    Language.SPANISH
).build()
    detected_language = detector.detect_language_of(get_response_element)
    print(f"Detected language: {detected_language}")
    end_time = time.time()
    response_time = end_time - start_time
    print(f"Response time: {response_time:.2f}seconds")
    assert get_response_element != ''
    print("Mesaj algılandı " + prompt)


