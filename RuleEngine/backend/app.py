from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Zakshada%4026@localhost/rule_engine_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Rule model
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_text = db.Column(db.Text, nullable=False)

# Initialize the database
with app.app_context():
    # Option A: Drop and recreate the table (use only if you can afford to lose data)
    db.drop_all()  # This will drop all tables
    db.create_all()  # This will create the tables again

    # Option B: If you want to keep the data, do not drop the table. 
    # Instead, run an ALTER TABLE command in your MySQL client to add the column.

# Create a rule
@app.route('/create-rule', methods=['POST'])
def create_rule():
    rule_data = request.json
    rule_text = rule_data.get('rule_text', '')
    if rule_text:
        new_rule = Rule(rule_text=rule_text)
        db.session.add(new_rule)
        db.session.commit()
        return jsonify({'message': 'Rule created successfully!', 'rule_id': new_rule.id})
    else:
        return jsonify({'message': 'No rule text provided'}), 400

# Modify a rule
@app.route('/modify-rule/<int:rule_id>', methods=['PUT'])
def modify_rule(rule_id):
    rule_data = request.json
    rule_text = rule_data.get('rule_text', '')
    rule = Rule.query.get(rule_id)
    if rule:
        rule.rule_text = rule_text
        db.session.commit()
        return jsonify({'message': 'Rule modified successfully!'})
    else:
        return jsonify({'message': 'Rule not found'}), 404

# Evaluate a rule (dummy evaluation for now)
@app.route('/evaluate-rule/<int:rule_id>', methods=['POST'])
def evaluate_rule(rule_id):
    user_data = request.json
    rule = Rule.query.get(rule_id)
    if rule:
        # Implement your rule evaluation logic here
        return jsonify({'message': 'Rule evaluated successfully', 'rule': rule.rule_text, 'user_data': user_data})
    else:
        return jsonify({'message': 'Rule not found'}), 404

# Combine rules (for simplicity, just returning rule texts concatenated)
@app.route('/combine-rules', methods=['POST'])
def combine_rules():
    rule_ids = request.json.get('rule_ids', [])
    combined_rules = []
    for rule_id in rule_ids:
        rule = Rule.query.get(rule_id)
        if rule:
            combined_rules.append(rule.rule_text)
    if combined_rules:
        return jsonify({'combined_rules': ' '.join(combined_rules)})
    else:
        return jsonify({'message': 'No valid rules found'}), 404

# Home route
@app.route('/')
def home():
    return "Welcome to the Rule Engine!"

if __name__ == '__main__':
    app.run(debug=True)
