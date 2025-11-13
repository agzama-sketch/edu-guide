from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///universities.db'
db = SQLAlchemy(app)

class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    field = db.Column(db.String(50), nullable=False)

@app.before_request
def setup_db():
    db.drop_all()
    db.create_all()
    if not University.query.first():
        universities = [
            ("Massachusetts Institute of Technology (MIT) — USA", "Technology"),
            ("Imperial College London — UK", "Engineering"),
            ("University of Oxford — UK", "Humanities"),
            ("Harvard University — USA", "Medicine"),
            ("University of Cambridge — UK", "Science"),
            ("Stanford University — USA", "Engineering"),
            ("ETH Zürich – Swiss Federal Institute of Technology — Switzerland", "Engineering"),
            ("National University of Singapore (NUS) — Singapore", "Technology"),
            ("University College London (UCL) — UK", "Science"),
            ("California Institute of Technology (Caltech) — USA", "Technology"),
            ("University of Pennsylvania (Penn) — USA", "Business"),
            ("University of California, Berkeley (UCB) — USA", "Technology"),
            ("The University of Melbourne (UniMelb) — Australia", "Medicine"),
            ("Peking University (PKU) — China", "Science"),
            ("Nanyang Technological University, Singapore (NTU) — Singapore", "Technology"),
            ("Cornell University — USA", "Engineering"),
            ("The University of Hong Kong (HKU) — Hong Kong", "Medicine"),
            ("The University of Sydney (USyd) — Australia", "Medicine"),
            ("The University of New South Wales (UNSW Sydney) — Australia", "Science"),
            ("Tsinghua University — China", "Engineering"),
            ("University of Chicago — USA", "Business"),
            ("Princeton University — USA", "Mathematics"),
            ("Yale University — USA", "Humanities"),
            ("Université PSL — France", "Science"),
            ("University of Toronto (U of T) — Canada", "Science"),
            ("École Polytechnique Fédérale de Lausanne (EPFL) — Switzerland", "Engineering"),
            ("The University of Edinburgh (UoE) — UK", "Humanities"),
            ("Technical University of Munich (TUM) — Germany", "Engineering"),
            ("McGill University — Canada", "Medicine"),
            ("Australian National University (ANU) — Australia", "Science"),
            ("Seoul National University (SNU) — South Korea", "Technology"),
            ("Johns Hopkins University (JHU) — USA", "Medicine"),
            ("The University of Tokyo (UTokyo) — Japan", "Science"),
            ("Columbia University — USA", "Business"),
            ("The University of Manchester (UoM) — UK", "Science"),
            ("The Chinese University of Hong Kong (CUHK) — Hong Kong", "Science"),
            ("Monash University — Australia", "Medicine"),
            ("University of British Columbia (UBC) — Canada", "Science"),
            ("Fudan University — China", "Business"),
            ("King's College London (KCL) — UK", "Medicine"),
            ("The University of Queensland (UQ) — Australia", "Science"),
            ("University of California, Los Angeles (UCLA) — USA", "Technology"),
            ("New York University (NYU) — USA", "Business"),
            ("University of Michigan-Ann Arbor — USA", "Engineering"),
            ("Shanghai Jiao Tong University (SJTU) — China", "Engineering"),
            ("Institut Polytechnique de Paris (IP Paris) — France", "Engineering"),
            ("The Hong Kong University of Science and Technology (HKUST) — Hong Kong", "Technology"),
            ("Zhejiang University (ZJU) — China", "Technology"),
            ("Delft University of Technology (TU Delft) — Netherlands", "Engineering"),
            ("Kyoto University — Japan", "Science"),
            ("Northwestern University — USA", "Business"),
            ("The London School of Economics and Political Science (LSE) — UK", "Social Sciences"),
            ("KAIST - Korea Advanced Institute of Science & Technology — South Korea", "Technology"),
            ("University of Bristol — UK", "Science"),
            ("University of Amsterdam (UvA) — Netherlands", "Social Sciences"),
            ("Yonsei University — South Korea", "Business"),
            ("The Hong Kong Polytechnic University (PolyU) — Hong Kong", "Engineering"),
            ("Carnegie Mellon University (CMU) — USA", "Technology"),
            ("Ludwig-Maximilians-Universität München (LMU) — Germany", "Humanities"),
            ("Universiti Malaya (UM) — Malaysia", "Medicine"),
            ("Duke University — USA", "Medicine"),
            ("City University of Hong Kong (CityU) — Hong Kong", "Technology"),
            ("KU Leuven — Belgium", "Science"),
            ("Sorbonne University — France", "Humanities"),
            ("The University of Auckland — New Zealand", "Science"),
            ("University of Texas at Austin (UT Austin) — USA", "Engineering"),
            ("Korea University — South Korea", "Technology"),
            ("National Taiwan University (NTU) — Taiwan", "Science"),
            ("The University of Warwick — UK", "Business"),
            ("University of Illinois Urbana-Champaign — USA", "Engineering"),
            ("Universidad de Buenos Aires (UBA) — Argentina", "Social Sciences"),
            ("University of California, San Diego (UCSD) — USA", "Technology"),
            ("Université Paris-Saclay — France", "Science"),
            ("KTH Royal Institute of Technology — Sweden", "Engineering"),
            ("Lund University — Sweden", "Science"),
            ("University of Washington — USA", "Medicine"),
            ("The University of Western Australia (UWA) — Australia", "Medicine"),
            ("University of Glasgow — UK", "Science"),
            ("Brown University — USA", "Humanities"),
            ("University of Birmingham — UK", "Science"),
            ("University of Southampton — UK", "Engineering"),
            ("The University of Adelaide — Australia", "Science"),
            ("University of Leeds — UK", "Business"),
            ("Universität Heidelberg — Germany", "Medicine"),
            ("Tokyo Institute of Technology (Tokyo Tech) — Japan", "Technology"),
            ("Osaka University — Japan", "Science"),
            ("Trinity College Dublin — Ireland", "Humanities"),
            ("University of Technology Sydney (UTS) — Australia", "Technology"),
            ("Durham University — UK", "Humanities"),
            ("Pennsylvania State University (Penn State) — USA", "Engineering"),
            ("Purdue University — USA", "Engineering"),
            ("Universidade de São Paulo (USP) — Brazil", "Science"),
            ("Pontificia Universidad Católica de Chile (UC) — Chile", "Humanities"),
            ("Lomonosov Moscow State University (MSU) — Russia", "Science"),
            ("Universidad Nacional Autónoma de México (UNAM) — Mexico", "Social Sciences"),
            ("University of Alberta — Canada", "Science"),
            ("Freie Universitaet Berlin — Germany", "Humanities"),
            ("Pohang University of Science And Technology (POSTECH) — South Korea", "Technology"),
            ("RWTH Aachen University — Germany", "Engineering"),
            ("University of Copenhagen — Denmark", "Science"),
        ]
        for i, (name, field) in enumerate(universities, start=1):
            ranked_name = f"{i}. {name}"
            db.session.add(University(name=ranked_name, field=field))
        db.session.commit()

@app.route('/')
def index():
    field = request.args.get("field", "all")
    query = University.query
    if field != "all":
        query = query.filter_by(field=field)
    universities = query.all()

    fields = [
        "all", "Technology", "Medicine", "Business", "Engineering",
        "Science", "Law", "Education", "Economics", "Mathematics",
        "Social Sciences", "Philosophy", "Humanities", "Biology",
        "Computer Science", "Public Health", "Architecture"
    ]
    return render_template(
        "index.html",
        universities=universities,
        fields=fields,
        selected_field=field,
        active_page="home"
    )
@app.route('/create')
def create():
    return render_template("create.html", active_page="create")

@app.route('/research')
def research():
    return render_template('research.html', active_page="research")

@app.route('/ask')
def ask():
    return render_template('ask.html', active_page="ask")

@app.route('/answer', methods=['POST'])
def answer():
    answers = [request.form.get(f'q{i}') for i in range(1, 6)]
    counts = {}
    for a in answers:
        if a:
            counts[a] = counts.get(a, 0) + 1
    if not counts:
        result = "Unknown"
        description = "Please answer at least one question!"
    else:
        result = max(counts, key=counts.get)
        descriptions = {
            "Engineering": "You love making, creating, and solving real-world problems. Engineering is a great choice for you!",
            "Medicine": "You care about others and are interested in how the human body works. Medicine is a great choice for you!",
            "Business": "You’re confident, organized, and communicative. Business, management, or finance are a great choices for you!",
            "Science and computer science": "You enjoy thinking, asking questions, and discovering how things work. Science or computer science are a great choices for you!",
            "Humanities": "You are creative and like thinking about people and ideas. Humanities, social studies, or art are a great choices for you!"
        }
        description = descriptions.get(result)

    return render_template('answer.html', result=result.capitalize(), description=description)

if __name__ == '__main__':
    app.run(debug=True)
