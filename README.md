# GitBrain Landing Page

This repository hosts the static landing page for GitBrain at [gitbrain.com](https://gitbrain.com).

## What is this?

A clean, accessible, static website that:
- Explains what GitBrain is and its core principles
- Showcases GitBrainLab projects with links to repositories
- Describes how the projects fit together as a cohesive ecosystem
- Works well on mobile devices and follows accessibility best practices

## Technology

- **Pure HTML + CSS** – No build step required
- **No external dependencies** – Self-contained, no CDNs
- **Mobile-responsive** – Works on all screen sizes
- **Accessible** – Skip links, semantic HTML, high contrast, keyboard navigation
- **Dark mode** – Respects `prefers-color-scheme`

## Preview Locally

Since this is a static site, you can preview it with any local web server:

### Using Python 3:
```bash
python -m http.server 8000
```

### Using Python 2:
```bash
python -m SimpleHTTPServer 8000
```

### Using Node.js (if you have npx):
```bash
npx serve
```

Then open http://localhost:8000 in your browser.

## Editing Content

All content is in static HTML files:

- **`index.html`** – Main landing page with all sections
- **`styles/main.css`** – All styles including responsive and dark mode
- **`assets/`** – Logo, favicon, and social card images
- **`404.html`** – Custom error page

### To update projects:

Edit the `<section id="projects">` in `index.html`. Each project is a `<article class="project-card">` with:
- Project name in `<h3>`
- Description in `<p>`
- GitHub link in `<a class="project-link">`

### To update principles:

Edit the `<section class="principles">` in `index.html`. Each principle is a `<li>` with `<strong>` for the title and `<span>` for the description.

## Deployment

This site is deployed using **GitHub Pages**.

### Configuration:

1. Go to **Settings → Pages** in the GitHub repository
2. Set **Source** to: Deploy from a branch
3. Select **Branch**: `main` 
4. Select **Folder**: `/ (root)`
5. Click **Save**

The `CNAME` file in the root configures the custom domain `gitbrain.com`.

### DNS Setup (for reference):

The DNS records for `gitbrain.com` should point to GitHub Pages:
- A records pointing to GitHub Pages IPs (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153)
- Or a CNAME record pointing to `gitbrainlab.github.io`

Note: DNS changes are handled outside this repository.

## File Structure

```
.
├── index.html          # Main landing page
├── 404.html            # Error page
├── CNAME               # Custom domain configuration
├── robots.txt          # Search engine directives
├── sitemap.xml         # Site map for SEO
├── README.md           # This file
├── styles/
│   └── main.css        # All styles
└── assets/
    ├── logo.svg        # GitBrain logo
    ├── favicon.svg     # Site favicon
    └── social-card.svg # Open Graph/Twitter card image
```

## License

See individual project repositories for their respective licenses.