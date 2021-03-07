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
            lecturer.rating += [rate]
        else:
            return 'Ошибка'

    def average_grade(self):
        avg_list = []
        for grade in self.grades.values():
            avg_list += grade
        return avg_list

    def __str__(self):
        return ('Студент' + '\n' + 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' +
                'Средняя оценка за домашние задания: ' +
                str(sum(self.average_grade()) / len(self.average_grade())) + '\n' + 'Курсы в процессе изучения: ' +
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
        self.rating = []

    def average_rate(self):
        avg_rate = sum(self.rating) / len(self.rating)
        return avg_rate

    def __str__(self):
        return ('Лектор' + '\n' + 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' +
                'Средняя оценка за лекции: ' + str(self.average_rate()) + '\n')

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
reviewer_andropov.rate_hw(student_ivanov, 'Git', 8)

reviewer_sidorova.rate_hw(student_petrova, 'Python', 9)

student_ivanov.rate_lecturer(lecturer_ignatenko, 'Python', 8)
student_ivanov.rate_lecturer(lecturer_andropov, 'Git', 6)


print(student_ivanov)
print(student_petrova)
print(reviewer_sidorova)
print(reviewer_andropov)
print(lecturer_ignatenko)
print(lecturer_andropov)

print(lecturer_ignatenko > lecturer_andropov)
print(student_ivanov > student_petrova)
