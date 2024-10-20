function createRule() {
    const ruleInput = document.getElementById("ruleInput").value;

    fetch('http://localhost:5000/create-rule', {  // Corrected the URL to match Flask route
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rule_text: ruleInput })  // Changed to match Flask's expected input
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("createResponse").innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function modifyRule() {
    const ruleId = document.getElementById("modifyRuleId").value;
    const modifyRuleInput = document.getElementById("modifyRuleInput").value;

    fetch(`http://localhost:5000/modify-rule/${ruleId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rule_text: modifyRuleInput })  // Changed to match Flask's expected input
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("modifyResponse").innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function evaluateRule() {
    const ruleId = document.getElementById("evaluateRuleId").value;
    const userDataInput = document.getElementById("userDataInput").value;

    fetch(`http://localhost:5000/evaluate-rule/${ruleId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(JSON.parse(userDataInput)) // Ensure the input is JSON
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("evaluateResponse").innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function combineRules() {
    const combineRuleIds = document.getElementById("combineRuleIds").value.split(",").map(Number);

    fetch('http://localhost:5000/combine-rules', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rule_ids: combineRuleIds })
    })
    .then(response => response.json())
    .then(data => {
        if (data.combined_rules) {
            document.getElementById("combineResponse").innerText = "Combined Rules: " + data.combined_rules;
        } else {
            document.getElementById("combineResponse").innerText = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
