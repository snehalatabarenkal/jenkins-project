from flask import Flask
app = Flask(__name__)

@app.route('/')
def portfolio():
    return '''
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    color: #333;
                }
                .header {
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }
                .container {
                    padding: 20px;
                }
                .about, .projects, .contact {
                    margin-bottom: 20px;
                }
                .project-item {
                    margin-bottom: 10px;
                    padding: 10px;
                    border: 1px solid #ddd;
                }
                .project-title {
                    font-weight: bold;
                    color: #4CAF50;
                }
                .footer {
                    background-color: #4CAF50;
                    color: white;
                    text-align: center;
                    padding: 10px;
                    position: fixed;
                    width: 100%;
                    bottom: 0;
                }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Anjali Kota</h1>
                <p>DevOps Engineer | Web Developer</p>
            </div>
            
            <div class="container">
                <div class="about">
                    <h2>About Me</h2>
                    <p>I am a DevOps engineer with a passion for cloud infrastructure, CI/CD, and automation. With a background in software development, I bring a unique perspective to building efficient and reliable systems.</p>
                </div>
                
                <div class="projects">
                    <h2>Projects</h2>
                    <div class="project-item">
                        <p class="project-title">Project 1: DevOps Pipeline</p>
                        <p>Created a Jenkins pipeline that integrates with SonarQube, OWASP Dependency Check, and Docker to automate the build and security scanning process.</p>
                    </div>
                    <div class="project-item">
                        <p class="project-title">Project 2: E-commerce Website</p>
                        <p>Developed a full-stack e-commerce platform using Flask, MySQL, and Docker, deployed on AWS.</p>
                    </div>
                </div>
                
                <div class="contact">
                    <h2>Contact</h2>
                    <p>Email: anjalikota161@gmail.com</p>
                    <p>LinkedIn: www.linkedin.com/in/anjalikota10</p>
                </div>
            </div>
            
            <div class="footer">
                <p>&copy; 2024 Anjali Kota</p>
            </div>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
