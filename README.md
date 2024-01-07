# The-Lea-Compiler
Just an repo for my programming language im making in python  
(This is not a finished product and readme)  

**I) Language's Concept**

Lea has a [Bash](https://github.com/topics/bash) like strongly typed syntax.  
However lacks the *_wierd_* bash syntax, and other unintuitive features.  
Don't worry, we've got our own syntax bullshit. 😊    
When I used other languages, I was quite annoyed that you can't recurse forever.  
So, I decided to fix that.  
In Lea, we don't give a fuck about recursion limit (It is gone!, At the expense of binary size).

**II) Variables**

Have you ever had problems with scope variable shit, well we fixed that.  
All variables are global, even Arguments!  

Here's how you can define, and free a variable!
```sh
## [Name]: [Flags split by space, Type flag is required] = [Value of the type]
A: String = "Hello, World! I Like "
echo $A + "\n" ## Hello, World! I Like

A = $A + "Lea!"
echo $A + "\n" ## Hello, World! I Like Lea!

free A
```

That's why we have a _stack_ to save variables state
```sh
A: Number = 13
echo $A ## 13

push A
A = 14
echo $A ## 14

pop A
echo $A ## 13
```

**III) Number Types**

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