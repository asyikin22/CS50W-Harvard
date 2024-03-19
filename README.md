# CS50W 
These are some notes I have taken from HarvardX CS50W on Web Programming with Python and JavaScript.

# HTML
**BASIC STRUCTURE**
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/f7546025-ce9f-4bf1-9e6a-01b8829d5f7b) <br>

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/030fdb36-5d6f-40c5-a3dd-4ec94fe8a362)

**DOCUMENT OBJECT MODEL (DOM)**
Definition: Tree like structures that describe how all HTML elements interact with each other <br>
* HTML as the parent element
* Head and Body - children
* Title & hello world as the children of head and body

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/a7e74f12-5ea9-42a9-b496-322380d3b276)

**COMMON HTML TAGS**

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/30f0756f-6c48-497c-b83c-18ffe90d2a50)

# CSS

**COMMON CSS PROPERTIES**
* Style it inline
* Inside 'head' element of HTML file, inside 'style' element.
* Link a separate CSS file to HTML file using <link rel="stylesheet href="style.css">

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/49ee93e4-b805-4c9d-9f11-c315bca81061)

**IDENTIFYING ELEMENTS**
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/4ce75f44-362d-4b79-a236-d9ec1ee08905)

**SPECIFICITY**
* We use this concept to determine which styles are applied to HTML element when CONFLICTING or OVERLAPPING styles are defined.
* It is calculated based on Selectors
* The higher the specificity value, the more precedence a style declaration has.
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/30491e0d-770d-40c0-874e-34f2a1ace10d)


**CSS SELECTORS**

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/ad555ada-c03d-4f86-b29a-5c7277211c84)

**RESPONSIVE DESIGN**

Definition: A concept that allows we pages to be responsive across different screen sizes, orientations, resolutions etc. on various devices

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/dca6f40a-ff22-48da-aa24-eafa80af2eb2)

# BOOTSTRAP
* Link: https://getbootstrap.com/
* Documentation: https://getbootstrap.com/docs/5.3/getting-started/introduction/
* Popular CSS libraries that we can use in order to use some styling that they have written
* We don’t need to write all the styling from scratch.
  1. Create HTML file
  2. Include Bootstrap’s CSS and JS.
  3. Open page!

**Responsiveness**
  1. Bootstrap's column model - the column will move around whenever a size of window changes
  2. It divides the page into 12 distinct columns

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/3036e50f-fc5a-41c8-92a2-3ec50dcb5505)

# SASS

* Syntactically Awesome Stylesheets
* An extension to CSS that adds additional features
* Making it easier to write codes and to avoid repetition
* Preprocessor scripting language that is interpreted or compiled into CSS

**FEATURES**
* Variable - factor our commonalities (fonts, colors, borders, styling in general)
* Nesting - Allows us to nest CSS selectors within one another.
* Inheritance - supports inheritance through the use of '@extend' directive, allowing us to share styles between selectors.

**HOW TO AVOID REPETITION WITH VARIABLE USING SASS**

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/bc9fd76d-f592-425f-ac59-f8b85a8e30c5)

# JAVASCRIPT
* It gives us the ability to directly manipulate the DOM (Document Object Model)
* 'script tag' - we're telling the browser that anything between these tags should be interpreted as JS code to be executed

**EVENTS**:
* Everything user does will generally be thought as an 'event'
  1. User clicks button
  2. User selects an option from a drop down list
  3. Submit a form. 

**EVENT LISTENER**:
* When an event happens, JS will run a particular block of codes or functions.
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/a5401d84-736c-46fe-8b85-e3b65dacae0b)

**VARIABLES**:
* Something that is keeping track of data like the number that we are currently have counted to
  
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/1e22b6d1-5128-4c75-a393-30cc085d1fa6)

**HOW TO MANIPULATE FUNCTIONS WITH (USING PREVIOUS EXAMPLE - COUNTER)**

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/6e3f5d10-b82d-4ff3-b869-9708c288004a)


**QUERY SELECTORS**
* Document.querySelectors: gives us the ability to look through an HTML page and extract an element out of that page
* So we can manipulate that HTML element using JS code

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/915ec58e-a56a-4584-a1eb-f66f6eee77ca)

**CONDITIONS**
* We can only run a certain blocks of code when a particular expression is true

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/5da360e3-bf15-4ab7-a93f-bd21f3d73a47)

**EVENT LISTENER (USING PREVIOUS EXAMPLE - COUNTER)**
* We are going to use the 'counter' function we have done earlier
* Replace 'onclick' with '
* The following example is without attaching event listener

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/eacc1189-ce5f-48c2-b079-3022eb7ec515)

* The following example shows how we can remove onclick property from HTML element and run it in javascript
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/4b042c8e-5721-4fbd-ae22-55e33c573a38)

* This example shows how we can attach event listener to a JS code

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/1b7d1b9f-cf11-45c7-8771-70a48285c50d)

**HANDLING USER INTERACTION USING JAVASCRIPT - FORM**
* Use query selector to read information from the page
* Access what users put in input field
* Use event handling and alert to respond dynamically when user submits the form

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/f25ed011-cd4a-4c74-af50-454a1addf95f)

**USING JAVASCRIPT TO STYLE WEBPAGE**

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/9109f0da-1df4-488e-8c7c-aae057043db1)

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/2d69cbe2-1d6d-484d-85e1-aa54a01fb988)

**HOW TO CONSOLIDATE THE FUNCTION AND AVOID UNNECESSARY REPETITIONS? - DATA ATTRIBUTE**
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/c0a0d4a8-abc5-48cb-877d-0ad619f43aeb)

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/5f72d2f1-046d-4bed-8051-1d98a4b37179)

**DROPDOWN MENU IN JAVASCRIPT**
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/999a7e4a-355c-44f9-b90e-55270ede86be)

**TO-DO-LIST WITH JAVASCRIPT**
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/cd30cce6-732c-4180-a492-8b4564773376)

![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/bf72fbd8-e59c-4ced-81df-aa546a7ad107)

**SETTING INTERVAL**
* JavaScript can allow codes to work even without user interaction.
* Interval means to a time-based event that occurs repeatedly at specified intervals.
  
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/c62ec710-8080-4e7d-be7a-6328fad54d6a)

**LOCAL STORAGE**
* It's a way for us to be able to store information inside of the user's web browser
* A page can ask to store a particular values inside the web browser
* Later on, on subsequent visits to that page, we can go back and extract those values that were previously stored inside local storage
* There are 2 ways to access local storage:
  
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/a6e5997b-be7f-417f-b509-893ed5d7e2f6)

**HOW TO USE LOCAL STORAGE IN JAVASCRIPT (WE WILL STILL USE EXAMPLE FROM COUNTER)**
![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/22691f21-e313-418f-af1d-e446d885fc46)

# APPLICATION PROGRAMMING INTERFACE (API)
* A well-defined structure way for services on the internet to communicate with each other
* If you want your application to interact with other service (Google map, weather service, etc.), you can use API
* API is a mechanism that allows you to communicate with another service by sending a request and receiving back data in a well-structure format
* That particular format is known as JSON - JavaScript Object Notation
    * It's a way of transferring data in the form of JavaScript objects.
    * Objects have properties and values associated with them ---> 'key-value' pairs
      
    ![image](https://github.com/asyikin22/CS50W-Harvard/assets/148519441/9e643064-07de-47de-ac3f-35feb77ae214)

**AJAX**
* Asynchronous JavaScript
* Even after a page has loaded, using JS, we can make additional web requests to ask for additional information from
  1. Our own web server
  2. Third party web server
     


      



































