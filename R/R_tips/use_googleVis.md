Try googleVis package
======


```r
rm(list = ls())
# suppress messages from requiring 'googleVis'
suppressMessages(library(googleVis))

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

# this won't work for M TODO: figure out why
print(M, "chart")
```

<!-- MotionChart generated in R 3.0.2 by googleVis 0.4.7 package -->
<!-- Sun Feb  9 17:18:01 2014 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataMotionChartIDef43d20ac91 () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
 "1",
new Date(2013,8,1),
10.01207057 
],
[
 "1",
new Date(2013,8,2),
11.50931182 
],
[
 "1",
new Date(2013,8,3),
8.770500836 
],
[
 "1",
new Date(2013,8,4),
9.972454839 
],
[
 "1",
new Date(2013,8,5),
9.58430418 
],
[
 "1",
new Date(2013,8,6),
8.810399025 
],
[
 "1",
new Date(2013,8,7),
11.44878047 
],
[
 "1",
new Date(2013,8,8),
11.46035475 
],
[
 "1",
new Date(2013,8,9),
10.54945317 
],
[
 "1",
new Date(2013,8,10),
10.47336964 
],
[
 "1",
new Date(2013,8,11),
11.57216397 
],
[
 "1",
new Date(2013,8,12),
9.477036127 
],
[
 "1",
new Date(2013,8,13),
8.93440672 
],
[
 "1",
new Date(2013,8,14),
9.89239122 
],
[
 "1",
new Date(2013,8,15),
9.651812313 
],
[
 "1",
new Date(2013,8,16),
10.11592054 
],
[
 "1",
new Date(2013,8,17),
8.211671331 
],
[
 "1",
new Date(2013,8,18),
10.25510693 
],
[
 "1",
new Date(2013,8,19),
9.509969878 
],
[
 "1",
new Date(2013,8,20),
8.827459333 
],
[
 "1",
new Date(2013,8,21),
9.338031732 
],
[
 "1",
new Date(2013,8,22),
9.821915158 
],
[
 "1",
new Date(2013,8,23),
11.43626648 
],
[
 "1",
new Date(2013,8,24),
9.517745683 
],
[
 "1",
new Date(2013,8,25),
9.810424715 
],
[
 "1",
new Date(2013,8,26),
10.59071402 
],
[
 "1",
new Date(2013,8,27),
9.573546283 
],
[
 "1",
new Date(2013,8,28),
10.94595831 
],
[
 "1",
new Date(2013,8,29),
10.80178946 
],
[
 "1",
new Date(2013,8,30),
10.3848434 
],
[
 "1",
new Date(2013,9,1),
11.02616715 
],
[
 "1",
new Date(2013,9,2),
10.34305049 
],
[
 "1",
new Date(2013,9,3),
9.642296943 
],
[
 "1",
new Date(2013,9,4),
10.02874081 
],
[
 "1",
new Date(2013,9,5),
11.45956554 
],
[
 "1",
new Date(2013,9,6),
9.831222328 
],
[
 "1",
new Date(2013,9,7),
7.804893762 
],
[
 "1",
new Date(2013,9,8),
9.763260088 
],
[
 "1",
new Date(2013,9,9),
8.369182239 
],
[
 "1",
new Date(2013,9,10),
9.636454222 
],
[
 "1",
new Date(2013,9,11),
9.25103059 
],
[
 "1",
new Date(2013,9,12),
11.09918264 
],
[
 "1",
new Date(2013,9,13),
11.69056788 
],
[
 "1",
new Date(2013,9,14),
9.031916845 
],
[
 "1",
new Date(2013,9,15),
10.43596734 
],
[
 "1",
new Date(2013,9,16),
11.42633855 
],
[
 "1",
new Date(2013,9,17),
11.33535672 
],
[
 "1",
new Date(2013,9,18),
10.79589972 
],
[
 "1",
new Date(2013,9,19),
10.60352294 
],
[
 "1",
new Date(2013,9,20),
10.47469625 
],
[
 "1",
new Date(2013,9,21),
11.46817445 
],
[
 "1",
new Date(2013,9,22),
10.26114392 
],
[
 "1",
new Date(2013,9,23),
10.01994295 
],
[
 "1",
new Date(2013,9,24),
9.797365173 
],
[
 "1",
new Date(2013,9,25),
10.14182103 
],
[
 "1",
new Date(2013,9,26),
8.401876635 
],
[
 "1",
new Date(2013,9,27),
10.13321988 
],
[
 "1",
new Date(2013,9,28),
11.17201783 
],
[
 "1",
new Date(2013,9,29),
12.22681493 
],
[
 "1",
new Date(2013,9,30),
11.86032647 
],
[
 "1",
new Date(2013,9,31),
9.956103904 
],
[
 "1",
new Date(2013,10,1),
10.90617886 
],
[
 "1",
new Date(2013,10,2),
7.827485719 
],
[
 "1",
new Date(2013,10,3),
9.015537348 
],
[
 "1",
new Date(2013,10,4),
11.28228292 
],
[
 "1",
new Date(2013,10,5),
8.88047637 
],
[
 "1",
new Date(2013,10,6),
10.86604452 
],
[
 "1",
new Date(2013,10,7),
8.864416238 
],
[
 "1",
new Date(2013,10,8),
8.538831287 
],
[
 "1",
new Date(2013,10,9),
9.866245965 
],
[
 "1",
new Date(2013,10,10),
11.98868043 
],
[
 "1",
new Date(2013,10,11),
9.637513261 
],
[
 "1",
new Date(2013,10,12),
10.67624984 
],
[
 "1",
new Date(2013,10,13),
9.142383998 
],
[
 "1",
new Date(2013,10,14),
9.492472276 
],
[
 "1",
new Date(2013,10,15),
11.63688417 
],
[
 "1",
new Date(2013,10,16),
8.983555523 
],
[
 "1",
new Date(2013,10,17),
10.96056625 
],
[
 "1",
new Date(2013,10,18),
9.933322138 
],
[
 "1",
new Date(2013,10,19),
9.633701025 
],
[
 "1",
new Date(2013,10,20),
10.21155717 
],
[
 "1",
new Date(2013,10,21),
9.489868973 
],
[
 "1",
new Date(2013,10,22),
10.10887943 
],
[
 "1",
new Date(2013,10,23),
9.907266712 
],
[
 "1",
new Date(2013,10,24),
10.21432357 
],
[
 "1",
new Date(2013,10,25),
10.0390214 
],
[
 "1",
new Date(2013,10,26),
10.14184872 
],
[
 "1",
new Date(2013,10,27),
10.37391988 
],
[
 "1",
new Date(2013,10,28),
10.3948244 
],
[
 "1",
new Date(2013,10,29),
11.28422833 
],
[
 "1",
new Date(2013,10,30),
9.69794126 
],
[
 "1",
new Date(2013,11,1),
9.246915634 
],
[
 "1",
new Date(2013,11,2),
10.05463922 
],
[
 "1",
new Date(2013,11,3),
10.50010307 
],
[
 "1",
new Date(2013,11,4),
10.42058894 
],
[
 "1",
new Date(2013,11,5),
10.46630131 
],
[
 "1",
new Date(2013,11,6),
7.791291671 
],
[
 "1",
new Date(2013,11,7),
8.871474148 
],
[
 "1",
new Date(2013,11,8),
10.55234445 
],
[
 "1",
new Date(2013,11,9),
9.862542784 
],
[
 "1",
new Date(2013,11,10),
10.04549772 
],
[
 "1",
new Date(2013,11,11),
9.810724416 
],
[
 "1",
new Date(2013,11,12),
9.863232187 
],
[
 "1",
new Date(2013,11,13),
9.676854523 
],
[
 "1",
new Date(2013,11,14),
11.35946267 
],
[
 "1",
new Date(2013,11,15),
9.506290242 
],
[
 "1",
new Date(2013,11,16),
9.149426551 
],
[
 "1",
new Date(2013,11,17),
10.52306849 
],
[
 "1",
new Date(2013,11,18),
10.15459699 
],
[
 "1",
new Date(2013,11,19),
11.2364086 
],
[
 "1",
new Date(2013,11,20),
11.21459253 
],
[
 "1",
new Date(2013,11,21),
10.39087731 
],
[
 "1",
new Date(2013,11,22),
10.2738244 
],
[
 "1",
new Date(2013,11,23),
10.39921434 
],
[
 "1",
new Date(2013,11,24),
10.37618639 
],
[
 "1",
new Date(2013,11,25),
10.12293196 
],
[
 "1",
new Date(2013,11,26),
10.14710131 
],
[
 "1",
new Date(2013,11,27),
10.16646787 
],
[
 "1",
new Date(2013,11,28),
8.906997323 
],
[
 "1",
new Date(2013,11,29),
10.4495864 
],
[
 "1",
new Date(2013,11,30),
10.05103765 
],
[
 "1",
new Date(2013,11,31),
9.688621949 
],
[
 "1",
new Date(2014,0,1),
9.901423942 
],
[
 "1",
new Date(2014,0,2),
9.503730311 
],
[
 "1",
new Date(2014,0,3),
10.40932495 
],
[
 "1",
new Date(2014,0,4),
5.653503762 
],
[
 "1",
new Date(2014,0,5),
11.48889714 
],
[
 "1",
new Date(2014,0,6),
11.13915966 
],
[
 "1",
new Date(2014,0,7),
10.32472766 
],
[
 "1",
new Date(2014,0,8),
9.353004983 
],
[
 "1",
new Date(2014,0,9),
11.27207107 
],
[
 "1",
new Date(2014,0,10),
10.84347837 
],
[
 "1",
new Date(2014,0,11),
11.07412271 
],
[
 "1",
new Date(2014,0,12),
11.08309532 
],
[
 "1",
new Date(2014,0,13),
9.547228902 
],
[
 "1",
new Date(2014,0,14),
9.527157214 
],
[
 "1",
new Date(2014,0,15),
11.22983387 
],
[
 "1",
new Date(2014,0,16),
8.441197733 
],
[
 "1",
new Date(2014,0,17),
9.641842792 
],
[
 "1",
new Date(2014,0,18),
9.659259561 
],
[
 "1",
new Date(2014,0,19),
10.5128711 
],
[
 "1",
new Date(2014,0,20),
10.51684198 
],
[
 "1",
new Date(2014,0,21),
9.876579033 
],
[
 "1",
new Date(2014,0,22),
9.006148939 
],
[
 "1",
new Date(2014,0,23),
9.816007574 
],
[
 "1",
new Date(2014,0,24),
10.99790253 
],
[
 "1",
new Date(2014,0,25),
8.558204763 
],
[
 "1",
new Date(2014,0,26),
9.625932343 
],
[
 "1",
new Date(2014,0,27),
11.27959933 
],
[
 "1",
new Date(2014,0,28),
9.57985431 
],
[
 "1",
new Date(2014,0,29),
10.17264303 
] 
];
data.addColumn('string','id');
data.addColumn('date','date');
data.addColumn('number','y');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartMotionChartIDef43d20ac91() {
var data = gvisDataMotionChartIDef43d20ac91();
var options = {};
options["width"] =    600;
options["height"] =    500;

    var chart = new google.visualization.MotionChart(
    document.getElementById('MotionChartIDef43d20ac91')
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
callbacks.push(drawChartMotionChartIDef43d20ac91);
})();
function displayChartMotionChartIDef43d20ac91() {
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
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartMotionChartIDef43d20ac91"></script>
 
<!-- divChart -->
  
<div id="MotionChartIDef43d20ac91"
  style="width: 600px; height: 500px;">
</div>

```r
print(N, "chart")
```

<!-- AnnotatedTimeLine generated in R 3.0.2 by googleVis 0.4.7 package -->
<!-- Sun Feb  9 17:18:01 2014 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataAnnotatedTimeLineIDef42c2182f1 () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
 new Date(2013,8,1),
10.01207057 
],
[
 new Date(2013,8,2),
11.50931182 
],
[
 new Date(2013,8,3),
8.770500836 
],
[
 new Date(2013,8,4),
9.972454839 
],
[
 new Date(2013,8,5),
9.58430418 
],
[
 new Date(2013,8,6),
8.810399025 
],
[
 new Date(2013,8,7),
11.44878047 
],
[
 new Date(2013,8,8),
11.46035475 
],
[
 new Date(2013,8,9),
10.54945317 
],
[
 new Date(2013,8,10),
10.47336964 
],
[
 new Date(2013,8,11),
11.57216397 
],
[
 new Date(2013,8,12),
9.477036127 
],
[
 new Date(2013,8,13),
8.93440672 
],
[
 new Date(2013,8,14),
9.89239122 
],
[
 new Date(2013,8,15),
9.651812313 
],
[
 new Date(2013,8,16),
10.11592054 
],
[
 new Date(2013,8,17),
8.211671331 
],
[
 new Date(2013,8,18),
10.25510693 
],
[
 new Date(2013,8,19),
9.509969878 
],
[
 new Date(2013,8,20),
8.827459333 
],
[
 new Date(2013,8,21),
9.338031732 
],
[
 new Date(2013,8,22),
9.821915158 
],
[
 new Date(2013,8,23),
11.43626648 
],
[
 new Date(2013,8,24),
9.517745683 
],
[
 new Date(2013,8,25),
9.810424715 
],
[
 new Date(2013,8,26),
10.59071402 
],
[
 new Date(2013,8,27),
9.573546283 
],
[
 new Date(2013,8,28),
10.94595831 
],
[
 new Date(2013,8,29),
10.80178946 
],
[
 new Date(2013,8,30),
10.3848434 
],
[
 new Date(2013,9,1),
11.02616715 
],
[
 new Date(2013,9,2),
10.34305049 
],
[
 new Date(2013,9,3),
9.642296943 
],
[
 new Date(2013,9,4),
10.02874081 
],
[
 new Date(2013,9,5),
11.45956554 
],
[
 new Date(2013,9,6),
9.831222328 
],
[
 new Date(2013,9,7),
7.804893762 
],
[
 new Date(2013,9,8),
9.763260088 
],
[
 new Date(2013,9,9),
8.369182239 
],
[
 new Date(2013,9,10),
9.636454222 
],
[
 new Date(2013,9,11),
9.25103059 
],
[
 new Date(2013,9,12),
11.09918264 
],
[
 new Date(2013,9,13),
11.69056788 
],
[
 new Date(2013,9,14),
9.031916845 
],
[
 new Date(2013,9,15),
10.43596734 
],
[
 new Date(2013,9,16),
11.42633855 
],
[
 new Date(2013,9,17),
11.33535672 
],
[
 new Date(2013,9,18),
10.79589972 
],
[
 new Date(2013,9,19),
10.60352294 
],
[
 new Date(2013,9,20),
10.47469625 
],
[
 new Date(2013,9,21),
11.46817445 
],
[
 new Date(2013,9,22),
10.26114392 
],
[
 new Date(2013,9,23),
10.01994295 
],
[
 new Date(2013,9,24),
9.797365173 
],
[
 new Date(2013,9,25),
10.14182103 
],
[
 new Date(2013,9,26),
8.401876635 
],
[
 new Date(2013,9,27),
10.13321988 
],
[
 new Date(2013,9,28),
11.17201783 
],
[
 new Date(2013,9,29),
12.22681493 
],
[
 new Date(2013,9,30),
11.86032647 
],
[
 new Date(2013,9,31),
9.956103904 
],
[
 new Date(2013,10,1),
10.90617886 
],
[
 new Date(2013,10,2),
7.827485719 
],
[
 new Date(2013,10,3),
9.015537348 
],
[
 new Date(2013,10,4),
11.28228292 
],
[
 new Date(2013,10,5),
8.88047637 
],
[
 new Date(2013,10,6),
10.86604452 
],
[
 new Date(2013,10,7),
8.864416238 
],
[
 new Date(2013,10,8),
8.538831287 
],
[
 new Date(2013,10,9),
9.866245965 
],
[
 new Date(2013,10,10),
11.98868043 
],
[
 new Date(2013,10,11),
9.637513261 
],
[
 new Date(2013,10,12),
10.67624984 
],
[
 new Date(2013,10,13),
9.142383998 
],
[
 new Date(2013,10,14),
9.492472276 
],
[
 new Date(2013,10,15),
11.63688417 
],
[
 new Date(2013,10,16),
8.983555523 
],
[
 new Date(2013,10,17),
10.96056625 
],
[
 new Date(2013,10,18),
9.933322138 
],
[
 new Date(2013,10,19),
9.633701025 
],
[
 new Date(2013,10,20),
10.21155717 
],
[
 new Date(2013,10,21),
9.489868973 
],
[
 new Date(2013,10,22),
10.10887943 
],
[
 new Date(2013,10,23),
9.907266712 
],
[
 new Date(2013,10,24),
10.21432357 
],
[
 new Date(2013,10,25),
10.0390214 
],
[
 new Date(2013,10,26),
10.14184872 
],
[
 new Date(2013,10,27),
10.37391988 
],
[
 new Date(2013,10,28),
10.3948244 
],
[
 new Date(2013,10,29),
11.28422833 
],
[
 new Date(2013,10,30),
9.69794126 
],
[
 new Date(2013,11,1),
9.246915634 
],
[
 new Date(2013,11,2),
10.05463922 
],
[
 new Date(2013,11,3),
10.50010307 
],
[
 new Date(2013,11,4),
10.42058894 
],
[
 new Date(2013,11,5),
10.46630131 
],
[
 new Date(2013,11,6),
7.791291671 
],
[
 new Date(2013,11,7),
8.871474148 
],
[
 new Date(2013,11,8),
10.55234445 
],
[
 new Date(2013,11,9),
9.862542784 
],
[
 new Date(2013,11,10),
10.04549772 
],
[
 new Date(2013,11,11),
9.810724416 
],
[
 new Date(2013,11,12),
9.863232187 
],
[
 new Date(2013,11,13),
9.676854523 
],
[
 new Date(2013,11,14),
11.35946267 
],
[
 new Date(2013,11,15),
9.506290242 
],
[
 new Date(2013,11,16),
9.149426551 
],
[
 new Date(2013,11,17),
10.52306849 
],
[
 new Date(2013,11,18),
10.15459699 
],
[
 new Date(2013,11,19),
11.2364086 
],
[
 new Date(2013,11,20),
11.21459253 
],
[
 new Date(2013,11,21),
10.39087731 
],
[
 new Date(2013,11,22),
10.2738244 
],
[
 new Date(2013,11,23),
10.39921434 
],
[
 new Date(2013,11,24),
10.37618639 
],
[
 new Date(2013,11,25),
10.12293196 
],
[
 new Date(2013,11,26),
10.14710131 
],
[
 new Date(2013,11,27),
10.16646787 
],
[
 new Date(2013,11,28),
8.906997323 
],
[
 new Date(2013,11,29),
10.4495864 
],
[
 new Date(2013,11,30),
10.05103765 
],
[
 new Date(2013,11,31),
9.688621949 
],
[
 new Date(2014,0,1),
9.901423942 
],
[
 new Date(2014,0,2),
9.503730311 
],
[
 new Date(2014,0,3),
10.40932495 
],
[
 new Date(2014,0,4),
5.653503762 
],
[
 new Date(2014,0,5),
11.48889714 
],
[
 new Date(2014,0,6),
11.13915966 
],
[
 new Date(2014,0,7),
10.32472766 
],
[
 new Date(2014,0,8),
9.353004983 
],
[
 new Date(2014,0,9),
11.27207107 
],
[
 new Date(2014,0,10),
10.84347837 
],
[
 new Date(2014,0,11),
11.07412271 
],
[
 new Date(2014,0,12),
11.08309532 
],
[
 new Date(2014,0,13),
9.547228902 
],
[
 new Date(2014,0,14),
9.527157214 
],
[
 new Date(2014,0,15),
11.22983387 
],
[
 new Date(2014,0,16),
8.441197733 
],
[
 new Date(2014,0,17),
9.641842792 
],
[
 new Date(2014,0,18),
9.659259561 
],
[
 new Date(2014,0,19),
10.5128711 
],
[
 new Date(2014,0,20),
10.51684198 
],
[
 new Date(2014,0,21),
9.876579033 
],
[
 new Date(2014,0,22),
9.006148939 
],
[
 new Date(2014,0,23),
9.816007574 
],
[
 new Date(2014,0,24),
10.99790253 
],
[
 new Date(2014,0,25),
8.558204763 
],
[
 new Date(2014,0,26),
9.625932343 
],
[
 new Date(2014,0,27),
11.27959933 
],
[
 new Date(2014,0,28),
9.57985431 
],
[
 new Date(2014,0,29),
10.17264303 
] 
];
data.addColumn('date','date');
data.addColumn('number','y');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartAnnotatedTimeLineIDef42c2182f1() {
var data = gvisDataAnnotatedTimeLineIDef42c2182f1();
var options = {};
options["width"] =    600;
options["height"] =    300;

    var chart = new google.visualization.AnnotatedTimeLine(
    document.getElementById('AnnotatedTimeLineIDef42c2182f1')
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
callbacks.push(drawChartAnnotatedTimeLineIDef42c2182f1);
})();
function displayChartAnnotatedTimeLineIDef42c2182f1() {
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
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartAnnotatedTimeLineIDef42c2182f1"></script>
 
<!-- divChart -->
  
<div id="AnnotatedTimeLineIDef42c2182f1"
  style="width: 600px; height: 300px;">
</div>

