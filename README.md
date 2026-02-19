
# Task-Oriented Adversarial Attacks for Aspect-Based Sentiment Analysis Models


####  Abstract
Adversarial attacks consist of deliberately modify deep learning inputs, mislead models, and cause incorrect results. Previous adversarial attacks on sentiment analysis models have demonstrated success in misleading these models. However, most existing attacks in sentiment analysis have applied a generalized approach to input modifications, without considering the characteristics and objectives of the different analysis levels. Specifically, for aspect-based sentiment analysis, there is a gap in attack methods that modify inputs in accordance with the evaluated aspects. Consequently, unnecessary modifications are made, compromising the input semantics, making the changes more detectable, and avoiding the identification of new vulnerabilities. In previous work, we proposed a model to generate adversarial examples in particular for aspect-based sentiment analysis. In this paper, we assess the effectiveness of our adversarial example model to negatively impacting aspect-based model results while maintaining high levels of the semantic inputs. To conduct this evaluation, we propose diverse adversarial attacks across different dataset domains, target architectures, and considering distinct levels of victim model knowledge, obtaining a comprehensive evaluation. The obtained results demonstrate that our approach surpasses existing attack methods in terms of accuracy reduction and semantic similarity, achieving a 65.30\% reduction in model accuracy with a low perturbation ratio of 7.79\%. These findings highlight the importance of considering task-specific characteristics when designing adversarial examples, as even simple modifications to elements that support task classification can successfully mislead models.
## Aspect-Based Adversarial Example Model

We consider that the modifications to generate adversarial examples should be designed in a particular way, altering the elements that support the input classification (according to the observed task). 

Our hypothesis relies on the idea that by focusing on aspect-based characteristics, modifications to generate adversarial examples will be performed on the minimum necessary terms that effectively support the aspect opinion, misleading the model to deal with the task rather than analyze patterns in a text. 

We propose a model for generating adversarial examples particularly oriented to aspect-based sentiment analysis, named as ABAA model. Our proposal considers the aspect-based characteristics to determine input modifications, taking care of preserving the input semantic and modifications imperceptibility. In the case of aspect-based analysis, its main characteristic relies on, within an opinion, each evaluated aspect that correlates to a specific term, which allows the user to determine the opinion expressed. 

![Aspect-Based Analysis Example](https://raw.githubusercontent.com/MonserratVH/ABAA-model/refs/heads/main/Figures/absa_example.jpg)




## ModificationProcess
When designing adversarial examples oriented to aspect-based analysis, two main challenges must be faced: i) to identify the terms that express aspect-opinion and ii) to define their possible modifications. First, given an opinion, it is necessary to correctly determine the term that uniquely identifies the sentiment (positive, negative, or neutral) for each evaluated aspect, establishing an aspect-term relation. Second, for each identified term, it is necessary to establish the set of possible modifications _N_ that each identified term could suffer, evaluating and controlling that each modification could be performed if they preserve the correct input semantics and successfully mislead the deep learning model. Under these considerations, we proposed the aspect-based adversarial examples model.

![Aspect-Based Adversarial Example - Modification Process](https://raw.githubusercontent.com/MonserratVH/ABAA-model/refs/heads/main/Figures/modification_process.jpg)
## AdversarialAttacks
We propose different adversarial attacks (white-box, gray-box, and black-box) to evaluate three principal characteristics of the ABAA model: 1) the effectiveness to negative impact on model results via a white-box attack, 2) the context independence across domains via a gray-box attack, and 3) the transferability among aspect-based models via a black-box attack. We denominate the designed attacks as ABAA attack. 

### White-box attack
To evaluate the negative impact of particularized aspect-based adversarial examples, we developed a white-box attack. The architecture of the white-box ABAA attack is illustrated in the following Figure

![White-box attack](https://raw.githubusercontent.com/MonserratVH/ABAA-model/refs/heads/main/Figures/whitebox_attack.jpg)

As the victim model, we use the approach [Sentiment Analysis using Specialized Aspect-Oriented Lexicons](http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6433), which proposes a term weighing scheme for aspect-based sentiment classification. This approach takes as input a set of sentiment lexicons (one by sentiment, i.e., positive, neutral, negative)  to assign weights to opinion terms based on their semantic proximity to a sentiment. Terms associated with a particular sentiment are given higher emphasis, facilitating the classification of the aspect’s opinion. The weighting scheme is evaluated using a CNN architecture.

Since this is a white-box attack, where full access to the model's knowledge is available, we take advantage of the sentiment lexicons used by the victim model to enhance the input modification. Following the established modification process, we include an extra validation step for filtering terms. If the term being evaluated exists in the model's lexicons and its semantic proximity is greater than or equal to β, it is considered a candidate to be modified.

### Gray-box attack
To evaluate the context independence of the ABAA model, we consider the same victim model and methodology defined in the white-box attack but using a different domain dataset. In this case, we follow the principles of a gray-box attack, where we have knowledge of the input data but no information on the victim model's performance is available. We assumed that the performance of the aspect-based analysis by the model should be the same, even when it is applied to a dataset from a different domain.

### Black-box attack
To evaluate the transferability of adversarial examples through the ABAA model, we designed a black-box attack. To generate adversarial examples, our attack implements a local model to perform input modifications as it is defined in white-box attack. The adversarial examples generated by the local model are then evaluated to determine if they achieve a change in the model's results. The modified inputs that successfully mislead the local model are stored in an adversarial dataset, which is subsequently transferred to the victim model. As victim model, we consider the ABSA classifier proposed by [Huang et al.](http://www.casos.cs.cmu.edu/events/summer_institute/2020/si_portal/pubs/2018_Aspect%20Level.pdf), which incorporates an attention-over-attention (AOA) mechanism with a Bi-LSTM neural network architecture and applies the BERT-base model. The architecture of this attack is illustrated in the following Figure.

![Black-box Attack](https://raw.githubusercontent.com/MonserratVH/ABAA-model/refs/heads/main/Figures/blackbox_attack.jpg)
## Related
As local model, we include a version of the method in A Semantic-Proximity Term-Weighting Scheme for Aspect Category Detection proposed by Vázquez-Hernández, Villaseñor-Pineda and Montes-y Gómez (2022)

- [A Semantic-Proximity Term-Weighting Scheme for Aspect Category Detection](http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6433)


As victim model in the black-box attack, we use the aspect-based sentiment analysis classifier proposed by Huang, Ou and Carley (2018), which implements an attention-over-attention (AOA) mechanism using a Bi-LSTM neuronal network architecture and applies the BERT-base mode.

- [paperswithcode](https://paperswithcode.com/paper/aspect-level-sentiment-classification-with)  
- [ABSA-PyTorch](https://github.com/songyouwei/ABSA-PyTorch)

We include a version of ABSA dataset from SemEval.The original datase is available on:
- [SemEval 2014 Task 4: AspectBasedSentimentAnalysis](https://www.kaggle.com/datasets/charitarth/semeval-2014-task-4-aspectbasedsentimentanalysis)

 GloVe: Global Vectors for Word Representation and include them on File directory. We use the Twitter emebddings 200 dimension vectors)

- [GloVe](https://nlp.stanford.edu/projects/glove/)

## How to cite
If you use this work, please cite the following paper:

**APA format**
Vázquez-Hernández, M., Algredo-Badillo, I., Villaseñor-Pineda, L., Lobato-Báez, M., Lopez-Pimentel, J. C., & Morales-Rosales, L. A. (2025). Task-Oriented Adversarial Attacks for Aspect-Based Sentiment Analysis Models. Applied Sciences, 15(2), 855.

**BibTex**
**BibTeX**

```bibtex
@article{vazquez2025task,
  title={Task-Oriented Adversarial Attacks for Aspect-Based Sentiment Analysis Models},
  author={V{\'a}zquez-Hern{\'a}ndez, M. and Algredo-Badillo, I. and Villase{\~n}or-Pineda, L. and Lobato-B{\'a}ez, M. and Lopez-Pimentel, J. C. and Morales-Rosales, L. A.},
  journal={Applied Sciences},
  volume={15},
  number={2},
  pages={855},
  year={2025},
  publisher={MDPI}
}

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
    [https://orcid.org/0000-0002-4753-9375](https://orcid.org/0000-0002-4753-9375)


## Acknowledgements

 - This work is supported by CONAHCYT/México scholarship 814461. Besides, it was founded by Catedras-CONAHCYT projects 882 and 613

