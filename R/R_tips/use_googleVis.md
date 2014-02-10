Try googleVis package
======


```r
rm(list = ls())
# suppress messages from requiring 'googleVis'
suppressMessages(library(googleVis))

set.seed(1121)
`?`(as.Date)
mydata <- data.frame(id = 1, y = rnorm(n = 151, mean = 10, sd = 1), date = as.Date(0:150, 
    origin = "2013-09-01"))

# Motion char is not the best one for this simple data set
M <- gvisMotionChart(mydata, idvar = "id", timevar = "date")

# Timeline plot makes more sense for this data set
N <- gvisAnnotatedTimeLine(mydata, datevar = "date", numvar = "y")
```



```r
# plot(M) won't work in RMarkdown

print(M, "chart")
```

<!-- MotionChart generated in R 3.0.2 by googleVis 0.4.7 package -->
<!-- Sun Feb  9 17:29:02 2014 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataMotionChartID118961334e89 () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
 "1",
new Date(2013,8,1),
10.14495831 
],
[
 "1",
new Date(2013,8,2),
10.43832206 
],
[
 "1",
new Date(2013,8,3),
10.15319122 
],
[
 "1",
new Date(2013,8,4),
11.08494257 
],
[
 "1",
new Date(2013,8,5),
11.99954487 
],
[
 "1",
new Date(2013,8,6),
9.188116818 
],
[
 "1",
new Date(2013,8,7),
10.16026796 
],
[
 "1",
new Date(2013,8,8),
10.58589231 
],
[
 "1",
new Date(2013,8,9),
10.36008796 
],
[
 "1",
new Date(2013,8,10),
9.974691602 
],
[
 "1",
new Date(2013,8,11),
10.15088092 
],
[
 "1",
new Date(2013,8,12),
10.11008235 
],
[
 "1",
new Date(2013,8,13),
11.3596812 
],
[
 "1",
new Date(2013,8,14),
9.673005441 
],
[
 "1",
new Date(2013,8,15),
9.283618052 
],
[
 "1",
new Date(2013,8,16),
11.80976904 
],
[
 "1",
new Date(2013,8,17),
10.50840111 
],
[
 "1",
new Date(2013,8,18),
9.47253967 
],
[
 "1",
new Date(2013,8,19),
10.13271882 
],
[
 "1",
new Date(2013,8,20),
9.84405698 
],
[
 "1",
new Date(2013,8,21),
10.06414686 
],
[
 "1",
new Date(2013,8,22),
9.927638318 
],
[
 "1",
new Date(2013,8,23),
10.08806548 
],
[
 "1",
new Date(2013,8,24),
10.29775377 
],
[
 "1",
new Date(2013,8,25),
9.335398702 
],
[
 "1",
new Date(2013,8,26),
8.848974303 
],
[
 "1",
new Date(2013,8,27),
10.4049346 
],
[
 "1",
new Date(2013,8,28),
9.538213117 
],
[
 "1",
new Date(2013,8,29),
9.20813246 
],
[
 "1",
new Date(2013,8,30),
10.08349197 
],
[
 "1",
new Date(2013,9,1),
9.117781028 
],
[
 "1",
new Date(2013,9,2),
8.745312989 
],
[
 "1",
new Date(2013,9,3),
7.969165088 
],
[
 "1",
new Date(2013,9,4),
8.638629472 
],
[
 "1",
new Date(2013,9,5),
9.591923226 
],
[
 "1",
new Date(2013,9,6),
10.8165362 
],
[
 "1",
new Date(2013,9,7),
9.528659141 
],
[
 "1",
new Date(2013,9,8),
11.4256711 
],
[
 "1",
new Date(2013,9,9),
10.18027402 
],
[
 "1",
new Date(2013,9,10),
10.20019809 
],
[
 "1",
new Date(2013,9,11),
8.672061533 
],
[
 "1",
new Date(2013,9,12),
10.85617856 
],
[
 "1",
new Date(2013,9,13),
8.579655714 
],
[
 "1",
new Date(2013,9,14),
10.05129836 
],
[
 "1",
new Date(2013,9,15),
9.242789339 
],
[
 "1",
new Date(2013,9,16),
9.52629637 
],
[
 "1",
new Date(2013,9,17),
8.338891203 
],
[
 "1",
new Date(2013,9,18),
11.07331666 
],
[
 "1",
new Date(2013,9,19),
10.86965765 
],
[
 "1",
new Date(2013,9,20),
9.387672353 
],
[
 "1",
new Date(2013,9,21),
11.57252159 
],
[
 "1",
new Date(2013,9,22),
9.250684608 
],
[
 "1",
new Date(2013,9,23),
10.38140259 
],
[
 "1",
new Date(2013,9,24),
10.20779636 
],
[
 "1",
new Date(2013,9,25),
9.043563747 
],
[
 "1",
new Date(2013,9,26),
10.03431821 
],
[
 "1",
new Date(2013,9,27),
10.180569 
],
[
 "1",
new Date(2013,9,28),
9.415338028 
],
[
 "1",
new Date(2013,9,29),
9.426857227 
],
[
 "1",
new Date(2013,9,30),
8.324115781 
],
[
 "1",
new Date(2013,9,31),
10.88596177 
],
[
 "1",
new Date(2013,10,1),
9.532807101 
],
[
 "1",
new Date(2013,10,2),
8.067058079 
],
[
 "1",
new Date(2013,10,3),
11.33405494 
],
[
 "1",
new Date(2013,10,4),
10.197089 
],
[
 "1",
new Date(2013,10,5),
10.44581546 
],
[
 "1",
new Date(2013,10,6),
10.82544928 
],
[
 "1",
new Date(2013,10,7),
10.50211207 
],
[
 "1",
new Date(2013,10,8),
8.197522733 
],
[
 "1",
new Date(2013,10,9),
10.10253423 
],
[
 "1",
new Date(2013,10,10),
8.2465891 
],
[
 "1",
new Date(2013,10,11),
10.37145068 
],
[
 "1",
new Date(2013,10,12),
9.145584837 
],
[
 "1",
new Date(2013,10,13),
9.50506015 
],
[
 "1",
new Date(2013,10,14),
9.913200058 
],
[
 "1",
new Date(2013,10,15),
10.31814302 
],
[
 "1",
new Date(2013,10,16),
10.08861259 
],
[
 "1",
new Date(2013,10,17),
10.63281623 
],
[
 "1",
new Date(2013,10,18),
9.7788055 
],
[
 "1",
new Date(2013,10,19),
10.52613013 
],
[
 "1",
new Date(2013,10,20),
10.01727437 
],
[
 "1",
new Date(2013,10,21),
8.973297658 
],
[
 "1",
new Date(2013,10,22),
10.91580156 
],
[
 "1",
new Date(2013,10,23),
10.05398771 
],
[
 "1",
new Date(2013,10,24),
11.31290362 
],
[
 "1",
new Date(2013,10,25),
10.28109023 
],
[
 "1",
new Date(2013,10,26),
11.85250812 
],
[
 "1",
new Date(2013,10,27),
9.872551588 
],
[
 "1",
new Date(2013,10,28),
10.33489774 
],
[
 "1",
new Date(2013,10,29),
9.407270941 
],
[
 "1",
new Date(2013,10,30),
11.93241747 
],
[
 "1",
new Date(2013,11,1),
10.22369106 
],
[
 "1",
new Date(2013,11,2),
8.392496699 
],
[
 "1",
new Date(2013,11,3),
9.425549443 
],
[
 "1",
new Date(2013,11,4),
9.711309299 
],
[
 "1",
new Date(2013,11,5),
11.48224372 
],
[
 "1",
new Date(2013,11,6),
7.950853378 
],
[
 "1",
new Date(2013,11,7),
9.860797457 
],
[
 "1",
new Date(2013,11,8),
9.966450142 
],
[
 "1",
new Date(2013,11,9),
9.462545303 
],
[
 "1",
new Date(2013,11,10),
11.76569565 
],
[
 "1",
new Date(2013,11,11),
11.29719549 
],
[
 "1",
new Date(2013,11,12),
10.21173469 
],
[
 "1",
new Date(2013,11,13),
10.1864651 
],
[
 "1",
new Date(2013,11,14),
9.996935625 
],
[
 "1",
new Date(2013,11,15),
10.62193562 
],
[
 "1",
new Date(2013,11,16),
12.13139143 
],
[
 "1",
new Date(2013,11,17),
7.803289202 
],
[
 "1",
new Date(2013,11,18),
9.771315335 
],
[
 "1",
new Date(2013,11,19),
10.70243318 
],
[
 "1",
new Date(2013,11,20),
10.52151926 
],
[
 "1",
new Date(2013,11,21),
10.75916732 
],
[
 "1",
new Date(2013,11,22),
11.3044121 
],
[
 "1",
new Date(2013,11,23),
11.34076806 
],
[
 "1",
new Date(2013,11,24),
10.85600346 
],
[
 "1",
new Date(2013,11,25),
13.28991177 
],
[
 "1",
new Date(2013,11,26),
10.69737309 
],
[
 "1",
new Date(2013,11,27),
9.567814247 
],
[
 "1",
new Date(2013,11,28),
9.368000531 
],
[
 "1",
new Date(2013,11,29),
10.54813151 
],
[
 "1",
new Date(2013,11,30),
10.83600796 
],
[
 "1",
new Date(2013,11,31),
10.65101215 
],
[
 "1",
new Date(2014,0,1),
9.156652401 
],
[
 "1",
new Date(2014,0,2),
9.382151064 
],
[
 "1",
new Date(2014,0,3),
9.783109416 
],
[
 "1",
new Date(2014,0,4),
8.84749358 
],
[
 "1",
new Date(2014,0,5),
8.663276213 
],
[
 "1",
new Date(2014,0,6),
9.097701802 
],
[
 "1",
new Date(2014,0,7),
10.20017893 
],
[
 "1",
new Date(2014,0,8),
9.261204795 
],
[
 "1",
new Date(2014,0,9),
9.403463449 
],
[
 "1",
new Date(2014,0,10),
10.13670434 
],
[
 "1",
new Date(2014,0,11),
10.19366165 
],
[
 "1",
new Date(2014,0,12),
9.931675859 
],
[
 "1",
new Date(2014,0,13),
10.1316871 
],
[
 "1",
new Date(2014,0,14),
10.48022865 
],
[
 "1",
new Date(2014,0,15),
10.29127993 
],
[
 "1",
new Date(2014,0,16),
8.96733274 
],
[
 "1",
new Date(2014,0,17),
10.75679918 
],
[
 "1",
new Date(2014,0,18),
10.93731806 
],
[
 "1",
new Date(2014,0,19),
10.08015498 
],
[
 "1",
new Date(2014,0,20),
8.890322046 
],
[
 "1",
new Date(2014,0,21),
9.385413815 
],
[
 "1",
new Date(2014,0,22),
10.49027849 
],
[
 "1",
new Date(2014,0,23),
9.615276667 
],
[
 "1",
new Date(2014,0,24),
10.00830955 
],
[
 "1",
new Date(2014,0,25),
11.79599444 
],
[
 "1",
new Date(2014,0,26),
8.813906226 
],
[
 "1",
new Date(2014,0,27),
10.27017713 
],
[
 "1",
new Date(2014,0,28),
8.302785923 
],
[
 "1",
new Date(2014,0,29),
9.190138019 
] 
];
data.addColumn('string','id');
data.addColumn('date','date');
data.addColumn('number','y');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartMotionChartID118961334e89() {
var data = gvisDataMotionChartID118961334e89();
var options = {};
options["width"] =    600;
options["height"] =    500;

    var chart = new google.visualization.MotionChart(
    document.getElementById('MotionChartID118961334e89')
    );
    chart.draw(data,options);
    

}
  
 
// jsDisplayChart
(function() {
var pkgs = window.__gvisPackages = window.__gvisPackages || [];
var callbacks = window.__gvisCallbacks = window.__gvisCallbacks || [];
var chartid = "motionchart";
  
// Manually see if chartid is in pkgs (not all browsers support Array.indexOf)
var i, newPackage = true;
for (i = 0; newPackage && i < pkgs.length; i++) {
if (pkgs[i] === chartid)
newPackage = false;
}
if (newPackage)
  pkgs.push(chartid);
  
// Add the drawChart function to the global list of callbacks
callbacks.push(drawChartMotionChartID118961334e89);
})();
function displayChartMotionChartID118961334e89() {
  var pkgs = window.__gvisPackages = window.__gvisPackages || [];
  var callbacks = window.__gvisCallbacks = window.__gvisCallbacks || [];
  window.clearTimeout(window.__gvisLoad);
  // The timeout is set to 100 because otherwise the container div we are
  // targeting might not be part of the document yet
  window.__gvisLoad = setTimeout(function() {
  var pkgCount = pkgs.length;
  google.load("visualization", "1", { packages:pkgs, callback: function() {
  if (pkgCount != pkgs.length) {
  // Race condition where another setTimeout call snuck in after us; if
  // that call added a package, we must not shift its callback
  return;
}
while (callbacks.length > 0)
callbacks.shift()();
} });
}, 100);
}
 
// jsFooter
</script>
 
<!-- jsChart -->  
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartMotionChartID118961334e89"></script>
 
<!-- divChart -->
  
<div id="MotionChartID118961334e89"
  style="width: 600px; height: 500px;">
</div>

```r
print(N, "chart")
```

<!-- AnnotatedTimeLine generated in R 3.0.2 by googleVis 0.4.7 package -->
<!-- Sun Feb  9 17:29:02 2014 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataAnnotatedTimeLineID11896f693639 () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
 new Date(2013,8,1),
10.14495831 
],
[
 new Date(2013,8,2),
10.43832206 
],
[
 new Date(2013,8,3),
10.15319122 
],
[
 new Date(2013,8,4),
11.08494257 
],
[
 new Date(2013,8,5),
11.99954487 
],
[
 new Date(2013,8,6),
9.188116818 
],
[
 new Date(2013,8,7),
10.16026796 
],
[
 new Date(2013,8,8),
10.58589231 
],
[
 new Date(2013,8,9),
10.36008796 
],
[
 new Date(2013,8,10),
9.974691602 
],
[
 new Date(2013,8,11),
10.15088092 
],
[
 new Date(2013,8,12),
10.11008235 
],
[
 new Date(2013,8,13),
11.3596812 
],
[
 new Date(2013,8,14),
9.673005441 
],
[
 new Date(2013,8,15),
9.283618052 
],
[
 new Date(2013,8,16),
11.80976904 
],
[
 new Date(2013,8,17),
10.50840111 
],
[
 new Date(2013,8,18),
9.47253967 
],
[
 new Date(2013,8,19),
10.13271882 
],
[
 new Date(2013,8,20),
9.84405698 
],
[
 new Date(2013,8,21),
10.06414686 
],
[
 new Date(2013,8,22),
9.927638318 
],
[
 new Date(2013,8,23),
10.08806548 
],
[
 new Date(2013,8,24),
10.29775377 
],
[
 new Date(2013,8,25),
9.335398702 
],
[
 new Date(2013,8,26),
8.848974303 
],
[
 new Date(2013,8,27),
10.4049346 
],
[
 new Date(2013,8,28),
9.538213117 
],
[
 new Date(2013,8,29),
9.20813246 
],
[
 new Date(2013,8,30),
10.08349197 
],
[
 new Date(2013,9,1),
9.117781028 
],
[
 new Date(2013,9,2),
8.745312989 
],
[
 new Date(2013,9,3),
7.969165088 
],
[
 new Date(2013,9,4),
8.638629472 
],
[
 new Date(2013,9,5),
9.591923226 
],
[
 new Date(2013,9,6),
10.8165362 
],
[
 new Date(2013,9,7),
9.528659141 
],
[
 new Date(2013,9,8),
11.4256711 
],
[
 new Date(2013,9,9),
10.18027402 
],
[
 new Date(2013,9,10),
10.20019809 
],
[
 new Date(2013,9,11),
8.672061533 
],
[
 new Date(2013,9,12),
10.85617856 
],
[
 new Date(2013,9,13),
8.579655714 
],
[
 new Date(2013,9,14),
10.05129836 
],
[
 new Date(2013,9,15),
9.242789339 
],
[
 new Date(2013,9,16),
9.52629637 
],
[
 new Date(2013,9,17),
8.338891203 
],
[
 new Date(2013,9,18),
11.07331666 
],
[
 new Date(2013,9,19),
10.86965765 
],
[
 new Date(2013,9,20),
9.387672353 
],
[
 new Date(2013,9,21),
11.57252159 
],
[
 new Date(2013,9,22),
9.250684608 
],
[
 new Date(2013,9,23),
10.38140259 
],
[
 new Date(2013,9,24),
10.20779636 
],
[
 new Date(2013,9,25),
9.043563747 
],
[
 new Date(2013,9,26),
10.03431821 
],
[
 new Date(2013,9,27),
10.180569 
],
[
 new Date(2013,9,28),
9.415338028 
],
[
 new Date(2013,9,29),
9.426857227 
],
[
 new Date(2013,9,30),
8.324115781 
],
[
 new Date(2013,9,31),
10.88596177 
],
[
 new Date(2013,10,1),
9.532807101 
],
[
 new Date(2013,10,2),
8.067058079 
],
[
 new Date(2013,10,3),
11.33405494 
],
[
 new Date(2013,10,4),
10.197089 
],
[
 new Date(2013,10,5),
10.44581546 
],
[
 new Date(2013,10,6),
10.82544928 
],
[
 new Date(2013,10,7),
10.50211207 
],
[
 new Date(2013,10,8),
8.197522733 
],
[
 new Date(2013,10,9),
10.10253423 
],
[
 new Date(2013,10,10),
8.2465891 
],
[
 new Date(2013,10,11),
10.37145068 
],
[
 new Date(2013,10,12),
9.145584837 
],
[
 new Date(2013,10,13),
9.50506015 
],
[
 new Date(2013,10,14),
9.913200058 
],
[
 new Date(2013,10,15),
10.31814302 
],
[
 new Date(2013,10,16),
10.08861259 
],
[
 new Date(2013,10,17),
10.63281623 
],
[
 new Date(2013,10,18),
9.7788055 
],
[
 new Date(2013,10,19),
10.52613013 
],
[
 new Date(2013,10,20),
10.01727437 
],
[
 new Date(2013,10,21),
8.973297658 
],
[
 new Date(2013,10,22),
10.91580156 
],
[
 new Date(2013,10,23),
10.05398771 
],
[
 new Date(2013,10,24),
11.31290362 
],
[
 new Date(2013,10,25),
10.28109023 
],
[
 new Date(2013,10,26),
11.85250812 
],
[
 new Date(2013,10,27),
9.872551588 
],
[
 new Date(2013,10,28),
10.33489774 
],
[
 new Date(2013,10,29),
9.407270941 
],
[
 new Date(2013,10,30),
11.93241747 
],
[
 new Date(2013,11,1),
10.22369106 
],
[
 new Date(2013,11,2),
8.392496699 
],
[
 new Date(2013,11,3),
9.425549443 
],
[
 new Date(2013,11,4),
9.711309299 
],
[
 new Date(2013,11,5),
11.48224372 
],
[
 new Date(2013,11,6),
7.950853378 
],
[
 new Date(2013,11,7),
9.860797457 
],
[
 new Date(2013,11,8),
9.966450142 
],
[
 new Date(2013,11,9),
9.462545303 
],
[
 new Date(2013,11,10),
11.76569565 
],
[
 new Date(2013,11,11),
11.29719549 
],
[
 new Date(2013,11,12),
10.21173469 
],
[
 new Date(2013,11,13),
10.1864651 
],
[
 new Date(2013,11,14),
9.996935625 
],
[
 new Date(2013,11,15),
10.62193562 
],
[
 new Date(2013,11,16),
12.13139143 
],
[
 new Date(2013,11,17),
7.803289202 
],
[
 new Date(2013,11,18),
9.771315335 
],
[
 new Date(2013,11,19),
10.70243318 
],
[
 new Date(2013,11,20),
10.52151926 
],
[
 new Date(2013,11,21),
10.75916732 
],
[
 new Date(2013,11,22),
11.3044121 
],
[
 new Date(2013,11,23),
11.34076806 
],
[
 new Date(2013,11,24),
10.85600346 
],
[
 new Date(2013,11,25),
13.28991177 
],
[
 new Date(2013,11,26),
10.69737309 
],
[
 new Date(2013,11,27),
9.567814247 
],
[
 new Date(2013,11,28),
9.368000531 
],
[
 new Date(2013,11,29),
10.54813151 
],
[
 new Date(2013,11,30),
10.83600796 
],
[
 new Date(2013,11,31),
10.65101215 
],
[
 new Date(2014,0,1),
9.156652401 
],
[
 new Date(2014,0,2),
9.382151064 
],
[
 new Date(2014,0,3),
9.783109416 
],
[
 new Date(2014,0,4),
8.84749358 
],
[
 new Date(2014,0,5),
8.663276213 
],
[
 new Date(2014,0,6),
9.097701802 
],
[
 new Date(2014,0,7),
10.20017893 
],
[
 new Date(2014,0,8),
9.261204795 
],
[
 new Date(2014,0,9),
9.403463449 
],
[
 new Date(2014,0,10),
10.13670434 
],
[
 new Date(2014,0,11),
10.19366165 
],
[
 new Date(2014,0,12),
9.931675859 
],
[
 new Date(2014,0,13),
10.1316871 
],
[
 new Date(2014,0,14),
10.48022865 
],
[
 new Date(2014,0,15),
10.29127993 
],
[
 new Date(2014,0,16),
8.96733274 
],
[
 new Date(2014,0,17),
10.75679918 
],
[
 new Date(2014,0,18),
10.93731806 
],
[
 new Date(2014,0,19),
10.08015498 
],
[
 new Date(2014,0,20),
8.890322046 
],
[
 new Date(2014,0,21),
9.385413815 
],
[
 new Date(2014,0,22),
10.49027849 
],
[
 new Date(2014,0,23),
9.615276667 
],
[
 new Date(2014,0,24),
10.00830955 
],
[
 new Date(2014,0,25),
11.79599444 
],
[
 new Date(2014,0,26),
8.813906226 
],
[
 new Date(2014,0,27),
10.27017713 
],
[
 new Date(2014,0,28),
8.302785923 
],
[
 new Date(2014,0,29),
9.190138019 
] 
];
data.addColumn('date','date');
data.addColumn('number','y');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartAnnotatedTimeLineID11896f693639() {
var data = gvisDataAnnotatedTimeLineID11896f693639();
var options = {};
options["width"] =    600;
options["height"] =    300;

    var chart = new google.visualization.AnnotatedTimeLine(
    document.getElementById('AnnotatedTimeLineID11896f693639')
    );
    chart.draw(data,options);
    

}
  
 
// jsDisplayChart
(function() {
var pkgs = window.__gvisPackages = window.__gvisPackages || [];
var callbacks = window.__gvisCallbacks = window.__gvisCallbacks || [];
var chartid = "annotatedtimeline";
  
// Manually see if chartid is in pkgs (not all browsers support Array.indexOf)
var i, newPackage = true;
for (i = 0; newPackage && i < pkgs.length; i++) {
if (pkgs[i] === chartid)
newPackage = false;
}
if (newPackage)
  pkgs.push(chartid);
  
// Add the drawChart function to the global list of callbacks
callbacks.push(drawChartAnnotatedTimeLineID11896f693639);
})();
function displayChartAnnotatedTimeLineID11896f693639() {
  var pkgs = window.__gvisPackages = window.__gvisPackages || [];
  var callbacks = window.__gvisCallbacks = window.__gvisCallbacks || [];
  window.clearTimeout(window.__gvisLoad);
  // The timeout is set to 100 because otherwise the container div we are
  // targeting might not be part of the document yet
  window.__gvisLoad = setTimeout(function() {
  var pkgCount = pkgs.length;
  google.load("visualization", "1", { packages:pkgs, callback: function() {
  if (pkgCount != pkgs.length) {
  // Race condition where another setTimeout call snuck in after us; if
  // that call added a package, we must not shift its callback
  return;
}
while (callbacks.length > 0)
callbacks.shift()();
} });
}, 100);
}
 
// jsFooter
</script>
 
<!-- jsChart -->  
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartAnnotatedTimeLineID11896f693639"></script>
 
<!-- divChart -->
  
<div id="AnnotatedTimeLineID11896f693639"
  style="width: 600px; height: 300px;">
</div>

