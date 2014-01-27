### This R script shows how to use wordcloud R package
library(wordcloud) # for using wordcloud
library(RColorBrewer) # for using more colors

### state.abb and state.area are part of R "datasets" package
wordcloud(words=state.name, freq=runif(n=length(state.name)) )
wordcloud(words=state.abb, freq=state.area)

### using more colors (instead of the default "black") and turn off random.order
wordcloud(words=state.abb, freq=state.area, colors=brewer.pal(8,"Dark2"), random.order=F)
