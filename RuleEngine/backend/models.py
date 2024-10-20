from database import db

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String(255), nullable=False)
    ast = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Rule {self.rule_string}>"
