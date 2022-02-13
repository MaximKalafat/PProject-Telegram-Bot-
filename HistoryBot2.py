from requests.api import get
import telebot
import re           
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from telebot import types

TOKEN = '1839643716:AAG_osM6yZYYKcKhq46YTPEKqnIoHT4sE28'

bot = telebot.TeleBot(TOKEN);


@bot.message_handler(commands = ['help'])
def menu_bot(message):
    bot.send_message(message.from_user.id, 'Привет! Чтобы использовать бота, просто напиши год, который тебя интересует.')


@bot.message_handler(commands=['about_bot'])
def about_bot(message):
    bot.send_message(message.from_user.id, 'Я - бот, который поможет тебе в познании истории России. Спасибо, что с нами!')
@bot.message_handler(commands=['about_creator'])
def about_me(message):
    bot.send_message(message.from_user.id, 'Привет! Здесь написано про создателя этого бота. Он - обычный парень, который решил немного помочь людям, которым интересна история России, либо людям, которые сдают историю. Он от всей души говорит вам спасибо за время проведенное с ботом. Если хотите с ним связаться, либо высказать свое мнение про бота, то вот его контакты: \nVK: https://vk.com/maximkalafat\nPHONE NUMBER: +79162854279') 


@bot.message_handler(commands=['start'])
def button_start(message):
    bot.send_message(message.from_user.id, 'Привет! Я - бот, который знает всех правителей, войны и важные события Руси с 862.')

currentYear = datetime.now().year
@bot.message_handler(content_types=['text'])
def get_msg(message):
    god = 0
    flag = 0
    # md = [0, str(0), str(0), str(0), str(0), str(0), str(0)]
    # while god == 0:
    try:
        god = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, 'Пожалуйста, введите только цифры!')
        flag = 1
    
    if flag != 1:
        if god < 862:
            bot.send_message(message.from_user.id, 'Дата основания Руси 862 год, мне известна информация только с этой даты!')

    
        # elif god > 1917 and god <= currentYear:
        #      bot.send_message(message.from_user.id, 'Правители после 1917 года - слишком просто.')
        elif god > currentYear:
             bot.send_message(message.from_user.id, 'Вы хотите узнать как долго Путин будет президентом? Я вам не скажу, это - секрет!')    
        else:
            if god <= 1917:
                get_history_inf(god)
                 #  сообщение о правителях
                bot.send_message(message.from_user.id, 'В ' + str(god) + ' году правителем Руси был' + praviteli.text + '\nГоды правления ' + god_pravlenia)
                get_war_inf(god)
                get_sobitia(god)
            else:
               get_war_inf(god)
               get_sobitia (god)
           
            # сообщение о войнах
            if md[0] == 0:
                bot.send_message(message.from_user.id, 'Война в этом году: ' + str(md[2]) + '\nДлительность: ' + str(md[1]) + '\nИтоги: ' + str(md[3]))
            if md[0] == 1:
                bot.send_message(message.from_user.id,'В этом году было две войны: ' + '\nПервая война: ' + str(md[2]) + '\nДлительность: ' + str(md[1]) + '\nИтоги: ' + str(md[3]) + '\nВторая война: ' + str(md[5]) + '\nДлительность: ' + str(md[4]) + '\nИтоги: ' + str(md[6]))
            if md[0] == 2:
                bot.send_message(message.from_user.id, 'В этом году не было войны. \nБлижайшие война: ' + str(md[2]) + '\nДлительность: ' + str(md[1]) + '\nИтоги: ' + str(md[3]) + '\nВторая ближайшая война: ' + str(md[5]) + '\nДлительность: ' + str(md[4]) + '\nИтоги: ' + str(md[6]))
            if md[0] == 4:
                bot.send_message(message.from_user.id, 'В этом году не было войны. Ближайшая война: ' + str(md[2]) + '\nДлительность: ' + str(md[1]) + '\nИтоги: ' + str(md[3]))
            # сообщения о ключевых событиях
            if iskl == 0:
                # if flag3 == 0:
                if flag3 == 1:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]))
                if flag3 == 2:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) )
                if flag3 == 3:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]))
                if flag3 == 4:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]))
                if flag3 == 5:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]))
                if flag3 == 6:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]))
                if flag3 == 7:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]))
                if flag3 == 8:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]) + '\n' + str(cl_dev[7]))
                if flag3 == 9:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]) + '\n' + str(cl_dev[7]) + '\n' + str(cl_dev[8]))
                if flag3 == 10:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]) + '\n' + str(cl_dev[7]) + '\n' + str(cl_dev[8]) + '\n' + str(cl_dev[9]))
                if flag3 == 11:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]) + '\n' + str(cl_dev[7]) + '\n' + str(cl_dev[8]) + '\n' + str(cl_dev[9]) + '\n' + str(cl_dev[10]))
                if flag3 == 12:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]) + '\n' + str(cl_dev[7]) + '\n' + str(cl_dev[8]) + '\n' + str(cl_dev[9]) + '\n' + str(cl_dev[10]) + '\n' + str(cl_dev[11]))
            if iskl == 1:
                bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev_iskl))
            if iskl == 2:
                bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev_iskl))
                if flag3 == 1:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]))
                if flag3 == 2:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) )
                if flag3 == 3:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]))
                if flag3 == 4:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]))
                if flag3 == 5:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]))
                if flag3 == 6:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]))
                if flag3 == 7:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]))
                if flag3 == 8:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]) + '\n' + str(cl_dev[7]))
                if flag3 == 9:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]) + '\n' + str(cl_dev[7]) + '\n' + str(cl_dev[8]))
                if flag3 == 10:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]) + '\n' + str(cl_dev[7]) + '\n' + str(cl_dev[8]) + '\n' + str(cl_dev[9]))
                if flag3 == 11:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]) + '\n' + str(cl_dev[7]) + '\n' + str(cl_dev[8]) + '\n' + str(cl_dev[9]) + '\n' + str(cl_dev[10]))
                if flag3 == 12:
                    bot.send_message(message.from_user.id, 'Ключевые события: \n' + str(cl_dev[0]) + '\n' + str(cl_dev[1]) + '\n' + str(cl_dev[2]) + '\n' + str(cl_dev[3]) + '\n' + str(cl_dev[4]) + '\n' + str(cl_dev[5]) + '\n' + str(cl_dev[6]) + '\n' + str(cl_dev[7]) + '\n' + str(cl_dev[8]) + '\n' + str(cl_dev[9]) + '\n' + str(cl_dev[10]) + '\n' + str(cl_dev[11]))
                

                



def corection_data(data):
    currentYear =  str(datetime.now().year)
    global lst
    data = data.replace('-', ' ')
    data = data.replace('.', ' ')
    data = data.replace('Между', ' ')
    data = data.replace('по', ' ')
    data = data.replace('и', ' ')
    data = data.replace('н в', currentYear)
    data = data.replace('вв', ' ')
    data = data.replace('XIII', '1300')
    data = data.replace('XI', '1001')
    data = data.replace('–', ' ')
    lst = data.split()


def pred_voina(k):
    if k > 864:  
        if k >= 1043 and k <= 1994:
            md[4] = td2_pred
            md[5] = nazvanie_voin_pred2
            md[6] = itog_voin_pred2
        else:
            md[4] = td_pred
            md[5] = nazvanie_voin_pred
            md[6] = itog_voin_pred
    else:
        md[0] = 4 
# В этой ^ функции нужно прописать условие, когда будущей войны нет, еще не знаем о текущем состоянии войны, тоесть показать только прошедшую войну.
# Под нее зарезервировано md[0] = 3




def get_war_inf(i): # функция парсинга сайта с датами о войне
    global md
    global td2_pred
    global td_pred
    global nazvanie_voin_pred
    global nazvanie_voin_pred2
    global itog_voin_pred
    global itog_voin_pred2
    md = [0, 0, 0, 0, 0, 0, 0]
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    url = 'https://histerl.ru/vse_mareriali/tablici/voini_v_kotorix_uchastvovala_rossia.htm'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    spisok_strok2 = soup.find_all('tr')                                                   # создаем список из строк со всей страницы HTML
    flag2 = 0
            
            
    for spisok2 in spisok_strok2:                                                         # перебираем каждую строку и работаем с текущей
        
 

        td = spisok2.find('td', {'width': '91'})                                          # ищем ячейку шириной 91
        td2 = spisok2.find('td', {'width': '92'})                                         # ищем ячейку шириной 92
    

        if td == None and td2 == None:
            continue                                                                      # игнорируем строки страницы, где нет ячеек шириной 91 и 92
        else:
            if td == None:                                                                # работаем с td2 ячейки шириной 92, потому что ячеек шириной 91 в этой строке нет
                nazvanie_voin2 = spisok2.find('td', {'width': '161'})                     # находим в текущей строке ячейку шириной 161 и берем от туда название войны
                itog_voin2 = spisok2.find('td', {'width': '215'})                         # находим в текущей строке ячейку шириной 215 и берем от туда итоги войны
                corection_data(td2.text)                                                  # вызываем функцию, которая обработает текстовое значение в числа и разбивает период на начало и конец
                if len(lst) == 2:                                                         # если дата войны имеет 2 значения (начало и конец)
                    if int(lst[0]) <= i and int(lst[1]) >= i:
                        # print(td2.text, nazvanie_voin2.text, ' ', itog_voin2.text)
                        
                        if flag2 == 1:
                            md[0] = 1
                            md[4] = td2.text
                            md[5] = nazvanie_voin2.text
                            md[6] = itog_voin2.text
                            break
                        else:
                            md = [0, td2.text, nazvanie_voin2.text, itog_voin2.text, 0, 0, 0]
                        flag2 = 1
                    else:
                        if flag2 == 0:
                            if i < int(lst[0]):
                                # print('В этот год войны не было. Ближайшая к этой дате война: ', td2.text, nazvanie_voin2.text, ' ', itog_voin2.text)
                                md[0] = 2
                                md[1] = td2.text
                                md[2] = nazvanie_voin2.text
                                md[3] = itog_voin2.text
                                pred_voina(i)
                                if flag2 == 1:
                                    break
                                flag2 = 1
                else:
                    if int(lst[0]) == i:
                        # print(td2.text, nazvanie_voin2.text, ' ', itog_voin2.text)
                        if flag2 == 1:                                                        # первая запись уже была, записываем вторую совпавшую дату войны
                            md[0] = 1                                                         # комбинация, когда в году две войны
                            md[4] = td2.text
                            md[5] = nazvanie_voin2.text
                            md[6] = itog_voin2.text
                            break                                                             # нашли 2 записи и выходим из цикла, чтобы не тратить ресурсы
                        else:
                            md = [0, td2.text, nazvanie_voin2.text, itog_voin2.text, 0, 0, 0]
                        flag2 = 1
                    else:
                        if flag2 == 0:
                            if i < int(lst[0]):
                                # print('В этот год войны не было. Ближайшая к этой дате война: ', td2.text, nazvanie_voin2.text, ' ', itog_voin2.text)
                                md[0] = 2
                                md[1] = td2.text
                                md[2] = nazvanie_voin2.text
                                md[3] = itog_voin2.text
                                pred_voina(i)
                                if flag2 == 1:
                                    break
                                flag2 = 1
                td2_pred = td2.text
                nazvanie_voin_pred2 = nazvanie_voin2.text
                itog_voin_pred2 = itog_voin2.text


            else:
                nazvanie_voin = spisok2.find('td', {'width': '160'})
                itog_voin = spisok2.find('td', {'width': '220'})
                if nazvanie_voin == None: 
                    nazvanie_voin = spisok2.find('td', {'width': '161'})
                    itog_voin = spisok2.find('td', {'width': '215'})
                
                corection_data(td.text)
                if len(lst) == 2:
                    if int(lst[0]) <= i and int(lst[1]) >= i:
                        # print(td.text, nazvanie_voin.text, ' ', itog_voin.text)
                        if flag2 == 1:
                            md[0] = 1
                            md[4] = td.text
                            md[5] = nazvanie_voin.text
                            md[6] = itog_voin.text
                            break
                        else:
                            md = [0, td.text, nazvanie_voin.text, itog_voin.text, 0, 0, 0]

                        flag2 = 1
                    else:
                        if flag2 == 0:
                            if i < int(lst[0]):
                                # print('В этот год войны не было. Ближайшая к этой дате война: ', td.text, nazvanie_voin.text, ' ', itog_voin.text)
                                md[0] = 2
                                md[1] = td.text
                                md[2] = nazvanie_voin.text
                                md[3] = itog_voin.text
                                pred_voina(i)
                                if flag2 == 1:
                                    break
                                flag2 = 1
                else:
                    if int(lst[0]) == i:
                        # print(td.text, nazvanie_voin.text, ' ', itog_voin.text)
                        if flag2 == 1:
                            md[0] = 1
                            md[4] = td.text
                            md[5] = nazvanie_voin.text
                            md[6] = itog_voin.text
                            break
                        else:
                            md = [0, td.text, nazvanie_voin.text, itog_voin.text, 0, 0, 0]
                        flag2 = 1
                    else:
                        if flag2 == 0:
                            if i < int(lst[0]):
                                # print('В этот год войны не было. Ближайшая к этой дате война: ', td.text, nazvanie_voin.text, ' ', itog_voin.text)
                                md[0] = 2
                                md[1] = td.text
                                md[2] = nazvanie_voin.text
                                md[3] = itog_voin.text
                                pred_voina(i)
                                if flag2 == 1:
                                    break
                                flag2 = 1
                td_pred = td.text
                itog_voin_pred = itog_voin.text
                nazvanie_voin_pred = nazvanie_voin.text



def get_sobitia(data):
    global cl_dev_iskl
    global cl_dev
    global iskl
    global flag3
    cl_dev = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    flag3 = 0
    iskl = 0
    if data == 941 or data == 944:
        cl_dev_iskl = '941, 944 – походы Игоря на Константинополь, договоры Руси с Византией'
        iskl = 1
        return
    if data == 1682 or data == 1689 or data == 1698:
        cl_dev_iskl = '1682, 1689, 1698 — восстания стрельцов'
        iskl = 1
        return
    if data == 1772 or data == 1793 or data == 1795:
        cl_dev_iskl = '1772, 1793, 1795 – Разделы Речи Посполитой'
        iskl = 1
        return
    if data >= 1001 and data <= 1100:
        cl_dev_iskl = 'XI в. – Правда Русская (Краткая редакция)'
        iskl = 2
    if data >= 1101 and data <= 1200:
        cl_dev_iskl = 'Начало XII в. – «Повесть временных лет»\nXII в. – Правда Русская (Пространная редакция)'
        iskl = 2

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    url = 'http://esa.school5-kstovo.edusite.ru/p25aa1.html'
    r = requests.get(url=url, headers=headers)
    r.encoding='cp1251'
    soup = BeautifulSoup(r.text, 'lxml')
    spisok_strok = soup.find_all('p')

    for spisok in spisok_strok:
        if spisok == None:
            continue
        else:
            td_developments = spisok.find('span')
            # developments = td_developments.find('span')
            if td_developments == None:
                continue
            
            # print (re.findall('\d+', td_developments.text))

            p = re.findall('\d+', td_developments.text)
            # print(td_developments.text

            if len(p) != 0:
                # print(p)
                i = 0
                while i < len(p):
                    if int(p[i]) < 800:
                        del p[i]
                    else:
                        i += 1
                if int(len(p)) == 1:
                    if int(p[0]) == data:
                        if flag3 == 0:
                            cl_dev[0] = td_developments.text
                            flag3 = 1
                        elif flag3 == 1:
                            cl_dev[1] = td_developments.text
                            
                        elif flag3 == 2:
                            cl_dev[2] = td_developments.text
                            flag3 = 3
                            
                        elif flag3 == 3:
                            cl_dev[3] = td_developments.text
                            flag3 = 4
                            
                        elif flag3 == 4:
                            cl_dev[4] = td_developments.text
                            flag3 = 5
                            
                        elif flag3 == 5:
                            cl_dev[5] = td_developments.text
                            flag3 = 6
                        
                        elif flag3 == 6:
                            cl_dev[6] = td_developments.text
                            flag3 = 7
                            
                        elif flag3 == 7:
                            cl_dev[7] = td_developments.text
                            flag3 = 8
                        elif flag3 == 8:
                            cl_dev[8] = td_developments.text
                            flag3 = 9
                        elif flag3 == 9:
                            cl_dev[9] = td_developments.text
                            flag3 = 10
                        elif flag3 == 10:
                            cl_dev[10] = td_developments.text
                            flag3 = 11
                        elif flag3 == 11:
                            cl_dev[11] = td_developments.text
                            flag3 = 12
                if int(len(p)) == 2:
                    if data >= int(p[0]) and data <= int(p[1]):
                        if flag3 == 0:
                            cl_dev[0] = td_developments.text
                            flag3 = 1
                            
                        elif flag3 == 1:
                            cl_dev[1] = td_developments.text
                            flag3 = 2
                            
                        elif flag3 == 2:
                            cl_dev[2] = td_developments.text
                            flag3 = 3
                            
                        elif flag3 == 3:
                            cl_dev[3] = td_developments.text
                            flag3 = 4
                            
                        elif flag3 == 4:
                            cl_dev[4] = td_developments.text
                            flag3 = 5
                            
                        elif flag3 == 5:
                            cl_dev[5] = td_developments.text
                            flag3 = 6
                        
                        elif flag3 == 6:
                            cl_dev[6] = td_developments.text
                            flag3 = 7
                            
                        elif flag3 == 7:
                            cl_dev[7] = td_developments.text
                            flag3 = 8
                        elif flag3 == 8:
                            cl_dev[8] = td_developments.text
                            flag3 = 9
                        elif flag3 == 9:
                            cl_dev[9] = td_developments.text
                            flag3 = 10
                        elif flag3 == 10:
                            cl_dev[10] = td_developments.text
                            flag3 = 11
                        elif flag3 ==11:
                            cl_dev[11]=td_developments.text
                            flag3 =12
                if int(len(p)) == 3:
                    continue
                if int(len(p)) == 4:
                    continue


                
# if iskl == 0:
#     print(cl_dev)
# if iskl == 1:
#     print(cl_dev_iskl)
# if iskl == 2:
#     print(cl_dev_iskl)
#     print(cl_dev)







def get_history_inf(chislo):
    headers = {
       "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    url = "http://www.spsl.nsc.ru/history/descr/main_p.htm"
    r = requests.get(url=url, headers=headers)
    r.encoding='cp1251'
    global praviteli
    global god_pravlenia
    soup = BeautifulSoup(r.text, "lxml")
    spisok_strok = soup.find_all('tr', {'align': 'LEFT'})


    for spisok in spisok_strok:
        td = spisok.find('td', {'width': '20%'})
        if td == None:
            continue
        else:
            data = td.find('b')
            data1 = [int(n) for n in data.text.split('-')]
            if data1[0] <= chislo and data1[1] >= chislo:
                praviteli = spisok.find("a")
                god_pravlenia = data.text
                # print(praviteli.text)



bot.polling(none_stop=True, interval = 0)