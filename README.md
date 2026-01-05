# GitBrain Landing Page

This repository hosts the static landing page for GitBrain at [gitbrain.com](https://gitbrain.com).

## What is this?

A clean, accessible, static website that:
- Explains what GitBrain is and its core principles
- Showcases GitBrainLab projects with links to repositories and documentation
- Describes how the projects fit together as a cohesive ecosystem
- Provides detailed project pages with architecture diagrams and use cases
- Works well on mobile devices and follows accessibility best practices

## Technology

- **Pure HTML + CSS** – No build step required
- **No external dependencies** – Self-contained, no CDNs
- **Typography** – Uses JetBrains Mono (self-hosted) for labels/module titles; font files included under `assets/fonts/jetbrains-mono/` with OFL license
- **Mobile-responsive** – Works on all screen sizes with responsive diagrams
- **Accessible** – Skip links, semantic HTML, high contrast, keyboard navigation, ARIA labels
- **Dark mode** – Premium dark theme by default

## File Structure

```
.
├── index.html              # Main landing page
├── architecture.html       # Integrated ecosystem architecture
├── 404.html                # Error page
├── CNAME                   # Custom domain configuration
├── robots.txt              # Search engine directives
├── sitemap.xml             # Site map for SEO
├── README.md               # This file
├── projects/               # Individual project detail pages
│   ├── context.html
│   ├── chartspec.html
│   ├── shelfsignals.html
│   ├── crowdcode.html
│   └── happenstance.html
├── docs/                   # Documentation hub
│   ├── index.html
│   ├── context.html
│   ├── chartspec.html
│   ├── shelfsignals.html
│   ├── crowdcode.html
│   └── happenstance.html
├── styles/
│   └── main.css            # All styles including responsive diagrams
└── assets/
    ├── logo.svg            # GitBrain logo
    ├── favicon.svg         # Site favicon
    ├── social-card.svg     # Open Graph/Twitter card image
    └── fonts/
        └── jetbrains-mono/  # Self-hosted JetBrains Mono font
            ├── JetBrainsMono-Regular.woff2
            ├── JetBrainsMono-SemiBold.woff2
            └── OFL.txt      # Font license (SIL Open Font License)
```

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

## Adding a New Project

To add a new project to the GitBrain ecosystem:

### 1. Update index.html

Add a new bento tile in the `<section id="projects">`:

```html
<article class="bento-tile" data-size="medium">
    <div class="tile-header">
        <h3>ProjectName</h3>
        <div class="tile-meta">
            <span class="meta-item">Type: Category</span>
            <span class="meta-item">Surface: Interface</span>
        </div>
    </div>
    <p class="tile-description">Short description of the project</p>
    <div class="tile-links">
        <a href="/projects/projectname.html" class="tile-link">Learn more →</a>
        <a href="/docs/projectname.html" class="tile-link">Docs →</a>
        <a href="https://github.com/gitbrainlab/ProjectName" class="tile-link" target="_blank" rel="noopener noreferrer">GitHub →</a>
    </div>
</article>
```

### 2. Create Project Detail Page

Create `/projects/projectname.html` using this template structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#0a0a0f">
    <title>ProjectName – GitBrain</title>
    <meta name="description" content="Project description">
    <link rel="canonical" href="https://gitbrain.com/projects/projectname.html">
    <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
    <link rel="stylesheet" href="/styles/main.css">
</head>
<body>
    <!-- Breadcrumb navigation -->
    <nav class="breadcrumb">
        <div class="container">
            <nav aria-label="Breadcrumb">
                <a href="/">Home</a>
                <span>→</span>
                <a href="/#projects">Projects</a>
                <span>→</span>
                <span aria-current="page">ProjectName</span>
            </nav>
        </div>
    </nav>

    <!-- Project header -->
    <header class="project-header">
        <div class="container">
            <h1 class="project-title">ProjectName</h1>
            <p class="project-tagline">One-line description</p>
            <div class="project-links">
                <a href="https://github.com/gitbrainlab/ProjectName" target="_blank" rel="noopener noreferrer">
                    <span>📦</span> View Repository
                </a>
                <a href="/docs/projectname.html">
                    <span>📚</span> Documentation
                </a>
            </div>
        </div>
    </header>

    <main id="main">
        <!-- At a Glance section -->
        <section class="project-section">
            <div class="container">
                <h2>At a Glance</h2>
                <dl class="project-attrs">
                    <div>
                        <dt>Why</dt>
                        <dd>Why this project exists / problem it solves</dd>
                    </div>
                    <div>
                        <dt>Benefit</dt>
                        <dd>Main benefit / value proposition</dd>
                    </div>
                    <div>
                        <dt>For</dt>
                        <dd>Target audience / who should use this</dd>
                    </div>
                    <div>
                        <dt>Use</dt>
                        <dd>How to use it at a high level</dd>
                    </div>
                </dl>
            </div>
        </section>

        <!-- Architecture section with diagrams -->
        <section class="project-section">
            <div class="container">
                <h2>Architecture</h2>
                
                <h3>Context Diagram</h3>
                <p>How the project interacts with external systems:</p>
                <pre class="diagram" aria-label="Context diagram for ProjectName">
┌─────────────────────┐
│       Users         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    ProjectName      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  External Systems   │
└─────────────────────┘
</pre>

                <h3>Internal Architecture</h3>
                <p>Key modules inside the project:</p>
                <pre class="diagram" aria-label="Internal architecture of ProjectName">
┌─────────────────────────────┐
│     ProjectName Core        │
├─────────────────────────────┤
│  ┌────────────────────┐     │
│  │   Component A      │     │
│  └─────────┬──────────┘     │
│            ▼                │
│  ┌────────────────────┐     │
│  │   Component B      │     │
│  └────────────────────┘     │
└─────────────────────────────┘
</pre>
            </div>
        </section>

        <!-- How to Use section -->
        <section class="project-section">
            <div class="container">
                <h2>How to Use</h2>
                <ol class="step-list">
                    <li>
                        <strong>Step 1 title</strong>
                        <span>Step 1 description</span>
                    </li>
                    <li>
                        <strong>Step 2 title</strong>
                        <span>Step 2 description</span>
                    </li>
                    <!-- Add 3-6 steps total -->
                </ol>
            </div>
        </section>

        <!-- Related Projects section -->
        <section class="project-section">
            <div class="container">
                <h2>Related Projects</h2>
                <div class="related-projects">
                    <a href="/projects/otherproject.html" class="related-project-card">
                        <h3>OtherProject</h3>
                        <p>How it relates to this project</p>
                    </a>
                    <a href="/architecture.html" class="related-project-card">
                        <h3>View Ecosystem</h3>
                        <p>See how this fits into the broader GitBrain architecture</p>
                    </a>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <nav class="footer-nav">
                <a href="/">Home</a>
                <a href="/#projects">Projects</a>
                <a href="/architecture.html">Architecture</a>
                <a href="https://github.com/gitbrainlab" target="_blank" rel="noopener noreferrer">GitHub</a>
            </nav>
            <p class="footer-copyright">© 2024 GitBrain. Open source projects.</p>
        </div>
    </footer>
</body>
</html>
```

### 3. Create Documentation Stub

Create `/docs/projectname.html` with getting started guide structure (see existing docs for template).

### 4. Update Ecosystem Architecture

Add the new project to `/architecture.html` in the integrated diagram and project links section.

### 5. Update Sitemap

Add entries to `sitemap.xml`:

```xml
<url>
    <loc>https://gitbrain.com/projects/projectname.html</loc>
    <lastmod>YYYY-MM-DD</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
</url>
<url>
    <loc>https://gitbrain.com/docs/projectname.html</loc>
    <lastmod>YYYY-MM-DD</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
</url>
```

## Diagram Style Guidelines

All architecture diagrams use ASCII box-drawing characters for consistency:

### Rules:
- Use box-drawing characters: `┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴ ┼`
- Arrows: `→ ←` or `▶ ▼ ▲ ◀`
- Keep diagrams under 75 characters wide for mobile readability
- Use `<pre class="diagram" aria-label="Description">` wrapper
- Include descriptive aria-label for accessibility
- Diagrams automatically scroll horizontally on narrow screens

### Example Context Diagram:
```
┌─────────────────────┐
│       Users         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Your Project     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Dependencies       │
└─────────────────────┘
```

### Example Internal Architecture:
```
┌─────────────────────────────────┐
│     Project Core                │
├─────────────────────────────────┤
│  ┌────────────────────┐         │
│  │   Module A         │         │
│  └─────────┬──────────┘         │
│            ▼                    │
│  ┌────────────────────┐         │
│  │   Module B         │         │
│  └────────────────────┘         │
└─────────────────────────────────┘
```

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

## License

See individual project repositories for their respective licenses.