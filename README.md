# The-Lea-Compiler
Just an repo for my programming language im making in python  
(This is not a finished product and readme)  
(May include concepts that are not finished yet!)  

**I) Language's Concept**

Lea has a [Bash](https://github.com/topics/bash) like strongly typed syntax.  
However lacks the *_wierd_* bash syntax, and other unintuitive features.  
Don't worry, we've got our own syntax bullshit. 😊    
When I used other languages, I was quite annoyed that you can't recurse forever.  
So, I decided to fix that.  
In Lea, we don't give a fuck about recursion limit (It is gone!, At the expense of binary size).

Lea requires `nasm` and `gcc` in the path to work properly

**II) Variables**

Have you ever had problems with scope variable shit, well we fixed that.  
All variables are global, even Arguments!  

Here's how you can define and use a variable
```sh
## [Name]: [Flags split by space, Type flag is required] = [Value of the type]
var A = "Hello, World! I Like "
echo(A + "\n")  ## Hello, World! I Like

A = A + "Lea!"
echo(A + "\n")  ## Hello, World! I Like Lea!

## When you reasign a variable, the original deletes itself
const var A = 10

## note first are the modifiers and then the var keyword
## else it is an error

var const A = 10 ## Error

## there are also encrypted variables
## they are slower but more safe

enc var A = 24 ## will be evaluated as 24, percieved as 24, but stored as 24 encrypted by a random variable specific 8-bit Integer
```

**III) Number Notations**

There are:
* Decimal Integers
* Decimal Floats
* Hexadecimal Integer (converted to decimal integer at compile time)
* Binary Integer (converted to decimal integer at compile time)

```sh
10 ## 10

10.2 ## 10.2

0x1a ## 26

0b101 ## 5
```

**IV) Functions**

Btw, you can emulate a new line by a `;`  
You can define a function and use it like so
[Name] :: [Argcount]; [codeblock / = [return value]]
```sh
fun1 :: 2
does
    var result = arg[0] + arg[1]
end

fun2 :: 2 = arg[0] - arg[1]

echo(fun1(3, 2))
echo(fun2(5, 2))
```