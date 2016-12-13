# BSQF - SQF preprocessor

Objective of this project is to implement a enhanced scripting language for
Armed Assault series and ability to translate it on the fly to good old SQF
without any hassle.

project status: not even close to version 1.0

### Contributing

I'm not looking for contributors at the moment as this is a side project
 of mine and the main objective is learning (by trial and error).


### Examples

#### Control Structures
https://community.bistudio.com/wiki/Control_Structures
##### IF - ELIF - ELSE

SQF
```
if (CONDITION) then {
    ...
} else {
    if (ANTOHER_CONDITION) {
        ...
    } else {
        ...
    }
}
```
BSQF
```
if (CONDITION) {
    ...
} elif (ANOTHER_CONDITION {
    ...
} else {
    ...
}
```

##### WHILE
SQF
```
while {CONDITION} then {
    ...
}
```
BSQF
```
while (CONDITION) {
    ...
}
```
##### FOR
SQF
```
for [{BEGIN}, {CONDITION}, {STEP}] do {
    ...
}

for "VARNAME" from STARTVALUE to ENDVALUE step STEP do {
    ...
}
```
BSQF
```
for (BEGIN; CONDITION; STEP) {
    ...
}
```
##### FOREACH
SQF
```
{ ... } forEach ARRAY;
```
BSQF
```
ARRAY.forEach({ ... });
ARRAY.forEach(FUNCTION);
forEach(ARRAY, { ... });
forEach(ARRAY, FUNCTION);
```

#### MISC

##### incrementing and decrementing
SQF
```
a = a + 1;
b = b - 2;
```
BSQF
```
a++;
b -= 2;
```

##### HINT

SQF
```
hint "stirng";
hint str 5;

```
BSQF
```
hint("string");
hint(5);
```

##### RANDOM

Note: Upper limit (max) is always exclusive

SQF
```
// random float between 0 and max
random max;

// random float between min and max
min + random (max - min);

// random float with Gaussian distribution
random [min, mid, max];

// random int between a and b
min + floor random (max - min);

// random int with gaussian distribution
floor random [min, mid, max];

```
BSQF
```
// random float between 0 and max
random(max);

// random float between min and max
random(min, max);

// random float with Gaussian distribution
random(min, max, mid);

// random int between min and max
randomInt(min, max);

// random int with gaussian distribution
randomInt(min, max, mid);

```

##### Indexing

SQF
```
ARRAY select INDEX;

```
BSQF
```
ARRAY[INDEX];
```

