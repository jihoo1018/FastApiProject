import torch
from transformers import GPT2LMHeadModel
from transformers import PreTrainedTokenizerFast
class Chatbot():
    def __init__(self):
        pass
tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2", bos_token='</s>', eos_token='</s>', unk_token='<unk>', pad_token='<pad>', mask_token='<mask>')
tokenizer.tokenize("안녕하세요. 한국어 GPT-2 입니다.😤:)l^o")
