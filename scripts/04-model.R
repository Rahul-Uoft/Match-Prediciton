#### Preamble ####
# Purpose: Models the datasets in two logistic regressions to be analyzed in paper
# Author: Rahul Gopeesingh
# Date: 30 March 2024
# Contact: rahul.gopeesingh@mail.utoronto.ca




#### Workspace setup ####
library(tidyverse)
library(rstanarm)
library(arrow)

#### Read data ####
set.seed(853)
analysis_data <- read_parquet("data/analysis_data/t1_data_filtered_max_level.parquet")
analysis_data$Outcome <- factor(analysis_data$Outcome)
### Model data ####
t1_model <-
  stan_glm(
    formula = Outcome ~ `CS at 10` + `Max Level Lead`,
    data = analysis_data,
    family = binomial(link = "logit"),
    prior = normal(location = 0, scale = 2.5, autoscale = TRUE),
    prior_intercept = normal(location = 0, scale = 2.5, autoscale = TRUE),
    prior_aux = exponential(rate = 1, autoscale = TRUE),
    seed = 853
  )


#### Save model ####
saveRDS(
  t1_model,
  file = "models/t1_model.rds"
)
###GenG####
geng_analysis_data <- read_parquet("data/analysis_data/t1_data_filtered_max_level.parquet")
geng_analysis_data$Outcome <- factor(geng_analysis_data$Outcome)
### Model data ####
geng_model <-
  stan_glm(
    formula = Outcome ~ `CS at 10` + `Max Level Lead`,
    data = analysis_data,
    family = binomial(link = "logit"),
    prior = normal(location = 0, scale = 2.5, autoscale = TRUE),
    prior_intercept = normal(location = 0, scale = 2.5, autoscale = TRUE),
    prior_aux = exponential(rate = 1, autoscale = TRUE),
    seed = 853
  )


#### Save model ####
saveRDS(
  geng_model,
  file = "models/geng_model.rds"
)
