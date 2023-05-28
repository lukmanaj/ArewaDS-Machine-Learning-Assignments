# Introduction to Machine Learning

The introduction to machine learning week was structured into four.Introduction covered setting up the working environment (python installation and conda environment) which has already been covered in our 30 Days of Python phase of the fellowship. In addition, the relationship between Machine Learning, Deep Learning, Artificial Intelligence and Data Science was explored too.
Applications of machine learning were also discussed some of which include:

1. Predicting likelihood of disease from a patient's medical history or reports
2. Leveraging weather data to predict weather events.
3. Understanding the sentiment of a text.
4. Detecting fake news to stop the spread of propaganda

Machine learning has an impact in many fields including finance, economics, earth science, space exploration, biomedical engineering, cognitive science, and even fields in the humanities.

## History of Machine Learning

Notable dates in the history of machine learning:

- 1763, 1812 Bayes Theorem and its predecessors. This theorem and its applications underlie inference, describing the probability of an event occurring based on prior knowledge.
- 1805 Least Square Theory by French mathematician Adrien-Marie Legendre. This theory, which you will learn about in our Regression unit, helps in data fitting.
- 1913 Markov Chains, named after Russian mathematician Andrey Markov, is used to describe a sequence of possible events based on a previous state.
- 1957 Perceptron is a type of linear classifier invented by American psychologist Frank Rosenblatt that underlies advances in deep learning.
- 1967 Nearest Neighbor is an algorithm originally designed to map routes. In an ML context it is used to detect patterns.
- 1970 Backpropagation is used to train feedforward neural networks.
- 1982 Recurrent Neural Networks are artificial neural networks derived from feedforward neural networks that create temporal graphs.

The AI winter between 1974 and 1980

The limitations that led to the AI winter included:

- Compute power was too limited.
- Combinatorial explosion. The amount of parameters needed to be trained grew exponentially as more was asked of computers, without a parallel evolution of compute power and capability.
- Paucity of data. There was a paucity of data that hindered the process of testing, developing, and refining algorithms.
- Are we asking the right questions?. The very questions that were being asked began to be questioned. Researchers began to field criticism about their approaches:
- Turing tests came into question by means, among other ideas, of the 'chinese room theory' which posited that, "programming a digital computer may make it appear to understand language but could not produce real understanding." (source)
- The ethics of introducing artificial intelligences such as the "therapist" ELIZA into society was challenged.

Today machine learning and AI touch almost every part of our lives. This era calls for careful understanding of the risks and potentials effects of these algorithms on human lives. As Microsoft's Brad Smith has stated, "Information technology raises issues that go to the heart of fundamental human-rights protections like privacy and freedom of expression. These issues heighten responsibility for tech companies that create these products. In our view, they also call for thoughtful government regulation and for the development of norms around acceptable uses.

## Fairness in Machine Learning

Here we were introduced to the concept of fairness and how a problem with the data can lead to bias in the algorithm. eg a machine learning algorithm that selects people who can be given loans can be biased towards a specific race or gender. We were also introduced to Fairlearn

## Techniques of Machine Learning

On a high level, the craft of creating machine learning (ML) processes is comprised of a number of steps:

- Decide on the question. Most ML processes start by asking a question that cannot be answered by a simple conditional program or rules-based engine. These questions often revolve around predictions based on a collection of data.
- Collect and prepare data. To be able to answer your question, you need data. The quality and, sometimes, quantity of your data will determine how well you can answer your initial question. Visualizing data is an important aspect of this phase. This phase also includes splitting the data into a training and testing group to build a model.
- Choose a training method. Depending on your question and the nature of your data, you need to choose how you want to train a model to best reflect your data and make accurate predictions against it. This is the part of your ML process that requires specific expertise and, often, a considerable amount of experimentation.
- Train the model. Using your training data, you'll use various algorithms to train a model to recognize patterns in the data. The model might leverage internal weights that can be adjusted to privilege certain parts of the data over others to build a better model.
- Evaluate the model. You use never before seen data (your testing data) from your collected set to see how the model is performing.
- Parameter tuning. Based on the performance of your model, you can redo the process using different parameters, or variables, that control the behavior of the algorithms used to train the model.
- Predict. Use new inputs to test the accuracy of your model.

The concepts of features and targets and splitting datasets to train and test and validation sets were all discussed. In all, an eventful and exciting first week of machine learning.
