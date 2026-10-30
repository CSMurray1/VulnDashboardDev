# Unified Vulnerability Platform

This GitHub Pages site combines three tools behind one Advisory Lens–styled switcher:

1. **Advisory Analysis** — the current `CSMurray-CISA/AdvisoryAnalysis` site, unchanged.
2. **Vulnerability Dashboard** — the original standalone `CSMurray1/VulnDashboard` `index.html`, unchanged.
3. **SSVC Scoring** — the multi-vendor SSVC dashboard from `CSMurray-CISA/ssvc`.

Each tool runs in its own same-site frame. This keeps its HTML, styles, scripts, state, file uploads, filters, and exports isolated from the other tools. The Vulnerability Dashboard therefore retains the behavior of the original standalone version instead of the altered version from the combined SSVC repository.

## Publish with GitHub Pages

Copy the complete contents of this folder into the root of the GitHub repository you want to publish. Keep all folders, including `.github`, `oracle-data`, and `vendor-data`.

Then open **Settings → Pages**, choose **Deploy from a branch**, select the branch and the root (`/`) folder, and save. There is no website build step.

The site opens to Advisory Analysis. The floating switcher changes between tools without resetting work already performed in another tool. Each tool also has a direct URL:

- `advisory-analysis.html`
- `vulnerability-dashboard.html`
- `ssvc-dashboard.html`

## SSVC vendor-data refresh

The included GitHub Actions workflow retains the SSVC repository's daily vendor-data refresh. After copying the site to a new repository, open **Actions → Refresh CISA SSVC Platform vendor data → Run workflow** once to confirm that Actions have write permission and the parsers can refresh the tracked data.

The entire `oracle-data/` and `vendor-data/` directories must remain in the repository. The SSVC dashboard reads those JSON files directly from GitHub Pages.

## Source mapping

- `index.html`: new unified platform switcher
- `advisory-analysis.html`, `app.js`, `styles.css`: AdvisoryAnalysis
- `vulnerability-dashboard.html`: original VulnDashboard standalone page
- `ssvc-dashboard.html`, `oracle-data/`, `vendor-data/`: SSVC dashboard and tracked data
- `scripts/`, `requirements.txt`, `.github/workflows/`: SSVC data-refresh automation
