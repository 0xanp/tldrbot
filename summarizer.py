import openai
from transformers import pipeline
from gensim.summarization import summarize as gensim_summarize
from dotenv import load_dotenv
import os

load_dotenv()

class Summarizer:
    def __init__(self, model='textrank'):
        self.model = model

    def summarize(self, message_history):
        text = message_history.get_message_history()
        if self.model == 'textrank':
            return self.summarize_textrank(text)
        elif self.model == 'transformers':
            return self.summarize_transformers(text)
        elif self.model == 'davinci':
            return self.summarize_davinci(text)
        else:
            raise ValueError(f"Invalid model name '{self.model}'")

    def summarize_textrank(self, text):
        summary = gensim_summarize(text)
        return summary

    def summarize_transformers(self, text):
        summarization_pipeline = pipeline("summarization")
        summary = summarization_pipeline(text, max_length=1000, min_length=30, do_sample=False)[0]['summary_text']
        return summary

    def summarize_davinci(self, text):
        openai.api_key = os.getenv("OPEN_AI_TOKEN")
        model_engine = "davinci"
        prompt = (f"Please summarize the following text:\n{text}")
        completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,
                                               stop=None, temperature=0.5)
        summary = completions.choices[0].text.strip()
        return summary
