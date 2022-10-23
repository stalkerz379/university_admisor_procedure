from typing import Generator
from collections import namedtuple
from pprint import pprint

Subject = namedtuple('Subject', ['name', 'score'], defaults=[None, 0])


class Applicant:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.specialisations = []
        self.subjects: dict[str, Subject] = {}
        self.__accepted = False
        self.best_score = 0
        self.final_best_score = 0

    @property
    def accepted(self):
        return self.__accepted

    @accepted.setter
    def accepted(self, new_value):
        if not self.accepted:
            self.__accepted = new_value

    def __str__(self):
        return f'{self.name} {self.surname} {self.final_best_score}'


class Department:

    def __init__(self, name: str, student_limit: int):
        self.name = name
        self.student_limit = student_limit
        self.__applicants = []

    @property
    def applicants(self):
        return self.__applicants

    def add_applicant(self, applicant: Applicant) -> None:
        if isinstance(applicant, Applicant):
            self.applicants.append(applicant)
        else:
            print(f'Error. The applicant should be an instance of <class Applicant>. Given: {type(applicant)}')

    def sort_applicants(self):
        self.applicants.sort(key=lambda stud: (-stud.final_best_score, stud.name, stud.surname))


class University:

    def __init__(self):
        self.__departments: list[Department] = []
        self.__all_applicants: list[Applicant] = []

    @property
    def departments(self):
        return self.__departments

    @property
    def all_applicants(self):
        return self.__all_applicants

    def add_department(self, department: Department):
        if isinstance(department, Department):
            self.departments.append(department)
        else:
            print(f"Error. The department should be an instance of <class Department>. Given: {type(department)}")

    def get_department(self, name: str) -> Department | None:
        for dep in self.departments:
            if dep.name.lower() == name.lower():
                return dep
        return None

    def set_best_score_for_applicants(self, subject1: str, subject2: str | None):
        for applicant in self.all_applicants:
            sub1 = applicant.subjects.get(subject1, Subject('', 0)).score
            sub2 = applicant.subjects.get(subject2, Subject('', 0)).score
            subjects_total = round((sub1 + sub2) / 2, 2) if sub2 != 0 else sub1
            if subjects_total > applicant.subjects.get('Universal').score:
                applicant.best_score = subjects_total
            else:
                applicant.best_score = applicant.subjects.get('Universal').score

    def sort_by_priority(self, specialisation_index: int) -> None:
        for dep in self.departments:
            subject1, subject2 = self.map_core_exam_for_department(dep.name)
            self.set_best_score_for_applicants(subject1, subject2)
            self.all_applicants.sort(key=lambda stud: (-stud.best_score, stud.name, stud.surname))
            for ind, student in enumerate(self.all_applicants, 0):
                if student.specialisations[specialisation_index] == dep.name and len(dep.applicants) < dep.student_limit and not student.accepted:
                    student.accepted = True
                    student.final_best_score = student.best_score
                    dep.add_applicant(student)
                if len(dep.applicants) == dep.student_limit:
                    break

    @staticmethod
    def map_core_exam_for_department(department_name: str) -> tuple[str, str | None]:
        """Returns tuple of subject names as strings or None if the second exam is not needed"""
        match department_name:
            case 'Biotech':
                return 'Chemistry', 'Physics'
            case 'Chemistry':
                return 'Chemistry', None
            case 'Engineering':
                return 'Computer science', 'Math'
            case 'Mathematics':
                return 'Math', None
            case 'Physics':
                return 'Physics', 'Math'

    def process_applicants(self):
        applicants_ = read_file('application_list.txt')
        for applicant in applicants_:
            applicant = applicant.split()
            student = Applicant(applicant[0], applicant[1])
            student.subjects.setdefault("Physics", Subject("Physics", float(applicant[2])))
            student.subjects.setdefault('Chemistry', Subject('Chemistry', float(applicant[3])))
            student.subjects.setdefault('Math', Subject('Math', float(applicant[4])))
            student.subjects.setdefault('Computer science', Subject('Computer science', float(applicant[5])))
            student.subjects.setdefault('Universal', Subject('Universal', float(applicant[6])))
            student.specialisations.extend([applicant[7], applicant[8], applicant[9]])
            self.all_applicants.append(student)
        self.sort_by_priority(0)
        self.sort_by_priority(1)
        self.sort_by_priority(2)

    def DEPRECATED(self):
        applicants_ = read_file('application_list.txt')
        for applicant in applicants_:
            applicant = applicant.split()
            student = Applicant(applicant[0], applicant[1], float(applicant[2]), applicant[3])
            student.specialisations.extend([applicant[3], applicant[4], applicant[5]])
            self.all_applicants.append(student)
        self.all_applicants.sort(key=lambda stud: (-stud.gpa, stud.name, stud.surname))
        for applicant in self.all_applicants:
            # if all departments reached student limit - then break main cycle
            if all(list(map(lambda dep_: dep_.student_limit == len(dep_.applicants), self.departments))):
                break
            for dep in applicant.specialisations:
                department = self.get_department(dep)
                if len(department.applicants) < department.student_limit:
                    department.add_applicant(applicant)
                    break  # if added then go need to iterate further

    def print_accepted_applicant(self):
        for dep in self.departments:
            print(dep.name)
            dep.sort_applicants()
            for stud in dep.applicants:
                print(stud)
            print()

    def write_dep_files(self):
        for dep in self.departments:
            dep.sort_applicants()
            with open(f"{dep.name.lower()}.txt", 'w', encoding='utf-8') as f_out:
                for stud in dep.applicants:
                    print(stud, file=f_out)


def read_file(file_path: str) -> Generator:
    with open(file_path) as f_in:
        for line in f_in:
            yield line.strip()


def main():
    accept_applicants = int(input())
    university = University()
    dep1 = Department('Biotech', accept_applicants)
    dep2 = Department('Chemistry', accept_applicants)
    dep3 = Department('Engineering', accept_applicants)
    dep4 = Department('Mathematics', accept_applicants)
    dep5 = Department('Physics', accept_applicants)
    for department in [dep1, dep2, dep3, dep4, dep5]:
        university.add_department(department)
    university.process_applicants()
    university.print_accepted_applicant()


if __name__ == '__main__':
    main()
