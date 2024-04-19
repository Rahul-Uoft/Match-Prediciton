# Match Prediction

## Overview

This repo is used to predict League of Legends matches. It uses Bayesian analysis and a logistic regression model. The model is based on the likelihood of a team winning a game based on having a level lead or a certain number of minions killed at 10 minutes.

## File Structure

The repo is structured as:

-   `data/raw_data` contains the raw data as obtained from the riot API
-   `data/analysis_data` contains the cleaned datasets that were constructed by fixing the column headers and removing unnecessary players.
-   `model` contains fitted models of both T1 and Gen G datasets.. 
-   `other` contains relevant literature, details about LLM chat interactions, and sketches.
-   `paper` contains the files used to generate the paper, including the Quarto document and reference bibliography file, as well as the PDF of the paper. 
-   `scripts` contains the R scripts used to simulate, download and clean data.


## Statement on LLM usage

Aspects of the code were written with the help of ChatGPT and the entire chat history is available in inputs/llms/usage.txt or available at https://chat.openai.com/share/526fe178-efec-43aa-8619-18f68fc58c8d
