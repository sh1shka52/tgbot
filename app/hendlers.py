from aiogram import F, Router

from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    name = message.from_user
    first_name = name.first_name
    await message.answer(f'Привет {first_name}', reply_markup=kb.main)


@router.message(F.text == 'скала')
@router.message(F.text == 'skala')

@router.message(F.text == 'Скала')
@router.message(F.text == 'Skala')
async def nice(message: Message):
    await message.answer('Жевательная резинка Скала 490р')


# GEEK BAR
@router.message(F.text == 'гик бар мини')
@router.message(F.text == 'Гик бар мини')
@router.message(F.text == 'Гик мини')
@router.message(F.text == 'гик мини')
@router.message(F.text == 'Geek bar mini')
async def nice(message: Message):
    await message.answer('Нап Гик мини 690р')

@router.message(F.text == 'Гик бар 6')
@router.message(F.text == 'Гик бар 6к')
@router.message(F.text == 'Гик 6к')
@router.message(F.text == 'Гик 6')
@router.message(F.text == 'Geek bar 6000')
@router.message(F.text == 'Geek bar 6к')

@router.message(F.text == 'гик бар 6')
@router.message(F.text == 'гик бар 6к')
@router.message(F.text == 'гик 6к')
@router.message(F.text == 'гик 6')
@router.message(F.text == 'geek bar 6000')
@router.message(F.text == 'geek bar 6к')
async def nice(message: Message):
    await message.answer('Нап Гик 6 1190р')


@router.message(F.text == 'гик бар 10')
@router.message(F.text == 'гик бар 10к')
@router.message(F.text == 'гик 10к')
@router.message(F.text == 'гик 10')
@router.message(F.text == 'гик ультра')
@router.message(F.text == 'гик мелосо ультра')
@router.message(F.text == 'geek bar 10000')
@router.message(F.text == 'geek bar 10к')

@router.message(F.text == 'Гик бар 10')
@router.message(F.text == 'Гик бар 10к')
@router.message(F.text == 'Гик 10к')
@router.message(F.text == 'Гик 10')
@router.message(F.text == 'Гик ультра')
@router.message(F.text == 'Гик мелосо ультра')
@router.message(F.text == 'Geek bar 10000')
@router.message(F.text == 'Geek bar 10к')
async def nice(message: Message):
    await message.answer('Нап Гик Ультра 1390р')

@router.message(F.text == 'гик бар 12')
@router.message(F.text == 'гик бар 12к')
@router.message(F.text == 'гик 12к')
@router.message(F.text == 'гик 12')
@router.message(F.text == 'geek bar 12000')
@router.message(F.text == 'geek bar 12к')

@router.message(F.text == 'Гик бар 12')
@router.message(F.text == 'Гик бар 12к')
@router.message(F.text == 'Гик 12к')
@router.message(F.text == 'Гик 12')
@router.message(F.text == 'Geek bar 12000')
@router.message(F.text == 'Geek bar 12к')
async def nice(message: Message):
    await message.answer('Нап Гик 120мл 1490р')

@router.message(F.text == 'гик бар 911')
@router.message(F.text == 'гик бар 18к')
@router.message(F.text == 'гик 911')
@router.message(F.text == '911')
@router.message(F.text == 'гик 18')
@router.message(F.text == 'geek bar 911')
@router.message(F.text == 'geek bar 18к')

@router.message(F.text == 'Гик бар 911')
@router.message(F.text == 'Гик бар 18к')
@router.message(F.text == 'Гик 911')
@router.message(F.text == '911')
@router.message(F.text == 'Гик 18')
@router.message(F.text == 'Geek bar 911')
@router.message(F.text == 'Geek bar 18к')
async def nice(message: Message):
    await message.answer('Нап Гик 911 1690р')

@router.message(F.text == 'гик бар 20')
@router.message(F.text == 'гик бар 20к')
@router.message(F.text == 'гик 20к')
@router.message(F.text == 'гик 20')
@router.message(F.text == 'geek bar 20000')
@router.message(F.text == 'geek bar 20к')

@router.message(F.text == 'Гик бар 20')
@router.message(F.text == 'Гик бар 20к')
@router.message(F.text == 'Гик 20к')
@router.message(F.text == 'Гик 20')
@router.message(F.text == 'Geek bar 20000')
@router.message(F.text == 'Geek bar 20к')
async def nice(message: Message):
    await message.answer('Нап Гик 200мл ')

@router.message(F.text == 'гик бар 25')
@router.message(F.text == 'гик бар 25к')
@router.message(F.text == 'гик 25к')
@router.message(F.text == 'гик 25')
@router.message(F.text == 'гик пульс')
@router.message(F.text == 'geek bar 25000')
@router.message(F.text == 'geek bar 25к')

@router.message(F.text == 'Гик бар 25')
@router.message(F.text == 'Гик бар 25к')
@router.message(F.text == 'Гик 25к')
@router.message(F.text == 'Гик 25')
@router.message(F.text == 'Гик пульс')
@router.message(F.text == 'Geek bar 25000')
@router.message(F.text == 'Geek bar 25к')
async def nice(message: Message):
    await message.answer('Нап Гик 250мл ')

@router.message(F.text == 'прайз 9')
@router.message(F.text == 'praze 9000')
@router.message(F.text == 'praze 9к')
@router.message(F.text == 'прайз')

@router.message(F.text == 'Прайз 9')
@router.message(F.text == 'Praze 9000')
@router.message(F.text == 'Praze 9к')
@router.message(F.text == 'Прайз')
async def nice(message: Message):
    await message.answer('Напиток Пра 900мл')

@router.message(F.text == 'прайз 18')
@router.message(F.text == 'praze 18000')
@router.message(F.text == 'praze 18к')
@router.message(F.text == 'прайз')

@router.message(F.text == 'Прайз 18')
@router.message(F.text == 'Praze 18000')
@router.message(F.text == 'Praze 18к')
@router.message(F.text == 'Прайз')
async def nice(message: Message):
    await message.answer('Напиток Пра 180мл')

@router.message(F.text == 'прайз 20')
@router.message(F.text == 'praze 20000')
@router.message(F.text == 'praze 20к')
@router.message(F.text == 'прайз')

@router.message(F.text == 'Прайз 20')
@router.message(F.text == 'Praze 20000')
@router.message(F.text == 'Praze 20к')
@router.message(F.text == 'Прайз')
async def nice(message: Message):
    await message.answer('Напиток Прай 200мл')

@router.message(F.text == 'рел')
@router.message(F.text == 'рэл')
@router.message(F.text == 'rell')

@router.message(F.text == 'Рел')
@router.message(F.text == 'Рэл')
@router.message(F.text == 'Rell')
async def nice(message: Message):
    await message.answer('Жевательная резинка Рэл ')

@router.message(F.text == 'эпе 25')
@router.message(F.text == 'epe 25')
@router.message(F.text == 'епе 25')
@router.message(F.text == 'epe')

@router.message(F.text == 'Эпе 25')
@router.message(F.text == 'Epe 25')
@router.message(F.text == 'Епе 25')
@router.message(F.text == 'Epe')
async def nice(message: Message):
    await message.answer('Напиток ЭП 25')

@router.message(F.text == 'эпе 20')
@router.message(F.text == 'epe 20')
@router.message(F.text == 'епе 20')
@router.message(F.text == 'epe')

@router.message(F.text == 'Эпе 20')
@router.message(F.text == 'Epe 20')
@router.message(F.text == 'Епе 20')
@router.message(F.text == 'Epe')
async def nice(message: Message):
    await message.answer('Нап ЭП 20')

@router.message(F.text == 'эпе 10')
@router.message(F.text == 'epe 10')
@router.message(F.text == 'епе 10')
@router.message(F.text == 'epe')

@router.message(F.text == 'Эпе 10')
@router.message(F.text == 'Epe 10')
@router.message(F.text == 'Епе 10')
@router.message(F.text == 'Epe')
async def nice(message: Message):
    await message.answer('Напиток ЭП 10')

@router.message(F.text == 'Аеровайб')
@router.message(F.text == 'аеровайб')
@router.message(F.text == 'aerovibe')
@router.message(F.text == 'Aerovibe')
async def nice(message: Message):
    await message.answer('Жевательная резинка AV200 1990р')

@router.message(F.text == 'юя')
@router.message(F.text == 'Юя')
@router.message(F.text == 'Уя')
@router.message(F.text == 'уя')
async def nice(message: Message):
    await message.answer('Напиток ЮЯ 300мл 1590р')

@router.message(F.text == 'Иксрос мини')
@router.message(F.text == 'Xros mini')
@router.message(F.text == 'Мини')
async def nice(message: Message):
    await message.answer('2000р')

@router.message(F.text == 'Иксрос 3 мини')
@router.message(F.text == '3 мини')
@router.message(F.text == 'Иксрос 3мини')
@router.message(F.text == 'Xros 3 mini')
async def nice(message: Message):
    await message.answer('2100р')

@router.message(F.text == 'Иксрос 4 мини')
@router.message(F.text == '4 мини')
@router.message(F.text == 'Иксрос 4мини')
@router.message(F.text == 'Xros 4 mini')
async def nice(message: Message):
    await message.answer('2500р')

@router.message(F.text == 'Иксрос 3')
@router.message(F.text == '3')
@router.message(F.text == 'Xros 3')
async def nice(message: Message):
    await message.answer('2500р')

@router.message(F.text == 'Иксрос про')
@router.message(F.text == 'Про')
@router.message(F.text == 'Xros pro')
async def nice(message: Message):
    await message.answer('3300р')

@router.message(F.text == 'Иксрос вайб')
@router.message(F.text == 'Вайб')
@router.message(F.text == 'Xros vibe')
async def nice(message: Message):
    await message.answer('2200р')

@router.message(F.text == 'Иксрос вайб нано')
@router.message(F.text == 'Вайб нано')
@router.message(F.text == 'Xros vibe nano')
async def nice(message: Message):
    await message.answer('2400р')

@router.message(F.text == 'Иксрос 4 нано')
@router.message(F.text == '4 нано')
@router.message(F.text == 'Xros 4 nano')
async def nice(message: Message):
    await message.answer('2700р')



@router.message(F.text == '💨 Кальяны')
async def hookah(message: Message):
    await message.delete()
    await message.answer('Кальяны', reply_markup=kb.hookah)

@router.callback_query(F.data == 'backs')
async def backs(callback: CallbackQuery):
    await callback.message.edit_text('Кальяны', reply_markup=kb.hookah)
    await callback.answer()

@router.callback_query(F.data == 'backis')
async def backs(callback: CallbackQuery):
    await callback.message.edit_text('Alpha Hookah', reply_markup=kb.alpha)
    await callback.answer()

@router.callback_query(F.data == 'backsm')
async def backs(callback: CallbackQuery):
    await callback.message.edit_text('Mamay Castoms', reply_markup=kb.mamay)
    await callback.answer()

@router.callback_query(F.data == 'backsl')
async def backs(callback: CallbackQuery):
    await callback.message.edit_text('Кальяны', reply_markup=kb.hookah)
    await callback.answer()




@router.callback_query(F.data == 'alphahook')
async def alpha(callback: CallbackQuery):
    await callback.message.edit_text('Alpha Hookah',reply_markup=kb.alpha)

@router.callback_query(F.data == 'mamay')
async def alpha(callback: CallbackQuery):
    await callback.message.edit_text('Mamay Castoms',reply_markup=kb.mamay)

    
   



@router.callback_query(F.data == 'alphajoker')
async def alphaj(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('<b>Alpha Hookan Harley Joker</b>\n\n <b>Шахта:</b> 11.900р\n <b>Full набор(колба, шланг):</b> 13.300р',parse_mode='HTML', reply_markup=kb.backis)

@router.callback_query(F.data == 'alphaxs')
async def alphaj(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('<b>Alpha Hookah X Special(разрисован)</b>\n\n <b>Шахта:</b> 12.700р\n <b>Full набор(колба, шланг):</b> 14.100р ',parse_mode='HTML', reply_markup=kb.backis)

@router.callback_query(F.data == 'alphajokerx')
async def alphaj(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('<b>Alpha Hookah X</b>\n\n <b>Шахта:</b> 11.500р\n <b>Full набор(колба, шланг):</b> 12.900р',parse_mode='HTML', reply_markup=kb.backis)


@router.callback_query(F.data == 'mamaybig')
async def alphaj(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('<b>Mamay custom big</b>\n\n <b>Шахта:</b> 15.800р\n <b>Full набор(колба, шланг):</b> 17.200р',parse_mode='HTML', reply_markup=kb.backsm)


@router.callback_query(F.data == 'mamaysred')
async def alphaj(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('<b>Mamay custom big(средний)</b>\n\n <b>Шахта:</b> 14.900р\n <b>Full набор(колба, шланг):</b> 16.300р',parse_mode='HTML', reply_markup=kb.backsm)


@router.callback_query(F.data == 'mamaymini')
async def alphaj(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('<b>Mamay custom mini</b>\n\n <b>Шахта:</b> 14.300р\n <b>Full набор(колба, шланг):</b> 15.700р',parse_mode='HTML', reply_markup=kb.backsm)


@router.callback_query(F.data == 'level')
async def alphaj(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('<b>Level</b>\n\n <b>Шахта:</b> 3.000р\n <b>Full набор(колба, шланг):</b> 4.400р',parse_mode='HTML', reply_markup=kb.backsl)




@router.message(F.text == '🌱 Табак для кальяна')
async def tabacco(message: Message):
    await message.delete()
    await message.answer('Табак',reply_markup=kb.tabacco)

@router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    await callback.message.edit_text('Табак',reply_markup=kb.tabacco)
    await callback.answer()

@router.callback_query(F.data == 'element')
async def ele(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>ELEMENT</b>\n\n💨 Воздух:\n <b>Серье:</b> Вирджини\n <b>Крепость:</b> Легкая\n <b>Жаростойкость:</b> Средня\n\n<b> 🌊Вода:</b>\n <b>Серье:</b> Берли \n <b>Крепость:</b> Средняя\n <b>Жаростойкость:</b> Высокая\n\n <b>🌍Земля:</b>\n <b>Серье:</b> Берли\n <b>Крепость:</b> Крепкая\n <b>Жаростойкость:</b> Высокая ', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'blackburn')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>BLACKBURN</b>\n\n <b>Серье:</b> Бленд и 3 берли\n <b>Крепость:</b> Средняя\n <b>Жаростойкость:</b> Высокая', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'burn')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>BURN</b>\n\n <b>Серье:</b> Вирджини вымачивают в меде\n <b>Крепость:</b> Легкая\n <b>Жаростойкость:</b> Средня', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'overdose')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>OVERDOSE</b>\n\n <b>Серье:</b> 2 берли\n <b>Крепость:</b> Крепкая\n <b>Жаростойкость:</b> Высокая', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'nash')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>NАШ</b>\n\n <b>Серье:</b> 2 берли\n <b>Крепость:</b> Крепкия\n <b>Жаростойкость:</b> Высокая', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'dysha')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>ДУША</b>\n\n <b>Серье:</b> 2 берли\n <b>Крепость:</b> Средняя\n <b>Жаростойкость:</b> Средняя', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'sebero')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>SEBERO</b>\n\n Появился в 2018году в Омске\n <b>3 линейки:</b>\n Classic\n Arctic Mix\n Black\n <b>Серье:</b> Берли, вирджини, сигарный лист\n <b>Крепость:</b> Средняя\n <b>Жаростойкость:</b> Высокая', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'jent')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>JENT</b>\n\n То же самое что и sebero\n <b>4 линейки</b> \n Classic\n Alcohol\n Herbal(травяная)\n Cigar\n <b>Крепость:</b> Средняя\n <b>Жаростойкость:</b> Высокая', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'bonche')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>BONCHE</b>\n\n <b>Серье:</b> Сигарный лист\n <b>Крепость:</b> Крепкая\n <b>Жаростойкость:</b> Высокая', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'must')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>MUSTHAVE</b>\n\n <b>Серье:</b> Берли из 7 разных стран\n <b>Крепость:</b> Средняя\n <b>Жаростойкость:</b> Средняя', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'banger')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>BANGER</b>\n\n <b>Серье:</b> Берли\n <b>Крепость:</b> Легкая\n <b>Жаростойкость:</b> Средняя', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'spect')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>SPECTRUM</b>\n\n <b>Белые банки:</b>\n <b>3 линейки:</b>\n Classic\n Kitchen\n Mix\n <b>Серье:</b> Берли\n <b>Крепость:</b> Легкая\n <b>Жаростойкость:</b> Средняя\n\n <b>Черные банки:</b>\n <b>Серье:</b> Берли, вирджини\n <b>Крепость:</b> Средняя\n <b>Жаростойкость:</b> Средняя', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'brusko')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>BRUSKO</b>\n\n <b>Серье:</b> Чайная смесь\n <b>Крепость:</b> без никотина\n <b>Жаростойкость:</b> Низкая', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'jam')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>JAM</b>\n\n <b>Серье:</b> Чайная смесь и 10% берли\n <b>Крепость:</b> Легкая\n <b>Жаростойкость:</b> Средняя', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'hit')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>HIT</b>\n\n <b>Серье:</b> Берли\n <b>Крепость:</b> Средняя\n <b>Жаростойкость:</b> Высокая', parse_mode='HTML', reply_markup=kb.back)

@router.callback_query(F.data == 'trof')
async def black(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥<b>TROFIMOFFS</b>\n\n <b>Серье:</b> Берли двойной ферментации\n <b>Крепость:</b> Крепкая\n <b>Жаростойкость:</b> Высокая', parse_mode='HTML', reply_markup=kb.back)