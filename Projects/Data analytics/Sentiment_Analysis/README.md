# Sentiment Analysis

## 📊 Overview

NLP-powered customer review sentiment classification using VADER and TextBlob to analyze product feedback, identify pain points, and prioritize product improvements.

**Business Context**: Product teams need to process large volumes of customer reviews to identify sentiment trends, prioritize feature requests, and address negative feedback driving churn.

## 🛠️ Tools & Technologies

- **Data Sources**: Product review text (10,000 reviews), Star ratings
- **Python Libraries**: `nltk`, `textblob`, `vader`, `sklearn`, `matplotlib`, `wordcloud`
- **Methods**: VADER sentiment scores, TextBlob polarity, Topic modeling (LDA), N-gram analysis, Sentiment-rating correlation

## 🔬 Methodology

Collect review text → Preprocess (lowercase, remove stopwords) → Apply VADER for compound sentiment scores → Extract topics using LDA → Correlate sentiment with star ratings → Generate word clouds for positive/negative reviews  

## 📈 Results & Insights

Overall sentiment: 68% positive, 22% neutral, 10% negative. Sentiment-rating correlation: 0.78 (strong agreement). Negative reviews focus on: "shipping delays" (32%), "poor quality" (28%), "customer service" (18%). Positive reviews highlight: "great value" (45%), "fast delivery" (38%). Topic modeling reveals 5 themes. Addressing top 3 negative topics could reduce 1-star reviews by estimated 35%.

**Visualizations**: Sentiment distributions, word clouds, topic proportions, sentiment-rating correlation

## 🔗 Links

- [Analysis Notebook](analysis.ipynb)

## 🏷️ Tags

`sentiment-analysis` `nlp` `vader` `customer-feedback` `topic-modeling` `text-mining` `product-analytics`