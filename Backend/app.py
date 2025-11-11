from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Internship

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

    # Add sample internships if empty
    if Internship.query.count() == 0:
        samples = [
            Internship(company="Google", role="Software Engineering Intern", duration="3 months", status="Completed"),
            Internship(company="Microsoft", role="Data Science Intern", duration="2 months", status="Ongoing"),
            Internship(company="Amazon", role="Cloud Computing Intern", duration="4 months", status="Completed"),
            Internship(company="Infosys", role="Web Developer Intern", duration="2 months", status="Ongoing"),
            Internship(company="TCS", role="Cybersecurity Intern", duration="3 months", status="Ongoing"),
        ]
        db.session.add_all(samples)
        db.session.commit()


@app.route("/internships", methods=["GET"])
def get_internships():
    internships = Internship.query.all()
    return jsonify([{
        "id": i.id,
        "company": i.company,
        "role": i.role,
        "duration": i.duration,
        "status": i.status
    } for i in internships])


@app.route("/internships", methods=["POST"])
def add_internship():
    data = request.json
    new_intern = Internship(
        company=data["company"],
        role=data["role"],
        duration=data["duration"],
        status=data["status"]
    )
    db.session.add(new_intern)
    db.session.commit()
    return jsonify({"message": "Internship added successfully!"})


@app.route("/internships/<int:id>", methods=["DELETE"])
def delete_internship(id):
    internship = Internship.query.get(id)
    if internship:
        db.session.delete(internship)
        db.session.commit()
        return jsonify({"message": "Internship deleted!"})
    return jsonify({"error": "Not found"}), 404


@app.route("/internships/<int:id>", methods=["PATCH"])
def update_internship(id):
    internship = Internship.query.get(id)
    if not internship:
        return jsonify({"error": "Not found"}), 404
    data = request.json
    if "status" in data:
        internship.status = data["status"]
    if "company" in data:
        internship.company = data["company"]
    if "role" in data:
        internship.role = data["role"]
    if "duration" in data:
        internship.duration = data["duration"]
    db.session.commit()
    return jsonify({"message": "Internship updated!"})


if __name__ == "__main__":
    app.run(debug=True)
