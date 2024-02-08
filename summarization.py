# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch 


model_dicts = "MEETING-SUMMARY-BART-LARGE-XSUM-SAMSUM-DIALOGSUM-AMI"
class Model():

    def __init__(self, model_dict=model_dicts):
        # torch.set_num_threads(12)
        self.tokenizer = AutoTokenizer.from_pretrained(model_dict)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_dict)

    def clean_text(self,text,num=500):
        run = len(text)/num
        a = 0
        b = 500
        txt_ = []
        for i in range(0,int(run)):
            txt_.append(text[a:b])
            a = b
            b += 500
        return txt_
        
    def summary(self,txt_):
        final_sum = []
        for input_text in txt_:
            # Tokenize input text
            inputs = self.tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True,padding=True)

            # Generate output summary
            output = self.model.generate(**inputs,
                max_length=700,  # Set the desired max length for the output
                num_beams=4,    # Adjust the number of beams for beam search
                temperature=0.8,  # Adjust the temperature for sampling (for models that support it)
                top_k=50,       # Adjust the top-k parameter for sampling (for models that support it)
                top_p=0.9)

            # Decode and print the generated summary
            generated_summary = self.tokenizer.decode(output[0], skip_special_tokens=True)
            final_sum.append(generated_summary)
            # print("Generated Summary:")
            # print(generated_summary)
        return ''.join(final_sum)
    
    def summarys(self,txt_):
        inputs = self.tokenizer(txt_, return_tensors="pt", max_length=1024, truncation=True,padding=True)

        # Generate output summary
        output = self.model.generate(**inputs,
            max_length=700,  # Set the desired max length for the output
            num_beams=4,    # Adjust the number of beams for beam search
            temperature=0.8,  # Adjust the temperature for sampling (for models that support it)
            top_k=50,       # Adjust the top-k parameter for sampling (for models that support it)
            top_p=0.9)

        # Decode and print the generated summary
        generated_summary = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_summary
