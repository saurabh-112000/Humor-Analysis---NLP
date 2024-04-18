# Comedic Dynamics - Analyzing Segmentation, Offense and Thematic Patterns in Stand Up Comedy transcripts

## Abstract
This project aims to enhance the transparency and safety of stand-up comedy by analyzing thematic patterns and sentiments within comedy specials. Utilizing NLP techniques such as topic modeling and sentiment analysis, we identify dominant themes and polarity scores, helping creators to better frame their content disclaimers.

## Introduction
The project examines stand-up comedy specials, focusing on controversial topics like race, ethnicity, and politics, which often lead to public debates. We aim to understand these thematic patterns and sentiments to propose improved content disclaimers, fostering a safer viewing experience.

## Background
Our approach leverages Topic Modeling to uncover hidden thematic structures and Offense Analysis in Comedy to understand potentially harmful effects of humor. Techniques include Latent Dirichlet Allocation (LDA) and Non-negative Matrix Factorization (NMF) to identify topics and sentiments within comedy transcripts.

## Approach
1. **Corpus Extraction**: Extracted from "Scraps from the Loft" using BeautifulSoup, covering over 450 transcripts in English.
2. **Text Preprocessing**: Involves cleaning text, language identification, tokenization, and Parts-of-Speech tagging using Python libraries.
3. **Offense and Subjectivity Analysis**: Employing the VADER  and TextBlob packages for sentiment and subjectivity analysis.
4. **Named Entity Recognition**: Using SpaCy's NLP model to identify and analyze entities within the transcripts.
5. **Topic Modeling**: Using LDA and NMF models to identify prevalent topics, with a focus on optimizing topic coherence.

## Results
The analysis identifies relationships between sentiment polarity and subjectivity, showing different trends among comedians. Topic modeling results in distinct thematic categories such as observational, cultural, and political comedy. NMF showed better performance in topic coherence compared to LDA.

## Conclusions
The project effectively maps out the thematic and emotional landscape of stand-up comedy, offering insights that can help tailor content disclaimers.
