from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='💨 Кальяны')],
                                     [KeyboardButton(text='🌱 Табак для кальяна')]],
                                     resize_keyboard=True)



hookah = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Alpha Hookah', callback_data='alphahook')],
                                               [InlineKeyboardButton(text='Mamay Castoms', callback_data='mamay')],
                                               [InlineKeyboardButton(text='Level', callback_data='level')]])

alpha = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Alpha Hookah Harley Joker', callback_data='alphajoker')],
                                              [InlineKeyboardButton(text='Alpha Hookah X Special(разрисован)', callback_data='alphaxs')],
                                              [InlineKeyboardButton(text='Alpha Hookah X', callback_data='alphajokerx')],
                                              [InlineKeyboardButton(text='⬅️ Назад', callback_data='backs')]])


mamay = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Mamay custom big', callback_data='mamaybig')],
                                              [InlineKeyboardButton(text='Mamay custom big(средний)', callback_data='mamaysred')],
                                              [InlineKeyboardButton(text='Mamay custom mini', callback_data='mamaymini')],
                                              [InlineKeyboardButton(text='⬅️ Назад', callback_data='backs')]])




tabacco = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Element', callback_data='element'),
                                                 InlineKeyboardButton(text='BlackBurn', callback_data='blackburn')],
                                                [InlineKeyboardButton(text='Burn', callback_data='burn'),
                                                 InlineKeyboardButton(text='OVERDOSE', callback_data='overdose')],
                                                [InlineKeyboardButton(text='Nаш', callback_data='nash'),
                                                 InlineKeyboardButton(text='Душа', callback_data='dysha')],
                                                [InlineKeyboardButton(text='SEBERO', callback_data='sebero'),
                                                 InlineKeyboardButton(text='JENT', callback_data='jent')],
                                                [InlineKeyboardButton(text='BONCHE', callback_data='bonche'),
                                                 InlineKeyboardButton(text='MUSTHAVE', callback_data='must')],
                                                [InlineKeyboardButton(text='BANGER', callback_data='banger'),
                                                 InlineKeyboardButton(text='SPECTRUM', callback_data='spect')],
                                                [InlineKeyboardButton(text='BRUSKO', callback_data='brusko'),
                                                 InlineKeyboardButton(text='JAM', callback_data='jam')],
                                                [InlineKeyboardButton(text='HIT', callback_data='hit'),
                                                 InlineKeyboardButton(text='Trofimoffs', callback_data='trof')]])

back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⬅️ Назад', callback_data='back')]])

backis = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⬅️ Назад', callback_data='backis')]])

backsm = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⬅️ Назад', callback_data='backsm')]])

backsl = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⬅️ Назад', callback_data='backsl')]])