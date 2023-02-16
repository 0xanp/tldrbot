from summa.summarizer import summarize

class ConversationSummarizer:
    def __init__(self, ratio: float = 0.2):
        self.ratio = ratio
    
    def summarize(self, text: str) -> str:
        summary = summarize(text, ratio=self.ratio)
        return summary
