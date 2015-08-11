![alt tag](https://raw.github.com/loucru1/flix/master/imgs/flix_small.png)

A command line tool to get the info on all the latest movies. 

# How it works
Flix parses www.google.com/movies to gather the current movie times at a given location. 

Ex:

```
$ flix 90210
Laemmle's Music Hall 3:

Love & Mercy
1:00 | 4:00 | 7:00pm 

Me and Earl and the Dying Girl
2:30pm 

Call Me Lucky
12:00 | 2:30 | 5:00 | 7:30 | 10:00pm 

Sneakerheadz
10:00pm 

Bolshoi Ballet: Ivan the Terrible
7:30pm 

Catch Me Daddy
12:00 | 5:00pm 

Reset
9:55pm
```

#Installation
Requirements: pipsi (https://github.com/mitsuhiko/pipsi)

1) Clone the flix repository
```
$ git clone https://github.com/loucru1/flix.git
``` 
2) Install flix using pipsi in flix directory. The --editable tag is useful to be able to make changes to the code.
```
$ pipsi install --editable .
```


  
