// Configure marked options
marked.setOptions({
    breaks: true,
    gfm: true,
    headerIds: false,
    mangle: false,
    headerPrefix: '',
    xhtml: true,
    html: true  // Allow HTML in the source
});

// Get the base URL for GitHub Pages
const baseUrl = window.location.hostname === 'localhost' 
    ? '' 
    : '/chengl7-lab.github.io';  // Explicitly set repository name for GitHub Pages

// Function to load markdown content
async function loadMarkdownContent(section, page = 'index') {
    try {
        let path;
        if (section === 'home') {
            path = `${baseUrl}/content/home.md`;
        } else {
            path = `${baseUrl}/content/${section}/${page}.md`;
        }
            
        console.log('Loading content from:', path); // Debug log
        const response = await fetch(path);
        if (!response.ok) {
            console.error('Failed to load:', path, response.status); // Debug log
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const markdown = await response.text();
        return markdown;
    } catch (error) {
        console.error('Error loading markdown:', error);
        return `<p>Error loading content. Please try again later.</p>`;
    }
}

// Function to render markdown content
function renderMarkdown(markdown) {
    console.log('Raw markdown:', markdown); // Debug log
    const html = marked.parse(markdown);
    console.log('Converted HTML:', html); // Debug log
    return html;
}

// Function to update content section
async function updateContent(section, page = 'index') {
    const contentSection = document.getElementById('content');
    contentSection.innerHTML = '<div class="loading">Loading...</div>';
    
    const markdown = await loadMarkdownContent(section, page);
    const html = renderMarkdown(markdown);
    
    contentSection.innerHTML = `<div class="markdown-content">${html}</div>`;
}

// Handle navigation
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', async (e) => {
        e.preventDefault();
        const section = e.target.getAttribute('href').substring(1);
        await updateContent(section);
        
        // Update active state
        document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
        e.target.classList.add('active');
        
        // Smooth scroll to section
        document.getElementById(section).scrollIntoView({ behavior: 'smooth' });
    });
});

// Handle markdown links
document.addEventListener('click', async (e) => {
    if (e.target.tagName === 'A' && e.target.getAttribute('href').startsWith('/')) {
        e.preventDefault();
        const path = e.target.getAttribute('href').substring(1);
        const parts = path.split('/');
        if (parts.length === 2) {
            await updateContent(parts[0], parts[1]);
        } else {
            await updateContent(parts[0]);
        }
    }
});

// Load initial content
document.addEventListener('DOMContentLoaded', () => {
    updateContent('home');
}); 