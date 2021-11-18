# Scalable coding challenge

## Installation

    make install

## Summary

The different parts of the assignement are displayed in notebooks. The rest of the code can be found in the `steam_challenge` folder.
## Thoughts

The preprocessing part was interesting as the dataset was split in three different parts. Then, I wasn't sure about the first prediction task, so I made a supervised classifier. For the last part, it was interesting to use graph data science for a recommender system.
## Suggestions for improvement


Here are some ideas that I could not implement due to lack of time.

For the part 1:

- Implement tests to verify the preprocessing (with _pytest_)

For the part 2.2:

- Take care of the fact the dataset was unbalanced (with _imbalanced-learn_)
- Perform NLP analysis on the _review_ feature (with _spaCy_ or _HuggingFace_)
- More complex models (with _scikit-learn_ or _pytorch_)
- Better hyperparameters optimization (with _Optuna_ or _Ray_)
- Model registry to keep track of different models and hyperparameters (with _MLFlow_)
- Take care of the time with the *release_date* feature (with _sktime_ or _darts_)

For the part 2.1:

- Better graph model for the user recommender (with _networkx_ and its _pagerank_ algorithm for example)
