from numpy import log, exp

# Количество писем и слов
spam_email = 30
not_spam_email = 23

sum_spam_words = 155
sum_not_spam_words = 153

P_ham = not_spam_email / (spam_email + not_spam_email)
P_spam = spam_email / (spam_email + not_spam_email)
print('1. Вероятность того, что письмо является спамом, исходя из тренировочного набора данных:', round(P_spam, 3))

# Количество значений из 5/2 ключевых слов на 10 строк таблицы спам/неспам
spam_words = (4, 4, 19, 10, 17, 0, 0)
not_spam_words = (11, 8, 15, 9, 46, 0, 0)


func_spam = lambda x: (1 + x) / (10 + 2 + sum_spam_words)
func_not_spam = lambda x: (1 + x) / (10 + 2 + sum_not_spam_words)

F_spam = log(P_spam) + sum(map(log, map(func_spam, spam_words)))
F_not_spam = log(P_ham) + sum(map(log, map(func_not_spam, not_spam_words)))

print('2. F(«спам»):', round(F_spam, 3))
print('3. F(«не спам»):', round(F_not_spam, 3))

P_spams = 1 / (1 + exp(-F_spam + F_not_spam))

print('4. Вероятность P(Класс = «спам» | Письмо):', round(P_spams, 3))
