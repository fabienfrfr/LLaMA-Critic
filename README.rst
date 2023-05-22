.. -*- mode: rst -*-

.. image:: https://raw.githubusercontent.com/fabienfrfr/LLaMA-Critic/main/branding/logo.png

**LLaMA-Critic** is PyTorch model trained for fact checking of a minimal LLaMA LLM model (7B)

This project explore a method to fine tune LLM model with Critic strategy.

**Ideas :** 
  - Environment : Universal Assertion Generator (Bayesian) - Possibilities of Reinforcement 
  - Actor with Critics (% True/False) : LLaMA (last layer is cut) + Attention Extention

*This project is based of minimal, hackable and readable example to load* `LLaMA <https://ai.facebook.com/blog/large-language-model-llama-meta-ai/>`__ (`arXiv <https://arxiv.org/abs/2302.13971v1>`__) `Meta <https://github.com/facebookresearch/llama>`__ *models and run inference. In order to download the checkpoints and tokenizer, fill this* `google form <https://forms.gle/jk851eBVbX1m5TAv5>`__ 


**Objectives :**

Usable in a single computer after training (max 16 Gb) and some smartphone.

.. image:: https://raw.githubusercontent.com/fabienfrfr/LLaMA-Critic/main/doc/LC_principles.png

**Principles of model :**

The model consists of two parts:

  - **Encoder**: The encoder takes the input context (a set of text). The last layer for predicting the next word is not considered, allowing us to pass the raw information from the model to the decoder. The Meta model has already been trained, and we will use it for transfer learning.
  - **Decoder**: This model will predict whether the sentence is true or false. It is also based on attention, but it is smaller than the previous model and corresponds to the one to be trained.


.. image:: https://raw.githubusercontent.com/fabienfrfr/LLaMA-Critic/main/doc/LLaMA-critic.png


**Simulation environment :**

The environement generate sentence of mathematic's relation, and also QCM and universal knowledge.

For an intransigent calculation, i.e. a single false sentence is enough for all the sentences to be false, the probability that a false sentence appears is defined by:

:math: P = \frac{1}{2^{N}}

With "N", the number of sentences possible in the training batch.

More detail in documentation with example.

**Perspective :**

This model opposes Yann LeCun's vision on the concept of "common sense" for achieving a general AI. Using this model, we can combine it with a large language model to predict only "plausible" sequences of words (Bayesian probability). This would involve replacing the last layer with one or multiple trainable layers to predict new words. 

.. image:: https://raw.githubusercontent.com/fabienfrfr/LLaMA-Critic/main/doc/LLaMA-Oracle.png

Here, the "critic" model will act as the error function for this new word model. If this new model works, we will call it the LLaMA-Oracle.
