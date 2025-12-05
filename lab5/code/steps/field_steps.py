from behave import given, when, then
from field import field

@given('есть товары "Ковер" и "Диван для отдыха"')
def step_given_simple_goods(context):
    context.items = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
                     {'title': 'Диван для отдыха', 'color': 'black'},
                     {'title': None, 'price': 1000}]

@given('есть товары с ценами')
def step_given_goods_with_prices(context):
    context.items = [{'title': 'Ковер', 'price': 2000},
                     {'title': 'Диван', 'price': 3000},
                     {'title': 'Стул', 'price': None}]

@given('есть товары с пропущенными данными')
def step_given_goods_with_missing(context):
    context.items = [{'title': None, 'price': 100},
                     {'title': 'Шкаф', 'price': None},
                     {'title': None, 'price': None}]

@when('извлекаю поле title')
def step_when_extract_title(context):
    context.result = list(field(context.items, 'title'))

@when('извлекаю поля title и price')
def step_when_extract_title_price(context):
    context.result = list(field(context.items, 'title', 'price'))

@then('получаю ["{value1}", "{value2}"]')
def step_then_get_list(context, value1, value2):
    assert context.result == [value1, value2]

@then('получаю словари с этими полями')
def step_then_get_dicts_simple(context):
    assert len(context.result) > 0
    assert all(isinstance(item, dict) for item in context.result)

@then('None значения пропускаются')
def step_then_none_filtered_simple(context):
    for item in context.result:
        for value in item.values():
            assert value is not None