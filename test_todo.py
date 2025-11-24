import os

from playwright.sync_api import Page, expect


#
# def test_select(page):
#     page.goto('https://zimaev.github.io/select/')
#     page.select_option('#floatingSelect', value="3")
#     page.select_option('#floatingSelect', index=1)
#     page.select_option('#floatingSelect', label="Нашел и завел bug")
#
# def test_select_multiple(page):
#     page.goto('https://zimaev.github.io/select/')
#     page.select_option('#skills', value=["playwright", "python"])
#
# def test_drag_and_drop(page):
#     page.goto('https://zimaev.github.io/draganddrop/')
#     page.drag_and_drop("#drag", "#drop")


# def test_new_tab(page: Page):
#     page.goto("https://zimaev.github.io/tabs/")
#     with page.context.expect_page() as tab:
#         page.get_by_text("Переход к Dashboard").click()
#
#     new_tab = tab.value
#     assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
#     sign_out = new_tab.locator('.nav-link', has_text='Sign out')
#     assert sign_out.is_visible()




def test_todo(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    input_field = page.get_by_placeholder('What needs to be done?')
    expect(input_field).to_be_empty()
    input_field.fill("Закончить курс по playwright")
    input_field.press('Enter')
    input_field.fill("Добавить в резюме, что умею автоматизировать")
    input_field.press('Enter')
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)
    todo_item.get_by_role('checkbox').nth(0).click()
    expect(todo_item.nth(0)).to_have_class('completed')