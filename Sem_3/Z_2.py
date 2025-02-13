﻿#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter

text = '22 ноября 1954 года, ровно 70 лет назад, в Нью-Йорке скончался видный советский деятель, прокурор и дипломат Андрей Вышинский. Ему было 70 лет. \
    Этнический поляк запомнился прежде всего тем, что создавал юридическое прикрытие политическим репрессиям 1930-х годов. Его полные насмешек и презрения гневные речи, \
        обличавшие «врагов народа», стали одним из символов эпохи. Как государственный обвинитель Вышинский отправил на плаху многих руководителей СССР — Зиновьева и Каменева, \
            Рыкова и Бухарина. Считается, что он был послушным исполнителем воли Сталина, который имел на своего прокурора убийственный компромат. «Лента.ру» — об одном\
                  из главных юристов в советской истории, которого одни называли неутомимым борцом с врагами народа, а другие — жестоким инквизитором и одним из самых страшных палачей.\
«Скажите, предатель и изменник Ягода, неужели во всей вашей гнусной и предательской деятельности вы не испытывали никогда ни малейшего сожаления, ни малейшего раскаяния? \
— почти кричал прокурор СССР Андрей Вышинский, испепеляя взглядом бывшего наркома внутренних дел, на лице которого отчетливо виднелись следы ночных допросов. — \
И сейчас, когда вы отвечаете, наконец, перед пролетарским судом за все ваши подлые преступления, вы не испытываете ни малейшего сожаления о сделанном вами?»\
«Да, сожалею, очень сожалею...» — раздался еле слышный голос.\
«О чем вы сожалеете, шпион и преступник Ягода?» — еле заметно ухмыльнулся Вышинский.\
«Очень сожалею, что, когда я мог это сделать, я всех вас не расстрелял!» — последовал быстрый ответ.'\

text = text.lower()
text_1 = re.sub(r'[^\w\s]', '', text)
new_text = text.split()

print(Counter(new_text).most_common()[:10])