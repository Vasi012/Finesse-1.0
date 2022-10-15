![Wirframe - 1](https://user-images.githubusercontent.com/96884287/190642118-ce305db6-49e0-4254-8eba-e5c0bea9a513.png)
![Wirframe - 2](https://user-images.githubusercontent.com/96884287/190642122-761f8500-fbc0-40b7-a59c-75ae539ecdaa.png)
![Wirframe - 3](https://user-images.githubusercontent.com/96884287/190642124-c6a9697b-57fd-44e0-aa22-c2abdfc177fe.png)
![Wirframe - 4](https://user-images.githubusercontent.com/96884287/190642127-7aea6881-8173-4953-8ca1-8cd15f271c42.png)
![Wirframe - 5](https://user-images.githubusercontent.com/96884287/190642129-a9c9dda4-4fce-4d2a-8ebc-c88fc1198df8.png)
![Wirframe - 6](https://user-images.githubusercontent.com/96884287/190642141-582cfba4-273a-4fe0-ba87-a15227bb3580.png)
![Wirframe - 7](https://user-images.githubusercontent.com/96884287/190642142-b32158cd-2bdf-4bb5-970a-f71ab87d31de.png)
![Wirframe - 8](https://user-images.githubusercontent.com/96884287/190642146-de11f7ee-aa84-497a-a1f6-846975127180.png)
![Wirframe - 9](https://user-images.githubusercontent.com/96884287/190642147-c511b344-c077-4641-a911-90dba301472b.png)
![Wirframe - 10](https://user-images.githubusercontent.com/96884287/190642148-5afb0f78-1a6e-4a10-9b1b-57a6d09b3044.png)
![Wirframe - 11](https://user-images.githubusercontent.com/96884287/190642152-58bf5547-d9ae-44a6-b929-0069d949af3c.png)
![Wirframe - 12](https://user-images.githubusercontent.com/96884287/190642154-3422e187-27f2-4044-9c5f-c0adaf69b7cc.png)
![Wirframe - 13](https://user-images.githubusercontent.com/96884287/190642156-bec2f6b7-9ec5-40f5-9863-b781bb39f0e7.png)
# Finesse

Finesse is a fictional event management platform. This company doesn’t have a fix location as it is mainly an online business.

Our mission is to deal directly with clients, organising future events of all kinds.
The online platform is simple structure so the users can have an overview of the events that finesse organised.

The website is divided in 2 main pages, the first page ‘home’ will be the page where users are directed once they navigate on the website. 
The home page is with attention structured to be simple and thick all the boxes for the users. 
The home page has the ‘’about us’’ section, a ‘’get in touch with us section’’, where users can get in touch with the management of the website directly via email. On the same page, users can see other informations about the website, and what is the company all about. They can subscribe to rechieve newsletters.  
On the Second page, users can interact with eachother via posts and comments. This section has been designed for members only.

<<<Mock Up>>>

### User-Experience-Design

######The-Strategy-Plane



###### Site-Goals

The website aims to help users find the organisers for their next event.
The website is relatively simple to use, and users can get from a part to another very easily without too much hassle. 
At the same time, the website comes with a blog section where users can interact with eachoter by posting or commenting to their/others posts. 

The site aims to provide customers with a simple and easy way to get in touch with the management and organise their future events, get subscribed to the newsletter and comment, add posts, edite and delete their own posts, liking / unliking posts. 

### Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. 
The users’ stories are considered software features and 95% of them have been implemented in order to match the requested owner criteria.  
All projects were assigned to ToDo, prioritized under the labels, must have, should have, could have. They were assigned to sprints and story pointed according to complexity. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located [here](https://github.com/users/Vasi012/projects/2) and can be viewed to see more information on the project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define the functionality that marks that story as complete.

##### Kanban image

Epics
The project had 7 main Epics (milestones):

EPIC 1 - Base Setup

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible, so it was the first epic to be delivered as all other features depend on the completion of the base setup.

EPIC 2 - Standalone Pages

The standalone pages epic is for small pages that did not have enough stories to warrant their own full epics. Instead of creating epics for tiny features, these small deliverables were all added under this epic.

EPIC 3 - Authentication Epic

The authentication epic is for all stories related to the registration, login and authorization of views. This epic provides critical functionality and value as without it the users won’t be able to see the blog posts, post or register to the website.

EPIC 4 – Subscribe to our newsletter

User with an account can subscribe to the website newsletter and they can be updated at all times with everything happening around the company from updates on the website to future events happening where they can attend and have a good time. 

EPIC 5 – Get in touch with us

The get in touch with us button located in the first page has been created to offer users the possibility to get in touch with the management asap. The users can use this button If they are new visitors of this website / users with an account. This button has been implemented that one a form is completed to be send in a format to the staff management and they can get in touch via email. Not needing to contact via phone. 

EPIC 6 - Deployment Epic

This epic is for all stories related to deploying the app to heroku so that the site is live for staff and customer use.

EPIC 7 - Documentation

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

User Stories
The following user stories (by epic) were completed:

EPIC 1 - Base Setup

As a developer, I need to create the base.html page and structure so that other pages can reuse the layout.

As a developer, I need to create static resources so that images, CSS and JavaScript work on the website.

As a developer, I need to set up the project so that it is ready for implementing the core features.

As a developer, I need to create the footer with social media links and contact information.

As a developer, I need to create the navbar so that users can navigate the website from any device.

EPIC 2 - Standalone Pages

As a developer, I need to implement a 404-error page to alert users when they have accessed a page that doesn't exist

As a developer, I need to implement a 500-error page to alert users when an internal server error occurs

As a developer, I need to implement a 403-error page to redirect unauthorised users to so that I can secure my views

As an Event Management online platform owner, I would like a home page so that customers can view information about the Finesse website. 

EPIC 3 - Authentication Epic

As a developer, I need to implement allauth so that users can sign up and have access to the website’s features.

As a site owner, I would like the allauth pages customized to that they fit in with the sites styling

EPIC 4 – Subscribe to our newsletter

As a site owner, I would like to keep all the website users informed with everything happening around the company such as future events.
As a developer I want to provide an easy way for my users to subscribe to the newsletters and limit the users to use the subscribe button just one time with an email address. This function has been implemented in order to prevent users from supra solicitate the system with the same email address more then once. 

EPIC 5 – Get in touch with us

As a developer I want to allow users to be able to get in touch with the site owners via email.
As a site owner I want users to complete a form and be able to detail what type of events they are looking for and receive an email with their inquiries. 
As a site user I want to be able to get in touch with the site owners asap and therefore completing the form will be very easy. 
EPIC 6 - Deployment Epic

As a developer, I need to set up white noise so that my static files are served in deployment

As a developer, I need to deploy the project to heroku so that it is live for customers

EPIC 7 - Documentation

Also, after this has been completed, I decided to add a profile section, where users can add, or edit their profile and alow them and other users to preview their profile. 

On the blog page I as a developer, implemented an edit and delete button, so users can edit or delete their own posts.

Tasks:

Complete readme documentation.
Complete testing documentation write up.


### The-Scope-Plane

Responsive Design - Site should be fully functional on all devices from 280px (as per last phone from Samsung Galaxy Fold).
Restricted role-based features
Home page with about us information, newsletters & blog page.

### The-Structure-Plane

Features
USER STORY - As a developer, I need to create the navbar so that users can navigate the website from any device

Implementation:

Navigation Menu

The Navigation contains links for Home, allauth options and once signed up blog section and Account (Profile editing).

The following navigation items are available on all pages:

Home -> index.html - Visible to all
Blog -> blog.html – Visible to all logged in users
Login -> login.html - Visible to all
Register -> signup.html - Visible to all
Logout -> logout.html - Visible to logged in users
Add post -> add_post.html - Visible to logged in users
Update post -> update_post.html - Visible to logged in users
Delete Post -> delete_post.html - Visible to logged in users
Edit Profile -> edit_profile_page.html - Visible to logged in users
Account Settings -> edit_profile.html - Visible to logged in users
Preview Profile. -> user_profile.html - Visible to all

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

Navbar>>>>>>

USER STORY - As Finesse owner, I would like a home page so that customers can view information about my event management platform.

Implementation:

Home Page

The home page contains a hero carousel image of events that took place and the Finesse information right after the hero image. This will immediately make it evident to the user, what the purpose of the website is.

Under the about us section there is a button, ‘Get in touch with us. This button will allow users to contact the website management via email in a very quick way reducing the hassle of navigating on the website, searching for company number or email address and after contacting the website management. 

The last section of the home page contains a footer, the footer has been carefully customised to contain 2 other buttons, one of the buttons will contain the working hours and a different button where users can subscribe to websites newsletter (this function will work if the user is logged in to the website.)


##### Footer

USER STORY - As a developer, I need to create the footer with social media links and contact information

Implementation:

Footer>>>>>>

A footer has been added to the bottom of the site, this contains a Twitter, Instagram and Facebook link so that users can follow Finesse on social media if they want to keep up to date with special offers not advertised on the website / newsletter. These icons have aria-labels added to ensure users with assistive screen reading technology know what the purpose of the links are for. They also open in new tabs as they lead users away from the site. The links have been carefully customised to direct users to the personal pages created especially for this project. 

USER STORY – As a user, I want to be able to subscribe to the website newsletters / to see what the business hours of this company are. 

Implementation:

Create 2 buttons with this required functionality 

The first button has been creating using the customised bootstrap canvas, once clicked on ‘working hours’ this will trigger a small window popping out from the right-hand side whit the business hours of the Company.

The second button has been creating using the customised bootstrap canvas, once clicked on ‘Subscribe to Newsletter’ this will trigger a small window popping out from the left-hand side with the subscribe form. This will work just if you are signed into the page otherwise a text will be showed where users are directed to log in to have access to this section. 

##### Toasts

Custom toasts were added on successful creation of an account, deleting an account, signed into an account, successfully submitted the get in touch with us form, successfully subscribed to newsletters. This will provide feedback to the user to relay information that the mentioned above have been successfully received or updated.


##### Favicon 

*A site wide favicon was implemented.* 

This provides an image in the tabs header to allow the user to easily identify the website if they have multiple tabs open.

Favicon>>>>>>

#### Error Pages

USER STORY - As a developer, I need to implement a 404-error page to alert users when they have accessed a page that doesn't exist

Implementation:

404 Page

As a developer, I need to implement a 404-error page to redirect users to the home page.

A 404 page has been implemented and will display if a user navigates to a broken link.

The 404 page will allow the user to easily navigate back to the main website if they direct to a broken link / missing page, without the need of the browsers back button.

USER STORY - As a developer, I need to implement a 403-error page to alert users when accessing a page/view that they do not have permission to view

Implementation:

403 Page

A 403-error page has been implemented to provide feedback to the user when they try to access unauthorized content. Users will be directed to this page if they alter the URL's and attempt to edit, delete or access pages that are restricted.

USER STORY - As a developer, I need to implement a 500-error page to alert users when an internal server error occurs

Implementation:

500 Page

A 500-error page has been displayed to alert users when an internal server error occurs. The message relays to users that the problem is on our end, not theirs.

Base Setup User Stories

The following stories were implemented in order to set up a base structure for all the HTML pages and the core installations and configurations needed to run the application. While these do not show as individual features, they were stories completed that were needed to implement all the stories above.

As a developer, I need to create the base.html page and structure so that other pages can reuse the layout.

As a developer, I need to create static resources so that images, CSS and JavaScript work on the website.

As a developer, I need to set up the project so that it is ready for implementing the core features


Features Left to Implement
In a future release I would like to implement messageing system that allow users to communicate with website owners without nedding of a 3rd party such as email. On the home page I would like to implement a rating system so users can see reviews left by others and trust the website. 

### The-Skeleton-Plane

Wireframes
Home page
Home Page>>>>>>

Signup page
Sign up Page>>>>>>

Log in
Login Page>>>>>>

Log Out
Logout Page>>>>>>

Blog
Blog page>>>>>>

404 Error
404 Error>>>>>>

403 Error
403 Error>>>>>>

500 Error
500 Error>>>>>>

Edit Profile
>>>>>>

Account Settings
>>>>>>

Preview Profile
>>>>>>

Add Post
>>>>>>

Delete Post
>>>>>>

Edit Post
>>>>>>


### Differences to Design

Initially the website was designed to be shared across multiple pages, however this has been changing in order to provide simple and user-friendly interface. This change reflects users a reduced features that probably my end up unused, restructured in a one-page content. 


### Database-Design
The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model is at the heart of the application as it is connected the blog side, linked by primary/foreign key relationships many to many and so on.


### Security

Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, api keys or sensitive information was added the repository. In production, these variables were added to the heroku config vars within the project.

### The-Surface-Plane

Design

###### Colour-Scheme
The main colour schemes for the website are white and violet ground. Black font / violet in some areas.

###### Typography
Domine font was used throughout the website. This font is from google fonts and was imported into the style sheet.

###### Imagery
The Website Logo and other pictures have been created using Photopea. 

The hero carousel images(GIF) were taken from Google Images which is a royalty free image site and the signature has been added using Photopea.

### Technolgies

HTML
The structure of the Website was developed using HTML as the main language.

CSS
The Website was styled using custom CSS in an external file.

JavaScript / jQuery / Ajax
JavaScript was used to make the forms and disable some buttons.

Python
Python was the main programming language used for the application using the Django Framework.

GitPod
The website was developed using Gitpod and Code Institute Templating.

GitHub
Source code is hosted on GitHub

Git
Used to commit and push code during the development of the Website

Bootstrap
This was used for various icons throughout the site / function ability

Favicon.io
favicon files were created at https://favicon.io/favicon-converter/

balsamiq
wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#

Photpea
This was used to create the logo in header / and add the sizing / logo on the picture used.

TinyPNG
This was used to compress the hero image for optimal load times


### Python Modules Used

Django Class based views (ListView, UpdateView, DeleteView, CreateView) - Used for the classes to create, read, update and delete
messages - Used to pass messages to the toasts to display feedback to the user upon actions
timedelta, date - Date was used in order to search for objects by date and timedelta for searching date ranges
External Python Modules

asgiref==3.5.2 -> The asgiref.sync module provides two wrappers that let you go between asynchronous and synchronous code at will, while taking care of the rough edges for you.
cloudinary==1.30.0 -> Cloundinary was set up for use but no custom uploads were made, settings remain for future development
dj-database-url==1.0.0 - Used to parse database url for production environment
dj3-cloudinary-storage==0.0.6 Storage system to work with cloudinary
Django==3.2.15  Framework used to build the application
django-allauth==0.51.0 Used for the sites authentication system, sign up, sign in, logout
django-crispy-forms==1.14.0  Used to style the forms on render
django-summernote==0.8.20.0 Summernote is a simple WYSIWYG editor. django-summernote allows you to embed Summernote into Django very handy.
gunicorn==20.1.0 Installed as dependency with another package
oauthlib==3.2.1 Installed as dependency with another package
psycopg2==2.9.3 Needed for heroku deployment
PyJWT==2.5.0 Installed as dependency with another package
python3-openid==3.2.0 Installed as dependency with another package
pytz==2022.2.1  pytz brings the Olson tz database into Python. This library allows accurate and cross platform timezone calculations using Python 2.4 or higher.
requests-oauthlib==1.3.1 This project provides first-class OAuth library support for Requests. 
sqlparse==0.4.3 Installed as dependency with another package
types-cryptography==3.3.23 Cryptography can be broken down into three different types: Secret Key Cryptography.Testing
Test cases and results can be found in the TESTING.md file. This was moved due to the size of the file.

### Deployment

Version Control

The site was created using the Gitpod editor and pushed to github to the remote repository ‘Finesse-1.0’.

The following git commands were used throughout development to push code to the remote repo:

git add <file> - This command was used to add the file(s) to the staging area before they are committed.

git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

git push - This command was used to push all committed code to the remote repository on github.

##### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

Navigate to heroku and create an account

Click the new button in the top right corner

Select create new app

Enter app name

Select region and click create app

Click the resources tab and search for Heroku Postgres

Select hobby dev and continue

Go to the settings tab and then click reveal config vars

Add the following config vars:

SECRET_KEY: (Your secret key)

DATABASE_URL: (This should already exist with add on of postgres)

EMAIL_HOST_USER: (email address)

EMAIL_HOST_PASS: (email app password)

CLOUNDINARY_URL: (cloudinary api url)

Click the deploy tab

Scroll down to Connect to GitHub and sign in / authorize when prompted

In the search box, find the repository you want to deploy and click connect

Scroll down to Manual deploy and choose the main branch

Click deploy

The app should now be deployed.

The live link can be found here: Live Site

Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

Click on the code drop down button

Click on HTTPS

Copy the repository link to the clipboard

Open your IDE of choice (git must be installed for the next steps)

Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

Navigate to the GitHub Repository you want to fork.

On the top right of the page under the header, click the fork button.

This will create a duplicate of the full project in your GitHub Repository.

### Credits

All media from the website has been created using Photopea & Google Images.
The readme and testing file has been created using Gareth McGirr steps and paraphrasing information.
The project has been build by myself inspiring from Sizzle and Steak & Code Institute Walkthrough.
Some bugs we’re fixed using Nik’s help and guidance.
Some features have been implemented with help from YouTube tutorials.
The Event management platform idea has been inspired from here. https://www.mgnevents.co.uk/
The texts have been created by me. 
The website has been created following YouTube tutorials and stack overflow. 
To W3Schools a platform that helped me to clarify some not understanding about Js.
Other issues and debugs have been fixed with help from colleagues in Slack.

Big thank you for my mentor Daisy, for all the guidance and unlimited messages send to her.

