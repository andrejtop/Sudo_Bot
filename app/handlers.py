from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold
import app.keyboards as kb
from app.fsm import Register
import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await rq.get_user(message.from_user.id)
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}! Добро пожаловать в наш магазин!", reply_markup=kb.main)


@router.message(F.text == "Каталог")
async def catalog_handler(message: Message) -> None:
    await message.answer("Выберите категорию товара", reply_markup=await kb.categories())


@router.callback_query(F.data.startswith("category_"))
async def category_handler(callback: CallbackQuery) -> None:
    await callback.answer('')
    await callback.message.answer('Выберите товар', reply_markup=await kb.products(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith("product_"))
async def category_handler(callback: CallbackQuery) -> None:
    product = await rq.get_product(callback.data.split('_')[1])
    await callback.answer('')
    await callback.message.answer(f'Название: {product.name}\nОписание: {product.description}\nЦена: {product.price}', reply_markup=await kb.products(callback.data.split('_')[1]))






# @router.callback_query(F.data == "tshirt")
# async def tshirt_handler(callback: CallbackQuery) -> None:
#     await callback.answer('')
#     await callback.message.answer("Тут будет каталог футболок")
#
#
# # @router.message(F.text == "/register")
# @router.message(Command('register'))
# async def register_handler(message: Message, state: FSMContext) -> None:
#     await state.set_state(Register.name)
#     await message.answer("Введите ваше имя:...")
#
# @router.message(Register.name)
# async def name_handler(message: Message, state: FSMContext) -> None:
#     await state.update_data(name=message.text)
#     await state.set_state(Register.age)
#     await message.answer("Введите ваш возраст:...")
#
# @router.message(Register.age)
# async def age_handler(message: Message, state: FSMContext) -> None:
#     await state.update_data(age=message.text)
#     await state.set_state(Register.number)
#     await message.answer("Введите ваш номер телефона:...", reply_markup=kb.get_number)
#
# @router.message(Register.number, F.contact)
# async def number_handler(message: Message, state: FSMContext) -> None:
#     await state.update_data(number=message.contact.phone_number)
#     data = await state.get_data()
#     await message.answer(f"Ваши данные:\n\n"
#                          f"Имя: {data['name']}\n"
#                          f"Возраст: {data['age']}\n"
#                          f"Номер телефона: {data['number']}")
#     await state.clear()


@router.message()
async def echo_handler(message: Message) -> None:

    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")