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










