# Computational Genomics Lab Website

This is the official website for the Computational Genomics Lab. The website is built using simple HTML, CSS, and JavaScript, with content managed through Markdown files.

## Repository Structure

```
.
├── index.html          # Main webpage
├── css/               # Stylesheets
│   └── style.css
├── js/                # JavaScript files
│   └── main.js
├── content/           # Markdown content files
│   ├── home.md
│   └── ...
├── images/           # Image assets
├── .git/             # Git repository
│   └── hooks/        # Git hooks
│       └── pre-commit
├── scripts/          # Utility scripts
│   └── update_publications.py
├── .gitignore        # Git ignore rules
├── LICENSE.md        # License file
└── README.md         # Documentation
```

## Setup Instructions

1. Clone this repository
2. Set up git hooks:
   ```bash
   # Make the hooks directory if it doesn't exist
   mkdir -p .git/hooks
   # Copy the pre-commit hook template
   cp scripts/git-hooks/pre-commit.template .git/hooks/pre-commit
   # Make the hook executable
   chmod +x .git/hooks/pre-commit
   ```
3. Edit markdown files in the `content/` directory to update website content
4. Add images to the `images/` directory
5. Commit and push changes to GitHub

## Git Hooks

### Pre-commit Hook for Date Updates

The repository includes a pre-commit hook template that automatically updates the "Last updated" date in markdown files when they are committed.

The hook will automatically:
- Update the "Last updated" date in modified markdown files
- Format the date as "Month Year" (e.g., "March 2024")
- Add the date line if it doesn't exist
- Stage the changes automatically

## Publication Management

### Automatic Publication Updates

The `scripts/update_publications.py` script helps manage publication entries in markdown files.

Features:
- Automatically updates publication lists from BibTeX files
- Maintains consistent formatting across all publication entries
- Supports multiple publication types (journal articles, conference papers, etc.)

To use the publication script:

1. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python scripts/update_publications.py
   ```

3. The script will:
   - Read publication data from BibTeX files
   - Update markdown files in the content directory
   - Maintain consistent formatting
   - Handle different publication types

## Local Development

To test the website locally:

1. Install a local web server (e.g., Python's `http.server`):
   ```bash
   python -m http.server 8000
   ```
2. Open your browser and navigate to `http://localhost:8000`

## GitHub Pages Setup

1. Go to your repository's Settings
2. Navigate to "Pages" in the sidebar
3. Under "Source", select "main" branch
4. Click "Save"

Your website will be available at `https://[username].github.io/[repository-name]`

## Content Management

- All content is written in Markdown format
- Content files are located in the `content/` directory
- Images should be placed in the `images/` directory
- The website automatically renders Markdown content

## Contributing

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Content Organization

### Directory Structure

Each content section (news, people, projects, publications) follows a consistent structure:

1. `index.md` - Main listing page for the section
2. Individual content files - One file per item

### Adding New Content

#### News Items
1. Create a new file in `content/news/` with format: `YYYY-MM-DD-title.md`
2. Add a link to the news item in `content/news/index.md`
3. Include date, title, and content in the new file

#### Lab Members
1. Create a new file in `content/people/` with format: `name.md`
2. Add a link to the member in `content/people/index.md`
3. Include member information, research interests, and publications
4. Add member photo:
   - Store photo in `images/people/` directory
   - Use format: `name.jpg` or `name.png`
   - Recommended size: 400x400 pixels
   - Photos should be professional headshots

#### Projects
1. Create a new file in `content/projects/` with format: `project-name.md`
2. Add a link to the project in `content/projects/index.md`
3. Include project title, description, team members, and status
4. Add project images if available:
   - Store images in `images/projects/` directory
   - Use descriptive filenames
   - Optimize images for web display

---
*Last updated: Maaliskuu 2025*