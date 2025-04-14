import bibtexparser
import os
from datetime import datetime

def create_publication_page(entry, output_dir):
    """Create a markdown page for a single publication."""
    # Create a filename from the key
    filename = f"{entry['ID']}.md"
    filepath = os.path.join(output_dir, filename)

    # Format authors
    authors = entry.get('author', '').replace(' and ', ', ')

    # Get URL if it exists
    url = entry.get('url', '')
    url_section = f"\n## URL\n[{url}]({url})" if url else ""

    # Create markdown content
    content = f"""# {entry['title']}

## Authors
{authors}

## Journal
*{entry.get('journal', '')}* {entry.get('volume', '')}({entry.get('number', '')}): {entry.get('pages', '')}

## Year
{entry.get('year', '')}

## DOI
[{entry.get('doi', '')}](https://doi.org/{entry.get('doi', '')})
{url_section}

## Publisher
{entry.get('publisher', '')}

[Back to Publications](/publications)
"""

    # Write to file
    with open(filepath, 'w') as f:
        f.write(content)

    return filename

def generate_publications():
    """Generate publication index from BibTeX file."""
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct paths relative to script location
    bib_file = os.path.join(script_dir, '..', 'content', 'publications', 'publications.bib')
    output_dir = os.path.join(script_dir, '..', 'content', 'publications')

    # Read BibTeX file
    with open(bib_file, 'r') as f:
        bib_database = bibtexparser.load(f)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Group publications by year
    publications_by_year = {}
    for entry in bib_database.entries:
        year = entry.get('year', '')
        if year not in publications_by_year:
            publications_by_year[year] = []
        publications_by_year[year].append(entry)

    # Generate index.md
    index_content = "# Publications\n\n"

    # Sort years in descending order
    for year in sorted(publications_by_year.keys(), reverse=True):
        index_content += f"## {year}\n\n"
        for entry in publications_by_year[year]:
            # Format authors
            authors = entry.get('author', '').replace(' and ', ', ')

            # Create detailed citation
            title = entry.get('title', '')
            journal = entry.get('journal', '')
            volume = entry.get('volume', '')
            number = entry.get('number', '')
            pages = entry.get('pages', '')
            doi = entry.get('doi', '')
            url = entry.get('url', '')
            publisher = entry.get('publisher', '')

            # Add publication details
            index_content += f"### {title}\n\n"
            index_content += f"**Authors**: {authors}\n\n"
            if len(number) > 0 and len(pages) > 0:
                  index_content += f"**Journal**: *{journal}* {volume}({number}): {pages}\n\n"
            else:
                  index_content += f"**Journal**: *{journal}* {volume}\n\n"
            
            # Add DOI and URL if they exist
            if doi:
                index_content += f"**DOI**: [{doi}](https://doi.org/{doi})\n\n"
            if url:
                index_content += f"**URL**: [{url}]({url})\n\n"
            
            index_content += f"**Publisher**: {publisher}\n\n"
            index_content += "---\n\n"  # Add separator between publications

        index_content += "\n"

    # Write index.md
    with open(os.path.join(output_dir, 'index.md'), 'w') as f:
        f.write(index_content)

if __name__ == '__main__':
    generate_publications()
