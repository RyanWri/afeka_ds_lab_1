import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC 

class Trainer:

    def __init__(self, train_df: pd.DataFrame, test_df: pd.DataFrame):
        self.X_train = train_df.drop("Survived", axis=1)
        self.Y_train = train_df["Survived"]
        self.X_test = test_df.drop("PassengerId", axis=1).copy()

    def train_lr(self):
        # Logistic Regression
        logreg = LogisticRegression()
        logreg.fit(self.X_train, self.Y_train)
        Y_pred = logreg.predict(self.X_test)
        acc_log = round(logreg.score(self.X_train, self.Y_train) * 100, 2)
        print(acc_log)
        return logreg
    
    def correlation_to_lr(self, df:pd.DataFrame, logreg: LogisticRegression) -> pd.DataFrame:
        coeff_df = pd.DataFrame(df.columns.delete(0))
        coeff_df.columns = ['Feature']
        coeff_df["Correlation"] = pd.Series(logreg.coef_[0])
        return coeff_df
    
    def train_svm(self):
        # Support Vector Machines
        svc = SVC()
        svc.fit(self.X_train, self.Y_train)
        Y_pred = svc.predict(self.X_test)
        acc_svc = round(svc.score(self.X_train, self.Y_train) * 100, 2)
        print(f"svm accuracy: {acc_svc}")