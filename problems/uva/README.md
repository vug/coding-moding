Visual Studio Code cannot do redirection of standard input from a file using the integrated terminal/debugger.
Instead just run the following command in command-line (Cmder)

```
python main.py < input.txt | diff output.txt -
```

# References

* [How is the input function supposed to work? \(Visual studio code\) : learnpython](https://www.reddit.com/r/learnpython/comments/7vfj5h/how_is_the_input_function_supposed_to_work_visual/)
* [redirect input from file · Issue \#20890 · microsoft/vscode](https://github.com/Microsoft/vscode/issues/20890)
* [command line \- Can't pipe into diff? \- Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/922/cant-pipe-into-diff)