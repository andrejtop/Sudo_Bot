from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from app.database.requests import get_categories, get_products_by_category
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Каталог"),
        ],
        [
            KeyboardButton(text="Корзина"),
        ],
        [
            KeyboardButton(text="Контакты"),
            KeyboardButton(text="О нас"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню',
    one_time_keyboard=True
)

async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def products(category_id):
    all_products = await get_products_by_category(category_id)
    keyboard = InlineKeyboardBuilder()
    for product in all_products:
        keyboard.add(InlineKeyboardButton(text=product.name, callback_data=f'product_{product.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

# catalog = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Футболки", callback_data="tshirt")
#         ],
#         [
#             InlineKeyboardButton(text="Кроссовки", callback_data="sneakers")
#         ],
#         [
#             InlineKeyboardButton(text="Кепки", callback_data="caps")
#         ]
#     ]
# )
#
# get_number = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Отправить номер", request_contact=True),
#         ]
#     ],
#     resize_keyboard=True,
# )