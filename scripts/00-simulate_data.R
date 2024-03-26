#### Preamble ####
# Purpose: Simulates data for teams winning a match after having a lead at 20 minutes
# Author: Rahul Gopeesingh
# Date: 26 March 2024
# Contact: rahul.gopeesingh@mail.utoronto.ca
# License: MIT



#### Workspace setup ####
library(tidyverse)

#### Simulate data ####
data <-
  tibble(
    win = sample(x = c("win", "lose"), size = 1000, replace = TRUE),
    leading_at_20 = sample(x = c("yes", "no"), size = 1000, replace = TRUE)
    
  )


