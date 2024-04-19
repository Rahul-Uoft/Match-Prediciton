#### Preamble ####
# Purpose: Simulates data for teams winning a match after having a lead at 20 minutes
# Author: Rahul Gopeesingh
# Date: 30 March 2024
# Contact: rahul.gopeesingh@mail.utoronto.ca
# License: MIT



#### Workspace setup ####
library(tidyverse)

#### Simulate data ####
simulated_data <-
  tibble(
    win = sample(x = c("win", "lose"), size = 100, replace = TRUE),
    cs_at_10 = sample(x = c(rnorm(80, 20)), size = 100, replace = TRUE),
    max_level_lead = sample(x = c(1,2), size= 100, replace = TRUE)
    
  )

simulated_data
