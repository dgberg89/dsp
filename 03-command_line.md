# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

###**Cheat Sheet of Commands**

+pwd - show working directory path
+mkdir - create a new directory
+rm -r - remove a directory and all associated child directories
+touch 'samplefile.txt' - creates a new file with name 'samplefile.txt' in the wqorking directory
+rm - delete/remove a file
+mv - move or rename a file (for move, type mv 'file' 'dir', to rename type mv 'file' 'new filename')
ls -a - list hidden files in the working directory
+cp - copy a fiule from one directory to another (syntax is cp 'file' 'directory to copy it to')
+cd - change directory (cd and then path to dir OR cd / for home directory OR cd .. to move back one directory)
+alias - allows you to create keyboard shortcuts for commands 

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

+ls - lists all files in the current  working directory
+ls -a - lists all files in the working directory INCLUDING hidden files
+ls -l - lists all files in the working directory in long version (added details for each file)
+ls -lh - lists files in long version with human readable format (for sizes)
+ls -lah - same as ls -lh, only hidden files also included
+ls -t - lists files in order of the last time they were modified
+ls -Glp - lists files in long formats without Group names and with a / at the end of each directory

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

+ls -C - lists files and directories in column format
+ls -R - lists all directories and subdirectories
+ls -1 - lists files and directories on a single line
+ls -S - lists files sorted by size
+ls -m - lists files with commas separating entries
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> From what I understand, 'xargs' is a command line command that helps run commands that are too long or have too many arguments.  It can execute commands that don't accept standard input (i.e echo or an argument piped in using |) with the arguments from standard input.
>> A good example I found online is 'ls | xargs cat'.  This line pipes the list command to xargs which then runs the following stdin command (cat) on all of the files in the list.  When I ran this in terminal, every line from every file from the dsp directory was printed to the Terminal.    

 

