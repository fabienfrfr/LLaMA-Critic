.. -*- mode: rst -*-

**Attribution required : Fabien Furfaro (CC 4.0 BY NC ND SA)**

.. image:: https://raw.githubusercontent.com/fabienfrfr/LLaMA-Critic/main/branding/logo.png 
	:align: center

**LLaMA-Critic** is PyTorch model trained for fact checking of a minimal LLaMA LLM model (7B)

This project explore a method to fine tune LLM model with Critic strategy.

Ideas
------------

  - Environment : Universal Assertion Generator (Bayesian) - Possibilities of Reinforcement 
  - Actor with Critics (% True/False) : LLaMA (last layer is cut) + Attention Extention

*This project is based of minimal, hackable and readable example to load* `LLaMA <https://ai.facebook.com/blog/large-language-model-llama-meta-ai/>`__ (`arXiv <https://arxiv.org/abs/2302.13971v1>`__) `Meta <https://github.com/facebookresearch/llama>`__ *models and run inference. In order to download the checkpoints and tokenizer, fill this* `google form <https://forms.gle/jk851eBVbX1m5TAv5>`__ 

Objectives
------------

Usable in a single computer after training (max 16 Gb) and some smartphone.

Adding causality notion in LLM model for futur fine tuning.

.. image:: https://raw.githubusercontent.com/fabienfrfr/LLaMA-Critic/main/doc/LC_principles.png

This opposes the notion of "Valley of knowledge" (actual llm model) and the concept of "Tree of knowledge" (expected model).

Principles of model
------------

The model consists of two parts:

  - **Encoder**: The encoder takes the input context (a set of text). The last layer for predicting the next word is not considered, allowing us to pass the raw information from the model to the decoder. The Meta model has already been trained, and we will use it for transfer learning.
  - **Decoder**: This model will predict whether the sentence is true or false. It is also based on attention, but it is smaller than the previous model and corresponds to the one to be trained.


.. image:: https://raw.githubusercontent.com/fabienfrfr/LLaMA-Critic/main/doc/LLaMA-critic.png


Simulation environment
------------

The environement generate sentence of mathematic's relation, and also QCM and universal knowledge.

The math sentence is based on simplified `DeepMind Mathematics dataset generator <https://github.com/deepmind/mathematics_dataset>`__) (use SymPy).

For natural language, we limit to the test of similarity (use word2vec). Also, subjective sentences taken into account where their values are between true and false (use nltk). 

For an intransigent calculation, i.e. a single false sentence is enough for all the sentences to be false (same principle for subjective sentence), the probability that a false sentence appears is defined by:

.. math:: P = \frac{1}{2^{N}}

With "N", the number of sentences possible in the training batch.

More detail in documentation with example.


Perspective
------------

This model opposes actual consensus vision on the concept of "common sense" for achieving a general AI. Using this model, we can combine it with a large language model to predict only "plausible" sequences of words (Bayesian probability). This would involve replacing the last layer with one or multiple trainable layers to predict new words. 

.. image:: https://raw.githubusercontent.com/fabienfrfr/LLaMA-Critic/main/doc/LLaMA-Oracle.png

Here, the "critic" model will act as the error function for this new word model. If this new model works, we will call it the LLaMA-Oracle. The dataset generated here can be upgrade be Tree of Thought method, and here, we conserve bad branch but the evaluation is used for optimization of LLaMA-Oracle.

An other ideas, more simple, is to use one model to predict the next-word and evaluation of prompt. This way, the model is fully trained for critical thinking by just adding a thought tree/chain evaluation neuron. In this way, it is an alternative to the simulation environment, we just need a dataset generator and a small modification of the model.

.. image:: https://raw.githubusercontent.com/fabienfrfr/LLaMA-Critic/main/doc/LLaMA-ToT-Critic.png


Citation
------------

If you find the model, data, and code in our project useful, please consider citing our work as follows:

	@article{llama-critic,
	author = {Fabien Furfaro},
	title = {Exploring of an LLaMA LLM model with Critic method for Fact Checking},
	year = {2023},
	publisher = {GitHub},
	journal = {GitHub repository},
	howpublished = {\url{https://github.com/fabienfrfr/LLaMA-Critic}},
	}


**References : **

	- `Vigogne Project <https://github.com/bofenghuang/vigogne>`__.
	- `Tree of Thought <https://github.com/ysymyth/tree-of-thought-llm>`__.
	- (...)
