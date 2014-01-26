### This R script shows how to use wordcloud R package
library(wordcloud)

### state.abb and state.area are part of R "datasets" package
wordcloud(words=state.name, freq=runif(n=length(state.name)) )
wordcloud(words=state.abb, freq=state.area)