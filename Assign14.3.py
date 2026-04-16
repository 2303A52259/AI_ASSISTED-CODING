<!---"""Create a semantic HTML5 structure for a personal portfolio website.

Requirements:
- Use proper semantic tags like <header>, <nav>, <section>, <article>, <footer>.
- Include the following sections:
  1. Home (with name and a short tagline)
  2. About (bio and list of technical skills)
  3. Projects (at least 3 project cards with title, description, and link placeholders)
  4. Contact (email, phone, and social media links)

- Add a navigation bar with anchor links to each section.
- Use meaningful class names for styling.
- Include a footer with copyright text.
- Ensure the structure is clean and well-indented.
- Do NOT include CSS, only HTML.

Output:
- Provide complete HTML code with comments explaining each section."""-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Portfolio</title>
</head><body>
    <!-- Header section with name and tagline -->
    <header>
        <h1>John Doe</h1>
        <p>Full Stack Developer | Tech Enthusiast</p>
    </header>
    <!-- Navigation bar with anchor links to each section -->
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    <!-- Home section -->
    <section id="home">
        <h2>Welcome to My Portfolio</h2>
        <p>Discover my work and experience in the world of technology.</p>
    </section>
    <!-- About section with bio and technical skills -->    
    <section id="about">
        <h2>About Me</h2>
        <p>I am a passionate full stack developer with over 5 years of experience in building web applications. I specialize in JavaScript, Python, and cloud technologies.</p>
        <h3>Technical Skills</h3>
        <ul>
            <li>JavaScript (React, Node.js)</li>
            <li>Python (Django, Flask)</li>
            <li>Cloud (AWS, Azure)</li>
            <li>Databases (MySQL, MongoDB)</li>
        </ul>
    </section>
    <!-- Projects section with project cards -->
    <section id="projects">
        <h2>Projects</h2>
        <article class="project-card">
            <h3>Project One</h3>
            <p>A web application that allows users to track their fitness goals.</p>
            <a href="#">View Project</a>
        </article>
        <article class="project-card">
            <h3>Project Two</h3>
            <p>An e-commerce platform built with React and Node.js.</p>
            <a href="#">View Project</a>
        </article>
        <article class="project-card">
            <h3>Project Three</h3>
            <p>A machine learning model for predicting stock prices.</p>
            <a href="#">View Project</a>
        </article>
    </section>
    <!-- Contact section with email, phone, and social media links -->
    <section id="contact">
        <h2>Contact Me</h2>
        <p>Email: <a href="mailto:john.doe@example.com">john.doe@example.com</a></p>
        <p>Phone: (123) 456-7890</p>
        <p>Follow me on social media:</p>
        <ul>
            <li><a href="https://twitter.com/johndoe" target="_blank">Twitter</a></li>
            <li><a href="https://linkedin.com/in/johndoe" target="_blank">LinkedIn</a></li>
            <li><a href="https://github.com/johndoe" target="_blank">GitHub</a></li>
        </ul>
    </section>
    <!-- Footer with copyright text -->
    <footer>
        <p>&copy; 2023 John Doe. All rights reserved.</p>
    </footer>
</body>
</html>