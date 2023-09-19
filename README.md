

# 2) MODEL DEPLOYMENT DEMONSTRATION
- run the Notebook Fizzbuzz task 2.ipynb to deploy the app huggingface-inference on port 8000. the app classifies text as toxic/non-toxic. the last cell in notebook is used to send request to the docker container and receive a response.
- the model used is "martin-ha/toxic-comment-model". I chose NLP task because of familiarity, and chose this model because of large number of downloads while also being a reasonable size to deploy. other models i tried were too big and were running into time out errors, so for purpose of demonstration only, i went for a smaller model instead. 

# 3) EXPLORATORY DATA ANALYSIS DEMONSTRATION

- for this task I chose the olivierdehaene/xkcd dataset because I wanted to try out multi-modal dataset. again one reason for picking this dataset is because of its smaller size, that was quick to load compared to some of the other datsets.
- use the notebook Dataset exploration.ipynb for this task.
- the first section shows a wordcloud of the most common words in the title. you can then use these to explore comics by keyword or create a story of multi-part comics.
