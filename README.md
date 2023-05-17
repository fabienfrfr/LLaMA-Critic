# LLaMA-critic
Exploring of an minimal LLaMA LLM model (7B) with Reinforcement Learning Critic method for Fact Checking

**Ideas :** 
  - Environment : Universal Assertion Generator (Bayesian)
  - Actor with Critics (% True/False) : LLaMA (last layer is cut) + Attention Extention


This project is based of minimal, hackable and readable example to load [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) ([arXiv](https://arxiv.org/abs/2302.13971v1)) [Meta](https://github.com/facebookresearch/llama) models and run inference. In order to download the checkpoints and tokenizer, fill this [google form](https://forms.gle/jk851eBVbX1m5TAv5)

**Principles of model :**

The model consists of two parts:

  - Encoder: The encoder takes the input context (a set of text). The last layer for predicting the next word is not considered, allowing us to pass the raw information from the model to the decoder. The Meta model has already been trained, and we will use it for transfer learning.
  - Decoder: This model will predict whether the sentence is true or false. It is also based on attention, but it is smaller than the previous model and corresponds to the one to be trained.

![LLaMA-critic](LLaMA-critic.png)

**Perspective :**

This model opposes Yann LeCun's vision on the concept of "common sense" for achieving a general AI. Using this model, we can combine it with a large language model to predict only "plausible" sequences of words. This would involve replacing the last layer with one or multiple trainable layers to predict new words. Here, the "critic" model will act as the error function for this model. If this model works, we will call it the ORACLE.
