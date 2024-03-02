from datetime import datetime

class Student:
    def __init__(self,student_id,name,dob,classification):
        self.student_id=student_id
        self.name=name
        self.dob=dob
        self.classification=classification

    def calculate_age(self):
        dob_date = datetime.strptime(self.dob, '%m-%d-%Y')
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        return age
    
    def registration_dates(self):
        if self.classification=='Sr':
            return '4/1 thru 4/3'
        elif self.classification=='Jr':
            return '4/4 thru 4/6'
        elif self.classification=='So':
            return '4/7 thru 4/9'
        elif self.classification=='Fr':
            return '4/10 thru 4/12'