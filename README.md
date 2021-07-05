# open-source-projects

## Contribution guidelines

### 0. Realization
This repository is divided into languages as folders. 
- **If the folder for your language doesn't exists create one.** Otherwise use the existing language folder and follow the next steps.
- Create a `new folder` with the name of the program inside the respective language folder(if it doesn't exist already).
- Inside that `new folder`, create another folder with the name `your-GitHub-username` add your program files/folders to this folder.
  - If the program already exists consider adding new changes only if you have an entirely different approach for that program. 
  - However, if you want to improve already existing code make an `Issue` for it.

> The above steps will make sure that the programs can be run by anyone without any modification to files or folders of that program.
```
/(root)
│
├── c++/
│	└── ...
├── java/
│	└── FizzBuzz/
│	│	└── tonyStark/
│	│		├── Dependences/
│	│		└── Main.java
│	└── ...
├ python/
│	└── ...
```
### 1. Fork this Repository

> You can fork this repository on GitHub by navigating at the top of this repository.

Github repository URL is composed of `https://github.com`/`owner_username`/`repository_name`

Eg. 
https://github.com/cstechnophiles/open-source-projects
when you fork a repository, everything inside it is copied to a new repository with you as the owner, and with a reference to the original repository. 
Eg. after forking you will have.
https://github.com/your-cool-username/open-source-projects

### 2. Clone the forked Repository

Cloning will create a local copy of the forked repository on your storage.
#### How to clone?
- We use the **`git clone repository_url`** command. 
Here the `repository_url` points to the fork of your repository. 
You can copy the `repository_url` by using the green `Clone` button from your forked repository page.

- Once you have the `repository_url`, you can clone the repository. The final command will cook like 
`git clone https://github.com/your-cool-username/open-source-projects.git`

This will create a new folder with a name same as `repository_name`
`open-source-projects` in your case. Change your directory to the local repository using `cd open-source-projects` so you can work inside it.
### 3. Create a New Branch

To create a new branch, in your terminal window, we use 
**`git branch new-branch-name`**

Make sure you use a descriptive name for branches so that others working on the project understand what this branch is for.
The new branch is created, switch to a new branch using the 
**`git checkout new-branch-name`**

After using this command in the terminal, it will say `Switched to branch 'new-branch-name'`
> You can use `git branch` without any arguments to get a list of all the local branches.

### 4. Open it inside your preferred editor
Use `code .`for VS Code, or `subl .` for Sublime text. You must have it installed and configured properly to use these commands. Alternatively, you can open this folder through your editor directly.

Once you enter this command, the whole code will automatically open in your editor.

Now, you can modify existing files or add new files to the project in your branch.

#### Make Changes Locally

Once you have modified existing files or added new files to the project. Add the changes to the staging area, using 
**`git add .`** or **`git add -A`**

To finalize and record the changes made to the repository, use 
**`git commit`** or **`git commit -m "commit message"`** as a shorthand.

Make sure to type a meaningful commit message.
_The commit message is very important as it explains what the change is about. Commit messages are also used to look back into the record of the changes made to the project, and who made them._

### 5. Push changes to your forked repository
To push these changes to your forked repository use
**`git push origin new-branch-name`**

### 6. Making a Pull Request or PR
When you push changes from your local repository to the forked repository, open the forked repository in a browser, it will suggest making a pull request. Alternatively, open the pull requests tab to create a new pull request.
> A pull request is made from your fork so your changes can be pulled from the original repository.
> 
That's it now the changes will be checked and merged into the original repository if there is no conflict and is approved by bots. Be patient!

> If you're experienced with git you can do most of the above steps through the terminal itself. By adding remotes and pushing changes to those remotes.
