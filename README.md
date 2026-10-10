# com-ssig — Réseau incendie de La Côte-de-Gaspé

Static site (French only) at **incendiecotedegaspe.com**: a network landing page, the Gaspé section replacing the WordPress site at incendiegaspe.com, and basic pages for **Cloridorme**, **Grande-Vallée** and **Murdochville**. Plain HTML + one shared stylesheet. No build step required to publish. Migrated 2026-10-10.

## What's in the repo

Primary domain: **incendiecotedegaspe.com** (`CNAME`). The four municipal domains forward to their section.

| Path | Content |
|---|---|
| `index.html` | Network landing page: links to the 4 municipalities, MRC prevention contact, 9-1-1, SOPFEU |
| `gaspe/` | Gaspé home (SSI Gaspé) |
| `gaspe/service/`, `gaspe/service/caserne-45/` … `caserne-52/`, `gaspe/service/recrutement/` | Service incendie, 7 casernes, recruitment |
| `gaspe/association/` | Association des pompiers volontaires (social side) |
| `gaspe/regroupement/` | Regroupement des pompiers volontaires du Grand Gaspé (union side) |
| `gaspe/outils/` | Burning permits + Règlement 627-96, restrictions, forest-fire and flood risk |
| `gaspe/prevention/` | Prevention (MRC) + prevention tips article |
| `gaspe/coordonnees/` | All contacts |
| `cloridorme/`, `grande-vallee/`, `murdochville/` | Basic municipal pages |
| `gaspe/caserne45/`, `gaspe/interactif/…`, `gaspe/ssi/recrutement/`, etc. | Redirect stubs for old WordPress URLs (reached via path-preserving forwarding of incendiegaspe.com) |
| `gaspe/wp-content/uploads/*.pdf` | The 5 PDFs, at their old path relative to the Gaspé section |
| `assets/`, `404.html`, `robots.txt`, `sitemap.xml`, favicons, `.nojekyll` | Shared plumbing |
| `tools/build.py` | Generator for all HTML pages. Edit content here, run `python3 tools/build.py`, commit. |

The **network bar** on every page switches between the four municipalities; "Réseau incendie" returns to the landing page. All links are relative.

## Publish on GitHub Pages

1. Repo **Settings → Pages**: Source = *Deploy from a branch*, Branch = `main`, folder `/ (root)`.
2. Custom domain: `incendiecotedegaspe.com` (already in `CNAME`). Wait for the DNS check, then tick **Enforce HTTPS**.

## DNS (Squarespace) — Pages first, DNS second

**incendiecotedegaspe.com** (change only these records):

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 · 185.199.109.153 · 185.199.110.153 · 185.199.111.153 (four records) |
| AAAA | @ | 2606:50c0:8000::153 · 8001::153 · 8002::153 · 8003::153 (four records) |
| CNAME | www | `adamnormand.github.io` |

**Forwarding (301) for the four municipal domains** — after incendiecotedegaspe.com is live with HTTPS:

| Domain (+ www) | Forward to | Path |
|---|---|---|
| incendiegaspe.com | `https://incendiecotedegaspe.com/gaspe/` | **Keep path** if Squarespace offers it, so old links (`/caserne45/`, `/wp-content/uploads/…pdf` used by the HubSpot portal and past emails) resolve |
| incendiecloridorme.com | `https://incendiecotedegaspe.com/cloridorme/` | Do not keep path |
| incendiegrandevallee.com | `https://incendiecotedegaspe.com/grande-vallee/` | Do not keep path |
| incendiemurdochville.com | `https://incendiecotedegaspe.com/murdochville/` | Do not keep path |

**incendiegaspe.com keeps its email and portal:** do not touch its MX/TXT (SPF, DKIM, DMARC) records — all `@incendiegaspe.com` addresses on the site stay valid — nor the `regroupement` CNAME (HubSpot member portal). Forwarding should only replace the web (@ and www) records. Test `https://` on every forwarded domain afterwards.

If Squarespace cannot keep the path for incendiegaspe.com, update the five PDF links in the HubSpot portal to `https://incendiecotedegaspe.com/gaspe/wp-content/uploads/…`.

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
