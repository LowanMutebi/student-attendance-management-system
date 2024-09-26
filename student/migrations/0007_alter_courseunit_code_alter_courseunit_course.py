# Generated by Django 5.0.6 on 2024-09-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_courseunit_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseunit',
            name='code',
            field=models.CharField(choices=[('SIS1101', 'Introduction to Introduction to computers and Information Systems'), ('SHM1101', 'Humanities and Comunication Skills'), ('SIS1102', 'Computer Applications'), ('SIS1103', 'Business Statistics'), ('SIS1104', 'Discrete Mathematics'), ('SIS1201', 'Management Information and Systems'), ('SIS1202', 'Introduction to Programming'), ('SIS1203', 'Business Computing'), ('SIS1204', 'Computer Maintenance and Management'), ('SIS1205', 'Internet TEchnologies and Web Authoring'), ('SIS1206', 'Industrial Attachment'), ('SIS2101', 'E-commmerce'), ('SIS2102', 'Information Systems Analysis And Design'), ('SIS2103', 'Database System Design and Development'), ('SIS2104', 'Object Oriented Programming'), ('SIS2105', 'Multimedia Systems'), ('SIS2201', 'Computer Networks and Data Communicatians'), ('SIS2202', 'Website Design, Programming and Administrations'), ('SIS2203', 'Database Systems Implementaion'), ('SIS2204', 'Research Methods'), ('SIS2205', 'Business Process Analysis and Modeling'), ('SIS2206', 'Industrial Attachment'), ('SIS3101', 'Systems Administration'), ('SIS3102', 'Information Systems Project Management'), ('SIS3103', 'Information Systems Security'), ('SIS3104', 'Software Engineering Principle'), ('SIS3105', 'Enterpreneurship Skills'), ('SIS3201', 'Decision Support Systems'), ('SIS3202', 'Social Issues in Society'), ('SIS3203', 'Organisatoin Behaviour'), ('SIS3204', 'Business Intelligence and data warehousing'), ('SIS3205', 'BIS Project'), ('SCS1101', 'Introdcution to Information Technology and COmputing'), ('SCS1102', 'Computer Applications '), ('SCS1103', 'Discrete Mathematical Structures'), ('SCS1104', 'Probability and Statistics'), ('SCS1105', 'DIfferential, Integration and Vector Calculus'), ('SCS1106', 'Humanities and Communication Skills'), ('SCS1201', 'Differential Equations and Systems Modeling'), ('SCS1202', 'Programming Languages and Fundamentals'), ('SCS1203', 'Linear Algebra'), ('SCS1204', 'Computer Architecture'), ('SCS1205', 'OPerationg Systems Concepts'), ('SCS1206', 'Computer Management and Maintenance'), ('SCS1207', 'Industrial Attachment'), ('SCS2101', 'Infomartion Systems and Design'), ('SCS2102', 'Numerical Analysis and Computation'), ('SCS2103', 'Introduction to Data Communication and Networking'), ('SCS2104', 'Structured Programming'), ('SCS2105', 'Network Management Concepts'), ('SCS2201', 'Operating Systems Implemtantion'), ('SCS2202', 'Object Oriented Programming Introduction'), ('SCS2203', 'Introduction to Database  Management Systems'), ('SCS2204', 'Software Engineering '), ('SCS2205', 'Internet Technologies'), ('SCS2206', 'Research Methods in Computing Science'), ('SCS3101', 'Graph Theory'), ('SCS3102', 'Data Structures and Algorithms'), ('SCS3103', 'Computer Graphics'), ('SCS3104', 'Distributed Computer Systems'), ('SCS3105', 'Intermediate Data Communication and Networking'), ('SHM3101', 'Enterpreneurship'), ('SCS3201', 'Intermediate Database Management Systems'), ('SCS3202', 'Microprocessor Base System Design'), ('SCS3203', 'Design and Analysis of Algorithm'), ('SCS3204', 'Geographic Information Systems and Processing'), ('SCS3205', 'Project'), ('DCS111', 'Introduction to Computer Science'), ('DCS112', 'Introduction to Computer Science Mathematics'), ('DCS113', 'Computer Applications'), ('DCS114', 'Comouter Architecture'), ('DCS115', 'Humanities and Communication Skills'), ('DCS121', 'Management Information Systems'), ('DCS122', 'Intermediate Computer Science Mathematics'), ('DCS123', 'Introduction to Database Management Systems'), ('DCS124', 'Introduction to Programming and Programming Methodology'), ('DCS125', 'Systems Analysis and Design'), ('DCS126', 'Industrial Attachment'), ('DCS211', 'Visual Basic Programming'), ('DCS213', 'Intermediate Database Management Systems'), ('DCS214', 'Web Deevelopment technology'), ('DCS215', 'Enterpreneurship Skills'), ('DCS221', 'Computer Management and Maintenance'), ('DCS222', 'Data Communications and Networking'), ('DCS223', 'Introduction to Operating Systems'), ('DCS224', 'Ethical, Legal and Social Issues and Social Issues in Computing'), ('DCS225', 'Project')], max_length=50),
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='course',
            field=models.CharField(choices=[('BIS', 'Bachelor of Information Systems'), ('BITC', 'Bachelor of Information Techonology'), ('DCS', 'Diploma in Computer Science')], max_length=50),
        ),
    ]
