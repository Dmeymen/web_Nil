# Professional Portfolio Website

An elegant, professional portfolio website built with **Streamlit**, featuring a modern blue and gray aesthetic. Perfect for showcasing your projects, skills, and professional achievements.

## ✨ Features

- **Modern Design**: Blue and gray color scheme with smooth gradients and hover effects
- **Responsive Layout**: Adapts beautifully to different screen sizes
- **Professional Sections**:
  - Hero section with social links (LinkedIn, GitHub, Email, Twitter)
  - About me section
  - Skills showcase organized by category
  - Featured projects with technology tags
  - Contact information
- **Social Links**: Direct connections to LinkedIn, GitHub, Email, and Twitter
- **Elegant UI**: Smooth animations, card-based layout, professional typography

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Streamlit

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd web_Nil
   ```

2. **Install dependencies** (optional, Streamlit should already be installed):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run portfolio.py
   ```

4. Open your browser and navigate to `http://localhost:8501`

## 📝 Customization

To personalize the portfolio, edit `portfolio.py` and update the following sections:

### Personal Information
- **Name & Title**: Update the hero section heading and tagline
- **About**: Modify the "About Me" section text
- **Location & Education**: Update the info box in the About section

### Social Links
Replace placeholder links with your actual profiles:
```python
# Email, LinkedIn, GitHub, Twitter links
```

### Skills
Update the `skills_data` dictionary to reflect your actual skills:
```python
skills_data = {
    "Frontend": ["React", "HTML5", "CSS3", ...],
    "Backend": ["Python", "FastAPI", ...],
    ...
}
```

### Projects
Modify the `projects` list to showcase your actual projects:
```python
projects = [
    {
        "title": "Your Project Name",
        "description": "Project description",
        "technologies": ["Tech1", "Tech2", ...],
        "link": "https://github.com/yourproject"
    },
    ...
]
```

### Colors & Styling
The color scheme uses:
- **Primary Blue**: `#2a5298` - for headers, accents, and borders
- **Secondary Blue**: `#1e3c72` - for backgrounds and hover states
- **Light Gray**: `#f8f9fa`, `#e8f1f8` - for backgrounds
- **Text**: `#2c3e50` - for readable contrast

To change colors, update the CSS in the `st.markdown()` section at the top of the file.

## 📁 Project Structure

```
web_Nil/
├── portfolio.py           # Main Streamlit application
├── requirements.txt       # Python dependencies
└── .streamlit/
    └── config.toml       # Streamlit configuration
```

## 🎨 Design Features

- **Gradient Backgrounds**: Modern linear gradients for visual appeal
- **Card-Based Layout**: Clean, organized information sections
- **Smooth Animations**: Hover effects and transitions
- **Professional Typography**: Clear hierarchy with different font sizes
- **Responsive Grid**: Auto-adapting layout for different screen sizes
- **Shadow Effects**: Subtle depth and elevation

## 📞 Contact

Update the contact section with your actual contact details:
- Email address
- Phone number
- LinkedIn profile
- GitHub profile

## 🔧 Technical Stack

- **Frontend**: HTML5, CSS3 (via Streamlit)
- **Backend**: Python
- **Framework**: Streamlit
- **Styling**: Inline CSS with custom themes

## 📱 Browser Support

Works on all modern browsers:
- Chrome/Chromium
- Firefox
- Safari
- Edge

## 💡 Tips for Best Results

1. Keep your project descriptions concise and impactful
2. Use relevant technologies/tags for each project
3. Update your social links to be functional
4. Regularly refresh your featured projects section
5. Consider adding a professional photo in the hero section (modify CSS to include background image)

## 📄 License

Feel free to use and customize this portfolio template for your personal use.

## 🤝 Support

For any questions or customizations, edit the `portfolio.py` file directly. Streamlit's hot reload feature will automatically refresh your browser when you save changes.

---

**Made with ❤️ using Python and Streamlit**
