library("rio")
library("dplyr")
library("tidyr")
url <- "https://github.com/lamethods/data/raw/main/1_moodleLAcourse/"
events <- import(paste0(url, "Events.xlsx"), setclass = "tibble")
demographics <- import(paste0(url, "Demographics.xlsx"), setclass = "tibble")
results <- import(paste0(url, "Results.xlsx"), setclass = "tibble") |>
mutate(
AchievingGroup = factor(
case_when(
ntile(Final_grade, 2) == 1 ~ "Low achiever",
ntile(Final_grade, 2) == 2 ~ "High achiever"
)
)
)