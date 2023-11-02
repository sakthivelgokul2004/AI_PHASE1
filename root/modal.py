from transformers import GPT2LMHeadModel, GPT2Tokenizer
from torch.optim import Adam
from torch.utils.data import DataLoader
import tqdm
import torch
from dataclass import ChatData
import os
from pathlib import Path

def train(chatData, model, optim):

    epochs = 12

    for i in tqdm.tqdm(range(epochs)):
        for X, a in chatData:
            X = X.to(device)
            a = a.to(device)
            optim.zero_grad()
            loss = model(X, attention_mask=a, labels=X).loss
            loss.backward()
            optim.step()
        torch.save(model.state_dict(), "model_state.pt")
        print(infer("hello how are you"))

def infer(inp):
    inp = "<startofstring> "+inp+" <bot>:"
    inp = tokenizer(inp, return_tensors="pt")
    X = inp["input_ids"].to(device)
    a = inp["attention_mask"].to(device)
    output = model.generate(X, attention_mask=a,max_length=40 )
    output = tokenizer.decode(output[0])
    return output

device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.add_special_tokens({"pad_token": "<pad>",
                                "bos_token": "<startofstring>",
                                "eos_token": "<endofstring>"})
tokenizer.add_tokens(["<bot>:"])

model = GPT2LMHeadModel.from_pretrained("gpt2",pad_token_id=tokenizer.pad_token_id,eos_token_id=tokenizer.eos_token_id,bos_token_id=tokenizer.bos_token_id)
model.resize_token_embeddings(len(tokenizer))

model = model.to(device)

chatData = ChatData( tokenizer)
chatData =  DataLoader(chatData, batch_size=64)
model.train()

optim = Adam(model.parameters(), lr=1e-3)


def load_or_train_model():
    if  os.path.isfile('model_state.pt'):
        path=Path("model_state.pt").absolute()
        print("loading the saved state from {path}".format(path=path))
        model.load_state_dict(torch.load(path, map_location=device))
    else:
        train(chatData, model, optim)




