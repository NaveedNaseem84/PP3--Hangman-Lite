# Hangman Lite in Python.

## Introduction
Hangman Lite is an interactive python-based game aimed to provide users of all ages with a seamless experience whilst playing hangman - extended to include a difficulty option.

The intended purpose is to provide a clean take on the all-time class game, providing responsive feedback with the options to view the rules and quit on demand. Potential uses for the game can be for individuals (children and adults!) who want to improve their spelling and vocabulary, their strategical thinking or simply just have fun to name a few. 
## Table of Contents

### [User Experience (UX)](#user-experience-ux-1)

* User Stories

* Mind Map: Ideas

* Wireframe Designs 

* UX View

* Pseudo - functions needed (Brainstorm)

* Process Map

### [Main Page](#main-page-1)

* Features

### [Testing](#testing-1)

* Fixed Bugs 

* Validation Testing

* Manual Testing

* API Testing

### [Future Developments](#future-developments-1)

###  [Workload Planning](#workload-planning-1)

###   [Site Production, Deployment and Contribution](#site-production-deployment-and-contribution-1) 

 * Site production

 * Deployment

 * Contribution

### [Technologies and tools Used](#technologies-and-tools-used-1)

* Languages used

* Frameworks, Libraries and Programs Used
     	
### [Credits](#credits-1)

* Content

 * General
  
 * Overall Credit

### [Personal Summary ](#personal-summary-1)

#
 

## User Experience (UX)
### User Stories
The following user stories have been created identifying the needs and requirements for the game. These have further provided the foundation for the project which I have kept in mind during all aspects of development and deployment.

As a user, I want:
* To be able to work on my spelling in a fun, interactive way.
* To be able to play using a variety of words.
* To have the option to make it challenging.
* To have clear, accessible instructions that are easy to understand.
* To see feedback on the choice made (correct/incorrect) in a clear way.
* A tally to see how many games have been won or lost.
* The choice to continue, restart or quit playing when a game has completed.

### Mind Map: Ideas

Following on from user stories and intended purpose, an initial mind map was created to capture the logic of the game. The purpose of this was provide a high-level understanding of how the user stories could be implemented:

![Mindmap](readme-images/initial-mind-map.png)

### Wireframe Designs
Following on from the mind map, a wireframe was created (shown below) with focus given on the user stories. This wireframe illustrates potential outputs based on the input received and types of validation to be included.

![Wireframe](readme-images/wireframe.png)

### UX View

Following on from the wireframe design, a final UX view of the game was designed. As the game is purely command line, the views illustrate the outputs dependant on state of the game:

![UX views](readme-images/UX-visualisation.png)

Having finalised the UX element completed provided a clear picture of the finished product. It has also provided me with a clear reference guide for the wording format and spacing to be used to ensure a positive user experience. 

### Pseudo - functions needed (Brainstorm)
Once the UX element had been completed, I mapped out the python functions needed for the game to perform as needed:

![ Pseudocode - python functions](readme-images/pseudo-functions.png)

### Process Map
The diagram below maps out the processes and the path taken evaluating the state of the game on the inputs made:

![process map](readme-images/process-map.png)

[Back to Contents.](#table-of-contents)

## Main page

### Features

The main page presents the player (user) with a python console in which the game is ran. The player is welcomed and invited to select a difficulty level:

![welcome - select difficulty](readme-images/welcome-screen.png)

**Please note:** For the purposes of this project, the following values have used to determine the difficulty:

1 = easy (12 attempts)

2 = medium (8 attempts)

3 = hard (4 attempts)

If an invalid input is received, the player is notified of this and prompted to try again:

![Invalid input](readme-images/invalid-input.png)

Once a valid input has been received, the game begins. The player is presented with a randomly selected word, a letter count, and a hint to guess the word. In addition to this, the player is also made aware of the number of attempts available to guess the word:

![new game](readme-images/new-game.png)

The player also has the option to view rules on demand at any point of the game by typing "help":

![help](readme-images/help.png)

There is also the option to quit which terminates the game:

![quit](readme-images/quit.png)

**Please note:** on quitting, the "Run Program" button would need to be clicked to restart the game again.

If the input matches a letter within the word, the player is notified, and the word is updated to show all instances of this matched letter:

![input-matched](readme-images/input-matched.png)

Should the input not match a letter within the word, an attempt is used up. The incorrect inputs are recorded and displayed back to the player in a convenient way along with the updated attempts left:

![input-not-matched](readme-images/not-matched.png)

Once a word has been completely guessed, the player is congratulated on their win along with a summary of the game:

![won](readme-images/won.png)

If the attempts are all used up, the game is deemed over. The player is commiserated and again a summary of the game given:

![loss](readme-images/lost.png)

Irrespective of a winning or losing, the player has the option to carry on playing, resetting, or quitting.

The option to carry on playing will load a new game with a running total of the games won or lost incremented respectively:

![play again](readme-images/play-again.png)

The option to reset will restart the game and the running totals for games won or lost reset. The player is advised of the reset and presented the initial difficulty menu:

![game reset](readme-images/reset.png)

The option to quit will terminate the program as documented above.

These inputs are also validated, the player is notified if there is an input error:

![Invalid input on game complete](readme-images/game-complete-invalid.png)

[Back to Contents.](#table-of-contents)

## Testing

### Fixed Bugs 
* **Issue 1 (ID 7ae0beb):** The player was able to input upper- and lower-case letters. This in turn meant that an upper-case letter was different from a lower-case letter therefore being classed as an incorrect guess. For example, 'T' would not be the same as 't'.

    * **Fix (ID 23b2c0f):** This was fixed by formatting the input received and the random word selected using the .lower() built in function. Once implemented, a re-test found no further issues. 

* **Issue 2 (ID 5bf8a81):** The totals for the games won or lost were not incrementing when the continue playing option was selected.

    * **Fix (ID 276bc43):** This was fixed by globalising the variables won and lost. Once implemented, a re-test found no further issues. 

### Validation Testing

The code has been tested with the following:

* Python
   * No errors returned when running the code on the [Code Institute Python Linter.](https://pep8ci.herokuapp.com/)
   
   * The following results were returned:

      ![Linter results](readme-images/linter-results.png)

### Manual Testing

The following manual testing was carried out to confirm if the game performed as required and results matched the expected output.

| Test  | Test Step/Action                    |Input Type         |Expected                      |Result                                                        | Result|
| :----:|:------------------------------------|:-----------------:|:-----------------------------------------------------------------------|:-------------------------------------------------|:--------:| 
| 1     |Enter invalid difficulty             |e.g 4/a/?          |Error, asked to try again                                               |Invalid input identified. Try again               |Pass      | 
| 2     |Enter valid difficulty               |1, 2, 3            |Start game                                                              |Game started                                      |Pass      |
| 3     |Enter number                         |int                |Validate and inform incorrect input                                     |Input validated correctly - asked to try again    |Pass      |
| 4     |Enter space                          |space              |validate and inform incorrect input                                     |Input validated correctly - asked to try again    |Pass      |
| 5     |More than one letter                 |string             |validate and inform incorrect input                                     |Input validated correctly - asked to try again    |Pass      |
| 6     |letter found                         |string             |update letter(s) in word                                                |Word updated                                      |Pass      |
| 7     |letter not in word                   |string             |reduce attempt, record letter used                                      |attempt reduced, letter recorded                  |Pass      |
| 8     |word guessed                         |string             |increment won score, summary of game, option to play again, reset, quit |Input validated correctly - options expected given|Pass      |
| 9     |word not guessed/attempts finished   |string             |increment lost score, summary of game, option to play again, reset, quit|Input validated correctly - options expected given|Pass      |
| 10    |play again                           |string: "y"        |load new game, running totals for won/lost                              |new game loaded, totals kept                      |Pass      |
| 11    |reset game                           |string: "r"        |load new game, reset won/lost totals                                    |new game loaded, totals reset                     |Pass      |
| 12    |quit game (at end or during)         |string: "q"/ "quit"|terminate the game                                                      |game terminated                                   |Pass      |
| 13    |enter "help"                         |string: "help"     |show the rules on demand                                                |rules shown whenever typed                        |Pass      |

### API Testing

The API has been evaluated to ensure that the game works correctly when there is data in the google sheet in the format `word: hint` as shown below:

![Google sheets format](readme-images/google-sheets-format.png)

Should there be no data present, the game will successfully pick this up and exit:

![Google sheets error](readme-images/google-sheets-error.png)

[Back to Contents.](#table-of-contents)

## Future Developments

There are three potential future developments for this project.

1. Expand the difficulty level - generate the complexity of the word/clue based on the difficulty selected.
2. A scores table showing the top wins with the least attempts used.
3. Retrieval of the words: should the API fail for any reason, add in the option to read them in locally from a text file which would prevent any negative user experience.

## Workload Planning

To break the project down, a live task board was utilised. Having this in place from the beginning has ensured that all the requirements from a development view have been captured. It has allowed me to successfully transition a task from "to do" right the way through to "done" whilst being able to keep track of any issues that presented a blocker and tackle them accordingly. A final view of the board can be seen below:

![Live workload board](readme-images/Hangman-Lite-workload.png)

[Back to Contents.](#table-of-contents)

## Site Production, Deployment and Contribution  

### Site production

The site was created using Gitpod’s VS Code workspace environment with all the relevant files and folder structures created within. To deploy to GitHub, the following commands were carried out in the command line terminal to commit and push the changes to the GitHub repository: 

1 `git add .`- (Staging the changes in the current working tree ready to be committed).

2 `git commit -m 'Meaningful commit message"` - (The working tree is prepared with an upload message).

3 `git push` - (changes are pushed out up to the GitHub repository).

### Deployment

The site was deployed using Heroku. The steps to deploy are as follows:

1. login to Heroku.
2. Select "create new app" .
3. Create app .
4. Select "Settings" tab at the top.
5. Scroll down to "Buildpacks" and **add in the following order:**
    * `heroku/python`
    * `heroku/nodejs`
6. Scroll down to "Config Vars" and add the following:
    * `Key: PORT`
    * `value: 8000`

**Note:** If you have credentials, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

7. Go to the "Deploy" tab at the top.
8. Select "GitHub" as the Deployment method.
9. Select "Connect to GitHub."
10. Search for your GitHub repository and click connect. Once connected, it will show as follows:

![Heroku/GitHub connection](readme-images/heroku-github.png)

11. Scroll down to "Manual deploy" and click "Deploy branch". The app will start to build installing the various packages listed and the dependencies from the `requirements.txt` file. Once complete, click on the "view" button which will take you to the live site:

![Successful deployment](readme-images/sucessful-deployment.png)

There is also the option to "Enable Automatic Deploys" which will build the app as soon as it is pushed to the GitHub repository and can be used if preferred.

The live link to the site can be found here: [Hangman Lite.](https://hangman-lite-2cf8212eb558.herokuapp.com/)


### Contribution

I welcome any contributions/recommendations/changes to the project. To do this, the GitHub repository would need to be forked from GitHub and downloaded locally so it can be worked on. 

GitHub has provided step by step instructions on how to do this [here.](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project#forking-a-repository)

[Back to Contents.](#table-of-contents)

## Technologies and tools Used
### Languages used
 * Python   
### Frameworks, Libraries and Programs Used

* #### The following libraries were used:
    * Import random
    * Import sys
    * Import gspread
     from google.oauth2.service_account import Credentials

* #### The following requirements were defined in the requirements.txt file for API connection to google sheets (also needed for deployment):

     `cachetools==5.5.0`

     `google-auth==2.35.0`

     `google-auth-oauthlib==1.2.1`

     `gspread==6.1.4`

     `oauthlib==3.2.2`

     `pyasn1==0.6.1`

     `pyasn1_modules==0.4.1`

     `requests-oauthlib==2.0.0`

     `rsa==4.9`

* #### **Google sheets**: 

    * Google sheets has been used to store the words used in the game and have been imported in using an API. 

* #### **Git/Gitpod**:

  * Gitpod’s workspace was used using the VSCode online editor using git to push to GitHub using version control. 

* #### **GitHub**:

  * GitHub has been used to store the version control repository for the project.

* #### **Heroku**:

  * Heroku has been used to build and deploy the project.

* #### **Figma:** [Figma: The Collaborative Interface Design Tool](https://figma.com/)

  * Figma has been used to create the process map and the UX illustrations of the site.


[Back to Contents.](#table-of-contents)    
## Credits
### Content
* The words used for the game were sourced from [The Game Gal.](https://www.thegamegal.com/wp-content/uploads/2011/11/Pictionary-Words-Medium.pdf) The hints were added in manually.

*   The implementation of the google Sheets API was done by following the [Love Sandwiches - Essentials CI Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/) and adapted to the naming convention of my project.

    * The code used from the project above (at global level):

      ```
          import gspread
          from google.oauth2.service_account import Credentials

          CREDS = Credentials.from_service_account_file('creds.json')
          SCOPED_CREDS = CREDS.with_scopes(SCOPE)
          GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
          SHEET = GSPREAD_CLIENT.open('hagman_lite_words')
          get_words = SHEET.worksheet('words')
      ```
    * The code used in the ```choose_random_word``` function:

      ``` 
        words = get_words.get_all_values()
      ```
   
    
* The implementation of the python exit function was done by following the tutorial [Python Exit – How to Use an Exit Function in Python to Stop a Program by Shittu Olumide ](https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/)

    * The code used from the tutorial:
    ```
    import sys
    ...
    sys.exit(0)
    ```
    * This code has been used in the ```quit_game``` function.
* The reading in the rules from a text file was utilised from Code Institute's [Python Essentials: Python I/O Exception Handling > Reading Data from a File.](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/e38bbf480aec434f9f00f0bf6285e35c/b2704e108fc94223bd931f672cf929d4/) 

  * The code utilised (and adapted into my project) was:
    
    ```
      file = open("instructions.txt", 'r')
        instructions = file.read()
        print(instructions)
        file.close()
    ```
  * This code has been used in the  ```display_instructions``` function.

**Please note**: Referencing comments have been placed in the respected code locations for the code used above.
### General
* The following resources have been used as a general guide for python and it's built in functions:

  * [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) 
  * [W3Schools](https://www.w3schools.com/python/default.asp) 
  * [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
  * [Learnpython.org](https://www.learnpython.org/)
  * [The Python Tutorial - Python Docs](https://docs.python.org/3/tutorial/index.html)
  
[Back to Contents.](#table-of-contents)
## Overall Credit

A huge thank you to Code Institute for the learning and lesson material which has been amazing and my fellow students on Slack for their support! 
## Personal Summary

As this project was my first full exposure to indept python, it has brought with it a decent learning curve. The detailed content, and the invaluable advice and guidance from an amazing mentor has allowed me to further develop and refine on my coding journey.

I have endeavoured to implement any guidance given on my previous projects with the view of incorporating this as part of my standard coding practice.

The main take away point from this project has been around the value of breaking the requirements down into smaller manageable tasks on a "to do" list. Having this in place from the beginning has enabled me to build up the project step by step without having to think of what do next. 

This has been taken on board with a view to maintaining this on future projects.

