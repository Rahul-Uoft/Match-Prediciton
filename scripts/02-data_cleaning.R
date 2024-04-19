#### Preamble ####
# Purpose: Cleans the raw data into a digestable format
# Author: Rahul Gopeesingh
# Date: 30 March 2024
# Contact: rahul.gopeesingh@mail.utoronto.ca


#### Workspace setup ####

library(tidyverse)
library(arrow)

#### Clean data ####
t1_data <-
  read_csv(
    "data/raw_data/t1rawdata.csv",
    col_types =
      cols(
        "votereg" = col_integer(),
        "presvote20post" = col_integer(),
        "gender4" = col_integer(),
        "educ" = col_integer()
      )
  )

ces2022

ces2022 <-
  ces2022 |>
  filter(votereg == 1,
         presvote20post %in% c(1, 2)) |>
  mutate(
    voted_for = if_else(presvote20post == 1, "Biden", "Trump"),
    voted_for = as_factor(voted_for),
    gender = if_else(gender4 == 1, "Male", "Female"),
    education = case_when(
      educ == 1 ~ "No HS",
      educ == 2 ~ "High school graduate",
      educ == 3 ~ "Some college",
      educ == 4 ~ "2-year",
      educ == 5 ~ "4-year",
      educ == 6 ~ "Post-grad"
    ),
    education = factor(
      education,
      levels = c(
        "No HS",
        "High school graduate",
        "Some college",
        "2-year",
        "4-year",
        "Post-grad"
      )
    )
  ) |>
  select(voted_for, gender, education)

#### Save data ####
write_parquet(ces2022, "data/analysis_data/ces2022clean.parquet")