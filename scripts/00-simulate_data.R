#### Preamble ####
# Purpose: Simulates data for teams winning a match after having a lead at 20 minutes
# Author: Rahul Gopeesingh
# Date: 30 March 2024
# Contact: rahul.gopeesingh@mail.utoronto.ca
# License: MIT



#### Workspace setup ####
library(tidyverse)

#### Simulate data ####

#simulate the win based on a random choice, as well as a small level lead just to test it.
#Then we simulate the cs level based on the fact that 100 cs is considered excellent 
#and 60 cs is considered poor but usually cs lies in between that number.
simulated_data <-
  tibble(
    win = sample(x = c("win", "lose"), size = 100, replace = TRUE),
    cs_at_10 = sample(x = c(rnorm(80, 20)), size = 100, replace = TRUE),
    max_level_lead = sample(x = c(1,2), size= 100, replace = TRUE)
    
  )

simulated_data
