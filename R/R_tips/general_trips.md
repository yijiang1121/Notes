Some R tips
======

R object names can start with a dot (.)
------


```r
.x <- c(1, 2)
print(.x)
```

```
## [1] 1 2
```

```r

# for a function
.len <- function(x) {
    length(x)
}
.len(c(1, 2, 3))
```

```
## [1] 3
```


About namespace in R
------
*TODO: this won't work with knitr (will explore later)*


```r
# save the default options
op <- options()
# options() can be used to examine all global options.
getOption("digits")
```

```
## [1] 4
```

```r

# :: can be used to access objects in a namespace use ::: if the object is
# not exported (private)
base::.Options$digits
```

```
## [1] 4
```

```r

## change digits to 2 below is a wrong way
base::.Options$digits <- 2
```

```
## Error: object 'base' not found
```

```r

# need to use assignInNamespace function
myOptions <- base::.Options
myOptions$digits <- 2
assignInNamespace(x = ".Options", myOptions, ns = "base")
```

```
## Error: locked binding of '.Options' cannot be changed
```

```r
base::.Options$digits
```

```
## [1] 4
```

```r
x <- 0.123456
# only show 2 digits
x
```

```
## [1] 0.1235
```

```r

myOptions$digits <- 5
assignInNamespace(x = ".Options", myOptions, ns = "base")
```

```
## Error: locked binding of '.Options' cannot be changed
```

```r
base::.Options$digits
```

```
## [1] 4
```

```r
# now show 5 digits (with rounding)
x
```

```
## [1] 0.1235
```

```r

# change the options back to default
options(op)
# return list
options("digits")
```

```
## $digits
## [1] 4
```

```r
# return value
getOption("digits")
```

```
## [1] 4
```

