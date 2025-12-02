def monet(n):
    if 5<=n<=19:
        return str(n)+' монет'
    elif n%10==1:
        return str(n)+' монета'
    elif 2<=n%10<=4:
        return str(n)+' монеты'
    else:
        return str(n)+' монет'
        
string_tarif=input('Введите название тарифа (1 час, 2 часа, 5 часов): ')
sum_string=input('Введите сумму, оторую вносите в автомат: ')
spisok_tarif={'1 час': 60,'2 часа': 100,'5 часов': 250}
if not string_tarif in spisok_tarif:
    print('Неверный тариф')
else:
    if sum_string.isdigit():
        int_string=int(sum_string)
        if int_string<spisok_tarif[string_tarif]:
            print("Недостаточно средств для оплаты выбранного тарифа")
        else:
            int_string-=spisok_tarif[string_tarif]
            monet_10=int_string//10
            monet_10=monet(monet_10)
            ost_10=int_string%10
            monet_5=ost_10//5
            monet_5=monet(monet_5)
            ost_5=ost_10%5
            monet_2=ost_5//2
            monet_2=monet(monet_2)
            ost_2=ost_5%2
            monet_1=ost_2
            monet_1=monet(monet_1)
            print(f"Оплачен тариф '{string_tarif}'. Ваша сдача: {monet_10} по 10 руб., {monet_5} по 5 руб., {monet_2} по 2 руб., {monet_1} по 1 руб.")
    else:
        print('Введенная сумма неккоректна.')
            
