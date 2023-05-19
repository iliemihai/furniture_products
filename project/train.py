from datasets import load_dataset
from sentence_transformers.losses import CosineSimilarityLoss

from setfit import SetFitModel, SetFitTrainer, sample_dataset


train_dataset = load_dataset("csv", sep=",", data_files={"train": "../data/train.csv"})
eval_dataset = load_dataset("csv", data_files={"val": "../data/test.csv"})


# Load a SetFit model from Hub
model = SetFitModel.from_pretrained("sentence-transformers/paraphrase-mpnet-base-v2")

# Create trainer
trainer = SetFitTrainer(
    model=model,
    train_dataset=train_dataset["train"],
    eval_dataset=eval_dataset["val"],
    loss_class=CosineSimilarityLoss,
    metric="accuracy",
    batch_size=16,
    num_iterations=20,  # The number of text pairs to generate for contrastive learning
    num_epochs=1,  # The number of epochs to use for contrastive learning
    column_mapping={
        "sentence": "text",
        "label": "label",
    },  # Map dataset columns to text/label expected by trainer
)

# Train and evaluate
trainer.train()
metrics = trainer.evaluate()

model._save_pretrained("../model")

# Run inference
preds = model(["Dellbeck - Brown - Rect Dining Room Ext Table", "Executive Chairs (1)"])
