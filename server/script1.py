import os
import sys
import inspect

from sqlalchemy import insert
from main import User, db, Education, Course, Mandatory
import email
from os import name
from pickle import NONE


db.drop_all()
db.create_all()

student1 = User(
    name="Oskar",
    email="oskar@outlook.com",
    grade=2,
    birthdate=20050619,
    education="Naturvetenskap",
    password_hash="$2b$12$LRut0dbm1tM9RD.5Gx/z8OuI0LC2qu.PWp8Ll6QilV7ygIg24pZvq",
)

student2 = User(
    name="Ida",
    email="ida@outlook.com",
    grade=3,
    birthdate=20040901,
    education="Samhällsvetenskap",
    password_hash="$2b$12$LRut0dbm1tM9RD.5Gx/z8OuI0LC2qu.PWp8Ll6QilV7ygIg24pZvq",
)

student3 = User(
    name="Liam",
    email="liam@outlook.com",
    grade=3,
    birthdate=20041022,
    education="Teknikvetenskap",
    password_hash="$2b$12$LRut0dbm1tM9RD.5Gx/z8OuI0LC2qu.PWp8Ll6QilV7ygIg24pZvq",
)

student4 = User(
    name="Tilda",
    email="tilda@outlook.com",
    grade=1,
    birthdate=20060212,
    education="Ekonomi",
    password_hash="$2b$12$LRut0dbm1tM9RD.5Gx/z8OuI0LC2qu.PWp8Ll6QilV7ygIg24pZvq",
)

student5 = User(
    name="Melvin",
    email="melvin@outlook.com",
    grade=1,
    birthdate=20060317,
    education="Naturvetenskap",
    password_hash="$2b$12$LRut0dbm1tM9RD.5Gx/z8OuI0LC2qu.PWp8Ll6QilV7ygIg24pZvq",
)

student6 = User(
    name="Hanna",
    email="hanna@outlook.com",
    grade=2,
    birthdate=20050505,
    education="Samhällsvetenskap",
    password_hash="$2b$12$LRut0dbm1tM9RD.5Gx/z8OuI0LC2qu.PWp8Ll6QilV7ygIg24pZvq",
)

student7 = User(
    name="Elias",
    email="elias@outlook.com",
    grade=3,
    birthdate=20040105,
    education="Teknikvetenskap",
    password_hash="$2b$12$LRut0dbm1tM9RD.5Gx/z8OuI0LC2qu.PWp8Ll6QilV7ygIg24pZvq",
)

student8 = User(
    name="Samuel",
    email="samuel@outlook.com",
    grade=3,
    birthdate=20041210,
    education="Ekonomi",
    password_hash="$2b$12$LRut0dbm1tM9RD.5Gx/z8OuI0LC2qu.PWp8Ll6QilV7ygIg24pZvq",
)

# ===================== Svenska =========================
course1 = Course(course_title="Svenska 1", points=100)
course2 = Course(course_title="Svenska 2", points=100)
course3 = Course(course_title="Svenska 3", points=100)
# ===================== Engelska =========================
course4 = Course(course_title="Engelska 5", points=100)
course5 = Course(course_title="Engelska 6", points=100)
course6 = Course(course_title="Engelska 7", points=100)

# ===================== Matematik =========================
course7 = Course(course_title="Matematik 1c", points=100)
course8 = Course(course_title="Matematik 2c", points=100)
course9 = Course(course_title="Matematik 3c", points=100)
course10 = Course(course_title="Matematik 4", points=100)
course11 = Course(course_title="Matematik 5", points=100)
# ===================== Samhällsorienterat =========================
course12 = Course(course_title="Historia 1", points=100)
course13 = Course(course_title="Religionskunskap 1", points=50)
course14 = Course(course_title="Samhällskunskap 1", points=100)
course15 = Course(course_title="Geografi 1", points=100)
course16 = Course(course_title="Samhällskunskap 2", points=100)
course17 = Course(course_title="Historia 2", points=100)
# ===================== Naturvetenskapligt =========================
course18 = Course(course_title="Biologi 1", points=100)
course19 = Course(course_title="Biologi 2", points=100)
course20 = Course(course_title="Kemi 1", points=100)
course21 = Course(course_title="Kemi 2", points=100)
course22 = Course(course_title="Fysik 1", points=150)
course23 = Course(course_title="Fysik 2", points=100)
course24 = Course(course_title="Finansiella beräkningar", points=100)
course25 = Course(course_title="Idrott och Hälsa 1", points=100)
course26 = Course(course_title="Matematik 1b", points=100)
course27 = Course(course_title="Matematik 2b", points=100)
course28 = Course(course_title="Matematik 3b", points=100)
course29 = Course(course_title="Moderna språk 1", points=100)
course30 = Course(course_title="Idrott och Hälsa 2", points=100)
course31 = Course(course_title="Teknik 1", points=150)
course32 = Course(course_title="Konstruktion 1", points=100)
course33 = Course(course_title="Teknik 2", points=100)
course34 = Course(course_title="Programmering 1", points=100)
course35 = Course(course_title="Naturkunskap 1", points=100)
course36 = Course(course_title="Företagsekonomi 1", points=100)
course37 = Course(course_title="Privatjuridik", points=100)
course38 = Course(course_title="Moderna språk 2", points=100)
course39 = Course(course_title="Psykologi 1", points=50)
course40 = Course(course_title="Företagsekonomi 2", points=100)
course41 = Course(course_title="Entreprenörskap och Företagande", points=100)
course42 = Course(course_title="Internationell ekonomi", points=100)
course43 = Course(course_title="Filosofi 1", points=50)
course44 = Course(course_title="Samhällskunskap 3", points=100)
course45 = Course(course_title="Religionskunskap 2", points=50)
course46 = Course(course_title="Politik och Hållbar utveckling", points=100)
course47 = Course(course_title="Etnicitet och Kulturmöten", points=100)
course48 = Course(course_title="Ledarskap och Organisation", points=100)
course49 = Course(course_title="Företagsekonomi Specialisering", points=100)
course50 = Course(course_title="Fysik 3", points=100)
course51 = Course(course_title="Matematik Specialisering", points=100)
course52 = Course(course_title="Teknik Specialisering", points=100)
course53 = Course(course_title="Gymnasiearbete", points=100)

# ===================== Gymnasieutbildningar =========================
education1 = Education(edu_name="Naturvetenskap")
education2 = Education(edu_name="Teknikvetenskap")
education3 = Education(edu_name="Samhällsvetenskap")
education4 = Education(edu_name="Ekonomi")


db.session.add(student1)
db.session.add(student2)
db.session.add(student3)
db.session.add(student4)
db.session.add(student5)
db.session.add(student6)
db.session.add(student7)
db.session.add(student8)
db.session.add(course1)
db.session.add(course2)
db.session.add(course3)
db.session.add(course4)
db.session.add(course5)
db.session.add(course6)
db.session.add(course7)
db.session.add(course8)
db.session.add(course9)
db.session.add(course10)
db.session.add(course11)
db.session.add(course12)
db.session.add(course13)
db.session.add(course14)
db.session.add(course15)
db.session.add(course16)
db.session.add(course17)
db.session.add(course18)
db.session.add(course19)
db.session.add(course20)
db.session.add(course21)
db.session.add(course22)
db.session.add(course23)
db.session.add(course24)
db.session.add(course25)
db.session.add(course26)
db.session.add(course27)
db.session.add(course28)
db.session.add(course29)
db.session.add(course30)
db.session.add(course31)
db.session.add(course32)
db.session.add(course33)
db.session.add(course34)
db.session.add(course35)
db.session.add(course36)
db.session.add(course37)
db.session.add(course38)
db.session.add(course39)
db.session.add(course40)
db.session.add(course41)
db.session.add(course42)
db.session.add(course43)
db.session.add(course44)
db.session.add(course45)
db.session.add(course46)
db.session.add(course47)
db.session.add(course48)
db.session.add(course49)
db.session.add(course50)
db.session.add(course51)
db.session.add(course52)
db.session.add(course53)
db.session.add(education1)
db.session.add(education2)
db.session.add(education3)
db.session.add(education4)


# =============== Mandatory courses för Natur ======================
# education1.mandatory_courses.append(course1)
# education1.mandatory_courses.append(course2)
# education1.mandatory_courses.append(course3)
# education1.mandatory_courses.append(course4)
# education1.mandatory_courses.append(course5)
# education1.mandatory_courses.append(course7)
# education1.mandatory_courses.append(course8)
# education1.mandatory_courses.append(course9)
# education1.mandatory_courses.append(course10)
# education1.mandatory_courses.append(course12)
# education1.mandatory_courses.append(course14)
# education1.mandatory_courses.append(course16)
# education1.mandatory_courses.append(course18)
# education1.mandatory_courses.append(course19)
# education1.mandatory_courses.append(course20)
# education1.mandatory_courses.append(course21)
# education1.mandatory_courses.append(course22)
# education1.mandatory_courses.append(course23)

# =============== Mandatory courses för Teknik ======================
# education2.mandatory_courses.append(course1)
# education2.mandatory_courses.append(course2)
# education2.mandatory_courses.append(course3)
# education2.mandatory_courses.append(course4)
# education2.mandatory_courses.append(course5)
# education2.mandatory_courses.append(course7)
# education2.mandatory_courses.append(course8)
# education2.mandatory_courses.append(course9)
# education2.mandatory_courses.append(course10)
# education2.mandatory_courses.append(course12)
# education2.mandatory_courses.append(course14)
# education2.mandatory_courses.append(course16)
# education2.mandatory_courses.append(course20)
# education2.mandatory_courses.append(course22)
# education2.mandatory_courses.append(course23)

# =============== Mandatory courses för Sam ======================
# education3.mandatory_courses.append(course1)
# education3.mandatory_courses.append(course2)
# education3.mandatory_courses.append(course3)
# education3.mandatory_courses.append(course4)
# education3.mandatory_courses.append(course5)
# education3.mandatory_courses.append(course7)
# education3.mandatory_courses.append(course8)
# education3.mandatory_courses.append(course12)
# education3.mandatory_courses.append(course13)
# education3.mandatory_courses.append(course14)
# education3.mandatory_courses.append(course15)
# education3.mandatory_courses.append(course16)
# education3.mandatory_courses.append(course17)

# =============== Mandatory courses för Ekonomi ======================
# education4.mandatory_courses.append(course1)
# education4.mandatory_courses.append(course2)
# education4.mandatory_courses.append(course3)
# education4.mandatory_courses.append(course4)
# education4.mandatory_courses.append(course5)
# education4.mandatory_courses.append(course7)
# education4.mandatory_courses.append(course8)
# education4.mandatory_courses.append(course9)
# education4.mandatory_courses.append(course12)
# education4.mandatory_courses.append(course13)
# education4.mandatory_courses.append(course14)
# education4.mandatory_courses.append(course15)
# education4.mandatory_courses.append(course16)
# education4.mandatory_courses.append(course17)
# education4.mandatory_courses.append(course24)


db.session.commit()

# =============== Mandatory courses för Natur ======================
natc1 = Mandatory(edumand=education1.id, coumand=course1.id)
natc2 = Mandatory(edumand=education1.id, coumand=course2.id)
natc3 = Mandatory(edumand=education1.id, coumand=course3.id)
natc4 = Mandatory(edumand=education1.id, coumand=course4.id)
natc5 = Mandatory(edumand=education1.id, coumand=course5.id)
natc6 = Mandatory(edumand=education1.id, coumand=course7.id)
natc7 = Mandatory(edumand=education1.id, coumand=course8.id)
natc8 = Mandatory(edumand=education1.id, coumand=course9.id)
natc9 = Mandatory(edumand=education1.id, coumand=course10.id)
natc10 = Mandatory(edumand=education1.id, coumand=course12.id)
natc11 = Mandatory(edumand=education1.id, coumand=course14.id)
natc12 = Mandatory(edumand=education1.id, coumand=course16.id)
natc13 = Mandatory(edumand=education1.id, coumand=course18.id)
natc14 = Mandatory(edumand=education1.id, coumand=course19.id)
natc15 = Mandatory(edumand=education1.id, coumand=course20.id)
natc16 = Mandatory(edumand=education1.id, coumand=course21.id)
natc17 = Mandatory(edumand=education1.id, coumand=course22.id)
natc18 = Mandatory(edumand=education1.id, coumand=course23.id)
natc19 = Mandatory(edumand=education1.id, coumand=course25.id)
natc20 = Mandatory(edumand=education1.id, coumand=course29.id)
natc21 = Mandatory(edumand=education1.id, coumand=course53.id)

# =============== Mandatory courses för Teknik ======================
tekc1 = Mandatory(edumand=education2.id, coumand=course1.id)
tekc2 = Mandatory(edumand=education2.id, coumand=course2.id)
tekc3 = Mandatory(edumand=education2.id, coumand=course3.id)
tekc4 = Mandatory(edumand=education2.id, coumand=course4.id)
tekc5 = Mandatory(edumand=education2.id, coumand=course5.id)
tekc6 = Mandatory(edumand=education2.id, coumand=course7.id)
tekc7 = Mandatory(edumand=education2.id, coumand=course8.id)
tekc8 = Mandatory(edumand=education2.id, coumand=course9.id)
tekc9 = Mandatory(edumand=education2.id, coumand=course10.id)
tekc10 = Mandatory(edumand=education2.id, coumand=course12.id)
tekc11 = Mandatory(edumand=education2.id, coumand=course14.id)
tekc12 = Mandatory(edumand=education2.id, coumand=course16.id)
tekc13 = Mandatory(edumand=education2.id, coumand=course20.id)
tekc14 = Mandatory(edumand=education2.id, coumand=course22.id)
tekc15 = Mandatory(edumand=education2.id, coumand=course23.id)
tekc16 = Mandatory(edumand=education2.id, coumand=course25.id)
tekc17 = Mandatory(edumand=education2.id, coumand=course29.id)
tekc18 = Mandatory(edumand=education2.id, coumand=course31.id)
tekc19 = Mandatory(edumand=education2.id, coumand=course32.id)
tekc20 = Mandatory(edumand=education2.id, coumand=course34.id)
tekc21 = Mandatory(edumand=education2.id, coumand=course53.id)

# =============== Mandatory courses för Sam ======================
samc1 = Mandatory(edumand=education3.id, coumand=course1.id)
samc2 = Mandatory(edumand=education3.id, coumand=course2.id)
samc3 = Mandatory(edumand=education3.id, coumand=course3.id)
samc4 = Mandatory(edumand=education3.id, coumand=course4.id)
samc5 = Mandatory(edumand=education3.id, coumand=course5.id)
samc6 = Mandatory(edumand=education3.id, coumand=course26.id)
samc7 = Mandatory(edumand=education3.id, coumand=course27.id)
samc8 = Mandatory(edumand=education3.id, coumand=course12.id)
samc9 = Mandatory(edumand=education3.id, coumand=course13.id)
samc10 = Mandatory(edumand=education3.id, coumand=course14.id)
samc11 = Mandatory(edumand=education3.id, coumand=course15.id)
samc12 = Mandatory(edumand=education3.id, coumand=course16.id)
samc13 = Mandatory(edumand=education3.id, coumand=course17.id)
samc14 = Mandatory(edumand=education3.id, coumand=course25.id)
samc15 = Mandatory(edumand=education3.id, coumand=course29.id)
samc16 = Mandatory(edumand=education3.id, coumand=course35.id)
samc17 = Mandatory(edumand=education3.id, coumand=course43.id)
samc18 = Mandatory(edumand=education3.id, coumand=course44.id)
samc19 = Mandatory(edumand=education3.id, coumand=course45.id)
samc20 = Mandatory(edumand=education3.id, coumand=course46.id)
samc21 = Mandatory(edumand=education3.id, coumand=course53.id)

# =============== Mandatory courses för Ekonomi ======================
ekoc1 = Mandatory(edumand=education4.id, coumand=course1.id)
ekoc2 = Mandatory(edumand=education4.id, coumand=course2.id)
ekoc3 = Mandatory(edumand=education4.id, coumand=course3.id)
ekoc4 = Mandatory(edumand=education4.id, coumand=course4.id)
ekoc5 = Mandatory(edumand=education4.id, coumand=course5.id)
ekoc6 = Mandatory(edumand=education4.id, coumand=course26.id)
ekoc7 = Mandatory(edumand=education4.id, coumand=course27.id)
ekoc8 = Mandatory(edumand=education4.id, coumand=course28.id)
ekoc9 = Mandatory(edumand=education4.id, coumand=course12.id)
ekoc10 = Mandatory(edumand=education4.id, coumand=course13.id)
ekoc11 = Mandatory(edumand=education4.id, coumand=course14.id)
ekoc12 = Mandatory(edumand=education4.id, coumand=course15.id)
ekoc13 = Mandatory(edumand=education4.id, coumand=course16.id)
ekoc14 = Mandatory(edumand=education4.id, coumand=course17.id)
ekoc15 = Mandatory(edumand=education4.id, coumand=course41.id)
ekoc16 = Mandatory(edumand=education4.id, coumand=course25.id)
ekoc17 = Mandatory(edumand=education4.id, coumand=course29.id)
ekoc18 = Mandatory(edumand=education4.id, coumand=course36.id)
ekoc19 = Mandatory(edumand=education4.id, coumand=course37.id)
ekoc20 = Mandatory(edumand=education4.id, coumand=course40.id)
ekoc21 = Mandatory(edumand=education4.id, coumand=course53.id)


db.session.add(natc1)
db.session.add(natc2)
db.session.add(natc3)
db.session.add(natc4)
db.session.add(natc5)
db.session.add(natc6)
db.session.add(natc7)
db.session.add(natc8)
db.session.add(natc9)
db.session.add(natc10)
db.session.add(natc11)
db.session.add(natc12)
db.session.add(natc13)
db.session.add(natc14)
db.session.add(natc15)
db.session.add(natc16)
db.session.add(natc17)
db.session.add(natc18)
db.session.add(natc19)
db.session.add(natc20)
db.session.add(natc21)
db.session.add(tekc1)
db.session.add(tekc2)
db.session.add(tekc3)
db.session.add(tekc4)
db.session.add(tekc5)
db.session.add(tekc6)
db.session.add(tekc7)
db.session.add(tekc8)
db.session.add(tekc9)
db.session.add(tekc10)
db.session.add(tekc11)
db.session.add(tekc12)
db.session.add(tekc13)
db.session.add(tekc14)
db.session.add(tekc15)
db.session.add(tekc16)
db.session.add(tekc17)
db.session.add(tekc18)
db.session.add(tekc19)
db.session.add(tekc20)
db.session.add(tekc21)
db.session.add(samc1)
db.session.add(samc2)
db.session.add(samc3)
db.session.add(samc4)
db.session.add(samc5)
db.session.add(samc6)
db.session.add(samc7)
db.session.add(samc8)
db.session.add(samc9)
db.session.add(samc10)
db.session.add(samc11)
db.session.add(samc12)
db.session.add(samc13)
db.session.add(samc14)
db.session.add(samc15)
db.session.add(samc16)
db.session.add(samc17)
db.session.add(samc18)
db.session.add(samc19)
db.session.add(samc20)
db.session.add(samc21)
db.session.add(ekoc1)
db.session.add(ekoc2)
db.session.add(ekoc3)
db.session.add(ekoc4)
db.session.add(ekoc5)
db.session.add(ekoc6)
db.session.add(ekoc7)
db.session.add(ekoc8)
db.session.add(ekoc9)
db.session.add(ekoc10)
db.session.add(ekoc11)
db.session.add(ekoc12)
db.session.add(ekoc13)
db.session.add(ekoc14)
db.session.add(ekoc15)
db.session.add(ekoc16)
db.session.add(ekoc17)
db.session.add(ekoc18)
db.session.add(ekoc19)
db.session.add(ekoc20)
db.session.add(ekoc21)


db.session.commit()
exit()
