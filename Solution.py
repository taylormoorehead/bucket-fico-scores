import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv('borrower_data.csv')

X = data.drop('default', axis=1)
y = data['default']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

def calculate_expected_loss(loan_properties):
    loan_properties = pd.DataFrame(loan_properties).transpose()
    probability_default = model.predict_proba(loan_properties)[:, 1]
    expected_loss = probability_default * 0.1
    return expected_loss

loan_properties = {
    'credit_lines_outstanding',
    'loan_amt_outstanding',
    'total_debt_outstanding',
    'income',
    'years_employed',
    'fico_score',
    'default'
}

expected_loss = calculate_expected_loss(loan_properties)
print('Expected Loss:', expected_loss)
