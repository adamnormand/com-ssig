# com-ssig — Réseau incendie de La Côte-de-Gaspé

Static site (French only) replacing the WordPress site at **incendiegaspe.com**, plus basic pages for **Cloridorme**, **Grande-Vallée** and **Murdochville**. Plain HTML + one shared stylesheet. No build step required to publish. Migrated 2026-10-10.

## What's in the repo

| Path | Content |
|---|---|
| `index.html` | Gaspé home (SSI Gaspé) |
| `service/` | Service incendie: overview, direction, dispatch protocol |
| `service/caserne-45/` … `caserne-52/` | 7 fire-station pages (coordinates, team, units, zone) |
| `service/recrutement/` | Recruitment (online form replaced by mailto) |
| `association/` | Association des pompiers volontaires (social side): history, activities, awards, Amis des pompiers, In memoriam, board |
| `regroupement/` | Regroupement des pompiers volontaires du Grand Gaspé (union side): documents, governance, contact; links to the HubSpot member portal |
| `outils/` | Boîte à outils: burning permits + full Règlement 627-96, SOPFEU/Ville restrictions, forest-fire risk, flood stations (York 020404, Dartmouth 020602) |
| `prevention/` | Prevention now handled by the MRC de La Côte-de-Gaspé (Guillaume Pelchat) + 2020-04-16 prevention tips article |
| `coordonnees/` | All contacts (SSI, MRC prevention, casernes, organizations) |
| `cloridorme/`, `grande-vallee/`, `murdochville/` | Basic municipal pages: 911, prevention (MRC), burning/SOPFEU |
| `caserne45/`, `interactif/…`, `ssi/recrutement/`, `contact/`, `legal/`, etc. | Redirect stubs from old WordPress URLs |
| `wp-content/uploads/*.pdf` | The 5 PDFs kept at their **original URLs** (the HubSpot portal and past emails link there) |
| `assets/style.css`, `assets/img/` | Stylesheet and 37 images (photos recompressed, max 1600 px) |
| `404.html`, `CNAME`, `.nojekyll`, `robots.txt`, `sitemap.xml`, favicons | Pages plumbing |
| `tools/build.py` | Generator for all HTML pages. Edit content here, run `python3 tools/build.py`, commit. |

The **network bar** at the top of every page (modelled on the "Réseau" bar at ceegim.com) switches between Gaspé, Cloridorme, Grande-Vallée and Murdochville. Links are relative paths, so they work on the github.io preview, on incendiegaspe.com, and through the three forwarded domains.

## Publish on GitHub Pages

1. Push these files to the root of `main` in the `com-ssig` repo.
2. Repo **Settings → Pages**: Source = *Deploy from a branch*, Branch = `main`, folder `/ (root)`.
3. Custom domain: `incendiegaspe.com` (already in `CNAME`). Wait for the DNS check, then tick **Enforce HTTPS**.

## DNS (Squarespace) — Pages first, DNS second

**incendiegaspe.com** (change only these records):

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | `<github-user>.github.io` |

Do **not** touch MX, TXT (SPF/DKIM/DMARC/verification), SRV, or the **`regroupement`** CNAME (HubSpot member portal stays live).

**The other three domains.** GitHub Pages allows one custom domain per repo. Recommended: use Squarespace **domain forwarding (301, with path)**:

- incendiecloridorme.com → `https://incendiegaspe.com/cloridorme/`
- incendiegrandevallee.com → `https://incendiegaspe.com/grande-vallee/`
- incendiemurdochville.com → `https://incendiegaspe.com/murdochville/`

Alternative if each must show its own domain in the address bar: three tiny repos, each with its own `CNAME`, holding a copy of that municipality page.

## Corrections made vs. the WordPress site

- Wrong links fixed: "Membres" tile and RSS pointed to uwindsorgss.ca; footer `/legal` was a 404; online recruitment form replaced by email.
- Casernes made consistent: 45 = Saint-Maurice, 46 = Rivière-au-Renard (home page had them swapped); territory is L'Anse-à-Valleau to **Fort-Prével** (home said Bougainville).
- Caserne emails corrected (47, 49, 50 pointed to caserne45/46).
- Address typo "14»8" → 148, boul. de Gaspé. Caserne 48 phone 360-4122 → 360-4012.
- Rosebridge team photo removed from Caserne 48 (kept on 52).
- Outdated content removed: COVID 2021 notice; `prevention@incendiegaspe.com` (prevention now MRC).
- Spelling/grammar fixed throughout (environs, includent, éparpillés, exigeances, propogation, Par fois, le zone, Annéee, Merites, Socitété, premis, rénumération, effecuter, lévés, charactère, Réussit, acceuil, DÉGÉGUÉ, Regroupements…).
- Regroupement document list: dead/mismatched links removed (see below), dates normalized YYYY-MM-DD.

## To confirm (open items)

1. ~~MRC prevention contact~~ — done 2026-10-10: Guillaume Pelchat, Coordonnateur en sécurité incendie, guillaume.pelchat@cotedegaspe.ca, 418 368-7000 poste 230 (cell number deliberately not published).
2. **Direction du Service** — sources conflict: Marc Grenier (Coordonnées), Éric Fugère (Recrutement/"par intérim"), Carl Sinnett (Organigramme août 2024, intérimaire). The site names no director; contact is `ssi@ville.gaspe.qc.ca`.
3. **Chiefs** — C45: Serge Minville (caserne page) vs Éric Fugère (Coordonnées); C48: Mitchell Legresley (site) vs Carl Sinnett (organigramme). Site uses the caserne pages.
4. **Business hours** — 9 h–16 h 30 (header) vs 9 h–16 h (footer). Site uses 16 h 30.
5. **Regroupement documents not online** — Règlement n° 2 (link pointed to n° 1), Entente 2023–2029 (pointed to 2016–2022 PDF), Salaires 2025 (pointed to 2024 PDF). Listed as "Document à venir". Upload them and add links.
6. **Burning permits** — still issued by SSI Gaspé (Règl. 627-96), or moved to the MRC with prevention?
7. **Municipal pages** — add each fire service's chief, station address and phone, and official municipality sites for Cloridorme and Grande-Vallée (only murdochville.com was confirmed).
8. **Petite-Vallée** is also in the MRC de La Côte-de-Gaspé but not in the network bar — add or leave out?
9. **Association** — presidents list ends at François Charbonneau while the board lists Bruno Lévesque as president; "Ami des pompiers" photos for Légion 59 and Bernard Clements were the **same file** on the old site (kept on Légion only); In memoriam "Gérard" caption was truncated on the old site; spelling Marie-Michèle vs Marie-Michelle Quirion; awards tables end at 2019.
10. **Louis-Philippe Laurin** was shown with eric.paquette@ email — not republished.
11. **Public union documents** — salary scale, work agreement and insurance brochures remain public, as before. Confirm that's intended.
12. Social links kept: Facebook, Instagram (Twitter/YouTube/RSS dropped).
