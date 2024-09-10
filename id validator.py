def ask_for_id():
    global isikukood
    while True:
        idcode = input('Please enter your national id: ')
        if idcode.isdecimal():
            if len(idcode) != 11:
                if len(idcode) < 11:
                    print('ID you entered is too short.')
                    continue
                else:
                    print('ID you entered is too long.')
                    continue
            else:
                isikukood = idcode
                return
        else:
            print('ID you entered is not numeric!')
            continue

def get_gender():
    n = isikukood[0]
    if n not in'09':
        if int(n) % 2 == 0:
            print('You are female')
        else:
            print('You are male')
    else:
        print('Something wrong with ID you entered')

def get_date_of_birth():
    day = isikukood[5:7]
    month = isikukood[3:5]
    year = isikukood[1:3]
    bcent = ''
    n = isikukood[0]
    if n not in '09':
        if n in '12':
            bcent = 18
        elif n in '34':
            bcent = 19
        elif n in '56':
            bcent = 20
        elif n in '78':
            bcent = 21
        print(f'{day}.{month}.{bcent}{year}')

    else:
        print('Something wrong with ID you entered')

def get_birth_region():
    n = isikukood[7:10]
    if int(n) in range(1,11):
        print('Kuressaare haigla')
    elif int(n) in range(11,20):
        print('Tartu Ülikooli Naistekliinik')
    elif int(n) in range(21,151):
        print('Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)')
    elif int(n) in range(151,161):
        print('Keila haigla')
    elif int(n) in range(161,221):
        print('Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)')
    elif int(n) in range(221,271):
        print('Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)')
    elif int(n) in range(271,371):
        print('Maarjamõisa kliinikum (Tartu), Jõgeva haigla')
    elif int(n) in range(371,421):
        print('Narva haigla')
    elif int(n) in range(421,471):
        print('Pärnu haigla')
    elif int(n) in range(471,491):
        print('Haapsalu haigla')
    elif int(n) in range(491,521):
        print('Järvamaa haigla (Paide)')
    elif int(n) in range(521,571):
        print('Rakvere haigla, Tapa haigla')
    elif int(n) in range(571,601):
        print('Valga haigla')
    elif int(n) in range(601,651):
        print('Viljandi haigla')
    elif int(n) in range(651,701):
        print('Lõuna-Eesti haigla (Võru), Põlva haigla')
    else :
        print('Other region')

def get_validation():
    n = isikukood[10]
    a = int(isikukood[0])
    b = int(isikukood[1])
    c = int(isikukood[2])
    d = int(isikukood[3])
    e = int(isikukood[4])
    f = int(isikukood[5])
    g = int(isikukood[6])
    h = int(isikukood[7])
    i = int(isikukood[8])
    j = int(isikukood[9])
    t = (1*a+2*b+3*c+4*d+5*e+6*f+7*g+8*h+9*i+1*j)
    if int(n) == int(t%11):
        print('Valid')
    elif int(t%11) == 10:
        u = (3*a+4*b+5*c+6*d+7*e+8*f+9*g+1*h+2*i+3*j)
        if int(n) == (u - int(u/11)):
            print('Valid')
        else:
            print('Not valid')
    else:
        print('Not valid')

def menu():
    ask_for_id()
    while True:
        user_choice = input('Please choose:\n'
                             '1.Gender\n'
                             '2.Date of birth\n'
                             '3.Birth region\n'
                             '4.Validation\n'
                             '5.Cange ID\n'
                             '0.Exit\n'
                             '-->')
        if user_choice =='1':
            get_gender()
        elif user_choice =='2':
            get_date_of_birth()
        elif user_choice == '3':
            get_birth_region()
        elif user_choice == '4':
            get_validation()
        elif user_choice == '5':
            ask_for_id()
        elif user_choice == '0':
            break
        else:
            print('Choice out of range.')


isikukood = ''
menu()