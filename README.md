# 5452_DS-AI_Project_TeamI
Guarding the Guardians: Detecting Bias and Underlying Agendas in Environmental Fact-checking Using Machine Learning Approaches 

Jean Marc Baquero - h12543815

Grégoire Bouvier - h12543344

---
Research Question:

Using machine learning models to calculate topic density, how does the comparison of the human-verified datasets used to train the Fake News detector algorithms against a diverse reference corpus reveal systematic selection bias in specific contentious environmental sectors?

Sub-questions:

Sub1: What are the core contentious environmental sectors and underlying socio-economic interests mapped within online climate discourse, and how can they be categorized for algorithmic bias detection?

Sub2: How do advanced embedding and topic modeling techniques (e.g., BERTopic or Transformer representations) compare in quantifying topic density discrepancies between fact-checked data and general media?

Sub3: How can this methodology be be operationalized over time and generalized to offer insights in other important news topics, such as health, politics, technology, etc. to practically surive the continuous introduction of new topics/narratives?

---

Acknowledgements:

Models and relevant documentation used:

- CorEx (supervised topic modeling): 

https://maartengr.github.io/BERTopic/

- BERTopic (transformer model):

https://github.com/gregversteeg/CorEx


Datasets / data sources:

Misinformation_detection (2018) on GitHub: https://github.com/sfu-discourse-lab/Misinformation_detection/blob/master/README.md

FakeNewsCorpus (2020) on GitHub: https://github.com/several27/FakeNewsCorpus

---

Workplan/Milestones:

Curate a sub-dataset with environment articles - 29.5.2026 >JM

Sub-dataset from 2 datasets – clean-up >JM 

Use CorEx, BERTopic to map subjects of contention – 5.6.2026 >JM

Literature on contentious subjects >BG

Compare to wider statistics to identify bias/blind-spots - 5.6.2026

Implement the model and map the topic density discrepancies on fact-checkers VS general media - 12.6.2026. >JM

Find the percentages of environmental sujets in google Analytics data/ international press sources >BG

Create Tags and add them to the dataset - 19.6.2026 >JM

Implementation -> how to integrate the tags in the original dataset - JM

Generalization for other topics and other contextual flags - 26.6.2026.

Presentation - 26.6.2026.

- storytelling

- pptx

---

Required installations //assuming python 3.14 and pip

- BERTopic

    pip install bertopic

- CorEx

    pip install corextopic

- Torch

    pip install torch

- sentence-transformer

    pip install sentence-transformers

- Pandas & others

    pip install pandas numpy scikit-learn seaborn matplotlib

- Requests

    pip install requests

---

For the GitHub link, please refer to: gihub.txt