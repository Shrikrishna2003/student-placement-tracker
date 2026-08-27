class StudentProfile:
    platform = "KodNest"
    total_students = 0

    def __init__(self, student_id, name, branch, score):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.__score = score
        StudentProfile.total_students += 1

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if StudentProfile.is_valid_score(new_score):
            self.__score = new_score
        else:
            print("Invalid score. Score must be between 0 and 100.")

    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100

    @staticmethod
    def normalize_name(name):
        return name.strip().title()

    def get_placement_status(self):
        if self.__score >= 80:
            return "Placement Ready"
        elif self.__score >= 60:
            return "Needs More Practice"
        else:
            return "Not Ready"

    def display_profile(self):
        print(f"\nStudent ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Mock Score: {self.score}")
        print(f"Placement Status: {self.get_placement_status()}")
        print(f"Platform: {StudentProfile.platform}")

    @classmethod
    def from_string(cls, student_data):
        student_id, name, branch, score = student_data.split(",")
        name = cls.normalize_name(name)
        branch = branch.strip()
        score = int(score)
        return cls(student_id.strip(), name, branch, score)

    @classmethod
    def change_platform(cls, new_platform):
        cls.platform = new_platform.strip()

    @classmethod
    def show_total_students(cls):
        print(f"Total Students: {cls.total_students}")


students = []


def find_student(student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None


while True:
    print("\n===== Student Placement Tracker =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Score")
    print("4. Change Platform")
    print("5. Show Total Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter student details (StudentID,Name,Branch,Score): ")

        try:
            temp_id = data.split(",")[0].strip()

            if find_student(temp_id):
                print("Student ID already exists.")
            else:
                student = StudentProfile.from_string(data)

                if StudentProfile.is_valid_score(student.score):
                    students.append(student)
                    print("Student added successfully.")
                else:
                    StudentProfile.total_students -= 1
                    print("Invalid score. Score must be between 0 and 100.")

        except:
            print("Invalid input format.")

    elif choice == "2":
        if students:
            for student in students:
                student.display_profile()
        else:
            print("No students found.")

    elif choice == "3":
        student_id = input("Enter Student ID: ").strip()
        student = find_student(student_id)

        if student:
            try:
                new_score = int(input("Enter New Score: "))
                old_score = student.score
                student.score = new_score

                if student.score != old_score or new_score == old_score:
                    if StudentProfile.is_valid_score(new_score):
                        print("Score updated successfully.")
                        print(f"Updated Score: {student.score}")
                        print(f"Updated Status: {student.get_placement_status()}")
            except:
                print("Please enter a valid number.")
        else:
            print("Student not found.")

    elif choice == "4":
        new_platform = input("Enter the new platform name: ")
        StudentProfile.change_platform(new_platform)
        print("Platform changed successfully.")

    elif choice == "5":
        StudentProfile.show_total_students()

    elif choice == "6":
        print("Thank you for using the Student Placement Tracker.")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 6.")