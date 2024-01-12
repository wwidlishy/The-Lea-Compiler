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
In Lea, we don't give a fuck about recursion limit (It is gone!)

Lea requires `nasm` and `ld` in the path to compile output, lea just generates assembly for linux

**Functional Patterns**

If you do not understand this syntax, check [Function Syntax](#functions)

```sh
## You can pass functions as arguments with & before function name
function_caller :: 1
does
    loc[0] = arg[0](15)
    echo(loc[0] >>> String)
end

add_five :: 1 = arg[0] + 5
function_caller(&add_five)
```

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

## Functions

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

Remember that you can reasign variables?  
You can do the same with functions

```sh
const var Number = 10

inc_n_times :: 1 = arg[0] + 1
echo(inc_n_times(Number) >>> String) ## 11

inc_n_times :: 1 = arg[0] + 2
echo(inc_n_times(Number) >>> String) ## 12
```

Every function when called creates three variables (It is not recommended to assign any value at that name outside of a function):
1) A list of local values: `loc`
2) A list of arguments:  `arg`
3) A returned value:  `result`  
(all of those will be deleted on function return)

**V) Loops & Checkpoints**

Loop's are a relic of the past, and a very bad practice overall.  
In Lea there are no loops, but you can achive the same output with checkpoints and recursion.

1) Method with a Function
    ```sh
    ## You can recurse forever, because this language is actually built right

    ## A function to print 1 to 5 forever
    myRecursiveFunction :: 1
    does
        arg[0] = arg[0] + 1
        if arg[0] > 5
        does
            arg[0] = 0
        end

        echo(arg[0] >>> String + "\n")
        var result = myRecursiveFunction(arg[0])
    end

    myRecursiveFunction(0)
    ```

2) Method with a Checkpoint
    ```sh
    ## Note: Code doesnt belong to a checkpoint
    ## A checkpoint is just a place in the code you can go to
    ## Checkpoints cannot be overwritten to prevent unexpected behaviour

    var number = 0

    ## The same behaviour as before
    ::Loop
        number = number + 1
        if number > 5
        does
            number = 0
        end
        
        echo(number >>> String)
        goto Loop

    ```

**VI) Error Catching**

Errors at runtime don't exit, they save the error code to a variable called `error`.  
It is not recomended to use it for storing data.

For example, conversion error detection
```sh
var string = "Can't be Number"
var number = string >>> Number

## Note: Else / Elsif must be in the same line as end of if / elsif

if error == "ConvertionError"
does
    echo(formats("Error: Unable to convert '%0' to Number, Invalid Number Literal", [string]))
    exit(0)
end else
    echo(number >>> String)
end
```
**Just to piss you off, But true**

This language was started just after the start of 2024 ... By a 14yo, without any help from AI  
Bet ya pissed mate, massive skill issue! (you can open an issue on it, idc)