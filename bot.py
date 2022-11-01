from tkinter import EW
from turtle import back
from xml.dom.minidom import CharacterData
import telebot
from telebot import types
TOKEN = '5486920742:AAFF6eKztR6AhsEErC19Cr-MVkKmA0ulMXc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('1. Кадастр. номер')
    item2 = types.KeyboardButton('2. Проект відведення')
    item3 = types.KeyboardButton("3. Поділ, об'єднання")
    item4 = types.KeyboardButton('ІНШІ ВИДИ РОБІТ')
    item5 = types.KeyboardButton('Про нас')
    item6 = types.KeyboardButton('Реквізити для оплати:')
     
    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'Привiт, {0.first_name}!' ' Я створений для того, щоб ти міг переглянути послуги данної галузі.'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '1. Кадастр. номер':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Процедура послуги')
            item2 = types.KeyboardButton('Необхідні документи')
            item3 = types.KeyboardButton('Питання та відповіді:')
            item4 = types.KeyboardButton('Вартість робіт та терміни')
            back = types.KeyboardButton('Назад!')
            bot.send_message(message.chat.id, '1. ТЕХНІЧНА ДОКУМЕНТАЦІЯ ДЛЯ ПРИСВОЄННЯ КАДАСТРОВОГО НОМЕРУ ЗЕМЕЛЬНІЙ ДІЛЯНЦІ', parse_mode='Markdown')
            bot.send_message(message.chat.id, 'Розробляється здебільшого на земельну ділянку під житловим будинком за наявності самого будинку та документів на нього.Також потрібна якщо у Вас є стара приватизація на руках - держакти на землю, видані з 1992 по 2003 р (червоні або помаранчеві)', parse_mode='Markdown')
            bot.send_message(message.chat.id, 'або рішення про передачу у власність (так зване "Декретне")', parse_mode='Markdown')
           
            markup.add(back, item1, item2, item3, item4)
            bot.send_message(message.chat.id, '1. Кадастр. номер', reply_markup = markup)

        elif message.text == 'Вартість робіт та терміни':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bot.send_message(message.chat.id, 'Стандартна вартість – 5 тис. грн. Після вивчення документів та зйомки уточнюється вартість кожного конкретного випадку. Аванс (це вартість замірів) – 2тис. грн. Розрахунок безготівковий (на банківський рахунок чи картку). У загальну вартість не входить винесення ділянки в натуру – від 800 грн (це потрібно якщо немає парканів).Розрахунковий термін одержання кадастрового номера – 3 місяці. Договір складається на 6 місяців, тому що можуть бути затримки під час підписання меж із сусідами.', reply_markup = markup)       
            bot.send_message(message.chat.id, 'Вартість робіт та терміни', reply_markup = markup)
        elif message.text == 'Назад!!':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Процедура послуги')
            item2 = types.KeyboardButton('Необхідні документи')
            item3 = types.KeyboardButton('Питання та відповіді:')
            item3 = types.KeyboardButton('Вартість робіт та терміни')
            
           
            bot.send_message(message.chat.id, '1. ТЕХНІЧНА ДОКУМЕНТАЦІЯ ДЛЯ ПРИСВОЄННЯ КАДАСТРОВОГО НОМЕРУ ЗЕМЕЛЬНІЙ ДІЛЯНЦІ', parse_mode='Markdown')
            bot.send_message(message.chat.id, '1. Кадастр. номер', reply_markup = markup)
            bot.send_message(message.chat.id, '1. Дві копії паспорта та ідентифікаційного коду.', reply_markup = markup)
            bot.send_message(message.chat.id, '2. Дві копії технічного паспорта на будинок і споруди.', reply_markup = markup)
            bot.send_message(message.chat.id, '3. Одна проста та одна завірена нотаріально копія правовстановлюючого документа на будинок (купівлі-продажу, спадщини, дарування, рішення суду)', reply_markup = markup)
            bot.send_message(message.chat.id, '4. Дві копії виписки про реєстрацію в БТІ або ДРРП.', reply_markup = markup)
            bot.send_message(message.chat.id, '5. Засвідчена нотаріально копія державного акту на право приватної власності на землю (для присвоєння кадастрового номера на земельну ділянку, яка була приватизована у 1992-2003 р.)', reply_markup = markup)
            
            markup.add(item1, item2, item3)
            
            bot.send_message(message.chat.id, '1. Кадастр. номер', reply_markup = markup)


        elif message.text == 'Процедура послуги':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
           
            bot.send_message(message.chat.id, ' 1) Вивчення документів (1 тиждень)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '2) Заміри ділянки (по домовленості)', reply_markup = markup)
            bot.send_message(message.chat.id, '3) Обробка вимірів (близько 2х тижнів)', reply_markup = markup)
            bot.send_message(message.chat.id, '4) Укладання договору та підписання техзавдання', reply_markup = markup)
            bot.send_message(message.chat.id, '5) Погодження меж із сусідами та в місцевій раді (це завдання замовника!). Потрібно розуміти чи є суперечки з сусідами про межу або, можливо, сусіди відсутні', reply_markup = markup)
            bot.send_message(message.chat.id, '6) Складання техдокументації (близько 2х тижнів)', reply_markup = markup)
            bot.send_message(message.chat.id, '7) Подача до кадастру (14 робочих днів, іноді двічі)', reply_markup = markup)
            bot.send_message(message.chat.id, '8) Підготовка 2-х примірників документів (1 тиждень)', reply_markup = markup)
            bot.send_message(message.chat.id, '9) Винесення меж ділянки в натуру (на місцевість) – робиться за потребою та домовленістю (за окрему плату)', reply_markup = markup)
            
            
            bot.send_message(message.chat.id, '1. Кадастр. номер', reply_markup = markup)










           

             
            
        elif message.text == 'процедура оформлення:':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bot.send_message(message.chat.id, '1) Вивчення документів (1 тиждень)', reply_markup = markup)
            bot.send_message(message.chat.id, '2) Заміри ділянки (по домовленості)', reply_markup = markup)
            bot.send_message(message.chat.id, '3) Обробка вимірів (близько 2х тижнів)', reply_markup = markup)
            bot.send_message(message.chat.id, '4) Укладання договору та підписання техзавдання', reply_markup = markup)
            bot.send_message(message.chat.id, '5) Погодження меж із сусідами та в місцевій раді (це завдання замовника!). Потрібно розуміти чи є суперечки з сусідами про межу або, можливо, сусіди відсутні', reply_markup = markup)
            bot.send_message(message.chat.id, '6) Складання техдокументації (близько 2х тижнів)', reply_markup = markup)
            bot.send_message(message.chat.id, '7) Подача до кадастру (14 робочих днів, іноді двічі)', reply_markup = markup)
            bot.send_message(message.chat.id, '7) Подача до кадастру (14 робочих днів, іноді двічі)', reply_markup = markup)
            bot.send_message(message.chat.id, '9) Винесення меж ділянки в натуру (на місцевість) – робиться за потребою та домовленістю (за окрему плату)', reply_markup = markup)
            

            



            
    



        elif message.text == 'Необхідні документи':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bot.send_message(message.chat.id, '1. Дві копії паспорта та ідентифікаційного коду.', reply_markup = markup)
            bot.send_message(message.chat.id, '2. Дві копії технічного паспорта на будинок і споруди.', reply_markup = markup)
            bot.send_message(message.chat.id, '3. Одна проста та одна завірена нотаріально копія правовстановлюючого документа на будинок (купівлі-продажу, спадщини, дарування, рішення суду)', reply_markup = markup)
            bot.send_message(message.chat.id, '4. Дві копії виписки про реєстрацію в БТІ або ДРРП.', reply_markup = markup)
            bot.send_message(message.chat.id, '5. Засвідчена нотаріально копія державного акту на право приватної власності на землю (для присвоєння кадастрового номера на земельну ділянку, яка була приватизована у 1992-2003 р.)', reply_markup = markup)
           
            
           
          
            
            bot.send_message(message.chat.id, 'Необхідні документи', reply_markup = markup)


        elif message.text == 'Питання та відповіді:':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bot.send_message(message.chat.id, '1) чи є на Вашій ділянці будинок? Якщо будинку немає фізично, то найімовірніше потрібно робити проект відведення (див. 2 вид робіт). Але якщо є держакт чи «декретне» рішення – будинок та документи на нього необовязкові.', reply_markup = markup)
            bot.send_message(message.chat.id, '2) чи є документи на будинок та реєстрація права? Якщо будинок є, але немає документів на нього – потрібно робити проект відведення (через дозвіл депутатів). Якщо немає лише реєстрації – потрібно спочатку зареєструвати у ДРРП право власності на будинок.', reply_markup = markup)
            bot.send_message(message.chat.id, '3) скільки господарів у будинку, чи всі згодні оформляти? На половину чи інші частини будинку ми кадастровий номер не робимо. У такому разі для оформлення потрібні документи та згода всіх співвласників.', reply_markup = markup)
            bot.send_message(message.chat.id, '4) чи робилася колись приватизація на цю ділянку, чи є держакт чи «декретне» рішення про передачу землі у власність? Якщо є обовязково потрібні.', reply_markup = markup)
            bot.send_message(message.chat.id, '5) чи немає суперечок із сусідами? Якщо є, це часто розтягує процес. Після зйомки стає зрозумілим. Часто через це зростає вартість робіт. Іноді є «накладки» - неправильно оформлена приватизація у сусідів, коли їхня ділянка «налазить» на Вашу (за документами). Тоді треба спершу виправити документи сусідів, а потім робити свої. Платить за це зацікавлена сторона.', reply_markup = markup)
            bot.send_message(message.chat.id, '6) скільки у Вас соток землі? можна оформлювати не більше 10 соток у місті, не більше 15 соток у селищах та 25ти у селах. Якщо у Вас ділянка більша – решту землі можна оформити лише після дозволу депутатів через проект відведення.', reply_markup = markup)
            bot.send_message(message.chat.id, '7) коли проводяться заміри? Зазвичай по четвергах з 8ми і до темноти, але час краще уточнити (вам обов’язково передзвонять)', reply_markup = markup)
            bot.send_message(message.chat.id, '8) чи можна якось надіслати документи? Потрібно!', reply_markup = markup)
            bot.send_message(message.chat.id, "(на вайбер чи телеграм) [+380950001178](tel:+380950001178),", parse_mode='Markdown')
            bot.send_message(message.chat.id, "а краще сканований у кольорі варіант на електронну пошту 0950001178@ukr.net ", parse_mode='Markdown')

           
            
    
            bot.send_message(message.chat.id, 'Питання та відповіді:', reply_markup = markup)
        

        elif message.text == '2. Проект відведення':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Процедура послуги:')
            item2 = types.KeyboardButton('Необхідні документи:')
            item3 = types.KeyboardButton('Питання та відповіді')
            item4 = types.KeyboardButton('Вартість робіт та терміни:')
            back = types.KeyboardButton('Назад!')
            bot.send_message(message.chat.id, '2. ПРОЕКТ ЗЕМЛЕУСТРОЮ ЩОДО ВІДВЕДЕННЯ ЗЕМЕЛЬНОЇ ДІЛЯНКИ', parse_mode='Markdown')
            bot.send_message(message.chat.id, 'Робиться на всі ділянки, на яких є будь-які будівлі, крім житлових будинків (дачний або садовий будиночок, гараж та інші,)', parse_mode='Markdown')
            bot.send_message(message.chat.id, 'а також на чисту землю під дачне будівництво, садівництво, городництво (ОСГ), під забудову тощо. АЛЕ: на період дії воєнного стану не розробляється!)', parse_mode='Markdown')
            
           
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, '2. Проект відведення', reply_markup = markup)


        elif message.text == 'ІНШІ ВИДИ РОБІТ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('4. Виправ. помилок')
            item2 = types.KeyboardButton('5. Сервітут частини')
            item3 = types.KeyboardButton('6. Зміна цільового')
            item4 = types.KeyboardButton('7. Геодезія, топографія')
            item5 = types.KeyboardButton('8. Винос в натуру')
            
            
            back = types.KeyboardButton('Назад!')
           
           
            markup.add(back, item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, 'ІНШІ ВИДИ РОБІТ', reply_markup = markup)


        elif message.text == "3. ТЕХНІЧНА ДОКУМЕНТАЦІЯ ДЛЯ ПОДІЛУ АБО ОБ'ЄДНАННЯ ДІЛЯНОК":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Процедура послуги!')
            item2 = types.KeyboardButton('Необхідні документи!')
            item3 = types.KeyboardButton('Питання та відповіді!')
            item4 = types.KeyboardButton('Вартість робіт та терміни!')
            back = types.KeyboardButton('Назад!')
         
            bot.send_message(message.chat.id, "Робиться на ділянки, які вже приватизовані (із наданим кадастровим номером).Коли є дві (або більше) поряд розташованих ділянок, які мають однакове цільове призначення, і одного власника можна ці ділянки об'єднати.)", parse_mode='Markdown')
            bot.send_message(message.chat.id, 'Розділити ділянку теоретично можна на будь-яку кількість ділянок, проте потрібно враховувати архітектурні норми (якщо передбачається будівництво)', parse_mode='Markdown')
           
            markup.add(back, item1, item2, item3, item4)

            bot.send_message(message.chat.id, "3. ТЕХНІЧНА ДОКУМЕНТАЦІЯ ДЛЯ ПОДІЛУ АБО ОБ'ЄДНАННЯ ДІЛЯНОК", reply_markup = markup)



        elif message.text == "Вартість робіт та терміни!":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        
            back = types.KeyboardButton('Назад!')
         
            bot.send_message(message.chat.id, "Стандартна вартість – від 6 тис. грн. Після вивчення документів та зйомки уточнюється вартість кожного конкретного випадку. Аванс (це вартість вимірів) – 2тис. грн. Розрахунок безготівковий (на банківський рахунок чи картку).", parse_mode='Markdown')
            bot.send_message(message.chat.id, 'У загальну вартість не входить реєстрація – 1200 грн + 600 грн за кожну нову ділянку (зазвичай люди це самі роблять, це просто, дешевше та не потрібна тоді довіреність) та винесення меж ділянки в натуру – від 800грн (це потрібно якщо немає парканів).Розрахунковий термін одержання кадастрового номера – 3 місяці. Договір складається на 6 місяців, тому що можуть бути затримки під час підписання меж із сусідами.', parse_mode='Markdown')
           
         

            bot.send_message(message.chat.id, "Вартість робіт та терміни!", reply_markup = markup)


        elif message.text == "4. Виправ. помилок":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
            bot.send_message(message.chat.id, "4. ТЕХНІЧНА ДОКУМЕНТАЦІЯ ЩОДО ВИПРАВЛЕННЯ ВІДОМОСТЕЙ У КАДАСТРІ", reply_markup = markup)
            bot.send_message(message.chat.id, "Робиться для внесення змін щодо приватизованої ділянки. В основному потрібна, щоб виправити координати ділянки (місце розташування) або змінити її конфігурацію.", parse_mode='Markdown')
            bot.send_message(message.chat.id, 'практично ідентична тій, як і щодо присвоєння кадастрового номера (див. 1й вид робіт). Спочатку необхідно виконати заміри та винесення ділянки в натуру.Розглядаємо окремо кожен випадок.', parse_mode='Markdown')  
            bot.send_message(message.chat.id, "4. Виправ. помилок", reply_markup = markup)

        elif message.text == "5. Сервітут частини":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bot.send_message(message.chat.id, "5. ТЕХНІЧНА ДОКУМЕНТАЦІЯ ЩОДО ВСТАНОВЛЕННЯ СЕРВІТУТУ НА ЧАСТИНУ ДІЛЯНКИ", reply_markup = markup)
         
            bot.send_message(message.chat.id, "Робиться найчастіше для розміщення тимчасових споруд на чужій землі (під кіоски), або для інших цілей встановлення сервітутів – прохід чи проїзд через сусідню ділянку, прокладання інженерних комунікацій тощо.", parse_mode='Markdown')
            bot.send_message(message.chat.id, 'Потрібна згода власника дільники, якщо це комунальна власність – дозвіл місцевої ради.Розглядаємо окремо кожен випадок.', parse_mode='Markdown')
          
           
            bot.send_message(message.chat.id, "5. Сервітут частини", reply_markup = markup)


        elif message.text == "6. Зміна цільового":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bot.send_message(message.chat.id, "6. ПРОЕКТ ЗЕМЛЕУСТРОЮ ЩОДО ЗМІНИ ЦІЛЬОВОГО ПРИЗНАЧЕННЯ ДІЛЯНКИ", reply_markup = markup)
         
            bot.send_message(message.chat.id, "Зазвичай робиться на вже приватизовану ділянку. Процедура послуги! практично ідентична тій, що проект відведення нової ділянки (див. 2й вид робіт). Потрібно розуміти, чи передбачено містобудівною документацією таке використання землі, яке Ви плануєте. ", parse_mode='Markdown')
            bot.send_message(message.chat.id, 'Якщо ні, потрібно спочатку розробляти детальний план території. Ще треба знати, що існують так звані «втрати» за зміну призначення сільськогосподарських земель (своєрідний податок).Розглядаємо окремо кожен випадок.', parse_mode='Markdown')
          
            bot.send_message(message.chat.id, "6. Зміна цільового", reply_markup = markup)


        
        elif message.text == "7. Геодезія, топографія":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
            bot.send_message(message.chat.id, "7. ГЕОДЕЗИЧНА ЗЙОМКА", reply_markup = markup)
            bot.send_message(message.chat.id, "Під проведення газу, електрики, води, під будівництво чи ландшафтний дизайн.Надаємо комплекс геодезичних робіт без прив'язки до документів на землю.", parse_mode='Markdown')
            bot.send_message(message.chat.id, "Складаємо топографічні плани місцевості масштабу 1:500 (та інших) з рельєфом для будь-яких цілей без узгодження з підприємствами (власниками комунікацій).Розглядаємо окремо кожен випадок.", reply_markup = markup)
            
            
        
            bot.send_message(message.chat.id, "7. Геодезія, топографія", reply_markup = markup)


        elif message.text == "8. Винос в натуру":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
            bot.send_message(message.chat.id, "8. ВИНОС В НАТУРУ ЗЕМЕЛЬНОЇ ДІЛЯНКИ (розбивка на місцевості)", reply_markup = markup)
            bot.send_message(message.chat.id, "Робиться або після виконання всіх робіт та затвердження документації – у такому разі це коштує від 800грн (іноді більше якщо складна ділянка), - у договорі зазначено, що за це сплачується окремо. Або виконується як окрема робота.", parse_mode='Markdown')
            bot.send_message(message.chat.id, 'Тоді вартість від 1500 грн. і вище залежно від того, де знаходиться ділянка, ступеня забудови та кількості точок, які потрібно визначити на місцевості.Для цього потрібно спочатку знати кадастровий номер ділянки та надати документи на перевірку. Якщо ми беремося – виїзд заплануємо у день зйомки (по домовленості).', parse_mode='Markdown')
            bot.send_message(message.chat.id, 'Зазвичай необхідно лише фізично визначити кутові точки ділянки на місцевості. До речі кілки (наприклад арматуру) Ви повинні самі надати та встановити (забити, закопати, забетонувати). Якщо Вам також потрібні документи – «Акт встановлення меж» або плани – потрібно обговорювати окремо терміни та вартість.', parse_mode='Markdown')
            bot.send_message(message.chat.id, "8. Винос в натуру", reply_markup = markup)


        elif message.text == "Про нас":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
         
            bot.send_message(message.chat.id, "ГЕОДЕЗІЯ ТА КАДАСТР", parse_mode='Markdown')
            bot.send_message(message.chat.id, "Документи на землю, геодезичні роботи, землеустрій, кадастровий номер, проекти відведення, зміна призначення землі, поділ та об'єднання ділянок, винесення в натуру, виправлення у кадастрі на території Полтавського району Полтавської області, Луцького району Волинської області, Рівненського та Дубенського районів Рівненської області.", parse_mode='Markdown')
            bot.send_message(message.chat.id, 'ФОП БАГІН Михайло Леонідович', parse_mode='Markdown')
            bot.send_message(message.chat.id, "сертифікат інженера-землевпорядника №000649 від 03.01.2013 р., ", parse_mode='Markdown')
            bot.send_message(message.chat.id, 'сертифікат інженера-геодезиста №015067 від 02.06.2021 р.наявні дозволи СБУ на відповідні території для роботи у воєнний час.', parse_mode='Markdown')
            bot.send_message(message.chat.id, "(вайбер, вотсап, телеграм) [+380950001178](tel:+380950001178)", parse_mode='Markdown')
            bot.send_message(message.chat.id, "0950001178@ukr.net (електронна пошта)", parse_mode='Markdown')

           

            bot.send_message(message.chat.id, "Про нас", reply_markup = markup)

 
      

        elif message.text == "Реквізити для оплати:":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
         
            bot.send_message(message.chat.id, "Реквізити для оплати:", parse_mode='Markdown')
            bot.send_message(message.chat.id, "Отримувач: Фізична особа-підприємець Багін Михайло Леонідович, ід.№2960810498; рах. UA943515330000026003052315082, Харківське ГРУ АТ КБ «Приватбанк» або картковий рахунок 4246 0010 3015 8731 отримувач є платником єдиного податку (3 група)Платник: гр. (краще вказувати ПІБ на кого оформляється земля)", parse_mode='Markdown')
            bot.send_message(message.chat.id, " Призначення платежу: За проведення робіт із землеустрою по договору №__, від ___ р.ПДВ не передбачено", parse_mode='Markdown')

           
           

            bot.send_message(message.chat.id, "Реквізити для оплати:", reply_markup = markup)
        


        elif message.text == "Питання та відповіді!":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

            
            bot.send_message(message.chat.id, "1) у якому році була приватизація землі? Чи є кадастровий номер? Якщо приватизація була до 2003 року (червоний чи помаранчевий держакт), то спочатку потрібно внести до кадастру цю ділянку, а потім щось із нею робити.", parse_mode='Markdown')
            bot.send_message(message.chat.id, "2) чи внесено ділянку до кадастру? Потрібно перевірити, чи «світиться» Ваша ділянка на публічній кадастровій карті map.land.gov.ua", parse_mode='Markdown')
            bot.send_message(message.chat.id, "3) на скільки частин ділитиметься ділянка та в яких площах? Ці дані обов'язково потрібно вписати до нотаріальної заяви.", parse_mode='Markdown')
            bot.send_message(message.chat.id, '4) чи є будинок, будівлі на ділянці? Чи є документи на будівлі та реєстрація права? Скільки власників на будівлю, чи всі згодні оформляти? За наявності будівель необхідні документи на них. У такому разі потрібні документи та згода всіх співвласників.', parse_mode='Markdown')
            bot.send_message(message.chat.id, '5) чи ділитимуться будівлі? Часто хочуть зробити поділ землі співвласники (половинщики) будинку. Там складніша процедура з присвоєнням адреси та виділенням у «одиницю» цих частин. За згодою сторін землю поділимо.', parse_mode='Markdown')
            bot.send_message(message.chat.id, '6) чи немає суперечок із сусідами? Якщо є, це часто розтягує процес. Після зйомки стає зрозумілим. Часто через це зростає вартість робіт. Іноді є «накладки» - неправильно оформлена приватизація у сусідів, коли їхня ділянка «налазить» на Вашу (за документами). Тоді треба спершу виправити документи сусідів, а потім робити свої. Платить за це зацікавлена сторона.', parse_mode='Markdown')
            bot.send_message(message.chat.id, '7) коли проводяться заміри? Зазвичай по четвергах з 8ми і до темноти, але час краще уточнити (вам обов’язково передзвонять)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '8) чи можна якось надіслати документи? Потрібно!', reply_markup = markup)
            bot.send_message(message.chat.id, "(на вайбер чи телеграм) [+380950001178](tel:+380950001178),", parse_mode='Markdown')
            bot.send_message(message.chat.id, "а краще сканований у кольорі варіант на електронну пошту 0950001178@ukr.net ", parse_mode='Markdown') 
            bot.send_message(message.chat.id, "Питання та відповіді!", reply_markup = markup)




      



        elif message.text == "Необхідні документи!":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

            
            bot.send_message(message.chat.id, "1. Копія паспорта та ідентифікаційного коду.", parse_mode='Markdown')
            bot.send_message(message.chat.id, "2. Нотаріальна заява на поділ чи об'єднання ділянок (оригінал, зазначити нові площі)", parse_mode='Markdown')
            bot.send_message(message.chat.id, '3. Засвідчена нотаріально копія державного акту на право приватної власності на землю або іншого документа, що встановлює право на землю (купівлі-продажу, спадщини, дарування, рішення суду), та/або реєстрації землі в ДРРП.', parse_mode='Markdown')
            bot.send_message(message.chat.id, '4. Завірена нотаріально копія правовстановлюючого документа на будинок (купівлі-продажу, спадщини, дарування, рішення суду) – якщо є будівлі та документи на них.', parse_mode='Markdown')
            bot.send_message(message.chat.id, '5. Копія виписки про реєстрацію в БТІ або ДРРП - якщо є будівлі та документи на них.', parse_mode='Markdown')
            bot.send_message(message.chat.id, '6. Копія технічного паспорта на будинок чи будівлі (за наявності)', parse_mode='Markdown')
            
            
          
            bot.send_message(message.chat.id, "Необхідні документи!", reply_markup = markup)


        elif message.text == 'Процедура послуги!':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        
            bot.send_message(message.chat.id, "1) Нотаріальна заява на поділ чи об'єднання ділянок (Це завдання замовника!)", parse_mode='Markdown')
            bot.send_message(message.chat.id, '2) Вивчення документів (1 тиждень)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '3) Заміри ділянки (по домовленості) ', parse_mode='Markdown')
            bot.send_message(message.chat.id, '4) Обробка вимірювань (близько 2 тижнів)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '5) Укладання договору та підписання техзавдання', parse_mode='Markdown')
            bot.send_message(message.chat.id, '6) Погодження меж ділянки із сусідами та у раді (Це завдання замовника!). Потрібно розуміти чи є суперечки з сусідами про межу або, можливо, сусіди відсутні', parse_mode='Markdown')
            bot.send_message(message.chat.id, '7) Складання техдокументації (близько 2х тижнів)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '8) Подача до кадастру (14 робочих днів, іноді двічі)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '9) Підготовка екземпляра документів (1 тиждень)', parse_mode='Markdown')
            bot.send_message(message.chat.id, 'Далі можуть бути такі завдання: ', parse_mode='Markdown')
            bot.send_message(message.chat.id, '10) Присвоєння адрес у виконкомі (Це завдання замовника!)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '11) Реєстрація в юстиції – кожна нова ділянка окремо (10 днів, якщо робимо ми – потрібна нотаріальна довіреність!)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '12) Винесення меж ділянки в натуру (за потребою та домовленістю) - за домовленістю можемо зробити за окрему плату', parse_mode='Markdown')
          
            
            
          
            

         

        elif message.text == 'Питання та відповіді':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bot.send_message(message.chat.id, '1) чи вже є дозвіл місцевої ради на проект? Якщо ні – спочатку потрібно звернутись до місцевої ради із заявою. Якщо незрозуміла площа ділянки можемо зробити заміри для цього.', reply_markup = markup)
            bot.send_message(message.chat.id, '2) скільки соток землі та яке цільове призначення? Якщо земля оформляється у межах безкоштовної приватизації – подивіться ст.118 та 121 Земельного кодексу. ', reply_markup = markup)
            bot.send_message(message.chat.id, "3) Чи є у Вас розуміння, що відділ архітектури «пропустить» цей проект? Зараз обов'язково потрібно розуміти, чи відповідає генплану Ваша ділянка (проектна). Якщо Ви не знаєте цього, краще спочатку зробити виміри і подати у відділ архітектури, щоб це дізнатися. У будь-якому випадку (крім оформлення городу) для розробки проекту потрібна виписка з містобудівної документації.", reply_markup = markup)
            bot.send_message(message.chat.id, '4) чи є будинок, будівлі на ділянці? Чи є документи на будови та реєстрація права? скільки господарів на будову, чи всі згодні оформляти? За наявності будівель необхідні документи на них. На половину чи інші частини будівель ми проект відведення не робимо. У такому разі потрібні документи та згода всіх співвласників.', reply_markup = markup)
            bot.send_message(message.chat.id, "5) чи є поруч інша ділянка, яка вам належить? Якщо так, то треба розуміти, які документи є на таку ділянку (кадастровий номер, техпаспорт на будинок). Бажано пред'явити ці документи розробнику. Часто за проектом оформляються надлишки, які розташовані біля будинку.", reply_markup = markup)
            bot.send_message(message.chat.id, '6) чи немає суперечок із сусідами? Якщо є, це часто розтягує процес. Після зйомки стає зрозумілим. Часто через це зростає вартість робіт. Іноді є «накладки» - неправильно оформлена приватизація у сусідів, коли їхня ділянка «налазить» на Вашу (за документами). Тоді треба спершу виправити документи сусідів, а потім робити свої. Платить за це зацікавлена сторона.', reply_markup = markup)
            bot.send_message(message.chat.id, '7) коли проводяться заміри? Зазвичай по четвергах з 8ми і до темноти, але час краще уточнити (вам обов’язково передзвонять)', reply_markup = markup)
            bot.send_message(message.chat.id, '8) чи можна якось надіслати документи? Потрібно!', reply_markup = markup)
            bot.send_message(message.chat.id, "(на вайбер чи телеграм) [+380950001178](tel:+380950001178),", parse_mode='Markdown')
            bot.send_message(message.chat.id, "а краще сканований у кольорі варіант на електронну пошту 0950001178@ukr.net ", parse_mode='Markdown')

            
            
        
            bot.send_message(message.chat.id, 'Питання та відповіді', reply_markup = markup)


        elif message.text == 'Вартість робіт та терміни:':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bot.send_message(message.chat.id, 'Стандартна вартість – від 7 до 10 тис. грн. Після вивчення документів та зйомки уточнюється вартість кожного конкретного випадку. Аванс (це вартість вимірів) – 2тис. грн. Розрахунок безготівковий (на банківський рахунок чи картку).', reply_markup = markup)
            bot.send_message(message.chat.id, ' У загальну вартість не входить реєстрація – 1200 грн (зазвичай люди це самі роблять, це просто, дешевше та не потрібна тоді довіреність) та винесення ділянки в натуру – від 800 грн (це потрібно якщо немає парканів).Розрахунковий термін одержання кадастрового номера – 4 місяці. Договір складається на 6 місяців, тому що можуть бути затримки під час підписання меж із сусідами.', reply_markup = markup)
            
            
            bot.send_message(message.chat.id, 'Вартість робіт та терміни:', reply_markup = markup)

        elif message.text == 'Процедура послуги:':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bot.send_message(message.chat.id, '1) Отримання дозволу у місцевій раді (Це завдання замовника!)', reply_markup = markup)
            bot.send_message(message.chat.id, '2) Вивчення документів (1 тиждень)', reply_markup = markup)
            bot.send_message(message.chat.id, '3) Заміри ділянки (по домовленості)', reply_markup = markup)
            bot.send_message(message.chat.id, '4) Обробка вимірювань (близько 2 тижнів)', reply_markup = markup)
            bot.send_message(message.chat.id, '5) Укладання договору та підписання техзавдання', reply_markup = markup)
            bot.send_message(message.chat.id, '6) Погодження меж ділянки із сусідами та у раді (Це завдання замовника!). Потрібно розуміти чи є суперечки з сусідами про межу або, можливо, сусіди відсутні', reply_markup = markup)
            bot.send_message(message.chat.id, '7) Розроблення проекту (близько 2х тижнів)', reply_markup = markup)
            bot.send_message(message.chat.id, '8) Отримання довідок та виписки з містобудівної документації (2-3 тижні)', reply_markup = markup)
            bot.send_message(message.chat.id, '9) Подача до кадастру (14 робочих днів, іноді двічі)', reply_markup = markup)
            bot.send_message(message.chat.id, '10) Підготовка 2-х примірників документів (1 тиждень)', reply_markup = markup)

            bot.send_message(message.chat.id, 'Далі можуть бути такі завдання:', reply_markup = markup)
            bot.send_message(message.chat.id, '11) Подання заяви до ради на приватизацію (Це завдання замовника!)', reply_markup = markup)
            bot.send_message(message.chat.id, '12) Реєстрація в юстиції* (10 днів, якщо робимо ми – потрібна нотаріальна довіреність!)', reply_markup = markup)
            bot.send_message(message.chat.id, '13) Винесення меж земельної ділянки в натуру* (за потребою та домовленістю)* - за домовленістю можемо зробити за окрему плату', reply_markup = markup)
            
        
        
            
            bot.send_message(message.chat.id, 'Процедура послуги:', reply_markup = markup)


        elif message.text == 'Необхідні документи:':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bot.send_message(message.chat.id, '1. Дві копії паспорта та ідентифікаційного коду.', reply_markup = markup)
            bot.send_message(message.chat.id, '2. Рішення місцевої ради «Дозвіл» на розробку проекту відведення землі - оригінал (краще два екз.)', reply_markup = markup)
            bot.send_message(message.chat.id, '3. Схема «бажаного розташування» ділянки, а щодо садових ділянок – генплан садового товариства.', reply_markup = markup)
            bot.send_message(message.chat.id, '4. Дві копії технічного паспорта на будинок чи будівлю (якщо вони є).', reply_markup = markup)
            bot.send_message(message.chat.id, '5. Одна проста та одна завірена нотаріально копія правовстановлюючого документа на будинок (купівлі-продажу, спадщини, дарування, рішення суду) - якщо є будівлі та документи на них.', reply_markup = markup)
            bot.send_message(message.chat.id, '6. Дві копії виписки про реєстрацію в БТІ або ДРРП - якщо є будівлі та документи на них.', reply_markup = markup)
           
           
            
            bot.send_message(message.chat.id, 'Необхідні документи:', reply_markup = markup)




        
        

        
        


        elif message.text == 'Назад!':         
             markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
             item1 = types.KeyboardButton('1. Кадастр. номер')
             item2 = types.KeyboardButton('2. Проект відведення')
             item3 = types.KeyboardButton("3. Поділ, об'єднання")
             item4 = types.KeyboardButton('ІНШІ ВИДИ РОБІТ')
             item5 = types.KeyboardButton('Про нас')
             item6 = types.KeyboardButton('Реквізити для оплати:')

           
                
             markup.add(item1, item2, item3, item4, item5, item6)
             bot.send_message(message.chat.id, 'Назад!', reply_markup = markup)


        elif message.text == "3. Поділ, об'єднання":         
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Процедура послуги!')
            item2 = types.KeyboardButton('Необхідні документи!')
            item3 = types.KeyboardButton("Питання та відповіді!")
            item4 = types.KeyboardButton('Вартість робіт та терміни!')
            back = types.KeyboardButton('Назад!')
             
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, "3. ТЕХНІЧНА ДОКУМЕНТАЦІЯ ДЛЯ ПОДІЛУ АБО ОБ'ЄДНАННЯ ДІЛЯНОК", reply_markup = markup)
            bot.send_message(message.chat.id, "Робиться на ділянки, які вже приватизовані (із наданим кадастровим номером).Коли є дві (або більше) поряд розташованих ділянок, які мають однакове цільове призначення, і одного власника можна ці ділянки об'єднати.", reply_markup = markup)
            bot.send_message(message.chat.id, "Розділити ділянку теоретично можна на будь-яку кількість ділянок, проте потрібно враховувати архітектурні норми (якщо передбачається будівництво)", reply_markup = markup)
            bot.send_message(message.chat.id, "3. Поділ, об'єднання", reply_markup = markup)
            back = types.KeyboardButton('Назад!')


        else:    bot.send_message(message.chat.id, "Немає такої відповіді! Якщо ви не знайшли відповідь на своє питання, то звертайтесь по цьому номеру: +380950001178")
        

bot.polling(none_stop = True)



