import shutil
import os


def with_user_input():
    print('Input the names one by one. When finished type exit and press enter')
    isExit = True
    while isExit:
        input_name = input('Name: ')
        if input_name.lower() == 'exit':
            isExit = False
        else:
            names_high.append(input_name)


def with_txt_input():
    input('Input a list of names into names.txt - full name per line, and press enter when youre done')
    input_file = open('names.txt', 'r')
    for input_name in (raw.strip() for raw in input_file):
        names_high.append(input_name)


seiNumber = input('Enter sei number: ')
author = input('Who is the author: ')
url = input('Whats the URL to the github repo: ')
names_high = []
inputChoice = input('Would you like to input name by name [1] or import through a file [2]?')
if inputChoice == '1':
    with_user_input()
elif inputChoice == '2':
    with_txt_input()
else:
    print('Wrong input try again')

if inputChoice == '1' or inputChoice == '2':
    names = []
    for high_name in names_high:
        names.append(high_name.lower().replace(' ', '_'))

    print(names)
    shutil.rmtree(f'sei{seiNumber}', ignore_errors=True)

    path = f'sei{seiNumber}'

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        # Create a readme file
        with open(f"{path}/README.md", "w+") as f:
            f.writelines(
                f"""
# SEi{seiNumber} ([General Assembly, Sydney](https://generalassemb.ly/sydney))

### Homework Repository

1. Repository Setup;
2. Do Your Homework;
3. Submit Your Homework.

### Repository Setup

You only need to do this once, not every time you're submitting homework!

- **Fork this repository**
  - _'Forking' creates a personal, 'forked' copy of this repository on your Github account._
  - Hit the **Fork** button in the top right-hand corner of this page.
- **Clone your forked repository to your computer**
  - _'Cloning' takes your 'forked' repository on GitHub and creates a local copy - or 'clone' - on your computer._
  - Make sure you're browser is open to **your** forked version of this repository on Github (eg [http://github.com/{{YOUR_USERNAME}}/sei{seiNumber}](http://github.com/{{YOUR_USERNAME}}/sei{seiNumber})).
  - Hit the **Clone or Download** button in the top right-hand corner of the page and copy the URL to your clipboard.
  - Open your computer's terminal to the directory in which you intend to store your homework.
  - `git clone url_of_your_fork_on_github` (where `url_of_your_fork_on_github` is the URL you copied after hitting 'Clone or Download', above).
- **Add an upstream remote repository**
  - _Adding an upstream repository links the local repository on your computer to the original repository on Github (i.e. mine, the one from which you created the fork)_
  - `cd sei34-homework`
  - `git remote add upstream {url}`
  - `git pull upstream master`

### Do your Homework

You should put each night's homework in a new folder within the appropriate directory of your homework repo. So, for day two, where you have two tasks ("Calculator" and "Strings"), you might do something like this:

1. Open Terminal/iTerm2;
2. Go to your local homework repo (eg, `cd ~/sei/homework`);
3. From here, go to the folder matching your name within that repo, and the appropriate week (eg, `taylor_swift/week_01`);
4. Create new folders for each of the day's homework tasks: (eg `mkdir calculator` and `mkdir strings`);
5. Create the files necessary to complete the homework in their respective directories;
6. Get to it!

### Submit Your Homework

You need to do this every time you're submitting homework.

- **Commit your work to your local repository progressively**
  - Make sure you are the correct folder containing the homework you want to submit.
  - `git add .`
  - `git commit -m "YOUR_COMMIT_MESSAGE_GOES_HERE"`(where `YOUR_COMMIT_MESSAGE_GOES_HERE` is your description of the work you are committing)
- **Push your changes to your forked repository**
  - `git pull upstream master` - merge changes that have been made to this repository into your own local repository.
  - `git push origin master`
- **Once you're finished, submit a pull request for me to accept your homework**
  - Navigate to your forked version of this repository on Github (eg [https://github.com/{{YOUR_USERNAME_HERE}}/sei{seiNumber}](https://github.com/{{YOUR_USERNAME_HERE}}/sei{seiNumber})).
  - Hit the **Pull request** button.
  - Make sure the destination for the pull request is set to my repository, not your own or anyone else's.
  * **IMPORTANT:** In the pull request comment, tell me the following:
    1. How difficult did you find this (out of 10)? 0 being no problems at all, 10 being impossible;
    2. Was there anything that you struggled with?;
    3. Is there anything that you'd like some further information on?;
    4. Roughly how long did it take?

**If you don't mention anything in the Pull Request comments, we will assume you had no problems at all with it, and you will receive no feedback about your homework.**

If you want to follow up on any issues you had with the homework, the ideal time for that will be during the more unstructured lab time after lunch - come and see Joel or myself then and we can go over any outstanding questions.

**Note:** if I haven't yet merged your Pull Request into my master homework repo before it's time to submit the next day's homework, you won't be able to create a new Pull Request. That's okay - for the new homework just add a new comment to the open (existing) Pull Request, featuring the same four points given above to describe your response to it.
            """
            )

        with open(f"{path}/.gitignore", 'w+') as f:
            f.writelines(
                """
.directory

### OSX ###
*.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon

# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

# End of https://www.gitignore.io/api/osx


# Ignore bundler config.
/.bundle

# Ignore the default SQLite database.
/db/*.sqlite3
/db/*.sqlite3-journal

# Ignore all logfiles and tempfiles.
/log/*

# ignore Rails cache files
tmp/
log/

!/log/.keep
!/tmp/.keep

node_modules/
/yarn-error.log

.byebug_history
                """
            )

        with open(f"{path}/pull_request_template.md", 'w+') as f:
            f.writelines(
                """
- How difficult did you find this (out of 10)? 0 being no problems at all, 10 being impossible

- Was there anything that you struggled with?

- Is there any particular code you want me to look into?

- Is there anything that you'd like some further information on?

- Roughly how long did it take?
                """
            )
        for name in names:
            try:
                os.mkdir(f'sei{seiNumber}/{name}')
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                with open(f'sei{seiNumber}/{name}/README.md', 'w+') as f:
                    f.writelines(
                        f"""
# {name}
## Homework folder
                        """
                    )
                print(f'Created a folder for {name}')

    print('Done!')
