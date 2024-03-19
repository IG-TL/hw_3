from selene import be, have, browser


def test_google_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('[id="search"]').should(have.text('QA.GURU — Курсы тестировщиков - онлайн-обучение ...'))
    print('positive')


def test_google_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('фъъъъъъъяяяяяъъъъ').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу фъъъъъъъяяяяяъъъъ ничего не найдено. '))
    print('negative')
