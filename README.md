
# Adversarial Attack Against Sentiment-Analysis Models Using an Aspect-Based Approach


##  Abstract
Adversarial examples are deep learning inputs strategically modified to mislead models and produce incorrect results. Previous work attacks oriented to sentiment analysis have demonstrated successfully confusing models by adversarial examples. However, the existing adversarial attacks focus mainly on document-level sentiment analysis and do not consider the specific characteristics of different analysis levels. In the case of aspect-based analysis, there is a lack of methods that perform modifications in accordance with evaluated aspects. As a result of this lack, unnecessary modifications are made and do not always succeed in misleading the model, avoiding the possibility of identifying new vulnerabilities. This work proposes a new model for generating aspect-based adversarial. This model is based on the hypothesis that modifying key terms related to a specific aspect within an opinion may lead to incorrect classifications with fewer and imperceptible modifications. We designed a black box attack based on the proposed model and evaluated it using different datasets and architectures in three different scenarios. The obtained results showed that our proposal outperformed document-level attacks and the state-of-the-art method in terms of accuracy reduction and high semantic similarity, achieving a 65.30 percentage point reduction of model accuracy, with a low word perturbation ratio of 7.79\%. These results highlight the importance of considering task-specific characteristics when designing adversarial examples, as simple modifications in the key elements that support the task classification achieve incorrect results.
## Aspect-Based Adversarial Example Model

We consider that the modifications to generate adversarial examples should be designed in a particular way, altering the elements that support the input classification (according to the observed task). 

Our hypothesis relies on the idea that by focusing on aspect-based characteristics, modifications to generate adversarial examples will be performed on the minimum necessary terms that effectively support the aspect opinion, misleading the model to deal with the task rather than analyze patterns in a text. 

We propose a model for generating adversarial examples particularly oriented to aspect-based sentiment analysis, named as ABAA model. Our proposal considers the aspect-based characteristics to determine input modifications, taking care of preserving the input semantic and modifications imperceptibility. In the case of aspect-based analysis, its main characteristic relies on, within an opinion, each evaluated aspect that correlates to a specific term, which allows the user to determine the opinion expressed. 

When designing adversarial examples oriented to aspect-based analysis, two main challenges must be faced: i) to identify the terms that express aspect-opinion and ii) to define their possible modifications. First, given an opinion, it is necessary to correctly determine the term that uniquely identifies the sentiment (positive, negative, or neutral) for each evaluated aspect, establishing an aspect-term relation. Second, for each identified term, it is necessary to establish the set of possible modifications _N_ that each identified term could suffer, evaluating and controlling that each modification could be performed if they preserve the correct input semantics and successfully mislead the deep learning model. Under these considerations, we proposed the aspect-based adversarial examples model.

We designed a black-box adversarial attack applying the proposed ABAA model to evaluate their impact on aspect-
based classifiers. To generate adversarial examples, our attack implements a local deep learning model to perform word-level modifications via the ABAA model and generate aspect-based adversarial examples. Those modified inputs that mislead the local model are reserved into an adversarial dataset to be later transferred to the victim model.
## Related
As local model, we include a version of the method in A Semantic-Proximity Term-Weighting Scheme for Aspect Category Detection proposed by Vázquez-Hernández, Villaseñor-Pineda and Montes-y Gómez (2022)

- [A Semantic-Proximity Term-Weighting Scheme for Aspect Category Detection](http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6433)


As victim model in the black-box attack, we use the aspect-based sentiment analysis classifier proposed by Huang, Ou and Carley (2018), which implements an attention-over-attention (AOA) mechanism using a Bi-LSTM neuronal network architecture and applies the BERT-base mode.

- [paperswithcode](https://paperswithcode.com/paper/aspect-level-sentiment-classification-with)  
- [ABSA-PyTorch](https://github.com/songyouwei/ABSA-PyTorch)

We include a version of ABSA dataset from SemEval.The original datase is available on:
- [SemEval 2014 Task 4: AspectBasedSentimentAnalysis](https://www.kaggle.com/datasets/charitarth/semeval-2014-task-4-aspectbasedsentimentanalysis)

To use the ABAA model it is necesary to download the GloVe: Global Vectors for Word Representation and include them on File directory. We use the Twitter emebddings 200 dimension vectors)

- [GloVe](https://nlp.stanford.edu/projects/glove/)


## Researchers

- _Monserrat Vázquez-Hernández_  
    mvazquez@inaoe.mx  
    https://orcid.org/0000-0001-9206-5706  

- _Ignacio Algredo-Badillo_  
    algredobadillo@inaoep.mx  
    https://orcid.org/0000-0002-4748-3500

- _Luis Villaseñor-Pineda_  
    villasen@inaoep.mx  
    https://orcid.org/0000-0003-1294-9128

- _Mariana Lobato-Báez_  
    mariana.lb@libres.tecnm.mx  
    https://orcid.org/0000-0002-2607-2032

- _Juan Carlos Lopez Pimentel_  
    clopezp@up.edu.mx  
    https://orcid.org/0000-0002-7844-3261

- _Luis Alberto Morales-Rosales (corresponding author)_ 
    lamorales@conacyt.mx  
    https://orcid.org/0000-0002-4753-9375 
## Acknowledgements

 - This work is supported by CONAHCYT/México scholarship 814461. Besides, it was founded by Catedras-CONAHCYT projects 882 and 613

