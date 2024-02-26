Nama: Erista Disti Kirani 

Summary Version Control System (Git and Github) 

Versioning merupakan pengatur dari versi dari sources code program 

Tools: 

- Version Control System (VCS) 
- Sources Code Manager (SCM) 
- Revision Control System (RCS) 

Git salah satu version control system populer yang digunakan para developer untuk mengembangkan software secara bersama-sama. 

The Staging area 

working directoory →git add→staging area→git commit→repository 

Git status, add, commit 

→ $ git status 

$ git add <directory>

$ git add hello.py 

$ git add .

$ git commit -m “add config file” 

Git diff and stash 

\# git diff 

\# change file 

\# add staging area 

$ git diff  - -stage 

\# stashing your work 

$ git stash 

\# re-applying your stash changes 

$ git stash apply 

Git log, checkout 

\# viewing an old verson 

$ git log  - -online 

\# b7119f2 continue doing crazy things 

\# 872fa7e try something crazy 

\# a1e8fb5 make some important changes to hello. txt 

$ git checkout a1e8fb5 

Git reset 

- soft

  uncommit changes, changes are left staged (index). 

- hard 

  uncommit + unstage + delete changes, nothing left. 
  
  git 












