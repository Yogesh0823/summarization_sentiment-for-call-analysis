## Table of Contents
1. [General Info](#Abstractive_summarization_sentiment-for-call-analysis)
2. [Installation](#Installation)
   
# Abstractive_summarization_sentiment-for-call-analysis
##### using this machine learning NLP summarization project you can short & also sort the large speech-to-text file and get important understandable topics in summary without hearing all long call you get the main point in this summary and also get sentiment on this call or on summary talk.
***
## NLP PROJECT
#### NLP Project :- using huggingface pre-trained transfromer fine-tuning model & pytorch library for summarization & sentiment.
1. After speech to text you can use this model for summarization on the long text file.
2. This model is best for call or meeting corpus summary.
3. Can also use this model for group disscussion text corpus.
***
# Download Pre-trained fine-tuning on 'facebook/bart-large-xsum' model with BART-LARGE-XSUM-SAMSUM-DIALOGSUM-AMI dataset.
1. open terminal where you want to download your model.
2. paste this in terminal
3. $git lfs install
4. $git clone https://huggingface.co/knkarthick/MEETING-SUMMARY-BART-LARGE-XSUM-SAMSUM-DIALOGSUM-AMI

# Installation
* open terminal where you want to save this project.
* $ git clone https://github.com/Yogesh0823/summarization_sentiment-for-call-analysis.git
* $ cd summarization_sentiment-for-call-analysis
* copy downloaded model folder here.
* create virtule environment in summarization_sentiment-for-call-analysis
* $ python3 -m venv 'venv-name'
* active vnev using $ source/'venv-name'/bin/activate
* install requirement.txt in venv.
* for getting output use $ uvicorn main:app --reload
![result](https://github.com/Yogesh0823/summarization_sentiment-for-call-analysis/blob/main/result-image/uvicorn-cmd.png)

* after runing this script click on link show in terminal http://127.0.0.1:8000 you get this screen.
![result](https://github.com/Yogesh0823/summarization_sentiment-for-call-analysis/blob/main/result-image/welcome-msg.png)

* Then add '/docs' in link http://127.0.0.1:8000/docs, then you get this screen.
![result](https://github.com/Yogesh0823/summarization_sentiment-for-call-analysis/blob/main/result-image/summ-1.png)

* After this click on post summarization text, you get this screen.
![result](https://github.com/Yogesh0823/summarization_sentiment-for-call-analysis/blob/main/result-image/summ-2-try-it-out.png)

* Then click try it out and you get input text box and click on execute. This is with only empty string and what we get output summary from this model and also sentiment. Note :- You just have to replace "string to your corpus"
![result](https://github.com/Yogesh0823/summarization_sentiment-for-call-analysis/blob/main/result-image/summ-3-empty.png)

* Replace string to some talking corpus and see what summary we get.
![result](https://github.com/Yogesh0823/summarization_sentiment-for-call-analysis/blob/main/result-image/summ-4-final.png)

## Model working good and we get perfect abstractive summary with sentiment.
* In this project i'm using fast api for GUI output. You can use without GUI and get summary in terminal but you have to modify summarization.py file for this.
* For increase length of output summary change your input corpus len should be more then 1000 (Count of words in text corpus) , if your len of input text is less then 1000 then its give you deafult output length.
* If your corpus have len more then 1000 or == to 1000 then you can change (increase or decrease) length. for this change "num==500" in def clean function in summarization.py file.
* Increasing the num gives you short out put decreasing the num gives you long summary output.
* num=500 is tested and perfect for more then 1000 words of corpus.





