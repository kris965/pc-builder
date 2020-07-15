## Table of Contents
1. [UX](#ux)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)

3. [Technologies Used](#technologies-used)

4. [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Validators](#validators)
    - [Compatibility and Responsiveness](#compatibility-and-responsiveness)

5. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)

6. [Credits](#credits)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

---
# PCBuilder

PCbuilder is a app where users can create their own PC builds by selecting components to share their ideas with the world,
And view all the builds created by others. Users are also able to edit and delete a build.

## UX
My goal in UX was to built a website which is minimalistic in design, 
So it is easy to use and easy to navigate through. 


### User Stories
**As a user:**
- I want to view the created builds
- I want to create my own build
- I want to be able to edit a build
- I want to be able to delete a build
- I want to be able to search for a build by a specific part
- I want all of the above to be achievable on mobile devices


#### Framework
- [Materialize](https://materializecss.com/), chosen for this project for its modern UI and easy to use of use. I used it for creating the navigation bar, cards, button, colors and made use of the grid system  
- [JQuery](https://jquery.com/) Was used for initializing Materialize elements


### Wireframes
- [Balsamiq Wireframes](https://balsamiq.com/) Was used to create the wireframes of this project
The wireframes for this project can be found in the wireframes directory.

---

## Features
### Existing Features
#### Navbar   

- The navbar is fixed at the top of the page, this allows a user to navigate throughout the website without having to scroll all the way up. The PCBuilder logo redirects the user to the home page.
On the smaller screens the navbar gets collapsed and a burger icon is visable. A menu will slide out from the left containing the menu items. 

#### Add a Build   
- By clicking on Add a build users are taking to a form where they can select their desired components. Where they can then click on add build to add it to the database

#### View all builds
- On this page users can view all the builds that have been created. The builds are displayed using cards with the build name given by the users. Users can click on the collapsible icon to view the parts that the build consists off.

#### Edit Build
- When users click on edit build they are taken to a form page which has the same layout as add a build, but the fields are pre-populated based on the build selected for editing. The user can then select what they want to be edited and save their changes

#### Delete Build
- Allows the user to delete a certain build from the database

#### Search Build
- User can use the dropdown menu in the navigation bar to select a component to search on. When selecting a component the user is taken to a search page where they then can select a part they want to search on. the user is then taken to a page which has the same layout as 'View all builds' displaying the builds that contain that part that the user has searched on.
---
### Feature ideas:
There are some features that I want to implement, but due to time wasn't able to do so. I might want to add these in the future:

#### Login function
- Login functionality so users can view their own builds they have added. 

#### Rating system
- Rating system so users can vote for a build and based on that create a page where builds are being displayed in rating order.

#### Favorite system
- Option for the user to select a build as favorite and save it to be viewed for later. 

---
## Technologies Used

- [GitPod](https://www.gitpod.io/) - IDE for developing this project.
- [Git](https://git-scm.com/) - used for version control.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - to build the foundation of the project.
- [CSS](https://developer.mozilla.org/en-US/docs/Archive/CSS3) - to create custom styles.
- [Jinja 2.10.1](https://jinja.palletsprojects.com/en/2.10.x/) - templating language for Python, to display back-end data in HTML.
- [Python 3.8.2](https://www.python.org/) -  back-end programming language used in this project.
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/) - microframework for building and rendering pages.
- [MongoDB Atlas](https://www.mongodb.com/) - NoSQL database for storing back-end data.
- [PyMongo](https://api.mongodb.com/python/current/) - For interaction between Python and MongoDB.
- [Materialize 1.0.0](https://materializecss.com/) - Framework used for the front-end design. 
- [JQuery 3.5.0](https://jquery.com/) - to simplify DOM manipulation andfor the initialisation of certain materialize components. 
- [Heroku](https://heroku.com/) - for the hosting of this project.
---

## Testing
### Manual Testing 

All the test are executed on desktop/laptop as well as on mobile devices/tablets. App is compatible with the following browsers: 
- IE 
- Edge
- Firefox
- Safari
- Opera
- Chrome
- iOS
- Android

### Home page
When clicked on the PCBuilder logo at the center of the navigation bar the user is taken to the homepage

#### Slider
Slider automatically goes through slides. User is able to navigate through the slides by clicking on the dots at the bottom center of the slider. When user clicks on the view all builds button, it takes them to the All builds page. When user clicks on Add a build button it takes the user to the Add a build page.

### Navigation 
All navigation links (main navigation bar, dropdown menu items, mobile side navigation and dropdown links in mobile side navigation) have been tested and each leads to their respective pages. User is able to navigate to previous and next page using the back and forward buttons.

### All Build
User can see all the builds that have been added displayed as card. Initially Showing the name. When clicking on the expand icon, User is able to see the name of the components and the name of the parts.

### Edit a build
When clicking on the red 'Edit' button, the user gets redirects to a form with pre-populated fields containing the values of the build they selected for editing. User can change the values of the fields. User can submit these changes by clicking on the 'Edit Build' button. When trying to submit a change with a empty name field a popup appears at the name field saying that this field is required.
When trying to submit a change when a option field is empty, the user is not able to submit the changes. 

### Delete a build
User can click on the red delete button to delete a build. User is then redirected to the "view all builds page" and the build that has been deleted is now not visible on the all builds page anymore.

### Add Build
When clicking on Add a build User is taken to a page with a form and is able to select from different parts and then use the 'add build' button to add the build to the 'view all builds' page which the user gets redirected to. User is now able to see the build that has been added.
User is not able to submit a form when the name field is empty, and a pop-up appears at the name field telling the user that this field is required. User is not able to add a build when option form is empty.

### Debugger
Throughout developing this project debug has been set to true for this app to display possible errors. 

##### bugs
 - When adding a build it was not sending data correctly and was sending Null values. fixed it by giving the collection name variable the right name. 
 - Bug where search results were not displaying. Fixed it by looping throuh the right collection variable ($regex search)
 - Bug where "search by" menu item in side navigation was not aligned with the other menu items. Fixed it by applying some padding in CSS

### Validators

#### Html
All the HTML files were tested with the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Note: because this service doesn't recognize Jinja templating language, it  does showe a some errors. Besides that there were no errors found.

#### CSS
CSS file was tested with the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). And No error were found

#### JavaScript
JS file was tested with [Esprima](https://esprima.org/demo/validate.html) And the code is syntactically valid

#### Python
Python file was tested using the pylint command in the terminal and were all PEP8 compliant.
except one for one error: app.py:14:4: W0611: Unused import env (unused-import). However this import is required to get the enviromental variable containing the MongoDB connection string. 


### Compatibility and Responsiveness
I've tested the responsiveness of this project using the chrome developer, using the different mobile devices available as well as rescaling the brower.

---

## Deployment
### Local Deployment
To be able to run this project, you must require the following tools:
- An IDE 
- [MongoDB Atlas](https://www.mongodb.com/) (for creation of your database)
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) (to install packages) 
- [Python](https://www.python.org/)   
#### Directions
1. You can clone this repository into the editor by pasting the following command into the terminal:   
`git clone https://github.com/kris965/pc-builder`    
Or you can save a copy of this repository by clicking the button "Clone or download" , then "Download Zip" button, and then extract the ZIP file to your folder.
2. In the terminal window change directory (CD) to the correct file location (directory that you have just created).
3. Set up environment variables:
    - Create **env.py** file in the root directory.
    - At the top of the file add `import os` to set the environment variables in the operating system.
    - Set up the connection to your MongoDB database(MONGO_URI) with the following syntax:  
    `os.environ["MONGO_URI"] = "YourMongoURI"`  
    .
4. Install all requirements needed to run this application using **requirements.txt** by running the following command in the terminal:   
`pip3 install -r requirements.txt`  
5. Create a new Database "pcbuilder" in [MongoDB Atlas](https://www.mongodb.com/).   
6. In "pcbuilder" database create five following collections:

###### build
```
_id: <ObjectId>
build_name: <String>
motherboard: <String>
processor: <String>
processor_cooler: <String>
memory: <String>
graphics_card: <String>
hard_drive: <String>
power_supply: <String>
case: <String>
```
###### case
```
_id: <ObjectId>
case: <String>
```
###### graphicscard
```
_id: <ObjectId>
graphics_card: <String>
```
###### harddrive
```
_id: <ObjectId>
hard_drive: <String>
```
###### memory
```
_id: <ObjectId>
memory: <String>
```
###### motherboard
```
_id: <ObjectId>
motherboard: <String>
```
###### powersupply
```
_id: <ObjectId>
power_supply: <String>
```
###### processor
```
_id: <ObjectId>
processor: <String>
```
###### processorcooler
```
_id: <ObjectId>
processor_cooler: <String>
```

7. You are now be able to run this application by running the app.py file using the command: `python3 app.py`.   

### Heroku Deployment
Deploying the app to [Heroku](https://heroku.com/):
1. Create a **requirement.txt** using the following command in the terminal:  
`pip3 freeze > requirements.txt`
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:   
`echo web: python run.py > Procfile`
3. `git add`, `git commit` and `git push` these files to theGitHub repository
4. Create a new app in Heroku.
5. If you use automatic deployement:
    From the Heroku dashboard link the new Heroku app to your GitHub repository:    
    - "Deploy" -> "Deployment method" -> "GitHub"
    - then "Enable automatic deployment"
6. To start the web process by usint the this command into the terminal: `heroku ps:scale web=1`
7. go to settings and click on Reveal Config Vars and set up the following:
    - **IP** : 0.0.0.0
    - **PORT** : 8080
    - **MONGO_URI** : `<link to your MongoDB database>`
    - **DEBUG**: **FALSE**  

8. The app will now be deployed and then ready to run. Click Open App to view the app.   

---

## Credits

### Media
 - Images for the slider on the home page were taken from [Unsplash](https://unsplash.com/).

### Acknowledgements
-  the Code Institute Slack community was really helpful during the development of this project.
- "Search build by" logic was inspired by Mark Sheenan's project.
- I took inspiration for the readme.md from Irina Tushina's project
- Thank's to my mentor for giving me feedback and helping me with the project planning. 
---

**This project is made for educational use**