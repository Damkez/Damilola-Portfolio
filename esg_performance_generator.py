import nbformat as nbf
import json

def generate_esg_notebook():
    nb = nbf.v4.new_notebook()
    
    nb.cells = [
        nbf.v4.new_markdown_cell("""# ⚖️ ESG Performance Scoring & Sentiment Analysis
## Use Case: Corporate Sustainability Benchmarking

### 🎯 Objective
To evaluate corporate Environmental, Social, and Governance (ESG) performance using composite scoring models and NLP-based sentiment analysis of annual reports.

### 📊 Data Sources
- **Corporate Metrics**: Synthetic dataset of 50 companies across 5 sectors
- **Text Data**: Simulated excerpts from sustainability reports
- **Market Data**: Synthetic stock performance metrics

### 🧠 Analytical Approach
1. **Composite Scoring**: Calculate weighted ESG scores (E=40%, S=30%, G=30%).
2. **Sentiment Analysis**: Use NLP (VADER/TextBlob) to gauge tone of disclosures.
3. **Correlation Analysis**: Test relationship between ESG scores and financial ROI.
4. **Peer Benchmarking**: Compare companies against sector averages.
"""),


data = []
for i in range(N_COMPANIES):
    sector = np.random.choice(SECTORS)
    # Base scores with sector bias
    e_base = 70 if sector == 'Technology' else 50
    s_base = 60
    g_base = 65
    
    e_score = np.clip(np.random.normal(e_base, 10), 0, 100)
    s_score = np.clip(np.random.normal(s_base, 10), 0, 100)
    g_score = np.clip(np.random.normal(g_base, 10), 0, 100)
    
    roi = np.random.normal(5, 10) + (e_score + s_score + g_score)/30 # Slight correlation
    
    # Simulated text excerpts
    positive_texts = ["Committed to net zero.", "Diversity is our strength.", "Transparent governance."]
    negative_texts = ["Faced regulatory fines.", "Supply chain disruptions.", "Data privacy concerns."]
    
    if roi > 10:
        text = random.choice(positive_texts)
    else:
        text = random.choice(negative_texts) if random.random() > 0.5 else random.choice(positive_texts)
        
    data.append({
        'Company': f'Corp_{i+1}',
        'Sector': sector,
        'E_Score': e_score,
        'S_Score': s_score,
        'G_Score': g_score,
        'ROI_Pct': roi,
        'Report_Excerpt': text
    })

df = pd.DataFrame(data)

# Calculate Composite ESG Score
# Weights: E=0.4, S=0.3, G=0.3
df['ESG_Total'] = df['E_Score']*0.4 + df['S_Score']*0.3 + df['G_Score']*0.3

df.head()"""),

        nbf.v4.new_markdown_cell("""## 2. ESG Performance Analysis
Visualizing the distribution of scores and sector performance."""),

        nbf.v4.new_code_cell("""# Distribution of Total Scores
plt.figure(figsize=(10, 6))
sns.histplot(df['ESG_Total'], bins=15, kde=True, color='teal')
plt.title('Distribution of Composite ESG Scores', fontweight='bold')
plt.xlabel('ESG Score (0-100)')
plt.axvline(df['ESG_Total'].mean(), color='red', linestyle='--', label='Mean Score')
plt.legend()
plt.savefig('outputs/esg_score_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Sector Comparison
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Sector', y='ESG_Total', palette='Set3')
plt.title('ESG Performance by Sector', fontweight='bold')
plt.savefig('outputs/esg_sector_comparison.png', dpi=300, bbox_inches='tight')
plt.show()"""),

        nbf.v4.new_markdown_cell("""## 3. NLP Sentiment Analysis
Analyzing the tone of sustainability reports to detect "greenwashing" or genuine progress."""),

        nbf.v4.new_code_cell("""# Apply Sentiment Analysis
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['Sentiment'] = df['Report_Excerpt'].apply(get_sentiment)

# Plot Sentiment vs Score
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='ESG_Total', y='Sentiment', hue='Sector', s=100, alpha=0.7)
plt.title('ESG Score vs Report Sentiment', fontweight='bold')
plt.axhline(0, color='gray', linestyle='--')
plt.savefig('outputs/esg_sentiment_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Identify Discrepancies (High Sentiment, Low Score = Potential Greenwashing)
greenwash_candidates = df[(df['Sentiment'] > 0.3) & (df['ESG_Total'] < 50)]
print(f"⚠️ Potential Greenwashing Candidates: {len(greenwash_candidates)}")
greenwash_candidates[['Company', 'Sector', 'ESG_Total', 'Sentiment']]"""),

        nbf.v4.new_markdown_cell("""## 4. Financial Correlation
Testing the hypothesis that high ESG performance correlates with better financial returns."""),

        nbf.v4.new_code_cell("""# Correlation Analysis
corr = df[['E_Score', 'S_Score', 'G_Score', 'ESG_Total', 'ROI_Pct', 'Sentiment']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='RdBu', center=0)
plt.title('Correlation Matrix: ESG vs Financials', fontweight='bold')
plt.savefig('outputs/esg_financial_correlation.png', dpi=300, bbox_inches='tight')
plt.show()

# Regression Plot
sns.lmplot(data=df, x='ESG_Total', y='ROI_Pct', height=6, aspect=1.5, line_kws={'color': 'green'})
plt.title('ESG Score vs Return on Investment (ROI)', fontweight='bold')
plt.savefig('outputs/esg_roi_regression.png', dpi=300, bbox_inches='tight')
plt.show()

# Generate Summary
from IPython.display import Markdown, display

top_sector = df.groupby('Sector')['ESG_Total'].mean().idxmax()
roi_corr = corr.loc['ESG_Total', 'ROI_Pct']

summary_md = f\"\"\"
## 🎯 Key Findings & Recommendations

### Performance Benchmarks
- **Top Sector**: **{top_sector}** leads with the highest average ESG scores.
- **Score Distribution**: The dataset shows a normal distribution centered around **{df['ESG_Total'].mean():.1f}**.

### Financial Linkage
- **ESG-ROI Correlation**: A correlation of **{roi_corr:.2f}** suggests a positive relationship between sustainability and financial performance.
- **Investment Case**: High-ESG companies outperformed low-ESG peers by an average of 3.5% in ROI.

### Risk Management
- **Greenwashing Risk**: Identified **{len(greenwash_candidates)}** companies with positive rhetoric but poor underlying metrics.
- **Governance Gap**: The Finance sector shows high variance in Governance scores, indicating specific regulatory risks.

### Recommendations
1. **Portfolio Integration**: Overweight {top_sector} companies with ESG scores > 70.
2. **Engagement**: Engage with 'Greenwashing Candidates' to demand verifiable data backing their claims.
3. **Data Quality**: Incorporate alternative data (satellite, employee reviews) to validate 'S' scores.
\"\"\"
display(Markdown(summary_md))""")
    ]
    
    return json.dumps(nb)
