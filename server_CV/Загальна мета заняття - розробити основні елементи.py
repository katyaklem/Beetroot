'''
Загальна мета заняття - розробити основні елементи сайта, що надає сервіс конструктора резюме для користувачів. 
Ідея полягає в тому, що користувач може додати свій обліковий запис, додавати/змінювати/видаляти контакти, навички та досвід роботи, 
а система згенерує сторінку з його резюме.

Для реалізації задуму треба:
1. Реалізвуати класи, які будуть виконувати роль моделей даних.
    - class Skill - описує одну за навичок користувача. 
    Навички можуть бути трьох категорій (category): 
    технології (technologies), методолії (methodologies) та мови (languages). 
    Кожна навичка характеризується такими параметрами: 
    назва (name), 
    досвід (experience) - кількість років використання цієї технології/методолгії/мови, 
    рівень володіння навичкою (level) - вибір з п'яти можливих варіантів: beginner, junior, middle, senior, expert. 

    - class Contact - описує контактні дані користувача. Описується полями тип 
    (contact_type) - вибір з варіантів 'phone' та 'email'; 
    та значення (value) - конкретна мейл-адреса або номер телефону користувача.
    
    - class JobExperience - описує доствід роботи користувача. Харкатеризується атрибутами: дата початку роботи (start_date), дата завершення роботи (end_date), компанія (company), посада (position).
    - class Person - описує особу самого користувача. Має атрибути  ім'я (first_name), прізвище (last_name), дата народження (birth_date), а також списки контактів (об'єкти класу Contact), навичок (об'єкти класу Skill) та досвіду роботи (об'єкти класу JobExperience). Кожен об'єкт класу має також атрибут id - унікальний ідентифікатор користувача в системі. 
2. Реалізувати відповідні методи для класу Person:
    - Для кожного зі списків (контакти, навички, досвід роботи) мають бути реалізовані методи додавання (add), видалення (delete) та оновлення (update) елементів списку. Для реалізації цих методів можливо буде необхідне додавання вспоміжних атрибутів для кожного класу.
    - Реалізвуати методи збереження інфомації про об'єкт класу Person разом з усіма вкладеними об'єктами у JSON файл та завантаження JSON файлу із створенням всіх вкладених об'єктів.
    - Реалізувати метод, який представляє список skills персони, розбитий за категоріями. Метод має вовертати словник, де ключами є категорії навичок, а значеннями - списки об'єктів навичок персони, що належать до цієї категорії, відсортовані за зменшенням досвіду (навичка з найбільшим значенням досвіду у цій категорії йде перша).
    - Реалізувати метод, який сортує досвід роботи персони від найбільш актуального до найбільш давнього (останній досвід роботи йде першим у відсортованому списку, найбільш давній - останнім)
3. За допомогою фреймворку Flask реалізувати простий сервер, який буде мати два url:
    - "/" - повертає список повних імен всіх персон (first_name + last_name), у текстовому представленні.
    - "/person/<int:person_id>" - повертає тектове представлення інформації про одного користувача.

За необхідності можна додавати будь-які службові атрибути та методи для будь-яких класів. Усе рішення має міститися в окремій папці з назвою cv_builder.

'''

class Skill:
    def __init__(self, category, name, experience, level):
        self.category = category
        self.name = name
        self.experience = experience
        self.level = level

    @classmethod
    def add_skill(cls, all_skills):
        obj = cls(category=None, name=None, experience=None, level=None)
        for skill in all_skills:
            setattr(obj, skill, all_skills[skill])
        return obj


    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if category in ['technologies', 'methodologies', 'languages']:
            self._category = category
        else:
            # raise ValueError дописать тут ошибку
            self._category = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level in ['beginner','junior','middle','senior','expert']:
            self._level = level
        else:
            # raise ValueError дописать тут ошибку
            self._level = None

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, experience):
        if experience.isdigit():
            self._experience = experience
        else:
            # raise ValueError дописать тут ошибку
            self._experience = None

class Contact:
    pass

class JobExperience:
    pass

class Person:
    pass