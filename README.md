# The-Lea-Compiler
Just an repo for my programming language im making in python

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

That's why we have a _stack_ to save variables state
```sh
A: Number = 13
echo $A

push A
A = 14
echo $A

pop A
echo $A
```