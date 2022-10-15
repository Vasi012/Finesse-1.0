# Testing File

##### All the tests conducted and bugs will be in this file.

# Authentication

Test 1 - *Description*:

Ensure a user can sign up to the website.

Steps:

1. Navigate to Finesse home page, and click on 'Register'.
2. Enter email address, username and password.
3. Click Sign Up.


Expected:

After filing up the required fields, and clicking on the 'Sign Up' button, the user will receive an email with the confirmation of his account being created.
The users will need to click on the link submitted to the account and they will be redirected to a confirmation page informing the users about the account being activated.
Now the users can navigate to 'Log in' and insert the details, click on the 'Sign in' button and they will be redirected to the home page.

Actual:

After filing up the required fields, and clicking on the 'Sign Up' button, the user will receive an email with the confirmation of his account being created.
The users will need to click on the link submitted to the account and they will be redirected to a confirmation page informing the users about the account being activated.
Now the users can navigate to 'Log in' and insert the details, click on the 'Sign in' button and they will be redirected to the home page.


Test 2 - *Description*:

Ensure a user can log in once an account has been registered. 

Steps:

1. Navigate to Finesse home page, and click on 'Login'
2. Fill up the login details created in previous test case.
3. Click login button.


Expected:

After filling up the fields created when registering their account, they can click the 'Login' button. 
Once the 'Login' button has been clicked the users will be redirected to the Home page.

Actual:

After filling up the fields created when registering their account, they can click the 'Login' button. 
Once the 'Login' button has been clicked the users will be redirected to the Home page.


Test 3 - *Description*:

Ensure a user can Sign out.

Steps:

1. If the users are logged into its account and they prefer to sign out, they can click on the 'Account' button from the Nav bar.
2. User can select 'Logout'.
3. After clicking 'Logout', the users will be redirected to a page where they will need to confirm to Sign out.

Expected:

User is logged out and back to the home page.

Actual:

User is logged out and back to the home page.


Test 4 - *Description:

Ensure a user can contact the site owner by clicking 'Get in touch with us'.
*This section has been created to allow users to contact the site owner without needing to be logged into their account.*

Steps:

1. Search Finesse.
2. User is redirected automatically to the Home page.
3. Scroll down until you see the button 'Get in touch with us'.
4. Click on the button.
5. A modal will pop up where the user is required to fill up some fields before sending the form.
    - Insert full name (required)
    - Insert Email Address (required)
    - Insert message (require)
6. After filling up the form fields, user can click on the 'Send' button.

Expected:

An email containing the details from the form has been send to site owner: eventswithfinesse@gmail.com

Actual:

An email containing the details from the form has been send to site owner: eventswithfinesse@gmail.com



Test 5 - *Description*:

Ensure a member of Finesse can subscribe to the news letter.

Steps:

1. Navigate to Finesse page.
2. Click login in the navbar, fill up the fields with the user details, click 'Login'.
3. User is redirected to the home page, logged into their account.
4. Scroll down to the footer of the page.
5. Click on 'Subscribe to News Letters'.
6. A OffCanvas will pop out from the left hand side of the screen with 2 fields (Email and Name).
7. User fills up correctly the fields, and clicks on the subscribe button.
8. A message is display informing the user that has successfully added in the list.

Expected:

If site users are not authenticated, the users will not be allowed to fill up details in the OffCanvas popup, and will be informed that will need to be logged into their account to be able to access that field.
If the users are authenticated, they can fill up the form and subscribe to the newsletter. 

In order to do not supra solicitate the Data Base:

1. The users which are connected to thei account are able to insert an email address just once. If they try to reuse the same address, a message will be displayed informing them about this.
2. A user has to insert the correct email address [example@email.com]. If not, a message will be showed informing the user about the error.
3. The 'Subscribe' button will be deactivated initially until the server checks if there is already the same email address.

Actual:

If the site users are not authenticated, the users will not be allowed to fill up details in the OffCanvas popup, and will be informed that they will need to be logged into their account to be able to access that field.
If the users are authenticated, they can fill up the form and subscribe to the newsletter. 


Test 5 - *Description*

Ensure all navigation links work on all pages.

Steps:

1. Navigate to Finesse page.
2. Click on all the navigation buttons. (User not authenticated)
3. Click on Logo, Home, Register, Login and reverse.
4. Click on all the navigation buttons. (User Authenticated)
5. Click on Logo, Home, Blog, Account (Dropdown button) -> Preview Profile, Edit Profile, Account Settings, Change E-mail, Logout and reverse.

##### Links

1. Name                    -> HTML page
2. Home                    -> index.html
3. Blog                    -> blog.html
4. Logout, Login, Register -> Sign up all auth page.
5. Add post                -> add_post.html
6. Update post             -> update_post.html
7. Delete Post             -> delete_post.html
8. Edit Profile            -> edit_profile_page.html
9. Account Settings        -> edit_profile.html
10. Preview Profile.        -> user_profile.html

Expected:

All navigation links direct to the correct pages as expected.

Actual:

All navigation links direct to the correct pages as expected.


### Blog

Test 6 - *Description*

The blog section is restricted for members only.
If the users want to be able to see the blog page, they will need to create an account and log into this account.

Steps:

1. Navigate to Finesse.
2. Create / Login into user account.
3. Click on the Blog Section.
4. User is redirected to the Blog page.
5. On the blog page user can see others posts, they can add a post (The post needs to be approved by an Admin).
6. If a post has been created by a user, the same user can edit or delete a blog post.
7. A user can add a comment in any posts. (The comment needs to be approved by an Admin).


Expected:

The users can navigate to blog.html (Blog), just after they login into their account. 
Once the users are logged into their account will be able preview the blog section, add a post, edit or delete their post and add a comment.

Actual: 

The users can navigate to blog.html (Blog), just after they login into their account. 
Once the users are logged into their account will be able preview the blog section, add a post, edit or delete their post and add a comment.


### Blog & Profiles

Test 7 - *Description*

User can preview other people profile by clicking on an icon next to the person's comment.


![image1](https://user-images.githubusercontent.com/96884287/195994806-a06882ad-fb55-41c1-a98c-05a977fe31e7.jpeg)


Steps:

1. Navigate to Finesse.
2. Create / Login into user account.
3. Click on 'Blog'.
4. Choose a post with comments from other users.
5. Click on the open book icon next to user username.
6. You will be redirected to preview that user profile.

The users can update their own profile by following the next steps
    1. Click on the 'Account' in navbar.
    2. Click on Account Settings.
        - Add a First and Last name.
        - Add an Email
    3. Click Update Profile.
    4. Click on 'Account' in navbar.
    5. Click on Edit Profile.
        - Add a Profile Picture.
        - Add a biography
        - Add a Website.
        - Add Social Media links.
    6. Click on Update profile page.
    7. Click on Account in the navbar.
    8. Click on Preview Profile

Now you can see what other users can see when they navigate on your profile.

Expected:

If the users did not update their profile, some default information will be in-place.
If the users completed the above steps, themselves or other users are now able to see their profile. (Preview Profile).

Actual:

If the users did not update their profile, some default information will be in-place.
If the users completed the above steps, themselves or other users are now able to see their profile. (Preview Profile).


## Footer Page

Testing was performed on the footer links by clicking the bootstrap icons, and ensuring that the Facebook icon opened Facebook in new tab, the Instagram icon opens Instagram in a new tab and the Twitter icon opened Twitter in a new tab.
These behave as expected. User is redirected to the official pages created by Finesse.
Testing was also performed on the 2 other buttons: 'Working Hours' and 'Subscribe to Newsletter', and both behave as expected.

### Other Testings

##### Accessibility

Wave Accessibility tool was used throughout development and for final testing of the deployed website to check for any aid accessibility testing.

Testing was focused to ensure the following criteria were met:

All forms have associated Labels or aria-labels so that this is read out on a screen reader to user who tab to form inputs. Colour contrast meet a minimum ratio as specified in WCAG 2.1 Contrast Guidelines.

Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user.

All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions.

All non textual content had alternative text or title so descriptions are read out to screen readers.

HTML page lang attribute has been set to English.

Aria properties have been implemented correctly.
WCAG 2.1 Coding best practices being followed.



Test - 8 *Description*

Each page has been tested to ensure that it meets the criteria required in WCAG 2.1.

The testing has been conducted by navigating on each page and use WAVE.

Home Page.

Results:

![image12](https://user-images.githubusercontent.com/96884287/195994850-52554e5a-deb4-4090-9ab7-3d735354e812.jpeg)


Blog Page.

Results:

![image13](https://user-images.githubusercontent.com/96884287/195994862-2916b590-75de-4f3c-a3e2-030324945cd9.jpeg)


Sign in / Sign Up / and other Django allauth.

Results:

![image9](https://user-images.githubusercontent.com/96884287/195994871-7a58d3c3-689e-4116-9d48-e6aa3039d694.jpeg)


Post Details:

![image11](https://user-images.githubusercontent.com/96884287/195994877-ccb2793e-bbe2-45be-a544-7d3b56b2afe0.jpeg)

We have 4 errors here and this is becose we pull from the backend the href used to allow users to navigate to other users profile.
Also, there is an error with the like button as there is just an icon (Heart) and no text. 

Add post

Results:

![image6](https://user-images.githubusercontent.com/96884287/195994978-e9d45190-9222-49dc-9fe9-8999278730d5.jpeg)

We have a contrast error as I'm unable to change the link color of the picture used. However, if a user hovers over this, will be able to see it in a darker colour and the error will dissaper. 

Edit Post, Preview Profile, Edit Profile

Results:

![image7](https://user-images.githubusercontent.com/96884287/195995034-ecfcda21-3a99-4f9d-a603-bd4719edde40.jpeg)


Delete Post.

Results:

![rgf](https://user-images.githubusercontent.com/96884287/195995578-e317a9e2-f33b-4a70-8b52-b8049dd0dc96.png)



Account Setting

Results:

![image10](https://user-images.githubusercontent.com/96884287/195995122-7540db17-a836-4fe0-8691-e490f6bdf6ac.jpeg)

We have a contrast error as I'm unable to change the link color of the picture used. However, if a user hovers over this, will be able to see it in a darker colour and the error will dissaper. 

Change Email

Results:

![sadsf](https://user-images.githubusercontent.com/96884287/195995605-03e5dc65-8d5e-4002-ad6c-93fb6361a11c.png)



#### Validator Testing

All pages were run through the w3 HTML Validator. Initially there were some errors due to stray script tags, misuse of headings within spans and some unclosed elements. All of these issues were corrected and all pages passed validation.

Due to the django templating language code used in the HTML files, these could not be copy and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.


Test - 9 *Description*

Each page has been opened and the HTML code has been put throughout HTML Validator.

Results:

Home Page, Blog Page, Sign up / Register / Login

![image2](https://user-images.githubusercontent.com/96884287/195995199-024a639a-b98a-4a6e-a23a-6b800c74180a.jpeg)

Post Detail:

![image0](https://user-images.githubusercontent.com/96884287/195995218-614d0423-90a3-460c-bde2-7dbd1dde36ed.jpeg)


##### Django / Python testing.

Test - 10 *Description*

Due to a last update the page pep8 used to test the python code is not accessible anymore. Therfore, tests were performed inside the terminal using flake8.

How do you use it?

Firstly, we open GitPod, open our project, and in the terminal we install flake8. 
  - pip install flake8
Once flake8 has been installed we need to run another command in the terminal.
  - python3 -m flake8 <name> (where name is the name of the app i.e: finesse).
  
  
The results using flake8 are as following:

eventsM -> No issues have been identify here. Everything works and run as expected.

![image3](https://user-images.githubusercontent.com/96884287/195995260-da042cec-f974-4283-a583-441aea39d82d.jpeg)


finesse -> The only errors in this page are generated by the settings.py file.
The reason for this errors is: 
  - 'env' imported but unused -> This is due to the fact that env.py is added to GitIgnore and will not be seen by the flake8.
  - The other errors are in regards with the length of some lines. As I couldn't find a way to split these lines but since they were auto generated and not my own custom code, i hope this is acceptable. Please refer to the below image.
  - The django auto generated code for AUTH_PASSWORD_VALIDATORS were showing up as lines too long. As mentioned above, since they were auto generated and not my own custom code, i hope this is acceptable.
  
![image8](https://user-images.githubusercontent.com/96884287/195995289-e261f4cc-a7f7-45bb-995a-9d44bfb40e06.jpeg)

finesseBlog -> No issues have been identify here, and everything works and run as expected.

![image14](https://user-images.githubusercontent.com/96884287/195995278-dc9ba49c-7e85-4c9e-a9f2-71bb64cbf995.jpeg)

![csadsffd](https://user-images.githubusercontent.com/96884287/195995401-7eda5632-68a3-410b-a80b-d7dc92827311.png)


### JSHint

Test 10 - *Description*

The JavaScript code was run through JSHint JavaScript validator. This validator flagged up issues with undefined variables as i have forgotten to use the let keyword. This was fixed and the only warnings remained were that they were unused variables. The functions were called via on click from the HTML elements themselves, so are in fact being used.

Other errors have occured because the browser doesn't use ES6 and JSHint couldn't run them.

JSHint Validator: 

![saadfgf](https://user-images.githubusercontent.com/96884287/195995400-f2a716af-e30e-4b6e-aa32-6507b331fd14.png)


This errors have been fixed, and now there are not any other errors.



### Lighthouse

ADD PICTURE

Responsiveness
All pages were tested to ensure responsiveness on screen sizes from 320px (and 280px) and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Test 11 - *Description*

Test using Lighthouse.

Steps:

1. Open browser and navigate to Finesse.
2. Open the developer tools (right click and inspect)
3. Set too responsive and decrease width to 320px and after too 280px.
4. Set the zoom to 50%.
5. Click and drag the responsive window to maximum width.

    ![Screenshot 2022-10-15 at 16 54 08](https://user-images.githubusercontent.com/96884287/195996026-dd1d2136-82f0-4145-a451-3da0e2e9e85f.jpg)
    
In this Lighthouse report we can see that everything works as expected. The performance my vary as the blog adds full size pictures in the blog section, also the home page has used gifs for in a carousel post for the hero image. Therfore, this will bring the performance a little bit low. However, this depends on user's internet speed.
    
    
Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlaped.

Actual:

Website behaves as expected.

Website was also opened on the following devices and no responsive issues were seen:

1. iPhone 14 Pro Max,
2. iPhone 13 Pro Max,
3. Samsung S9
4. Laptop
5. 32" desktop screen.

Everything works as expected.

Bugs

A bug has been noticed when adding or updating posts on some screen devices.
I will conduct daily tests in order to prevent bugs to appear, and fix them in the 2.0 version of the website. 







