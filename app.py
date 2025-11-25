from flask import Flask, render_template, request
app = Flask(__name__)

universities = [
    {"name": "1. Massachusetts Institute of Technology (MIT) — USA", "field": "Technology"},
    {"name": "2. Imperial College London — UK", "field": "Engineering"},
    {"name": "3. University of Oxford — UK", "field": "Humanities"},
    {"name": "4. Harvard University — USA", "field": "Medicine"},
    {"name": "5. University of Cambridge — UK", "field": "Science"},
    {"name": "6. Stanford University — USA", "field": "Engineering"},
    {"name": "7. ETH Zürich – Swiss Federal Institute of Technology — Switzerland", "field": "Engineering"},
    {"name": "8. National University of Singapore (NUS) — Singapore", "field": "Technology"},
    {"name": "9. University College London (UCL) — UK", "field": "Science"},
    {"name": "10. California Institute of Technology (Caltech) — USA", "field": "Technology"},
    {"name": "11. University of Pennsylvania (Penn) — USA", "field": "Business"},
    {"name": "12. University of California, Berkeley (UCB) — USA", "field": "Technology"},
    {"name": "13. The University of Melbourne (UniMelb) — Australia", "field": "Medicine"},
    {"name": "14. Peking University (PKU) — China", "field": "Science"},
    {"name": "15. Nanyang Technological University, Singapore (NTU) — Singapore", "field": "Technology"},
    {"name": "16. Cornell University — USA", "field": "Engineering"},
    {"name": "17. The University of Hong Kong (HKU) — Hong Kong", "field": "Medicine"},
    {"name": "18. The University of Sydney (USyd) — Australia", "field": "Medicine"},
    {"name": "19. The University of New South Wales (UNSW Sydney) — Australia", "field": "Science"},
    {"name": "20. Tsinghua University — China", "field": "Engineering"},
    {"name": "21. University of Chicago — USA", "field": "Business"},
    {"name": "22. Princeton University — USA", "field": "Mathematics"},
    {"name": "23. Yale University — USA", "field": "Humanities"},
    {"name": "24. Université PSL — France", "field": "Science"},
    {"name": "25. University of Toronto (U of T) — Canada", "field": "Science"},
    {"name": "26. École Polytechnique Fédérale de Lausanne (EPFL) — Switzerland", "field": "Engineering"},
    {"name": "27. The University of Edinburgh (UoE) — UK", "field": "Humanities"},
    {"name": "28. Technical University of Munich (TUM) — Germany", "field": "Engineering"},
    {"name": "29. McGill University — Canada", "field": "Medicine"},
    {"name": "30. Australian National University (ANU) — Australia", "field": "Science"},
    {"name": "31. Seoul National University (SNU) — South Korea", "field": "Technology"},
    {"name": "32. Johns Hopkins University (JHU) — USA", "field": "Medicine"},
    {"name": "33. The University of Tokyo (UTokyo) — Japan", "field": "Science"},
    {"name": "34. Columbia University — USA", "field": "Business"},
    {"name": "35. The University of Manchester (UoM) — UK", "field": "Science"},
    {"name": "36. The Chinese University of Hong Kong (CUHK) — Hong Kong", "field": "Science"},
    {"name": "37. Monash University — Australia", "field": "Medicine"},
    {"name": "38. University of British Columbia (UBC) — Canada", "field": "Science"},
    {"name": "39. Fudan University — China", "field": "Business"},
    {"name": "40. King's College London (KCL) — UK", "field": "Medicine"},
    {"name": "41. The University of Queensland (UQ) — Australia", "field": "Science"},
    {"name": "42. University of California, Los Angeles (UCLA) — USA", "field": "Technology"},
    {"name": "43. New York University (NYU) — USA", "field": "Business"},
    {"name": "44. University of Michigan-Ann Arbor — USA", "field": "Engineering"},
    {"name": "45. Shanghai Jiao Tong University (SJTU) — China", "field": "Engineering"},
    {"name": "46. Institut Polytechnique de Paris (IP Paris) — France", "field": "Engineering"},
    {"name": "47. The Hong Kong University of Science and Technology (HKUST) — Hong Kong", "field": "Technology"},
    {"name": "48. Zhejiang University (ZJU) — China", "field": "Technology"},
    {"name": "49. Delft University of Technology (TU Delft) — Netherlands", "field": "Engineering"},
    {"name": "50. Kyoto University — Japan", "field": "Science"},
    {"name": "51. Northwestern University — USA", "field": "Business"},
    {"name": "52. The London School of Economics and Political Science (LSE) — UK", "field": "Social Sciences"},
    {"name": "53. KAIST — South Korea", "field": "Technology"},
    {"name": "54. University of Bristol — UK", "field": "Science"},
    {"name": "55. University of Amsterdam (UvA) — Netherlands", "field": "Social Sciences"},
    {"name": "56. Yonsei University — South Korea", "field": "Business"},
    {"name": "57. The Hong Kong Polytechnic University (PolyU) — Hong Kong", "field": "Engineering"},
    {"name": "58. Carnegie Mellon University (CMU) — USA", "field": "Technology"},
    {"name": "59. Ludwig-Maximilians-Universität München (LMU) — Germany", "field": "Humanities"},
    {"name": "60. Universiti Malaya (UM) — Malaysia", "field": "Medicine"},
    {"name": "61. Duke University — USA", "field": "Medicine"},
    {"name": "62. City University of Hong Kong (CityU) — Hong Kong", "field": "Technology"},
    {"name": "63. KU Leuven — Belgium", "field": "Science"},
    {"name": "64. Sorbonne University — France", "field": "Humanities"},
    {"name": "65. The University of Auckland — New Zealand", "field": "Science"},
    {"name": "66. University of Texas at Austin (UT Austin) — USA", "field": "Engineering"},
    {"name": "67. Korea University — South Korea", "field": "Technology"},
    {"name": "68. National Taiwan University (NTU) — Taiwan", "field": "Science"},
    {"name": "69. The University of Warwick — UK", "field": "Business"},
    {"name": "70. University of Illinois Urbana-Champaign — USA", "field": "Engineering"},
    {"name": "71. Universidad de Buenos Aires (UBA) — Argentina", "field": "Social Sciences"},
    {"name": "72. University of California, San Diego (UCSD) — USA", "field": "Technology"},
    {"name": "73. Université Paris-Saclay — France", "field": "Science"},
    {"name": "74. KTH Royal Institute of Technology — Sweden", "field": "Engineering"},
    {"name": "75. Lund University — Sweden", "field": "Science"},
    {"name": "76. University of Washington — USA", "field": "Medicine"},
    {"name": "77. The University of Western Australia (UWA) — Australia", "field": "Medicine"},
    {"name": "78. University of Glasgow — UK", "field": "Science"},
    {"name": "79. Brown University — USA", "field": "Humanities"},
    {"name": "80. University of Birmingham — UK", "field": "Science"},
    {"name": "81. University of Southampton — UK", "field": "Engineering"},
    {"name": "82. The University of Adelaide — Australia", "field": "Science"},
    {"name": "83. University of Leeds — UK", "field": "Business"},
    {"name": "84. Universität Heidelberg — Germany", "field": "Medicine"},
    {"name": "85. Tokyo Institute of Technology (Tokyo Tech) — Japan", "field": "Technology"},
    {"name": "86. Osaka University — Japan", "field": "Science"},
    {"name": "87. Trinity College Dublin — Ireland", "field": "Humanities"},
    {"name": "88. University of Technology Sydney (UTS) — Australia", "field": "Technology"},
    {"name": "89. Durham University — UK", "field": "Humanities"},
    {"name": "90. Pennsylvania State University (Penn State) — USA", "field": "Engineering"},
    {"name": "91. Purdue University — USA", "field": "Engineering"},
    {"name": "92. Universidade de São Paulo (USP) — Brazil", "field": "Science"},
    {"name": "93. Pontificia Universidad Católica de Chile (UC) — Chile", "field": "Humanities"},
    {"name": "94. Lomonosov Moscow State University (MSU) — Russia", "field": "Science"},
    {"name": "95. Universidad Nacional Autónoma de México (UNAM) — Mexico", "field": "Social Sciences"},
    {"name": "96. University of Alberta — Canada", "field": "Science"},
    {"name": "97. Freie Universitaet Berlin — Germany", "field": "Humanities"},
    {"name": "98. Pohang University of Science And Technology (POSTECH) — South Korea", "field": "Technology"},
    {"name": "99. RWTH Aachen University — Germany", "field": "Engineering"},
    {"name": "100. University of Copenhagen — Denmark", "field": "Science"},
]
fields = [
    "all", "Technology", "Medicine", "Business", "Engineering",
    "Science", "Law", "Education", "Economics", "Mathematics",
    "Social Sciences", "Philosophy", "Humanities", "Biology",
    "Public Health", "Architecture"
]
@app.route('/')
def index():
    selected = request.args.get("field", "all")

    if selected == "all":
        filtered_universities = universities
    else:
        filtered_universities = [
            u for u in universities if u["field"] == selected
        ]
    return render_template(
        "index.html",
        universities=filtered_universities,
        fields=fields,
        selected_field=selected,
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