from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from summarization import Model
import sentiment
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI()
model = Model()


class SummarizationRequest(BaseModel):
    text: str

class SummarizationResponse(BaseModel):
    summary: str
    sentiments : str

# Load the pre-trained model and tokenizer
# model_name = "MEETING_SUMMARY"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
senti_token ,senti_model = sentiment.load_sentiment_model()

@app.get("/")
async def root():
    return {"message": "Welcome to Summarization & Sentiment using ML Model."}

@app.post("/summarize", response_model=SummarizationResponse)
async def summarize_text(request: SummarizationRequest):
    try:
        text = request.text

        # Tokenize input text
        # inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True, padding=True)

        # # Generate output summary
        # output = model.generate(**inputs,
        #                         max_length=150,  # Set the desired max length for the output
        #                         num_beams=4,     # Adjust the number of beams for beam search
        #                         temperature=0.8,  # Adjust the temperature for sampling (for models that support it)
        #                         top_k=50,         # Adjust the top-k parameter for sampling (for models that support it)
        #                         top_p=0.9)

        # Decode and return the generated summary
        # generated_summary = tokenizer.decode(output[0], skip_special_tokens=True)
        if len(text) >= 1000:
            cln_txt = model.clean_text(text)
            generated_summary = model.summary(cln_txt)
        else:
            generated_summary = model.summarys(text)

        sentiments = sentiment.inference(generated_summary,senti_token,senti_model)
        return {"summary": generated_summary,"sentiments":sentiments}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



