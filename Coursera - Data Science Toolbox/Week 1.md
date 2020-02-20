# Week 1

## Welcome to the Data Scientist Tool Box

**Amazon Polly** an online voice synthesizer by Amazon web service can be used to generate real time voice application by providing Rmd or Md files.

In this course it is used to keep the content updated since recording again for course is time consuming. In this they have used AWS poly to generate voice from Rmd files will displaying the slides, Both of which is easily updateable.

 ## What is Data Science

Data Science - Using Data to answer questions

Data Scientist is someone “who combines the skills of software programmer, statistician and storyteller slash artist to extract the nuggets of gold hidden under mountains of data” - Economist



Big Data - Volume, Velocity, Variety

- About 300 hours of video content is being uploaded in YouTube every minute and the numbers is growing exponentially.
- Due to cheaper computing and storage capacity.

Famous Data Scientists 

1. Nate Silver - American statistician and editor in chief of [fivethirtyeight.com](https://fivethirtyeight.com) 

2. Daryl Morey  - GM of basketball
3. Hilary Mason - Co-founder of FastForward Labs

## What is Data

" A set of Values of qualitative and quantitative variables"

Set - In statistics, the population you are trying to discover something about

Variable - Measurement or Characteristic of an item

Qualitative variable - Measurement or characteristic about qualities

Quantitative variable - Measurements or information about quantities or numerical items 

## Getting Help

As a data scientist we are measured on the ability to solve problems. To solve them we need to know to get help

 [Roger Peng’s video](https://youtu.be/ZFaWxxzouCY)  on how to get help.

Rubber Dug Debugging - Many programmers have had the experience of explaining a programming problem to someone else, possibly even to someone who knows nothing about programming, and then hitting upon the solution in the process of explaining the problem. In describing what the code is supposed to do and observing what it actually does, any incongruity between these two becomes apparent. 

## The Data Science Process

The parts of data science project:

- Forming the question
- Finding or generating data
- Explore the data
- Model the data
- Derive insights
- Communicate to others

Example:  

1. Data scientist named [Hilary Parker](https://hilaryparker.com/about-hilary-parker/). Her work can be found [on her blog](https://hilaryparker.com/), and the specific project we’ll be working through here is from 2013 and titled [“Hilary: the most poisoned baby name in US history”](https://hilaryparker.com/2013/01/30/hilary-the-most-poisoned-baby-name-in-us-history/). 
2. Prediction Risk of Opioid Overdoses in Providence, RI - [Interactive Shiny App](https://jordanbutz.shinyapps.io/directory/)

# Week 2

## Installing R:

R is a software mainly focused on statistics and graphing. R is open source. Can be extended to make websites (blogdown), maps, analyzing videos etc

CRAN - Comprehensive R Archive Network.

## Installing R-studio:

 R-studio allows you to write, edit and store code, generate, view and store plots, manage files, objects and dataframes, and integrate with version control systems.

## R-studio tour

1. Main menu
2. Source
3. Console
4. Environment
5. Files, plots, packages and help

## R - Packages

Package -  Collection of functions, data, and code conveniently provided in a nice, complete format.

Library - Place where the packages are located in our system. package is like a book inside a library

3 Main ways to locate package:

- [CRAN](https://cran.r-project.org)
- GitHub
- [Bioconductor ](https://www.bioconductor.org)

There are more than 18000 packages to solve various problems finding them can be tedious. so CRAN has segmented the available packages into 35 different categories under [CRAN task view](https://cran.r-project.org/web/views/). Other good source to find the packages is at [R documentation](https://www.rdocumentation.org) which gives us great way to search all these available packages and select the one that is suitable for us.

### Installing Packages through R-studio

Run `install.packages('ggplot2')` here `ggplot2` is used as an example, replace it with the package of your choice.

For installing multiple packages at once use `install.packages(c('ggplot2','devtools'))` `c` is used to pass in packages as a vector which r will install simultaneously.

Easier approach would be to use R-studio `tools` menu to `install packages`. which by default points to CRAN as source.

### Installing Packages through Bioconductor

To install Bioconductor packages directly from R-studio we have an intermediate package in CRAN which must be installed, `BiocManager` which allows us to download packages from Bioconductor

After installing `BiocManager` run the following command `BiocManager::install()` with the package name to install packages from Bioconductor. 

<u>Note:</u> Applicable for R version greater than `3.5`

### Installing Packages from GitHub

Similar to Bioconductor to install packages directly from GitHub we need a intermediate package from `CRAN` to be downloaded `devtools`. 

After installing the `devtools` package load it by running `library(devtools)` command.

Now that the `devtools` is installed and loaded run `install_GitHub('author/package')`  where we need to replace the author/package with the corresponding details.

### Loading Packages

We have installed a package doesn't mean that the package is running, to start the package run `library()` command and pass in the package name without any quotes.

To load a package in R-studio packages tab in the bottom right and click on the checkbox near it to load the package.

###  Managing Packages

To list all the installed packages run `installed.packages()` or `library()` without anything in-between the parenthesis.

To check the packages which has got update since our install run `old.packages()`

To update all the packages run `update.packages()`

To remove package run `remove.packages()` by passing in the package that you want to remove.

All the above said functions can be done with the help of `packages` tab in the bottom right of R-studio.

Check the version of R that we are running with `version` command. more info can be found by running `sessionInfo()` command.

To get help about the function available inside a package click on the package name from the `packages` tab. this will launch the manual or help for that packages. 

In order to get additional help run `browseVignettes('ggplot2')` which launches a localhost in with relevant details of that package

## Projects in R

Built-in functionality of R-studio which helps in organizing the work environment and keep multiple projects separate from one another.

`File` `->` `New Project` will create a new project with the name and location of the project which is specified. R-studio creates a file inside the specified location with `.Rproj` extension and changes the working directory to the given location.

### Benefits of Rproj

1. Organizing
2. Easier to share all the generated files.
3. Association with version control
4. Project remembers the documents which where open when the session was closed.

# Week 3

## Version Control (VC)

**What is version control?** Its a system that records changes that are made to a file or a system of file over time. VC takes a snapshot of the project and save those snapshots in order to let user revert back to the older version of the file if needed.

Keeps record of all changes made to the file since its creation which is helpful incase of collaborating with many people.

**Types of Version Control System?** 

- Distributed Version Control system (DVC) - All users have their own local copy of the project which is then pushed to the source of truth - Git
- Centralized Version Control system (CVC) - All files are kept at the source of truth and file is locked out when a person is accessing it. - Subversion

[Reference](https://confluence.atlassian.com/get-started-with-bitbucket/types-of-version-control-856845192.html)

### Git and GitHub

**Git** is a software used to keep track of all the changes made to file or a system of file

**GitHub** is an online service where all the project files which are tracked can be hosted online for access from multiple places. Similar to Dropbox for tracked files

### Vocabulary of Git

**Repository** aka **Repo** similar to the project folder which consist of Local Files. A Repo can be hosted on GitHub and can be made public or given access to particular logins

**Commit** is to take a screenshot of the repo at the current stage. `git commit -m "sample msg"`

**Push** is to update the remote repo with the changes made in the local repo. `git push`

**Pull** is to update the local repo with the changes made in the remote repo. `git pull`

**Staging** is act of preparing the files in the working directory to commit. `git add`

**Branch** is like a parallel universe where changes are not reflected to the main repository but is handled separately. This changes can then be **merged** back into the main branch. In case of **conflict** between the files git asks the user to select which one of the edit to proceed with preventing data loss

**Clone** is the process of creating a local copy of the project.

**Fork** is a personal copy of the repository. A open source project can be forked and changes can be made. eg: fork of Linux can be taught as fedora, ubuntu etc.

###  Best Practice

- Address single issue in a commit
- Always write a useful commit message
- Check whether you are up to date with the remote repo

## GitHub and Git

Signup to free [GitHub](https://GitHub.com/join) account.

[Intro to GitHub](https://youtu.be/w3jLJU7DT5E) by GitHub

[Overview of GitHub](https://d3c33hcgiwev3.cloudfront.net/hK4GbBszEem5_xLqNrIdUA.processed/full/720p/index.webm?Expires=1575763200&Signature=hNYRxlXenFIIVob7zXqFLd2mQPMAqMNfnYgfTQ0TXvQvFmxNZikV-jSa3xsNZ2cNUcqbaTk5Z0JEypZyVSwXi~9CreyiEtZMGI5r9~IQHyMejPZ003joY90Q9gLk8eQiHF9aZcvIsLOg-01yz10~62fKM4XuJSgiGWo1eEshK-I_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) from course

## Linking GitHub and R-studio

1. ` Tools > Global Options > Git/SVN ` in R-studio

2. Check whether the executable is in the correct location

3. Create `RSA key ` and `view public key` and `Ctrl+C` to copy it

4. Navigate to GitHub `Settings -> SSH and GPG Keys` 

5. Create an instance with SSH key and paste the copied key

6. Confirm with the GitHub password

   We are all set to use git inside R-studio.

7. Create a new repo in GitHub and copy the clone link

8. Now create a project with `version control` and paste in the Repo URL 

9. Now any changes made to the project folder can be staged, committed and pushed to the remote repo setup at GitHub

## Projects with Version Control

The last section went over the details of creating a new project and linking it to GitHub. Suppose we already have a project locally that we are trying to upload it to our GitHub we should follow the following procedure.

1. Navigate to the project folder right click and open `git bash here`

2. Initialize git in the current folder by running `git init`

3. Add the files of the project to staging area by `git add .`

4. Once the files has been added to the staging area commit to the local repo using `git commit -m "commit msg"`

5. Now we have to setup a remote repo, for this create a new repo in GitHub and copy the URL like before

6. Navigate back to the `git bash` and run the following command `git remote add origin (COPIED URL HERE)` &  `git push -u origin master`

7. We have our link to remote repo ready we can now stage, commit and push to the remote repo from R-studio like before.

# Week 4

## R Markdown




## Resources

1. [R packages](http://r-pkgs.had.co.nz/) by Hadley Wickham
2. [Advanced R](https://adv-r.hadley.nz/) by Hadley Wickham
3. [R for Data Science](https://r4ds.had.co.nz/)  by Hadley Wickham
4.  [R Markdown cheatsheet](http://www.rstudio.com/wp-content/uploads/2016/03/rmarkdown-cheatsheet-2.0.pdf)
5. 



