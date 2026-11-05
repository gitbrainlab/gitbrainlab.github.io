# Contributing to the static catalog

This guide is for the HTML catalog in this repository (project pages, `architecture.html`, and the docs stubs). The public site at [gitbrain.com](https://gitbrain.com) is a Capsule vision page served by Cloudflare. Changes here update the files in git, and a local preview. They do not update that vision page.

The short public note is [README.md](../README.md).

## File structure

```
.
├── index.html              # Catalog home
├── architecture.html       # Integrated ecosystem architecture
├── 404.html                # Error page
├── CNAME                   # Still set to gitbrain.com; see "Pages and DNS" below
├── robots.txt              # Search engine directives for this tree
├── sitemap.xml             # Catalog URLs
├── README.md               # Public note for this repository
├── projects/               # Individual project detail pages
│   ├── context.html
│   ├── chartspec.html
│   ├── shelfsignals.html
│   ├── crowdcode.html
│   └── happenstance.html
├── docs/                   # Docs stubs (HTML) plus this guide
│   ├── index.html
│   ├── context.html
│   ├── chartspec.html
│   ├── shelfsignals.html
│   ├── crowdcode.html
│   ├── happenstance.html
│   └── CONTRIBUTING.md
├── styles/
│   └── main.css            # All styles including responsive diagrams
├── assets/
│   ├── logo.svg            # GitBrain logo
│   ├── favicon.svg         # Site favicon
│   ├── social-card.svg     # Open Graph/Twitter card image
│   └── fonts/
│       └── jetbrains-mono/  # Self-hosted JetBrains Mono font
│           ├── JetBrainsMono-Regular.woff2
│           ├── JetBrainsMono-SemiBold.woff2
│           └── OFL.txt      # Font license (SIL Open Font License)
└── specs/civicspec/        # CivicSpec (separate from the project pages)
```

Project pages use the name CrowdCode, matching `projects/crowdcode.html` and the `gitbrainlab/CrowdCode` repository.

## Adding a new project

To add a project page to this catalog:

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

### 2. Create the project detail page

Create `/projects/projectname.html` using this structure. The `canonical` links below are paths from the older catalog. They are not routes on the current Cloudflare vision page.

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

### 3. Create a documentation stub

Create `/docs/projectname.html` with a getting-started structure (see the existing HTML stubs).

### 4. Update the ecosystem architecture

Add the project to `/architecture.html` in the integrated diagram and the project links section.

### 5. Update the sitemap

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

Those `loc` values match the older catalog sitemap. They are not URLs on the current vision page.

## Diagram style

Architecture diagrams use ASCII box-drawing characters.

### Rules

- Use box-drawing characters: `┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴ ┼`
- Arrows: `→ ←` or `▶ ▼ ▲ ◀`
- Keep diagrams under 75 characters wide for mobile readability
- Use `<pre class="diagram" aria-label="Description">` wrapper
- Include a descriptive aria-label
- Diagrams scroll horizontally on narrow screens

### Example context diagram

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

### Example internal architecture

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

## Pages and DNS

GitHub Pages publishes this repository from branch `main`, folder `/`. The `CNAME` file still contains `gitbrain.com`, which makes `gitbrainlab.github.io` redirect to that host.

Public DNS for `gitbrain.com` points at Cloudflare and serves the Capsule vision page. Leave the live domain on that setup. Preview the catalog locally, or read the files in this repository, to see the project pages.
