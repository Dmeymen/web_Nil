import streamlit as st
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Professional Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for blue and gray aesthetic
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        color: #2c3e50;
    }
    
    .main {
        background-color: #f8f9fa;
    }
    
    .navbar {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .hero-section {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 4rem 2rem;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 3rem;
        box-shadow: 0 10px 30px rgba(30, 60, 114, 0.2);
    }
    
    .hero-section h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .hero-section p {
        font-size: 1.3rem;
        opacity: 0.95;
        margin-bottom: 1.5rem;
    }
    
    .social-links {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin-top: 2rem;
        flex-wrap: wrap;
    }
    
    .social-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.75rem 1.5rem;
        background-color: rgba(255,255,255,0.2);
        color: white;
        text-decoration: none;
        border-radius: 5px;
        transition: all 0.3s ease;
        border: 2px solid rgba(255,255,255,0.3);
        font-weight: 500;
    }
    
    .social-btn:hover {
        background-color: rgba(255,255,255,0.3);
        border-color: white;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .section-title {
        color: #1e3c72;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 3rem 0 2rem 0;
        padding-bottom: 1rem;
        border-bottom: 3px solid #2a5298;
        display: inline-block;
    }
    
    .project-card {
        background: white;
        border-radius: 10px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border-left: 5px solid #2a5298;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
        transform: translateY(-5px);
    }
    
    .project-card h3 {
        color: #1e3c72;
        margin-bottom: 0.5rem;
        font-size: 1.5rem;
    }
    
    .project-card .tags {
        margin-top: 1rem;
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .tag {
        background-color: #e8f1f8;
        color: #2a5298;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
    
    .skill-category {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        border-top: 4px solid #2a5298;
    }
    
    .skill-category h4 {
        color: #1e3c72;
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }
    
    .skill-item {
        background-color: #f0f4f8;
        padding: 0.5rem 0.8rem;
        margin-bottom: 0.5rem;
        border-radius: 4px;
        color: #2c3e50;
        font-size: 0.9rem;
    }
    
    .footer {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        text-align: center;
        padding: 2rem;
        margin-top: 4rem;
        border-radius: 10px;
    }
    
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #2a5298, transparent);
        margin: 2rem 0;
    }
    
    .contact-box {
        background: white;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border-left: 5px solid #2a5298;
        margin-top: 2rem;
    }
    
    .contact-box h3 {
        color: #1e3c72;
        margin-bottom: 1rem;
    }
    
    .contact-item {
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .contact-item strong {
        color: #1e3c72;
        min-width: 100px;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1>Professional Portfolio</h1>
    <p>Full Stack Developer | Problem Solver | Innovation Enthusiast</p>
    <div class="social-links">
        <a href="mailto:your.email@example.com" class="social-btn">📧 Email</a>
        <a href="https://linkedin.com/in/yourprofile" target="_blank" class="social-btn">💼 LinkedIn</a>
        <a href="https://github.com/yourprofile" target="_blank" class="social-btn">🐙 GitHub</a>
        <a href="https://twitter.com/yourprofile" target="_blank" class="social-btn">𝕏 Twitter</a>
    </div>
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    I'm a passionate developer with expertise in building elegant, scalable web applications. 
    With a strong foundation in full-stack development and a keen eye for design, I create 
    solutions that are both beautiful and functional.
    
    My approach combines technical excellence with user-centric design, ensuring every project 
    delivers measurable impact. I'm constantly learning and staying current with the latest 
    technologies to deliver cutting-edge solutions.
    """)

with col2:
    st.info("📍 **Location:** Your City, Country\n\n⏰ **Timezone:** UTC+1\n\n🎓 **Education:** Your University")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Skills Section
st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)

skills_data = {
    "Frontend": ["React", "HTML5", "CSS3", "JavaScript", "Tailwind CSS", "Streamlit"],
    "Backend": ["Python", "FastAPI", "Django", "SQL", "PostgreSQL", "MongoDB"],
    "Tools & Platforms": ["Git", "Docker", "AWS", "GitHub", "VS Code", "Figma"],
    "Soft Skills": ["Problem Solving", "Team Leadership", "Communication", "Project Management"]
}

cols = st.columns(2)
for idx, (category, items) in enumerate(skills_data.items()):
    with cols[idx % 2]:
        st.markdown(f"""
        <div class="skill-category">
            <h4>{category}</h4>
            {"".join([f'<div class="skill-item">✓ {item}</div>' for item in items])}
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Projects Section
st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "title": "E-Commerce Platform",
        "description": "Full-stack e-commerce solution with real-time inventory management and payment integration. Built with React, FastAPI, and PostgreSQL.",
        "technologies": ["React", "FastAPI", "PostgreSQL", "Stripe API"],
        "link": "#"
    },
    {
        "title": "Analytics Dashboard",
        "description": "Interactive data visualization dashboard providing real-time insights into business metrics. Features custom charts and automated reporting.",
        "technologies": ["Python", "Streamlit", "Pandas", "Plotly"],
        "link": "#"
    },
    {
        "title": "Task Management App",
        "description": "Collaborative task management application with real-time updates, team collaboration features, and project tracking capabilities.",
        "technologies": ["React", "Django", "WebSockets", "MongoDB"],
        "link": "#"
    },
    {
        "title": "AI Content Generator",
        "description": "Intelligent content generation tool leveraging machine learning for creating blog posts, social media content, and marketing copy.",
        "technologies": ["Python", "OpenAI API", "FastAPI", "React"],
        "link": "#"
    }
]

for project in projects:
    st.markdown(f"""
    <div class="project-card">
        <h3>{project['title']}</h3>
        <p>{project['description']}</p>
        <div class="tags">
            {"".join([f'<span class="tag">{tech}</span>' for tech in project['technologies']])}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<h2 class="section-title">Get In Touch</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="contact-box">
        <h3>Let's Connect</h3>
        <div class="contact-item">
            <strong>Email:</strong>
            <a href="mailto:your.email@example.com">your.email@example.com</a>
        </div>
        <div class="contact-item">
            <strong>LinkedIn:</strong>
            <a href="https://linkedin.com/in/yourprofile" target="_blank">linkedin.com/in/yourprofile</a>
        </div>
        <div class="contact-item">
            <strong>GitHub:</strong>
            <a href="https://github.com/yourprofile" target="_blank">github.com/yourprofile</a>
        </div>
        <div class="contact-item">
            <strong>Phone:</strong>
            <a href="tel:+1234567890">+1 (234) 567-890</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.success("💡 **Open to Opportunities**\n\nI'm always interested in new projects and collaboration opportunities!")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="footer">
    <p>© {datetime.now().year} Your Name. All rights reserved.</p>
    <p style="opacity: 0.8; margin-top: 0.5rem;">Crafted with ❤️ using Python and Streamlit</p>
</div>
""", unsafe_allow_html=True)
