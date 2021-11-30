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
    
    - class JobExperience - описує доствід роботи користувача. 
    Харкатеризується атрибутами: дата початку роботи (start_date), 
    дата завершення роботи (end_date), 
    компанія (company), 
    посада (position).

    - class Person - описує особу самого користувача. 
    Має атрибути  ім'я (first_name), 
    прізвище (last_name), 
    дата народження (birth_date), 
    а також списки контактів (об'єкти класу Contact), 
    навичок (об'єкти класу Skill) 
    та досвіду роботи (об'єкти класу JobExperience). 
    Кожен об'єкт класу має також атрибут id - унікальний ідентифікатор користувача в системі. 

2. Реалізувати відповідні методи для класу Person:
    - Для кожного зі списків (контакти, навички, досвід роботи) мають бути реалізовані 
    методи додавання (add), 
    видалення (delete) 
    та оновлення (update)
    елементів списку. 
    Для реалізації цих методів можливо буде необхідне додавання вспоміжних атрибутів для кожного класу.
    

    - Реалізвуати методи збереження інфомації про об'єкт класу Person разом з усіма вкладеними об'єктами 
    у JSON файл та завантаження JSON файлу із створенням всіх вкладених об'єктів.
    
    - Реалізувати метод, який представляє список skills персони, розбитий за категоріями. 
    Метод має вовертати словник, де ключами є категорії навичок, а значеннями - списки об'єктів навичок персони, 
    що належать до цієї категорії, відсортовані за зменшенням досвіду (навичка з найбільшим значенням досвіду у цій категорії йде перша).
    
    - Реалізувати метод, який сортує досвід роботи персони від найбільш актуального до найбільш давнього 
    (останній досвід роботи йде першим у відсортованому списку, найбільш давній - останнім)

3. За допомогою фреймворку Flask реалізувати простий сервер, який буде мати два url:
    - "/" - повертає список повних імен всіх персон (first_name + last_name), у текстовому представленні.
    - "/person/<int:person_id>" - повертає тектове представлення інформації про одного користувача.

За необхідності можна додавати будь-які службові атрибути та методи для будь-яких класів. Усе рішення має міститися в окремій папці з назвою cv_builder.

'''

import datetime
import json
import os

class Person:
    persons_list = []
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.contacts = []
        self.skills = []
        self.job_experience = []
        self.id = len(Person.persons_list)
        Person.persons_list.append(self)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birth_date} {self.contacts}'

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.birth_date} {self.contacts}'

    def add_contact(self, contact_type, value):
        self.contacts.append(Contact(contact_type, value))

    def del_contact(self, contact_value):
        for contact in self.contacts:
            if contact_value == contact.value:
                del self.contacts[self.contacts.index(contact)]

    def update_contact(self, past_contact, new_contact):
        for contact in self.contacts:
            if past_contact == contact.value:
                contact.value = new_contact

    def add_skill(self, category, name, experience, level):
        self.skills.append(Skill(category, name, experience, level))

    def del_skill(self, name):
        for skill in self.skills:
            if skill.name == name:
                del self.skills[self.skills.index(skill)]

    def update_skill(self, category, name, experience, level):
        for skill in self.skills:
            if skill.name == name:
                skill.category = category
                skill.experience = experience
                skill.level = level

    def add_experience(self, start_date, end_date, company, position):
        self.job_experience.append(Job_experience(start_date, end_date, company, position))

    def del_experience(self, company):
        for experience in self.job_experience:
            if experience.company == company:
                del self.job_experience[self.job_experience.index(experience)]

    def uppdate_experience(self, start_date, end_date, company, position):
        for experience in self.job_experience:
            if experience.company == company and experience.position == position:
                experience.start_date = start_date
                experience.end_date = end_date
                experience.company = company
                experience.position = position

    @classmethod
    def list_to_json(cls):
        person_list = [t.__dict__ for t in cls.persons_list]
        return json.dumps(person_list)

    def dump_json(self):
        file_name = 'person.json'
        path_json = os.path.join(os.getcwd(), 'data', file_name)
        item = {}
        for key, val in self.__dict__.items():
            item[key] = val
            if key in ['contact', 'skills', 'experience']:
                item[key] = [i.__dict__ for i in val]
        with open(path_json, 'w') as file:
            json.dump(item, file)

    @classmethod
    def load_json(cls):
        file_name = 'person.json'
        path_json = os.path.join(os.getcwd(), 'data', file_name)
        with open(path_json, 'r') as file:
            dict_person = json.load(file)
        obj_person = Person.add_person_obj(dict_person)
        return obj_person

    def to_json(self):
        return json.dumps(self.__dict__)

class Job_experience:
    jobs_experience_list = []
    def __init__(self, start_date, end_date, company, position):
        self.start_date = start_date
        self.end_date = end_date
        self.company = company
        self.position = position
        JobExperience.jobs_experience_list.append(self)

    @classmethod
    def add_experience_obj(cls, dict_experience):
        obj = cls(start_date=None, end_date=None, company=None, position=None)
        for experience in dict_experience:
            setattr(obj, experience, dict_experience[experience])
        return obj


class Skill:
    skills_list = []
    def __init__(self, category, name, experience, level):
        self.category = category
        self.name = name
        self.experience = experience
        self.level = level
        Skill.skills_list.append(self)

    @classmethod
    def add_skills_obj(cls, dict_skills):
        obj = cls(category=None, name=None, experience=None, level=None)
        for skill in dict_skills:
            setattr(obj, skill, dict_skills[skill])
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
        if type(experience) == int:
            self._experience = experience
        else:
            # raise ValueError дописать тут ошибку
            self._experience = None


class Contact:
    contacts_list = [] 
    def __init__(self, contact_type, value):
        self.contact_type = contact_type
        self.value = value
        Contact.contacts_list.append(self)

    def __str__(self):
        return f'{self.contact_type} {self.value}'

    @property
    def contact_type(self):
        return self._contact_type 

    @contact_type.setter
    def contact_type(self, contact_type):
        if contact_type in ['phone', 'email']:
            self._contact_type = contact_type
        else:
            self.contact_type = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.contact_type == None:
            self._value = None
        elif self.contact_type == 'email':
            if '@' in value:
                self._value = value
            else:
                self._value = None
        else:
            if type(value) == int:
                self._value = value
            else:
                self._value = None

    @classmethod
    def add_contacts_obj(cls, dict_contacts):
        obj = cls(contact_type=None, value=None)
        for contact in dict_contacts:
            setattr(obj, contact, dict_contacts[contact])
        return obj

person = Person('Katya', 'Klem', '1999')
person.add_contact('phone', 911)

#person.load_json() 
#person.to_json()
#person.dump_json() 
person.list_to_json()
