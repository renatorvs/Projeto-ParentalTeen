# Copilot Instructions for Projeto Parentalteen

## Project Overview
This is a static website project composed primarily of HTML and CSS files, with a single JavaScript file (`mailchimp.js`). The site appears to be informational, with multiple pages for blog posts, benefits, education, and popups.

## Architecture & Structure
- **HTML Files**: Each page is a standalone HTML file (e.g., `index.html`, `blog.html`, `beneficios.html`). Blog posts are named as `titulo-do-post-*.html`.
- **CSS**: All styling is centralized in `styles.css`.
- **JavaScript**: Only `mailchimp.js` is present, likely handling newsletter or form integration.
- **No build system**: There are no build scripts, package managers, or test frameworks. All files are edited directly.

## Key Patterns & Conventions
- **Page Addition**: To add a new page, create a new `.html` file and link it in `index.html` or other navigation sections.
- **Styling**: All custom styles should go in `styles.css`. Inline styles are discouraged.
- **JavaScript Usage**: Place all scripts in `mailchimp.js`. Avoid adding new JS files unless necessary.
- **Naming**: Blog post files follow the pattern `titulo-do-post-N.html`.
- **Popup Integration**: `popup.html` is used for modal or popup content. Reference it from other pages as needed.

## Developer Workflow
- **Edit Directly**: Make changes directly to HTML, CSS, or JS files. No compilation or build steps required.
- **Preview**: Open HTML files in a browser to preview changes. No local server is required.
- **Debugging**: Use browser developer tools for inspecting layout, styles, and JS errors.

## Integration Points
- **Mailchimp**: `mailchimp.js` integrates with Mailchimp for newsletter signup. Update this file for changes to form handling or API integration.

## Examples
- To add a new blog post: Copy an existing `titulo-do-post-*.html` file, update the content, and link it in `index.html`.
- To update site-wide styles: Edit `styles.css`.
- To change newsletter logic: Edit `mailchimp.js`.

## Important Files
- `index.html`: Main landing page and navigation hub.
- `styles.css`: Central stylesheet for all pages.
- `mailchimp.js`: Handles newsletter signup logic.
- `popup.html`: Used for modal/popup content.

---

For questions or unclear patterns, review existing files for examples before introducing new conventions. If a workflow or integration is not documented here, it is likely not present in this project.
