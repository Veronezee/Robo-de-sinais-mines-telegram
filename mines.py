from datetime import datetime, timedelta
import random
import telebot
import time

chat_id = "SEU CHAT ID"
user_id = "SEU USER ID"

LINK_SITE = '[JOGUE AGORA](https://www.link.com)'

bot = telebot.TeleBot(token=chat_id)


while True:
    try:
        resultados = range(1, 26)
        aposta = random.sample(resultados, 5)
        dc = {

            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: '11',
            12: '12',
            13: '13',
            14: '14',
            15: '15',
            16: '16',
            17: '17',
            18: '18',
            19: '19',
            20: '20',
            21: '21',
            22: '22',
            23: '23',
            24: '24',
            25: '25'
        }

        for i in dc:
            if i in aposta:
                dc[i] = "💎"
            else:
                dc[i] = "🟦"

        bb = random.randint(3, 5)

        tt = random.randint(3, 5)
        ha = datetime.now()
        na = random.randint(5, 7)
        ta = timedelta(minutes=na)
        nh = ha + ta
        nh = nh.strftime('%H:%M')

        msg = (f'''
✅ ENTRADA CONFIRMADA ✅
Seguinte sinal gerado:
Aposte com:  {bb} 💣

         {dc[1]} {dc[2]} {dc[3]} {dc[4]} {dc[5]}
         {dc[6]} {dc[7]} {dc[8]} {dc[9]} {dc[10]}
         {dc[11]} {dc[12]} {dc[13]} {dc[14]} {dc[15]}
         {dc[16]} {dc[17]} {dc[18]} {dc[19]} {dc[20]}
         {dc[21]} {dc[22]} {dc[23]} {dc[24]} {dc[25]}

⏰ Válido até: {nh}
🎯 Tentativas: {tt}x
🖥 Site:  {LINK_SITE}''')
        
        bot.send_message(chat_id=user_id, text=(
            msg), parse_mode='MARKDOWN', disable_web_page_preview=True)
        while True:
            hc = datetime.now().strftime('%H:%M')
            if hc == nh:
                bot.send_message(chat_id=user_id, text=(f'''✅ Sinal Expirado.'''))
                na = random.randint(120, 300)
                time.sleep(na)
                break
    except:
        pass

# Meu instagram @iago_veroneze