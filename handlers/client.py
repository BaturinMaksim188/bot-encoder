from func.client_func import *


# ------------------------------------------------------FSMContext------------------------------------------------------
@dp.message_handler(state="*", commands="cancel")
async def command_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Вам неоткуда выходить.", reply_markup=kb_start)
        return
    else:
        await state.finish()
    await message.answer("Завершено.", reply_markup=kb_start)


# ------------------------------------------------------FSMContext------------------------------------------------------

# handler for command "/start"
@dp.message_handler(commands="start", state="*")
async def command_start(message: types.Message):
    await States.CHOICE_W.set()
    await message.answer("Привет, выбери метод шифрования!", reply_markup=kb_all)


# handler for button to v1 or v2 or decode state
@dp.message_handler(content_types=['text'], state=States.CHOICE_W)
async def command_start(message: types.Message, state: FSMContext):
    if message.text == "Матричный":
        await States.CHOICE_v1.set()
        text_info_v1 = "Подготавливаем матрицу MxN.\nПодготавливаем два ключа KM и KN.(Определены заранее)\n\n1) " \
                       "Сообщение " \
                       "по строкам записываем в матрицу MxN.\n2) По краям матрицы записываем ключи.\n3) Строки " \
                       "переставляем так, чтобы буквы ключа стали упорядоченными по алфавиту. То же делаем со " \
                       "столбцами.\n4) Списываем буквы из матрицы по столбцам."
        await message.answer(f"Отлично! Вот немного информации об этом шифре:\n\n{text_info_v1}\n\nОтправь своё "
                             f"сообщение, чтобы его зашифровать!")
    elif message.text == "ADFGX":
        await States.CHOICE_v2.set()
        text_info_v2 = "Матрицу 5х5 случайным образом записывают (Определенным образом) буквы латинского " \
                       "алфавита.\nИспользуем слово-ключ (Определено заранее).\n\n1) Каждой букве " \
                       "сообщения ставим в соответствие 2 буквы (по матрице).\n2) Полученный текст записываем под " \
                       "ключом.\n3) Переставляем столбцы так, чтобы буквы ключа упорядочились по алфавиту.\n4) " \
                       "Записываем буквы из полученной матрицы (по столбцам) в шифр."
        await message.answer(f"Отлично! Вот немного информации об этом шифре:\n\n{text_info_v2}\n\nОтправь своё "
                             f"сообщение, чтобы его зашифровать!")
    elif message.text == "Мне нужен матричный дешифровщик!":
        await States.CHOICE_TO_DECODE_v1.set()
        await message.answer("Отлично, отправь мне свой шифр!")
    else:
        await state.finish()
        await message.answer("Вы повели себя неправильно!\n\nПовторите команду /start")


# ______________________________________________________________________________________________________________________
# No text v1 handler
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_v1)
async def not_a_text_v1(message: types.Message):
    await message.answer("Это не текст, введите текст или /cancel")


# No text CTDv1 handler
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_TO_DECODE_v1)
async def not_a_text_v1(message: types.Message):
    await message.answer("Это не текст, введите текст или /cancel")


# No text v2 handler
@dp.message_handler(
    content_types=['photo', 'video', 'video_note', 'voice', 'poll', 'venue', 'audio', 'document', 'dice',
                   'animation', 'contact', 'sticker', 'location'], state=States.CHOICE_v2)
async def not_a_text_v2(message: types.Message):
    await message.answer("Это не текст, введите текст или /cancel")


# ______________________________________________________________________________________________________________________

# Text to v1 handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_v1)
async def text_application(message: types.Message, state=FSMContext):

    out = await cipher_v1(message.text.lower().replace(' ', ''))

    await message.answer(f"Вот ваш шифр: \n\n{out}\n\nБудьте здоровы!")
    await state.finish()


# Text to CTDv1 handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_TO_DECODE_v1)
async def text_application(message: types.Message, state=FSMContext):

    out = await decipher_v1(message.text.lower().replace(' ', ''))

    await message.answer(f"Вот ваш текст: \n\n{out}\n\nБудьте здоровы!")
    await state.finish()


# Text to v2 handler
@dp.message_handler(content_types=['text'], state=States.CHOICE_v2)
async def text_application(message: types.Message, state=FSMContext):

    out = await cipher_v2(message.text.lower().replace(' ', ''))

    await message.answer(f"Вот ваш шифр: {out}\n\nБудьте здоровы!")
    await state.finish()


# ----------------------------------------------------------------------------------------------------------------------
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start', state=None)
