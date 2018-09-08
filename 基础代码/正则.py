import re
str = "http://www.mininova.org/tor/2676093"
print re.search('/tor/(\d+)',str).group(1)