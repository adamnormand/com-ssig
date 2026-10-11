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
| `gaspe/regroupement/` | Regroupement des pompiers volontaires du Grand Gaspé (union side): overview, governance, contact |
| `gaspe/regroupement/portail/` | Members' portal — replaces regroupement.incendiegaspe.com (repo `com-rpgg`). Data in `tools/rpgg_data.json` |
| `gaspe/outils/` | Burning permits + Règlement 627-96, restrictions, forest-fire and flood risk |
| `gaspe/prevention/` | Prevention (MRC) + prevention tips article |
| `gaspe/coordonnees/` | All contacts |
| `cloridorme/`, `grande-vallee/`, `murdochville/` | Basic municipal pages |
| `gaspe/caserne45/`, `gaspe/interactif/…`, `gaspe/ssi/recrutement/`, etc. | Redirect stubs for old WordPress URLs (reached via path-preserving forwarding of incendiegaspe.com) |
| `gaspe/wp-content/uploads/*.pdf` | The 5 PDFs, at their old path relative to the Gaspé section |
| `assets/`, `404.html`, `robots.txt`, `sitemap.xml`, favicons, `.nojekyll` | Shared plumbing |
| `tools/build.py` | Generator for all HTML pages. Edit content here, run `python3 tools/build.py`, commit. |
| `tools/optimize_images.py` | One-off image optimiser (max 1000 px, JPEG q72, logos quantised). Run once on new originals only; it re-encodes on every pass. |

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

**regroupement.incendiegaspe.com** (old members' portal, `com-rpgg`): forward to `https://incendiecotedegaspe.com/gaspe/regroupement/portail/` (no path), then archive the `com-rpgg` repo and remove its GitHub Pages custom domain.

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

1. ~~MRC prevention contact~~ — done: Guillaume Pelchat, Coordonnateur en sécurité incendie, guillaume.pelchat@cotedegaspe.ca, 418 368-7000 poste 230 (cell not published).
2. **Direction du Service (Gaspé)** — Marc Grenier (Coordonnées) vs Éric Fugère (Recrutement) vs Carl Sinnett (Organigramme 2024-08). Site names no director.
3. **Gaspé chiefs** — C45: Serge Minville vs Éric Fugère; C48: Mitchell Legresley vs Carl Sinnett.
4. **Gaspé hours** — 16 h 30 used (old site also showed 16 h).
5. ~~Regroupement documents~~ — Règlement n° 2, Entente 2023–2029 and Salaires 2025 now linked (Google Drive, from com-rpgg).
6. **8 Regroupement documents lost with HubSpot** (listed without link on the portal): 2026-01-25 Assurances vie; PV CMEX 2024-11-17; PV CMEL 2024-11-19 and 2024-11-24; 2024-09-27 modification (Journée de la vérité et de la réconciliation); AXA Assurances vie 100K$; Guide d'entretien de l'habit de combat; Formulaire d'accusé de réception. Upload to Drive and add the URLs in `tools/rpgg_data.json`.
7. **AGA 2026 date** — portal calendar said 2026-03-02, the 2026-03-09 notice says 2026-03-23. Calendar now shows only past events + "dates à confirmer".
8. **Burning permits** — Gaspé still per Règl. 627-96 (SSI Gaspé); none of the three municipal sites publish a permit process, so their pages send citizens to the town hall + SOPFEU.
9. **Cloridorme** — chief Samuel Gagné has two phone numbers on the municipal site (418 360-7948 and 418 355-9911); not published, contact via town hall.
10. **Murdochville** — director: André Côté (directeur par intérim, Nous joindre page) vs René Robinson (Services sécurité page, with Côté as captain). Site uses André Côté. Firefighter roster on the town site not republished.
11. **Petite-Vallée** is in the MRC but not in the network.
12. **Association** — presidents list vs current board; duplicate Légion/Clements photo; truncated "Gérard" caption; Marie-Michèle vs Marie-Michelle; awards end 2019.
13. **Public union documents** — salary scales, work agreements and insurance brochures remain public, as on the old portal.

Sources for municipal content (2026-10-10): cotedegaspe.ca/securite-incendie and /post/operation-prevention; municipalitecloridorme.ca (sécurité incendie, urgences); grandevallee.ca (sécurité incendie, urgences); murdochville.com (services sécurité, nous joindre).
