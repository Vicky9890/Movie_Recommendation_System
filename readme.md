# Movie Recommendation System using ML

This repository implements a Movie Recommendation System using machine learning tools such as **pandas**, **numpy**, **difflib**, **CountVectorizer** from **sklearn.feature_extraction.text**, and **cosine_similarity** from **sklearn.metrics.pairwise**. The recommendation system suggests movies based on user preferences and employs natural language processing techniques to find similarities between movie descriptions.

## Description

A Movie Recommendation System is an application designed to provide personalized movie suggestions to users based on their preferences and viewing history. It leverages machine learning algorithms and data analysis techniques to understand user behavior and movie characteristics, ultimately offering tailored recommendations.

## Types of Recommendation Systems

- **Collaborative Filtering:** Recommends movies based on the preferences and behaviors of similar users.

- **Content-Based Filtering:** Recommends movies similar to those the user has enjoyed in the past, based on attributes like genres, descriptions, or actors.

- **Hybrid Models:** Combines collaborative and content-based approaches for more accurate and diverse recommendations.

## About difflib 

**difflib** is a Python library that provides tools for comparing sequences, including strings, and producing human-readable differences or deltas. It is part of the standard library, making it readily available for use without requiring additional installations.

## Key Components

- User Input.
- Data Collection.
- Data Preprocessing.
- Feature Extraction.
- Machine Learning Models.
- Similarity Calculation.
- User Profiling.
- Recommendation Generation.

## Requirements

- Python

To run the code, you need to have the following libraries installed:

- pandas
- numpy
- difflib
- sklearn

You can install the required libraries using pip:

```bash
   pip install pandas numpy scikit-learn
```
## Usage

To use the Movie Recommendation System, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Vicky9890/Movie_Recommendation_System.git
```

2. Navigate to the project directory:
```bash
cd Movie_Recommendation_System
```

3. Run the recommendation system:
```bash
jupyter-notebook Movie_Recommendation_System.ipynb
```
This script prompts the user to input their favorite movie. The recommendation system then suggests movies based on the similarity of their descriptions.

## Data

The movie recommendation system uses a dataset containing information about various movies. The dataset is stored in the [movies_data.csv](https://github.com/Vicky9890/Movie_Recommendation_System/blob/master/Dataset/movies_data.csv) file. You can replace this file with your own dataset following the same structure.

## Implementation Details

The recommendation system employs the following machine learning tools:

- **pandas and numpy:** For data manipulation and numerical operations.
- **difflib:** To find close matches for user-inputted movie names, enhancing user experience.
- **CountVectorizer:** Converts movie descriptions into numerical vectors.
- **cosine_similarity:** Measures the similarity between movie vectors, helping in recommending movies with similar content.

## Results

The recommendation system has been designed to provide accurate and relevant movie suggestions. Users can customize the system by adjusting parameters or incorporating their datasets.
