# Fake Review Detector

A Python desktop application that helps identify potentially fake product reviews using rule-based analysis.

## Project Overview
This user-friendly application analyzes review text to assess its authenticity through pattern matching and keyword detection. Built with Python, it provides an intuitive interface for users to evaluate the likelihood of a review being genuine.

## Key Features

### Interactive Interface
- Direct review text input capability
- Clear user interaction through intuitive buttons and labels
- Prominent display of authenticity assessment results

### Suspicious Pattern Detection
- Identifies predefined phrases commonly found in fake reviews
- Examples include "amazing product," "absolutely perfect"
- Pattern matches contribute to overall fake score calculation

### Keyword Analysis
- Scans for suspicious words indicating potential inauthenticity
- Keywords like "fake," "paid," "influencer" increase suspicion score
- Automated scoring system based on keyword presence

### Length Analysis
- Evaluates review length against established thresholds
- Flags unusually short or long reviews as potentially suspicious
- Contributes to the overall authenticity assessment

### Result Breakdown
- Displays final fake score with probability assessment
- Provides verdict: "likely genuine" or "fake review detected"
- Lists specific reasons for flagging suspicious content

## Limitations
- Rule-based approach effectiveness depends on predefined patterns quality
- May miss sophisticated fake reviews using nuanced language
- Limited to explicit pattern matching without contextual understanding

## Future Development Plans
- [ ] Implement machine learning models using real review training data
- [ ] Add customizable suspicious pattern and keyword lists
- [ ] Integrate sentiment analysis for emotional tone evaluation
![Screenshot 2024-12-04 195150](https://github.com/user-attachments/assets/da4b5ed4-a3c1-4e08-a6d0-6aadcffdf784)
![Screenshot 2024-12-04 195235](https://github.com/user-attachments/assets/9e87cd79-65df-470c-b9f1-9ed71634eda9)
![Screenshot 2024-12-04 195255](https://github.com/user-attachments/assets/081512ef-ff98-4a4b-af5a-e8180bdec5ca)

