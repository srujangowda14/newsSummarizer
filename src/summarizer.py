from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model = "facebook/bart-large-cnn")

def summarize_text(text, max_length = 40, min_length = 15):
    text = text[:2000]
    summary = summarizer_pipeline(
        text,
        max_length = max_length,
        min_length = min_length,
        do_sample = False  
    )

    return summary[0]["summary_text"]

if __name__ == "__main__":
    sample_text = """
    Artificial intelligence is transforming industries across the globe. From healthcare to finance, 
    AI-powered systems are enabling smarter decision-making, automating tasks, and improving efficiency. 
    However, experts also caution about ethical concerns, including bias, privacy, and job displacement. 
    Companies are now working toward responsible AI practices to ensure transparency and fairness.
    """
    print("summary")
    print(summarize_text(sample_text))