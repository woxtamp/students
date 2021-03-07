class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.rating:
                lecturer.rating[course] += [rate]
            else:
                lecturer.rating[course] = [rate]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        average_grade = str(sum(grades_list) / len(grades_list))
        return average_grade

    def __str__(self):
        return ('Студент' + '\n' + 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' +
                'Средняя оценка за домашние задания: ' +
                self.average_grade() + '\n' + 'Курсы в процессе изучения: ' +
                ', '.join(self.courses_in_progress) + '\n' + 'Завершённые курсы: ' +
                ', '.join(self.finished_courses) + '\n')

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка! Это не студент!'
        else:
            if self.average_grade() > other.average_grade():
                return ('Студент ' + self.name + ' ' + self.surname + ' успешнее, чем ' +
                        other.name + ' ' + other.surname + '\n')
            else:
                return ('Студент ' + other.name + ' ' + other.surname + ' успешнее, чем ' +
                        self.name + ' ' + self.surname + '\n')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def average_rate(self):
        rates_list = []
        for rate in self.rating.values():
            rates_list += rate
        average_rate = str(sum(rates_list) / len(rates_list))
        return average_rate

    def __str__(self):
        return ('Лектор' + '\n' + 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' +
                'Средняя оценка за лекции: ' + self.average_rate() + '\n')

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка! Это не лектор!'
        else:
            if self.average_rate() > other.average_rate():
                return ('Лектор ' + self.name + ' ' + self.surname + ' успешнее, чем ' +
                        other.name + ' ' + other.surname + '\n')
            else:
                return ('Лектор ' + other.name + ' ' + other.surname + ' успешнее, чем ' +
                        self.name + ' ' + self.surname + '\n')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Проверяющий' + '\n' + 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n'


student_ivanov = Student('Иванов', 'Иван', 'male')
student_ivanov.courses_in_progress += ['Python', 'Git']

student_petrova = Student('Петрова', 'Ольга', 'female')
student_petrova.courses_in_progress += ['Python']
student_petrova.finished_courses += ['Git']

reviewer_sidorova = Reviewer('Анна', 'Сидорова')
reviewer_sidorova.courses_attached += ['Python']

reviewer_andropov = Reviewer('Анатолий', 'Андропов')
reviewer_andropov.courses_attached += ['Git']

lecturer_ignatenko = Lecturer('Марина', 'Игнатенко')
lecturer_ignatenko.courses_attached += ['Python']

lecturer_andropov = Lecturer('Анатолий', 'Андропов')
lecturer_andropov.courses_attached += ['Git']

reviewer_sidorova.rate_hw(student_ivanov, 'Python', 7)
reviewer_andropov.rate_hw(student_ivanov, 'Git', 6)

reviewer_sidorova.rate_hw(student_petrova, 'Python', 9)

student_ivanov.rate_lecturer(lecturer_ignatenko, 'Python', 8)
student_ivanov.rate_lecturer(lecturer_andropov, 'Git', 6)

student_petrova.rate_lecturer(lecturer_ignatenko, 'Python', 9)

print(student_ivanov)
print(student_petrova)
print(reviewer_sidorova)
print(reviewer_andropov)
print(lecturer_ignatenko)
print(lecturer_andropov)

print(student_ivanov > student_petrova)
print(lecturer_ignatenko > lecturer_andropov)


def avg_grades_all(students_list, course):
    all_grades_list = []
    for student in students_list:
        if student.grades.get(course) is not None:
            all_grades_list += student.grades.get(course)
        else:
            pass
    all_grades_avg = str(sum(all_grades_list) / len(all_grades_list))
    print('Средняя оценка всех студентов за домашние задания по курсу ' + course + ': ' + all_grades_avg)


def avg_rates_all(lecturer_list, course):
    all_rates_list = []
    for lecturer in lecturer_list:
        if lecturer.rating.get(course) is not None:
            all_rates_list += lecturer.rating.get(course)
        else:
            pass
    all_rates_avg = str(sum(all_rates_list) / len(all_rates_list))
    print('Средняя оценка всех лекторов в рамках курса ' + course + ': ' + all_rates_avg)


avg_grades_all([student_ivanov, student_petrova], 'Python')
avg_grades_all([student_ivanov, student_petrova], 'Git')

avg_rates_all([lecturer_ignatenko, lecturer_andropov], 'Python')
avg_rates_all([lecturer_ignatenko, lecturer_andropov], 'Git')
