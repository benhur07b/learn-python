---
title: "Version control"
description: "Use version control systems to streamline development and collaboration in Python projects."
---

Version control is a critical practice for managing changes to code, documents, or projects over time. It allows developers to track every modification, collaborate with others, and revert to previous versions if needed. It enable teams to work on the same project without overwriting each other’s changes, resolve conflicts, and maintain a clear history of development. By using version control, you can:  

- **Track changes** systematically, making it easy to understand who made what change and when.  
- **Branch and merge** code, enabling parallel development (e.g., experimenting with new features without disrupting the main project).  
- **Revert to earlier versions** if a bug is introduced or a feature fails.  
- **Collaborate seamlessly** with teammates, ensuring everyone works on a consistent, up-to-date codebase. 

## Common tools/systems
### Git 
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. 

Install  Git from https://git-scm.com/.

#### Basic terminologies
1. **Repostory** - A **repository** (or **repo**) is a storage location for all the files, code, and history of a project. It can be **local** (on your computer) or **remote** (on a server like GitHub or GitLab).

2. **Branch** - A **branch** is a separate line of development. It allows you to work on new features, fix bugs, or experiment without affecting the main code (e.g., the `main` or `master` branch). 

3. **Merge** - **Merging** is the process of combining changes from one branch into another. For example, you might merge a feature branch into the `main` branch to integrate new code.  

4. **Clone** - **Cloning** is creating a **copy** of a remote repository on your local machine. This allows you to work on the project locally and sync changes back to the remote server.  

5. **Fork** - A **fork** is a **copy** of a remote repository (e.g., on GitHub) that belongs to **your account**. It’s commonly used for contributing to open-source projects or making changes without affecting the original repository.  

6. **Commit** - A **commit** is a **snapshot** of changes made to the files in a repository. Each commit has a **message** that describes what was changed. Commits are atomic (they capture changes in one logical unit).  

7. **Push** - **Pushing** sends your **local changes** (commits) to a **remote repository** (e.g., GitHub). This is how you share your work with others or update a remote server.  

8. **Pull Request (PR)** - A **pull request** is a **proposal** to merge your changes (from a branch) into another branch (e.g., `main`). It allows collaborators to review your code, suggest changes, and approve the merge.  

#### Usage
After installing Git, you need to configure your username and email address. 
```sh
git config --global user.name "Your Name"
git config --global user.email "Your Email"
```

You can run the following command to check your configuration.
```sh
git config --global --list
```

To **create** a new Git repository (assuming you are already inside the project folder):
```sh
git init
```

To **add** files to the staging area:
```sh
git add .
```

To **commit** the changes:
```sh
git commit -m "Initial commit"
```

To **push** the changes to a remote repository (master branch):
```sh
git push origin master
```

To **pull** changes from a remote repository (current branch):
```sh
git pull
```

To clone a remote repository:
```sh
git clone <REPOSITORY_URL>
```

To **create a new branch**:
```sh
git checkout -b <NEW_BRANCH>
```

To switch to an existing branch:
```sh
git checkout <EXISTING_BRANCH>
```

### Git-based platforms/systems

1. GitHub
    - https://github.com
2. GitLab
    - https://gitlab.com
3. Codeberg
    - https://codeberg.org/
    - non-profit, community-led effort that provides Git hosting and other services 
4. Gitea
    - https://about.gitea.com/
    - self-hosted devops platform
5. Forgejo
    - https://forgejo.org/
    - self-hosted lightweight software forge forked from Gitea