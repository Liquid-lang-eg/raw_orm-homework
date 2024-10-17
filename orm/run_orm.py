from db_backend_orm import AlchemyBack

class DataBaseManagerORM:

    def __init__(self):
        self.choice = None
        self.select()

    def start_program(self):
        print('''
        Вы можете выбрать из предложенных ниже вариантов
        0 - 7
        Данная программа предлагает следующий функционал:
        1 - получить все из таблицы musicstores
        2 - получить все из таблицы vinyl
        3 - получить данные о магазине по названию магазина
        4 - получить данные о магазине по адресу
        5 - получить все о пластинке по названию
        6 - добавить магазин в таблицу musicstores
        7 - добавить пластинку в таблицу vinyl

        0 - завершить программу
        ''')

    def select(self):
        while True:
            self.start_program()
            try:
                self.choice = int(input('Выберите из вариантов, введите число: '))
                break
            except ValueError:
                print('Пожалуйста введите число')
        if self.choice == 0:
            print('Программа закрыта')
        elif self.choice == 1:
            self.get_all_stores()
            return self.select()
        elif self.choice == 2:
            self.get_all_vinyl()
            return self.select()
        elif self.choice == 3:
            self.get_music_store_by_name()
            return self.select()
        elif self.choice == 4:
            self.get_music_store_by_address()
            return self.select()
        elif self.choice == 5:
            self.get_vinyl_by_title()
            return self.select()
        elif self.choice == 6:
            self.add_store()
            return self.select()
        elif self.choice == 7:
            self.add_vinyl()
            return self.select()
        else:
            print('Пожалуйста выберите из доступных опций: ')
            return self.select()



    def get_all_stores(self):
        stores = AlchemyBack.get_all_stores()
        if isinstance(stores, str):
            print(stores)
        else:
            print('Вот список магазинов')
            for store in stores:
                print(store)

    def get_all_vinyl(self):
        vinyl = AlchemyBack.get_all_vinyl()
        if isinstance(vinyl, str):
            print(vinyl)
        else:
            print('Вот список пластинок')
            for album in vinyl:
                print(album)

    def get_music_store_by_name(self):
        name = input('Введите название магазина: ')
        print(AlchemyBack.get_music_store_by_name(name))

    def get_music_store_by_address(self):
        address = input('Введите адрес магазина: ')
        print(AlchemyBack.get_music_store_by_address(address))

    def get_vinyl_by_title(self):
        vinyl = input('Введите название винила: ')
        print(AlchemyBack.get_vinyl_by_title(vinyl))

    def add_store(self):
        name = input('Введите название магазина: ')
        address = input('Введите адрес магазина: ')
        print(AlchemyBack.add_store(name, address))


    def add_vinyl(self):
        title = input('Введите название пластинки: ')
        author_name = input('Введите автора пластинки: ')
        print('Вот список магазинов, первый столбец это id'
              'выберите id того магазина в котором есть пластинка')
        self.get_all_stores()
        while True:
            try:
                store_id = int(input('Введите id магазина: '))
                year = int(input('Введите id магазина: '))
                break
            except ValueError:
                print('Введите значение из данных либо null')


        print(AlchemyBack.add_vinyl(title, author_name, store_id, year))

manager = DataBaseManagerORM()