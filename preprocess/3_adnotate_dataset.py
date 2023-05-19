from transformers import T5Tokenizer, T5ForConditionalGeneration
from tqdm import tqdm
import torch

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl")

text_lines = open("../data/dedup_data.csv", "r").readlines()
g = open("../data/adnotated_data.csv", "w")


def generate(input_text):
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=32)
    return tokenizer.decode(output[0], skip_special_tokens=True)


g.write("text" + "," + "product")
for line in tqdm(text_lines):
    if len(line.split()) < 20:
        prompt_text = """Is "{0}" an Entity Name refering to a furniture product  like "Ikea brown chair" or "Jisk round table" ? Exclude single nouns like "sofa", "coach" or single names like "Ikea". Respond Yes or No""".format(
            line
        )
        print(line, generate(prompt_text))
        g.write(line + "," + generate(prompt_text))
    else:
        g.write(line + "," + "None")
