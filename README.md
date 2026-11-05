# GitBrainLab static catalog

This repository is a static HTML and CSS catalog of GitBrainLab projects, published with GitHub Pages from `main`. The site at [gitbrain.com](https://gitbrain.com) is a separate Capsule vision page served by Cloudflare.

## Status

Checked 2026-11-05:

- DNS for `gitbrain.com` uses Cloudflare nameservers. The address records are Cloudflare (`104.21.14.33`, `172.67.157.174`), and the HTTPS response is `server: cloudflare`.
- The live page title is “Knowledge your AI can use, still yours to publish.” It describes Capsules, Campus, and a public MCP door. That HTML is not in this repository. A search of the public gitbrainlab repositories did not find it.
- The live page links to the [adopt kit](https://github.com/gitbrainlab/gitbrain-adopt), [app.gitbrain.com](https://app.gitbrain.com), and [mcp.gitbrain.com](https://mcp.gitbrain.com). The adopt-kit repo does not contain the vision page.
- `index.html` in this repo is the older catalog (“Open frameworks for collaborative development”). It still lists context, ChartSpec, ShelfSignals, CrowdCode, and happenstance. The live page does not.
- GitHub Pages for this repo still builds `main` at `/`. The root `CNAME` is `gitbrain.com`, so `https://gitbrainlab.github.io/` redirects there and visitors see the Cloudflare page. The latest recorded Pages build is commit `20dfb41` (2026-10-10).

Editing this repository does not change the Cloudflare page.

## What the catalog contains

A self-contained site: no build step, no external scripts, responsive layout, and a dark theme. JetBrains Mono is self-hosted under `assets/fonts/jetbrains-mono/` (SIL Open Font License).

| Page | Name in this repo | Repository |
| --- | --- | --- |
| [context](projects/context.html) | context | [gitbrainlab/context](https://github.com/gitbrainlab/context) |
| [ChartSpec](projects/chartspec.html) | ChartSpec | [gitbrainlab/ChartSpec](https://github.com/gitbrainlab/ChartSpec) |
| [ShelfSignals](projects/shelfsignals.html) | ShelfSignals | [gitbrainlab/ShelfSignals](https://github.com/gitbrainlab/ShelfSignals) |
| [CrowdCode](projects/crowdcode.html) | CrowdCode | [gitbrainlab/CrowdCode](https://github.com/gitbrainlab/CrowdCode) |
| [happenstance](projects/happenstance.html) | happenstance | [gitbrainlab/happenstance](https://github.com/gitbrainlab/happenstance) |

These pages and the [CrowdCode repository](https://github.com/gitbrainlab/CrowdCode) use the name CrowdCode. The label crowd.codes does not appear on these pages or on the live vision page. An ecosystem diagram is in [architecture.html](architecture.html). Short docs stubs are in `docs/`.

[CivicSpec](specs/civicspec/README.md) is also in this tree: an experimental contract for evidence-backed civic knowledge. Production adoption and assertion review are separate decisions.

## Preview locally

```bash
python -m http.server 8000
```

`npx serve` works as well. Open http://localhost:8000 to view this catalog.

Layout, new project pages, and diagram style: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).

## License

Project licenses live in their own repositories. CivicSpec records its status under `specs/civicspec/`.
