from crypt import methods
from email import message
import json
from operator import truediv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

from flask import Flask, jsonify, request, abort
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)


app = Flask(__name__, static_folder="../client", static_url_path="/")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "abc123"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


@app.route("/")
def client():
    return app.send_static_file("client.html")


# ----------------------------------------------------------------------------------------
# =========================== CLASS USER STARTING ====================================
# ----------------------------------------------------------------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    birthdate = db.Column(db.Integer, nullable=False)
    education = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    current_average = db.Column(db.Float, nullable=True)
    has_finished = db.relationship("Finished", backref="usefin", lazy=True)
    request_course = db.relationship(
        "Request_course", backref="user_cou_req", lazy=True
    )
    request_other = db.relationship("Request_other", backref="user_oth_req", lazy=True)


def __repr__(self):
    return "<User {}: {} {} {} {} {}".format(
        self.id,
        self.name,
        self.grade,
        self.birthdate,
        self.education,
        self.current_average,
    )


def serialize_user(self):
    return dict(
        id=self.id,
        name=self.name,
        email=self.email,
        grade=self.grade,
        birthdate=self.birthdate,
        education=self.education,
        password_hash=self.password_hash,
        current_average=self.current_average,
    )


# ----------------------------------------------------------------------------------------
# =========================== CLASS USER ENDING ====================================
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# =========================== CLASS COURSE STARTING ====================================
# ----------------------------------------------------------------------------------------
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_title = db.Column(db.String, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    mandatory_for = db.relationship("Mandatory", backref="coum", lazy=True)
    optional_for = db.relationship("Optional", backref="couo", lazy=True)
    finished_by = db.relationship("Finished", backref="fincou", lazy=True)


def __repr__(self):
    return "<Course {}: {} {}".format(self.id, self.course_title, self.points)


def serialize_course(self):
    return dict(id=self.id, course_title=self.course_title, points=self.points)


# ----------------------------------------------------------------------------------------
# =========================== CLASS COURSE ENDING ====================================
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# =========================== CLASS EDUCATION STARTING ====================================
# ----------------------------------------------------------------------------------------
class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    edu_name = db.Column(db.String, nullable=False)
    mandatory_courses = db.relationship("Mandatory", backref="edum", lazy=True)
    optional_courses = db.relationship("Optional", backref="eduo", lazy=True)


def __repr__(self):
    return "<Education {}: {}".format(self.id, self.edu_name)


def serialize_education(self):
    return dict(id=self.id, edu_name=self.edu_name)


# ----------------------------------------------------------------------------------------
# =========================== CLASS EDUCATION ENDING ====================================
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# =========================== CLASS MANDATORY STARTING ====================================
# ----------------------------------------------------------------------------------------
class Mandatory(db.Model):
    edumand = db.Column(db.Integer, db.ForeignKey("education.id"), primary_key=True)
    coumand = db.Column(db.Integer, db.ForeignKey("course.id"), primary_key=True)


def __repr__(self):
    return "Mandatory: {}: {}".format(self.edumand, self.coumand)


def serialize_mandatory(self):
    return dict(edumand=self.edumand, coumand=self.coumand)


# ----------------------------------------------------------------------------------------
# =========================== CLASS MANDATORY ENDING ====================================
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# =========================== CLASS OPTIONAL STARTING ====================================
# ----------------------------------------------------------------------------------------
class Optional(db.Model):
    eduopt = db.Column(db.Integer, db.ForeignKey("education.id"), primary_key=True)
    couopt = db.Column(db.Integer, db.ForeignKey("course.id"), primary_key=True)


def __repr__(self):
    return "Optional: {}: {}".format(self.eduopt, self.couopt)


def serialize_optional(self):
    return dict(eduopt=self.eduopt, couopt=self.couopt)


# ----------------------------------------------------------------------------------------
# =========================== CLASS OPTIONAL ENDING ====================================
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# =========================== CLASS FINNISHED STARTING ====================================
# ----------------------------------------------------------------------------------------
class Finished(db.Model):
    finished_student = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    finished_course = db.Column(
        db.Integer, db.ForeignKey("course.id"), primary_key=True
    )
    final_grade = db.Column(db.String(1), nullable=False)


def __repr__(self):
    return "Optional: {}: {} {}".format(
        self.finished_student, self.finished_course, self.final_grade
    )


def serialize_finished(self):
    return dict(
        finished_student=self.finished_student,
        finished_course=self.finished_course,
        final_grade=self.final_grade,
    )


# ----------------------------------------------------------------------------------------
# =========================== CLASS FINNISHED ENDING ====================================
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# =========================== CLASS COURSE REQUEST STARTING ====================================
# ----------------------------------------------------------------------------------------
class Request_course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_title = db.Column(db.String, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    kommun = db.Column(db.String, nullable=False)
    school = db.Column(db.String, nullable=False)
    student = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


def __repr__(self):
    return "Request_course: {}: {} {} {}".format(
        self.id, self.course_title, self.points, self.kommun, self.school
    )


def serialize_requested_course(self):
    return dict(
        id=self.id,
        course_title=self.course_title,
        points=self.points,
        kommun=self.kommun,
        school=self.school,
        student=self.student,
    )


# ----------------------------------------------------------------------------------------
# =========================== CLASS COURSE REQUEST ENDING ====================================
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# =========================== CLASS OTHER REQUEST ENDING ====================================
# ----------------------------------------------------------------------------------------


class Request_other(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_type = db.Column(db.String(8), nullable=False)
    message = db.Column(db.String, nullable=False)
    student = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


def __repr__(self):
    return "Request_other: {}: {} {} {}".format(
        self.id, self.request_type, self.message, self.student
    )


def serialize_requested_other(self):
    return dict(
        id=self.id,
        request_type=self.request_type,
        message=self.message,
        student=self.student,
    )


# ----------------------------------------------------------------------------------------
# =========================== CLASS OTHER REQUEST ENDING ====================================
# ----------------------------------------------------------------------------------------

# ################################################################################
# ################################## METHODS #####################################
# ################################################################################
def set_password(self, password):
    self.password_hash = bcrypt.generate_password_hash(password).decode("utf8")


def calc_snitt(coursepoints, grades):

    coursetimesgrade = 0
    returnval = 0
    totpoints = 0
    nrofcourses = len(coursepoints)
    for i in range(nrofcourses):
        totpoints = totpoints + coursepoints[i]
        if grades[i] == "E":
            coursetimesgrade = coursetimesgrade + coursepoints[i] * 10
        elif grades[i] == "D":
            coursetimesgrade = coursetimesgrade + coursepoints[i] * 12.5
        elif grades[i] == "C":
            coursetimesgrade = coursetimesgrade + coursepoints[i] * 15
        elif grades[i] == "B":
            coursetimesgrade = coursetimesgrade + coursepoints[i] * 17.5
        elif grades[i] == "A":
            coursetimesgrade = coursetimesgrade + coursepoints[i] * 20
        else:
            coursetimesgrade = coursetimesgrade + 0
    returnval = coursetimesgrade / totpoints
    return float(returnval)


def savefin(uid, cid, g):
    fin = Finished(finished_student=uid, finished_course=cid, final_grade=g)
    db.session.add(fin)


def recursive_gradecalc_all_new(av_goal, coursepoints, grades, available_grades, merit):
    loopsize = int(len(coursepoints))
    for i in available_grades:
        for j in range(loopsize):
            grades[j] = i
            if float(calc_snitt(coursepoints, grades)) + float(merit) >= av_goal:
                return jsonify(grades)
    return "Funkade inte"


def recursive_gradecalc_av_exists(
    av_goal, coursepoints, grades, available_grades, merit, breakpointindex
):
    loopsize = int(len(coursepoints))
    for i in available_grades:
        for j in range(breakpointindex, loopsize):
            grades[j] = i
            if float(calc_snitt(coursepoints, grades)) + float(merit) >= av_goal:
                new_grades = []
                for k in range(breakpointindex, loopsize):
                    new_grades.append(grades[k])
                return jsonify(new_grades)


# //////////////////////////////////////////////////////////////
# /////////////////// ROUTES ALL THE WAY ///////////////////////
# //////////////////////////////////////////////////////////////
@app.route("/users", methods=["GET", "POST"])
def users():

    if request.method == "GET":

        all_students_returned = []
        all_students = User.query.all()
        if all_students == null:
            return "NO students sir"
        else:
            for i in all_students:
                s = serialize_user(i)
                all_students_returned.append(s)
            return jsonify(all_students_returned)
    if request.method == "POST":
        student_data = request.get_json()
        new_student = User(
            name=student_data["name"],
            email=student_data["email"],
            grade=student_data["grade"],
            birthdate=student_data["birthdate"],
            education=student_data["education"],
        )
        db.session.add(new_student)
        db.session.commit()
        return "You Added a fella!"


@app.route("/users/<int:user_id>", methods=["GET", "PUT"])
def user(user_id):
    this_user = User.query.filter_by(id=user_id).first()
    if request.method == "GET":

        if this_user == None:
            abort(404)
        else:
            return jsonify(serialize_user(this_user))
    elif request.method == "PUT":
        if request.get_json(force=True).get("email", False):
            setattr(this_user, "email", request.get_json()["email"])
        if request.get_json(force=True).get("current_average", False):
            setattr(this_user, "current_average", request.get_json()["current_average"])
        db.session.commit()
        return jsonify(serialize_user(this_user))


@app.route("/users/<int:user_id>/finished", methods=["POST", "GET"])
def finished(user_id):
    if request.method == "POST":
        this_user = User.query.filter_by(id=user_id).first()
        courses = []
        grades = []
        resp = "startval"
        if this_user == None:
            abort(404)
        else:
            data = request.get_json()
            loopsize = int(len(data) / 2)
            for i in range(loopsize):
                ct = data["nc" + str(i)]
                c = Course.query.filter_by(course_title=ct).first()
                cnr = c.id
                courses.append(cnr)
            for i in range(loopsize):
                grades.append(data["ng" + str(i)])
            if len(courses) == len(set(courses)):
                for i in range(loopsize):
                    coursenr = courses[i]
                    gradeval = grades[i]
                    savefin(user_id, coursenr, gradeval)
                resp = "ok"
                db.session.commit()
                return jsonify(resp)
            else:
                resp = "duplicate"
                return jsonify(resp)
    elif request.method == "GET":
        myfin_cou = []
        allfin = Finished.query.all()
        for i in allfin:
            if i.finished_student == user_id:
                cid = i.finished_course
                cou = Course.query.filter_by(id=cid).first()
                ct = cou.course_title
                myfin_cou.append(ct)
        return jsonify(myfin_cou)


@app.route("/users/<int:user_id>/points", methods=["GET"])
def points(user_id):
    if request.method == "GET":
        myfin_points = []
        allfin = Finished.query.all()
        for i in allfin:
            if i.finished_student == user_id:
                cid = i.finished_course
                cou = Course.query.filter_by(id=cid).first()
                cp = cou.points
                myfin_points.append(cp)
        return jsonify(myfin_points)


@app.route("/users/<int:user_id>/grades", methods=["GET"])
def grades(user_id):
    if request.method == "GET":
        myfin_grades = []
        allfin = Finished.query.all()
        for i in allfin:
            if i.finished_student == user_id:
                cg = i.final_grade
                myfin_grades.append(cg)
        return jsonify(myfin_grades)


@app.route("/signup", methods=["POST"])
def signup():
    if request.method == "POST":
        data = request.get_json()
        new_user = User(
            name=data["name"],
            email=data["email"],
            grade=data["grade"],
            birthdate=data["birthdate"],
            education=data["education"],
        )
        set_password(new_user, data["password"])
        db.session.add(new_user)
        db.session.commit()
        return serialize_user(new_user)


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        user = User.query.filter_by(email=data["email"]).first()
        if user == None:
            abort(401)
        else:
            if bcrypt.check_password_hash(user.password_hash, data["password"]):
                access_token = create_access_token(identity=user.id)
                output_list = {"token": access_token, "user": serialize_user(user)}
                return jsonify(output_list)
            else:
                abort(401)


@app.route("/educations", methods=["GET"])
def educations():
    if request.method == "GET":
        educations_to_return = []
        all_educations = Education.query.all()
        for i in all_educations:
            e = serialize_education(i)
            educations_to_return.append(e)
        return jsonify(educations_to_return)


@app.route("/courses", methods=["GET"])
def courses():
    if request.method == "GET":
        courses_to_return = []
        all_courses = Course.query.all()
        for i in all_courses:
            c = serialize_course(i)
            courses_to_return.append(c)
        return jsonify(courses_to_return)


@app.route("/mandatorys", methods=["GET"])
def mandatorys():
    if request.method == "GET":
        mandlist = []
        m = Mandatory.query.all()
        for i in m:
            a = serialize_mandatory(i)
            mandlist.append(a)
        return jsonify(mandlist)


@app.route("/user/<int:user_id>/mand", methods=["GET"])
def user_mand(user_id):
    if request.method == "GET":
        u = User.query.filter_by(id=user_id).first()
        if u == None:
            abort(401)
        else:
            m_courses = []
            u_ed = u.education
            edu = Education.query.filter_by(edu_name=u_ed).first()
            eid = edu.id
            allmand = Mandatory.query.all()
            for m in allmand:
                em = m.edumand
                if em == eid:
                    course_id_this = m.coumand
                    course_this = Course.query.filter_by(id=course_id_this).first()
                    this_cou_title = course_this.course_title
                    m_courses.append(this_cou_title)
        return jsonify(m_courses)


@app.route("/user/<int:user_id>/mand/points", methods=["GET"])
def user_mand_points(user_id):
    if request.method == "GET":
        u = User.query.filter_by(id=user_id).first()
        if u == None:
            abort(401)
        else:
            m_courses_points = []
            u_ed = u.education
            edu = Education.query.filter_by(edu_name=u_ed).first()
            eid = edu.id
            allmand = Mandatory.query.all()
            for m in allmand:
                em = m.edumand
                if em == eid:
                    course_id_this = m.coumand
                    course_this = Course.query.filter_by(id=course_id_this).first()
                    this_cou_points = course_this.points
                    m_courses_points.append(this_cou_points)
        return jsonify(m_courses_points)


@app.route("/users/<int:user_id>/mand/finished", methods=["GET"])
def mand_finished(user_id):
    # data = request.get_json()
    if request.method == "GET":
        mymand_fin = []
        u = User.query.filter_by(id=user_id).first()
        uid = u.id
        if u == None:
            abort(401)
        else:
            ued = u.education
            edu = Education.query.filter_by(edu_name=ued).first()
            eid = edu.id
            allmand = Mandatory.query.filter_by(edumand=eid)
            allmandcou = []
            allfinished = Finished.query.all()
            finished_by_user = []
            for i in allfinished:
                if i.finished_student == uid:
                    finished_by_user.append(i)

            finished_by_user_cou = []
            for x in finished_by_user:
                y = x.finished_course
                finished_by_user_cou.append(y)
            for i in allmand:
                m = i.coumand
                allmandcou.append(m)
            for j in allmandcou:
                if j in finished_by_user_cou:
                    f = Finished.query.filter_by(finished_course=j).first()
                    g = f.final_grade
                    mymand_fin.append(g)
                else:
                    mymand_fin.append("---")
            return jsonify(mymand_fin)


@app.route("/average", methods=["POST"])
def average():
    if request.method == "POST":
        coulist = []
        points = []
        gradeslist = []
        allcou = Course.query.all()
        data = request.get_json()
        size = int(len(data) / 2)
        for i in range(size):
            coulist.append(data["v" + str(i)])
        for i in coulist:
            for j in allcou:
                serialize_course(j)
                if i == j.course_title:
                    p = j.points
                    points.append(p)
        for i in range(size):
            thisgrade = str(data["v" + str(size + i)])
            gradeslist.append(thisgrade)
        return jsonify(calc_snitt(points, gradeslist))


@app.route("/resetfinished/<int:user_id>", methods=["DELETE"])
def resetfinished(user_id):
    if request.method == "DELETE":
        Finished.query.filter_by(finished_student=user_id).delete()
        db.session.commit()
        return "Deletde"


@app.route("/users/<int:user_id>/mand/remaining", methods=["GET"])
def mand_remaining(user_id):
    remaining = []
    fincou = []
    if request.method == "GET":
        this_user = User.query.filter_by(id=user_id).first()
        edu_tit = this_user.education
        ed = Education.query.filter_by(edu_name=edu_tit).first()
        edu_id = ed.id
        allmand = Mandatory.query.filter_by(edumand=edu_id)
        this_fin = Finished.query.filter_by(finished_student=user_id)
        for i in this_fin:
            c = i.finished_course
            fincou.append(c)
        for i in allmand:
            if i.coumand not in fincou:
                course = Course.query.filter_by(id=i.coumand).first()
                ct = course.course_title
                remaining.append(ct)
        return jsonify(remaining)


@app.route("/users/<int:user_id>/all-remaining", methods=["GET"])
def all_remaining(user_id):
    course_ids = []
    finished_ids = []
    remaining = []
    all_courses = Course.query.all()
    this_fin = Finished.query.filter_by(finished_student=user_id)
    for i in all_courses:
        c_id = i.id
        course_ids.append(c_id)
    for i in this_fin:
        c = i.finished_course
        finished_ids.append(c)
    for i in course_ids:
        if i not in finished_ids:
            this_course = Course.query.filter_by(id=i).first()
            ct = this_course.course_title
            remaining.append(ct)
    return jsonify(remaining)


@app.route(
    "/users/<int:user_id>/required-grades/<float:req_average>/<float:final_merit>",
    methods=["POST"],
)
def required_grades(user_id, req_average, final_merit):
    if request.method == "POST":
        data = request.get_json()
        points = []
        first_gradelist = []

        this_user = User.query.filter_by(id=user_id).first()
        curr_average = this_user.current_average
        loopsize = int(len(data))
        for i in range(loopsize):
            c = data["r" + str(i)]
            this_course = Course.query.filter_by(course_title=c).first()
            p = this_course.points
            points.append(p)
            first_gradelist.append("F")
        available_grades = ["E", "D", "C", "B", "A"]
        if curr_average == None:
            check_total = 0
            for i in points:
                check_total = int(check_total) + int(i)
            if check_total < 2500:
                return jsonify("no")
            else:
                return recursive_gradecalc_all_new(
                    req_average, points, first_gradelist, available_grades, final_merit
                )
        else:
            all_coupoints = []
            all_grades = []
            finished_by_user = Finished.query.filter_by(finished_student=user_id)
            for i in finished_by_user:

                g = i.final_grade
                all_grades.append(g)
                cid = i.finished_course
                cou = Course.query.filter_by(id=cid).first()
                p = cou.points
                all_coupoints.append(p)
            old_courses_size = int(len(all_grades))
            for i in range(loopsize):
                new_c = data["r" + str(i)]
                new_course = Course.query.filter_by(course_title=new_c).first()
                point = new_course.points
                all_coupoints.append(point)
                all_grades.append("F")

            check_tot = 0
            for i in all_coupoints:
                check_tot = int(check_tot) + int(i)
            if check_tot < 2500:
                return jsonify("no")
            else:
                return recursive_gradecalc_av_exists(
                    req_average,
                    all_coupoints,
                    all_grades,
                    available_grades,
                    final_merit,
                    old_courses_size,
                )
            # return jsonify(old_courses_size)


@app.route("/contact-us/<int:user_id>/course-suggestion", methods=["POST"])
def course_suggestion(user_id):
    if request.method == "POST":
        data = request.get_json()
        this_user = User.query.filter_by(id=user_id).first()
        if this_user == None:
            return "none"
        else:
            new_sugg = Request_course(
                course_title=data["course_title"],
                points=data["points"],
                kommun=data["kommun"],
                school=data["school"],
                student=user_id,
            )
            db.session.add(new_sugg)
            db.session.commit()
            return serialize_requested_course(new_sugg)


@app.route("/contact-us/<int:user_id>/other-suggestion", methods=["POST"])
def other_suggestion(user_id):
    if request.method == "POST":
        data = request.get_json()
        this_user = User.query.filter_by(id=user_id).first()
        if this_user == None:
            return "none"
        else:
            new = Request_other(
                request_type=data["request_type"],
                message=data["message"],
                student=user_id,
            )
            db.session.add(new)
            db.session.commit()
            return serialize_requested_other(new)


if __name__ == "__main__":
    app.run(debug=True)
