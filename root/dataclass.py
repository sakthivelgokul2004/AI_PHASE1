from torch.utils.data import Dataset
import pandas as pd

class ChatData(Dataset):
    def __init__(self, tokenizer):
        self.data  =pd.read_csv("dialogs.txt",sep="\t",names=["question","answer"])

        self.X = []

        for index,row in self.data.iterrows():
                self.X.append(" <startofstring> " +row['question']+ " <bot>: " +row['answer']+" <endofstring> ")

        self.X = self.X[:5000]

        self.X_encoded = tokenizer(self.X,max_length=40, truncation=True, padding="max_length", return_tensors="pt")
        self.input_ids = self.X_encoded["input_ids"]
        self.attention_mask = self.X_encoded["attention_mask"]

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return (self.input_ids[index], self.attention_mask[index])




