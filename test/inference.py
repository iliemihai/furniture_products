from sklearn.metrics import f1_score, precision_score, recall_score
import numpy as np
from setfit import SetFitModel
import pandas as pd


saved_model = SetFitModel._from_pretrained("../model")

df = pd.read_csv("../data/eval.csv")
lines = df["sentence"].values

# Run inference
res = []
for line in lines:
    preds = saved_model([line])
    res.append(preds.item())
    if preds.item() == 1:
        print("Product {0} is an furniture product name".format(line))
    else:
        print("Product {0} is not an furniture product name".format(line))

y_pred = np.array(res)
y_test = np.array(df["label"].values)

print("F1 score: ", f1_score(y_test, y_pred, average="macro"))
print("Precission: ", precision_score(y_test, y_pred, average="macro"))
print("Recall: ", recall_score(y_test, y_pred, average="macro"))
