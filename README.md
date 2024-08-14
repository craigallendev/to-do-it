<img src="https://github.com/user-attachments/assets/bd3c5511-f295-4eb7-9d9d-7ee9dfd08454" alt="To-Do-It Logo" width="400" height="96px"/>

To-Do-It is a task management application designed to help users stay organized, focused, and productive. Whether you're managing a complex project, juggling multiple personal tasks, or simply trying to keep track of daily to-dos, To-Do-It provides a streamlined interface that makes it easy to plan, prioritize, and accomplish your goals.

Targeted at individuals, professionals, and students who need a reliable system to manage their tasks, To-Do-It offers a solution that adapts to a variety of workflows. With features like task categorization and priority settings, this app is designed to help users stay on top of their responsibilities and achieve more in less time. To-Do-It is a productivity tool that empowers users to take control of their time and accomplish their objectives with ease.

![Screenshot 2024-08-13 at 19 25 55](https://github.com/user-attachments/assets/5adbcc72-980f-4530-a0fd-e45df771d20a)

## Wireframes
To lay the groundwork for the project, I utilized Figma to create low-fidelity wireframes. These wireframes were essential in visualizing the layout, structure, and user flow of the application before diving into the actual development.

### Figma for Wireframing
- Tool Used: Figma
- Type of Wireframes: Low-Fidelity

The primary purpose of the low-fidelity wireframes was to:

Define Layouts: Establish the basic structure of each page, including the arrangement of elements such as headers, navigation bars, content sections, and footers.
Outline User Flow: Visualize the user journey through the application, ensuring that navigation and interactions are intuitive and logical.
Identify Key Features: Highlight the core functionalities and components of the application, such as the task management interface, search functionality, and user authentication processes.
Process
Sketch Initial Concepts:

Started by sketching initial ideas on paper to outline the fundamental layout and features.
Create Wireframes in Figma:

Transitioned to Figma to create digital versions of these sketches.
Designed wireframes for key pages including the task list, task form and login, and the footer with social links.

Benefits
Using low-fidelity wireframes in Figma provided several benefits:

Early Visualization: Enabled early visualization of the application’s layout and functionality, facilitating better planning and design.
Clear path of what to build.

Conclusion
The low-fidelity wireframes created in Figma played a crucial role in shaping the project’s design and ensuring a user-centered approach. They served as a tool for guiding the development process and contributed to a well-organized and intuitive application.

<img src="https://github.com/user-attachments/assets/6e99f3e5-62c0-4a32-ac0d-de2c51e4a81c" width="400" height="auto" alt="Wireframe Screenshot 1" />
<img src="https://github.com/user-attachments/assets/fdb37801-ca3b-4864-ae7a-c508c5ad4f8e" width="400" height="auto" alt="Wireframe Screenshot 2" />
<img src="https://github.com/user-attachments/assets/b897f948-826c-4cd7-966e-1de047847b25" width="400" height="auto" alt="Wireframe Screenshot 3" />

## Entity-Relationship Diagram (ERD)
The application is designed around two primary entities: User and Task. Below is a brief explanation of their relationship and how they interact within the Application.

- User and Task Relationship
The ERD illustrates a one-to-many relationship between the User and Task models:

User (1) → Task (many): Each user can be associated with multiple tasks, but each task is linked to only one user. This relationship is implemented using a foreign key in the Task model, which references the User model. This allows tasks to be assigned to users while maintaining the flexibility for tasks to exist without a user assignment, as the foreign key can be null or blank.

Key Entities:
User:

The User model represents the individuals who interact with the application. Each user has a unique ID, along with other attributes like username and password.
Task:

The Task model represents the tasks created by users. Each task has attributes such as title, description, completion status, category, priority, and a reference to the user it belongs to.
This supports core functionality such as task creation, editing, assignment, and tracking, ensuring that the system is both flexible and easy to manage.

![Screenshot 2024-08-14 at 08 32 06](https://github.com/user-attachments/assets/0be3d367-76e3-429c-a6bc-1e5aef9e3aa3)

## Features 

## Navigation Bar: 
- The navigation bar provides users with easy access to different sections of the app, ensuring a smooth and intuitive user experience. Whether you’re logging in, registering, or navigating between your tasks, the navigation bar keeps everything just a click away, making task management more efficient.
  
![Screenshot 2024-08-13 at 19 55 34](https://github.com/user-attachments/assets/492dc44b-4711-4d11-ab05-933bd0161240)
![Screenshot 2024-08-13 at 19 55 45](https://github.com/user-attachments/assets/2a03ff3f-e980-4864-b75c-8b7e658ae044)
![Screenshot 2024-08-13 at 19 55 52](https://github.com/user-attachments/assets/eee6070c-cabf-4fed-8f77-ba2c40ee0458)

 ## Search Task Bar: 
 - The search task bar allows users to quickly locate specific tasks within their to-do list. This feature is especially useful for users with a large number of tasks, enabling them to find and focus on what matters most without having to scroll through endless lists.
   
![Screenshot 2024-08-13 at 19 56 52](https://github.com/user-attachments/assets/8ef12ed6-a3eb-4496-8f38-805bc1873671)

## Footer with Social Links: 
- The footer includes links to social media platforms, allowing users to connect with the app’s community or share their productivity achievements.
  
![Screenshot 2024-08-13 at 19 56 31](https://github.com/user-attachments/assets/f29d5d84-a2e6-4869-9e5e-e8bf46c36c6c)

## Login Page: 
- The login page ensures that users’ task data is secure and accessible only to them. By logging in, users can personalize their experience and keep their tasks organized across different devices, maintaining productivity wherever they go.
  
![Screenshot 2024-08-13 at 19 57 12](https://github.com/user-attachments/assets/a91f56de-132a-43b5-bd5b-d3a51609110f)

## Register Page: 
- The register page invites new users to create an account, giving them access to all of To-Do-It’s features. This is the entrance to a more organized life, allowing users to start managing their tasks and priorities in a structured way.
  
![Screenshot 2024-08-13 at 19 57 23](https://github.com/user-attachments/assets/52615ac9-f25e-42ef-8ec9-0380f521bfd2)

## Add To-Do: 
- The core feature of To-Do-It is the ability to add new tasks. Users can give each task a title and description, choose a category, and assign a priority level. This feature helps users to break down their goals into manageable steps, categorize them for clarity, and prioritize them to ensure the most important tasks get done first.
  
<img src="https://github.com/user-attachments/assets/23f7be7c-c260-4db5-b2da-8d0091f17ed4" alt="Screenshot 2024-08-13 at 19 58 45" width="400" height="auto">

<img src="https://github.com/user-attachments/assets/498f2378-9099-423c-8238-caacdebe029e" alt="Screenshot 2024-08-13 at 19 58 54" width="400" height="auto">

<img src="https://github.com/user-attachments/assets/5544c378-0f88-455b-a506-7a8a632e96c0" alt="Screenshot 2024-08-13 at 20 07 15" width="400" height="auto">

<img src="https://github.com/user-attachments/assets/62843580-8c16-466a-bc25-261efd5c0a72" alt="Screenshot 2024-08-13 at 20 07 24" width="400" height="auto">




### Future Features

- Profile Page with Profile Picture: A dedicated profile page will allow users to personalize their experience by adding a profile picture and updating their login details. This feature will enhance the user experience by making the app feel more tailored and secure, with the ability to easily manage personal information.

- Enhanced Login Page: The login process will be improved with a more comprehensive sign-in page that includes fields for email, first and last name, and an option to recover forgotten passwords. This added functionality will provide a more secure and user-friendly way for users to access their accounts, ensuring their data remains protected.

- Due Date for To-Dos: A date-to-complete feature will be added to tasks, allowing users to set deadlines for their to-dos. This will help users manage their time more effectively by not only organizing tasks by priority but also by when they need to be completed. This feature will be particularly useful for users who need to stay on track with deadlines and ensure timely completion of their tasks.
- 
## Technologies Used

- Frontend: HTML, CSS, BootStrap, Django
  
- Backend: Django, Python 

- Database: PostgreSQL
  
- Hosting: Github and Heroku

## User Experience Design 
- Our user experience design is centered around creating an intuitive and seamless interaction for our users. I believe that a well-crafted UX enhances user satisfaction.

- Consistency and Familiarity:
I focused on creating a consistent experience throughout the application. Common UI and familiar design elements are used to make the app easy to naviagte.

- Accessibility:
Ensuring my application is accessible to all users is a top priority. I adhered to the Web Content Accessibility Guidelines (WCAG) to provide an inclusive experience, including support for screen readers and sufficient color contrast.

- Responsive Design:
My application is designed to be fully responsive, offering a smooth and optimized experience across different devices and screen sizes. Whether accessed on a mobile phone, tablet, or desktop, the application adjusts seamlessly to the user’s environment.

- Usability Testing
Usability testing played a crucial role in refining the user experience. I conducted multiple rounds of testing with users to identify issues and gain insights. Feedback from these sessions was used to make informed design decisions, resulting in a more user-friendly application.

-User Stories
To ensure my design is closely aligned with user needs, I developed user stories that capture the motivations of my target audience. These user stories serve as the foundation for our design and development processes, providing clear and actionable insights into what users need to accomplish with our application.

![Screenshot 2024-08-14 at 01 46 19](https://github.com/user-attachments/assets/9581d2df-ee46-4e44-9231-349206ef88d4)


Example User Story:
As a user, I can select a category for my task so that I can visualize what kind of task it is.
Each user story is written in a format that highlights the user’s perspective, ensuring that every feature and design decision is focused on delivering value to the end-user.

## MoSCoW Prioritization
To effectively manage and prioritize the features and tasks during the design and development process, we employed the MoSCoW prioritization method. This helped us decide between essential and non-essential features.

Must-Haves (M):
These are the critical features that the application cannot function without. For example, the ability for users to create and manage tasks is a must-have feature.

Should-Haves (S):
Important features that should be included if possible, but the application can still function without them. An example might be the ability to sort tasks by custom categories.

Could-Haves (C):
Features that are desirable but not essential. These are typically included if time and resources permit. An example could be advanced filtering options for tasks.

Won’t-Haves (W):
Features that are agreed to be out of scope for the current iteration. These are often revisited in future updates. For example, creating a user profie where users can upload a profile picture.

This method ensured that I focused on delivering the most useful features first, while still keeping track of potential upgrades for later development.

![Screenshot 2024-08-14 at 01 44 01](https://github.com/user-attachments/assets/2ad34a45-90a9-449c-bf08-82ed848ffb9e)
![Screenshot 2024-08-14 at 01 44 12](https://github.com/user-attachments/assets/8eaf71d4-a0e0-4c04-9862-de5c6c5d7901)
![Screenshot 2024-08-14 at 01 44 19](https://github.com/user-attachments/assets/320130f4-feb4-4af8-b739-eedd8e241e66)
![Screenshot 2024-08-14 at 01 50 14](https://github.com/user-attachments/assets/1d1c2cde-42d0-4ff8-b555-1694bb484477)

## Agile
- My development process follows Agile methodologies to ensure flexibility, continuous improvement, and rapid delivery of features. By adopting Agile, I am able to respond quickly to changes, continuously iterate on the product, and maintain a focus on delivering value to my users.

- I work in short sprints to continuously develop and deliver new features.

  
- Throughout the development process, I gathered feedback from users. This feedback was used to make adjustments and improvements, ensuring the product evolved based on real user needs.

## Project Management with GitHub Projects
To manage my Agile process, I utilized GitHub Projects Kanban board. This tool helped me visualize and track the progress of my tasks and user stories throughout the development.

- Kanban Board
Our Kanban board is divided into columns such as To Do, In Progress, Done and Future Features. This structure allowed me to easily track the status of each task and prioritize work.
![Screenshot 2024-08-14 at 01 19 43](https://github.com/user-attachments/assets/48af7ebd-55e3-4fc6-bb4e-bc7774aafb52)

- User Stories and Tasks
User stories and tasks are shown as cards on the Kanban board. Each card includes a description and acceptance criteria. Cards are moved across the board as they progress through the development stages.

## Testing 

## Feature Testing
- To-Do-It has undergone comprehensive testing to ensure that all features work as intended and provide users with a smooth and effective experience:

- Navigation Bar: Thoroughly tested for functionality across all pages, ensuring that it correctly links to the home, login, and registration pages, and smoothly adapts to different screen sizes.

- Search Task Bar: Verified that the search functionality returns accurate results and performs well with both short and long task lists. Testing was done across various browsers to ensure consistency.

- Footer with Social Links: Checked to ensure that all social media links in the footer are operational and direct users to the correct destinations.

- Login Page: Both manual and automated tests were performed to ensure that the login process is smooth. Edge cases, such as incorrect passwords and empty fields, were tested to verify appropriate error handling.

- Register Page: Tested to ensure that new user registration works correctly, including validation of user inputs and successful account creation.

- Add To-Do: Verified that tasks can be added with a title, description, category, and priority. Ensured that the tasks are correctly displayed in the user’s task list and the data is accurately saved and retrieved.

-Cross-Browser and Cross-Device Compatibility
To-Do-It has been tested across multiple browsers, including Chrome, Firefox, Safari, and Edge, to ensure consistent performance and appearance. Additionally, the app has been tested on various screen sizes and devices, from desktops and laptops to tablets and smartphones, to confirm that the responsive design works as expected. Key considerations include:

- Responsive Layout: Ensured that all elements adjust correctly and maintain usability across different screen sizes.
-Browser Compatibility: Verified that all functionalities work seamlessly across different browsers, addressing any discrepancies in appearance or performance.

## Testing Methodology
- W3C Validation: Used the W3C HTML and CSS validation services to check for any syntax errors. All identified issues were corrected to ensure that the code is standards-compliant and error-free.
- I also ran my python through https://pep8ci.herokuapp.com/#. All issues were fixed to meet code standards and made sure they are error free.

<img src="https://github.com/user-attachments/assets/528b4468-a880-4647-a459-6004e43d9d2f" width="500" height="auto" alt="Testing Screenshot 1" />
<img src="https://github.com/user-attachments/assets/33964809-053a-4cfa-a129-53cf9e6786c4" width="500" height="auto" alt="Testing Screenshot 2" />

- Automated Tests: Implemented a automated test for the CustomLoginView, to ensure that login functionality is working as expected.

![Screenshot 2024-08-13 at 23 12 03](https://github.com/user-attachments/assets/4f64c8a2-550d-4992-b773-c0168650a087)

- Manual Testing: Conducted extensive manual testing by interacting with the site, exploring different user flows, and checking to ensure that all features are functioning correctly.

## Known Issues and Bugs

- Responsive Design Adjustment: Although the app is generally responsive, there are some edge cases where elements might display suboptimally on very small screens. Further adjustments will be made to improve the experience on all devices.
  
## Future Testing and Improvements

- Ongoing testing will continue to focus on resolving known issues. Future updates will include additional automated tests and further refinements to ensure the app remains robust and user-friendly.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)
  - Python
   - No errors were found when passing through (https://pep8ci.herokuapp.com/#) 

## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
- A new repository was created on github.
    
## Deployment to Heroku
### Create a Heroku Application:

- Log in to your Heroku account.
Click on the New button and select Create New App.
Enter a unique name for the app and choose the region closest to the user base.
Link the GitHub Repository to Heroku:

- In the Heroku dashboard for your app, go to the Deploy tab.
Choose GitHub as the deployment method.
Search for and connect your GitHub repository to Heroku.
Deploy the Application:

- Once the repository is linked, you can deploy the application by selecting the branch you want to deploy from and clicking Deploy Branch.
Heroku will build and deploy the application, and you will see logs indicating the deployment process.

### Verify Deployment:
- After deployment, Heroku provides a URL where your application is live.
Visit this URL to ensure that the application is running as expected.

The live link can be found here - https://to-do-it-project-5434f63ab691.herokuapp.com/login/?next=/

## Credits 

Robson Vinicius https://codepen.io/robsonvinicius/pen/bGpKQrw I used this source code for my footer icons adjusted to match my site style.



