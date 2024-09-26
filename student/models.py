from django.db import models
from users.models import customUser, COURSE_CHOICES

# Create your models here.

COURSE_UNIT_CHOICES = [
    ('SIS1101', 'Introduction to Introduction to computers and Information Systems', 'BIS'),
    ('SHM1101', 'Humanities and Comunication Skills', 'BIS'),
    ('SIS1102', 'Computer Applications', 'BIS'),
    ('SIS1103', 'Business Statistics', 'BIS'),
    ('SIS1104', 'Discrete Mathematics', 'BIS'),
    ('SIS1201', 'Management Information and Systems', 'BIS'),
    ('SIS1202', 'Introduction to Programming', 'BIS'),
    ('SIS1203', 'Business Computing', 'BIS'),
    ('SIS1204', 'Computer Maintenance and Management','BIS'),
    ('SIS1205', 'Internet TEchnologies and Web Authoring','BIS'),
    ('SIS1206', 'Industrial Attachment','BIS'),
    ('SIS2101', 'E-commmerce','BIS'),
    ('SIS2102', 'Information Systems Analysis And Design','BIS'),
    ('SIS2103', 'Database System Design and Development', 'BIS'),
    ('SIS2104', 'Object Oriented Programming', 'BIS'),
    ('SIS2105', 'Multimedia Systems', 'BIS'),
    ('SIS2201', 'Computer Networks and Data Communicatians', 'BIS'),
    ('SIS2202', 'Website Design, Programming and Administrations', 'BIS'),
    ('SIS2203', 'Database Systems Implementaion', 'BIS'),
    ('SIS2204', 'Research Methods', 'BIS'),
    ('SIS2205', 'Business Process Analysis and Modeling', 'BIS'),
    ('SIS2206', 'Industrial Attachment', 'BIS'),
    ('SIS3101', 'Systems Administration', 'BIS'),
    ('SIS3102', 'Information Systems Project Management', 'BIS'),
    ('SIS3103', 'Information Systems Security', 'BIS'),
    ('SIS3104', 'Software Engineering Principle', 'BIS'),
    ('SIS3105', 'Enterpreneurship Skills', 'BIS'),
    ('SIS3201', 'Decision Support Systems', 'BIS'),
    ('SIS3202', 'Social Issues in Society', 'BIS'),
    ('SIS3203', 'Organisatoin Behaviour', 'BIS'),
    ('SIS3204', 'Business Intelligence and data warehousing', 'BIS'),
    ('SIS3205', 'BIS Project', 'BIS'),
    ('SCS1101', 'Introdcution to Information Technology and COmputing', 'BITC'),
    ('SCS1102', 'Computer Applications ', 'BITC'),
    ('SCS1103', 'Discrete Mathematical Structures', 'BITC'),
    ('SCS1104', 'Probability and Statistics', 'BITC'),
    ('SCS1105', 'DIfferential, Integration and Vector Calculus', 'BITC'),
    ('SCS1106', 'Humanities and Communication Skills', 'BITC'),
    ('SCS1201', 'Differential Equations and Systems Modeling', 'BITC'),
    ('SCS1202', 'Programming Languages and Fundamentals', 'BITC'),
    ('SCS1203', 'Linear Algebra', 'BITC'),
    ('SCS1204', 'Computer Architecture', 'BITC'),
    ('SCS1205', 'OPerationg Systems Concepts', 'BITC'),
    ('SCS1206', 'Computer Management and Maintenance', 'BITC'),
    ('SCS1207', 'Industrial Attachment', 'BITC'),
    ('SCS2101', 'Infomartion Systems and Design', 'BITC'),
    ('SCS2102', 'Numerical Analysis and Computation', 'BITC'),
    ('SCS2103', 'Introduction to Data Communication and Networking', 'BITC'),
    ('SCS2104', 'Structured Programming', 'BITC'),
    ('SCS2105', 'Network Management Concepts', 'BITC'),
    ('SCS2201', 'Operating Systems Implemtantion', 'BITC'),
    ('SCS2202', 'Object Oriented Programming Introduction', 'BITC'),
    ('SCS2203', 'Introduction to Database  Management Systems', 'BITC'),
    ('SCS2204', 'Software Engineering ', 'BITC'),
    ('SCS2205', 'Internet Technologies', 'BITC'),
    ('SCS2206', 'Research Methods in Computing Science', 'BITC'),
    ('SCS3101', 'Graph Theory', 'BITC'),
    ('SCS3102', 'Data Structures and Algorithms', 'BITC'),
    ('SCS3103', 'Computer Graphics', 'BITC'),
    ('SCS3104', 'Distributed Computer Systems', 'BITC'),
    ('SCS3105', 'Intermediate Data Communication and Networking', 'BITC'),
    ('SHM3101', 'Enterpreneurship', 'BITC'),
    ('SCS3201', 'Intermediate Database Management Systems', 'BITC'),
    ('SCS3202', 'Microprocessor Base System Design', 'BITC'),
    ('SCS3203', 'Design and Analysis of Algorithm', 'BITC'),
    ('SCS3204', 'Geographic Information Systems and Processing', 'BITC'),
    ('SCS3205', 'Project', 'BITC'),
    ('DCS111', 'Introduction to Computer Science', 'DCS'),
    ('DCS112', 'Introduction to Computer Science Mathematics','DCS'),
    ('DCS113', 'Computer Applications', 'DCS'),
    ('DCS114', 'Comouter Architecture', 'DCS'),
    ('DCS115', 'Humanities and Communication Skills', 'DCS'),
    ('DCS121', 'Management Information Systems', 'DCS'),
    ('DCS122', 'Intermediate Computer Science Mathematics', 'DCS'),
    ('DCS123', 'Introduction to Database Management Systems', 'DCS'),
    ('DCS124', 'Introduction to Programming and Programming Methodology', 'DCS'),
    ('DCS125', 'Systems Analysis and Design', 'DCS'),
    ('DCS126', 'Industrial Attachment', 'DCS'),
    ('DCS211', 'Visual Basic Programming', 'DCS'),
    ('DCS213', 'Intermediate Database Management Systems', 'DCS'),
    ('DCS214', 'Web Deevelopment technology', 'DCS'),
    ('DCS215', 'Enterpreneurship Skills', 'DCS'),
    ('DCS221', 'Computer Management and Maintenance', 'DCS'),
    ('DCS222', 'Data Communications and Networking', 'DCS'),
    ('DCS223', 'Introduction to Operating Systems', 'DCS'),
    ('DCS224', 'Ethical, Legal and Social Issues and Social Issues in Computing', 'DCS'),
    ('DCS225', 'Project', 'DCS'),

]

class CourseUnit(models.Model):
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    code = models.CharField(max_length=50, choices=[(code, name) for code, name, _ in COURSE_UNIT_CHOICES])
    lecturer = models.ForeignKey(customUser, on_delete=models.CASCADE, limit_choices_to={'is_lecturer': True}, related_name='course_units')  

    def __str__(self):
        course_name_dict = {code: name for code, name, _ in COURSE_UNIT_CHOICES}
        course_name = course_name_dict.get(self.code, 'Unknown Course')
        return f'{self.code} - {course_name} by {self.lecturer.username}'

class Enrollment(models.Model):
    student = models.ForeignKey(customUser, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    course_unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.student.username} enrolled in {self.course_unit}'