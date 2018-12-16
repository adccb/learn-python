# learn-python

this is a repo that's more or less just a failing test suite to help you learn python. here's how to get the code and run it.

## prerequisites

- `python3`: download python 3.7 from [here](https://www.python.org/downloads/).
- `git`: this project is hosted on github, so you'll need to follow [these instructions](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-mac-md) to be able to use git.

## how to install

in a terminal, pick a directory you're comfortable keeping this repository in. you can see where you are with the `pwd` command. you can see all the files (and subdirectories, etc) in your current directory by typing `ls`. change between directories like `cd path/to/new/directory`. make new directories with `mkdir new_directory_name`.

once you've found somewhere you're comfortable keeping this repo, run the following command:

```bash
git clone https://github.com/mxtetrachord/learn-python # clone the directory locally
cd learn-python # move into the new directory
```

## using the test suite

from there, you should see two subdirectories, `src/` and `test/`. source files go in `src/`, and test files in `test/`. you'll only need to modify the files in `src/`; stuff in `test/` is just to verify your work. to make changes, you'll need a standalone text editor; for this i recommend [sublime text](https://www.sublimetext.com/).

when you have a solution you want to test, from a terminal run the following command:
```bash
./run_tests
```

and you'll see output in that terminal regarding your test suite.

that's all you need to know—get cracking!
