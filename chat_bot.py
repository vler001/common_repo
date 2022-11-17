
print("Вітаю на чатботі!"
      "Назовіть себе.")
name = input("Введіть ім'я: ")
print('Вітаю', name, '''\nОберіть уподобання:\n\tc Кіно\n\tm Музика \n\tp Ігри\n\tg Пропоную пограти\n\t0 Вихід\n''')

cinema_ganr = 'Жанри фільмів : Драма, Комедія, Жахи'
dr = "Пропоную переглянути драматичні фільми: 'Дике поле', 'Донбас', 'Птахи'"
kom = "Пропоную переглянути комедійні фільми: 'Ескорт', 'Липучка', 'Пропозиція'"
hr = "Пропоную переглянути фільми жахів: 'Веном', 'Аквапарк', 'Вони'"

musik_ganr = 'Музикальні жанри : Рок, Класика, Джаз'
r = "Пропоную послухати рок плей ліст: 'Мураками', 'Скорпіонс', 'Металіка'"
cl = "Пропоную послухати класичні твори : 'Бах', 'Бетховен', 'Моцарт'"
j = "Пропоную послухати джазовий плей ліст : 'Боб Зоп', 'Бені Харіс', 'Джим БІл'"

play_ganr = 'Ігрові жанри ЖАркади, Стратегії, Логіка'
ar = "Пропоную аркадні ігри: 'Маріо', 'Докер', 'Джунглі'"
stg = "Пропоную ігри-стратегії: 'Імперія', 'Цивілізація', 'Ворд Крафт'"
log = "Пропоную ігри на логіку: 'Шахи', 'Шахмати', 'Го'"

while True:
      choice = input('Введіть ваше уподобання: ')
      if choice == 'c':
            print('''\nОберіть жанр кіно:\n\tdr Драма\n\tkom Комедія \n\thr Жахи\n\t0 Назад\n''')
            choice1 = input('Виберіть Жанр фільму : ')
            if choice1 == 'dr':
                  print(dr, 'для перегляду фільму перейдіть: https://onlinekino.today')
            elif choice1 == 'kom':
                  print(kom, 'для перегляду фільму  перейдіть: https://onlinekino.today')
            elif choice1 == 'hr':
                  print(hr, 'для перегляду фільму  перейдіть: https://onlinekino.today')

      if choice == 'm':
            print('''\nОберіть  музи жанр :\n\tr Рок\n\tcl ККласика \n\tj Джаз\n\t0 Назад\n''')
            choice2 = input('Виберіть Музикальний жанр : ')
            if choice2 == 'r':
                  print(r, 'для прослуховування плей ліста перейдіть: https://onlinemusik.today')
            elif choice2 == 'cl':
                  print(cl, 'для прослуховування плей ліста перейдіть: https://onlinemusik.today')
            elif choice2 == 'j':
                  print(j, 'для прослуховування плей ліста перейдіть: https://onlinemusik.today')
      if choice == 'p':
            print('''\nОберіть жанр гри:\n\tar Аркади\n\tstg Стратегії \n\tlog Логіка\n\t0 Назад\n''')
            choice3 = input('Ігровий жанр : ')
            if choice3 == 'ar':
                  print(ar,'для початку гри перейдіть: https://onlinegame.today')
            elif choice3 == 'stg':
                  print(stg, 'для початку гри перейдіть: https://onlinegame.today')
            elif choice3 == 'log':
                  print(log, 'для початку гри перейдіть: https://onlinegame.today')
      if choice == 'g':
            def guess_number():
                  print('Давай пограємо, ти маєш  3 спроби вгадати  число 0-10 що я загадав')
                  comp_number = random.randint(0, 11)
                  attempts = range(3, 0, -1)
                  for i in attempts:
                        user_number = int(input(f'Введи номер(маєш {i} спроби): '))
                        if i == 1 and user_number != comp_number:
                              print("Вибач! Ти не вгадав  мій номер")
                        elif user_number > comp_number:
                              print('Це більше ніж я загадав, спрбуй ще!')
                        elif user_number < comp_number:
                              print('Це менше ніж я загадав, спрбуй ще!')
                        else:
                              print(f'Влучно! Мій номер був {comp_number}')
                              break


            guess_number()
            while True:
                  should_continue = input("Бажаєш повторити? (так/ні): ").lower()
                  if should_continue == 'так':
                        guess_number()
                  elif should_continue == 'ні':
                        print('Чудово пограли. До зустрічі!')
                        break
                  else:
                        print('Некоректний вибір')
      elif choice == 0:
            print('exit')
      break
