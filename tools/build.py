# -*- coding: utf-8 -*-
"""Génère le site statique com-ssig (incendiegaspe.com + pages municipales).
Usage : python3 tools/build.py   (régénère les pages HTML à la racine du dépôt)"""
import os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
MAJ = '2026-10-10'

# ---- Réglages à compléter (voir README, section « À confirmer ») ----
MRC_PREV = {
    'nom': 'Guillaume Pelchat',
    'titre': 'Coordonnateur en sécurité incendie',
    'org': 'MRC de La Côte-de-Gaspé',
    'courriel': 'guillaume.pelchat@cotedegaspe.ca',
    'tel': '418 368-7000, poste 230', 'tel_href': '+14183687000,230',
    'adresse': '298-A, boulevard York Sud, Gaspé (Québec) G4X 2L6',
    'site': 'https://www.cotedegaspe.ca',
}

SSI = {
    'adresse': '148, boul. de Gaspé, Gaspé (Québec) G4X 1A9',
    'courriel': 'ssi@ville.gaspe.qc.ca',
    'tel1': '(418) 360-4012', 'tel1_href': '+14183604012',
    'tel2': '(418) 368-2104, poste 8551', 'tel2_href': '+14183682104,8551',
    'telec': '(418) 368-1452',
    'heures': 'Lundi au vendredi, 9 h à 16 h 30 · Samedi et dimanche : fermé',
}
SOCIAL = [('Facebook', 'https://www.facebook.com/ssigaspe'), ('Instagram', 'https://www.instagram.com/ssigaspe/')]

RESEAU = [('gaspe', 'Gaspé', '', 'incendiegaspe.com'),
          ('cloridorme', 'Cloridorme', 'cloridorme/', 'incendiecloridorme.com'),
          ('grande-vallee', 'Grande-Vallée', 'grande-vallee/', 'incendiegrandevallee.com'),
          ('murdochville', 'Murdochville', 'murdochville/', 'incendiemurdochville.com')]

NAV_GASPE = [('accueil', 'Accueil', ''), ('service', 'Service incendie', 'service/'),
             ('association', 'L’Association', 'association/'), ('regroupement', 'Regroupement', 'regroupement/'),
             ('outils', 'Boîte à outils', 'outils/'), ('prevention', 'Prévention', 'prevention/'),
             ('coordonnees', 'Coordonnées', 'coordonnees/')]

e = html.escape


def page(path, title, body, *, desc='', site='gaspe', nav=None, current=None, municipalite=None, root=None):
    depth = path.count('/')
    r = root if root is not None else '../' * depth
    reseau = ''.join(
        f'<li><a href="{r}{p}" title="{dom}"{" aria-current=\"page\"" if k == site else ""}>{n}</a></li>'
        for k, n, p, dom in RESEAU)
    if site == 'gaspe':
        brand = (f'<a class="marque" href="{r}"><img src="{r}assets/img/ssig-logo.png" alt="Service de sécurité incendie — Ville de Gaspé" width="800" height="326"></a>')
        items = nav or NAV_GASPE
    else:
        brand = (f'<a class="marque" href="{r}{site}/"><span class="txt"><small>Sécurité incendie</small>{e(municipalite)}</span></a>')
        items = nav
    navhtml = ''.join(
        f'<li><a href="{r}{p}"{" aria-current=\"page\"" if k == current else ""}>{n}</a></li>' for k, n, p in items)
    if site == 'gaspe':
        foot = f'''<div class="cols">
<div><h4>Service de sécurité incendie de Gaspé</h4><p>{SSI['adresse']}<br><a href="tel:{SSI['tel1_href']}">{SSI['tel1']}</a> · <a href="mailto:{SSI['courriel']}">{SSI['courriel']}</a><br>{SSI['heures']}</p></div>
<div><h4>Liens</h4><ul class="sans"><li><a href="{r}service/">Service incendie</a></li><li><a href="{r}association/">Association des pompiers volontaires</a></li><li><a href="{r}regroupement/">Regroupement des pompiers volontaires</a></li><li><a href="{r}prevention/">Prévention (MRC)</a></li></ul></div>
<div><h4>Suivez-nous</h4><ul class="sans">{''.join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n, u in SOCIAL)}</ul></div>
</div>
<div class="bas">© 2026 Centre de services partagés aux organisations des premiers répondants de Gaspé · Nous soutenons le Service de sécurité incendie de Gaspé, l’Association des pompiers volontaires de Gaspé et le Regroupement des pompiers volontaires du Grand Gaspé. · Mise à jour : {MAJ}</div>'''
    else:
        foot = f'''<div class="cols">
<div><h4>Sécurité incendie — {e(municipalite)}</h4><p>En cas d’urgence, composez le <b>9-1-1</b>.</p></div>
<div><h4>Prévention</h4><p>{MRC_PREV['org']}<br><a href="{r}{site}/#prevention">Responsable : {MRC_PREV['nom']}</a></p></div>
<div><h4>Réseau</h4><ul class="sans">{''.join(f'<li><a href="{r}{p}">{n}</a></li>' for k, n, p, d in RESEAU if k != site)}</ul></div>
</div>
<div class="bas">Réseau incendie de La Côte-de-Gaspé · Mise à jour : {MAJ}</div>'''
    doc = f'''<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc or title)}">
<meta name="theme-color" content="#14213d">
<link rel="icon" href="{r}favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="{r}favicon.png">
<link rel="apple-touch-icon" href="{r}apple-touch-icon.png">
<link rel="stylesheet" href="{r}assets/style.css">
</head>
<body>
<a class="sr" href="#contenu">Aller au contenu</a>
<div class="reseau"><div class="wrap"><span class="lbl">Réseau incendie</span><ul>{reseau}</ul><span class="urg">Urgence : <b>9-1-1</b></span></div></div>
<header class="entete"><div class="wrap">{brand}
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" onclick="var n=document.getElementById('nav');var o=n.classList.toggle('ouvert');this.setAttribute('aria-expanded',o)">Menu</button>
<nav class="princ" id="nav" aria-label="Menu principal"><ul>{navhtml}</ul></nav>
</div></header>
<main id="contenu">
{body.replace('{r}', r)}
</main>
<div class="urgence-bande">EN CAS D’URGENCE, COMPOSEZ LE <a href="tel:911">9-1-1</a></div>
<footer class="pied"><div class="wrap">{foot}</div></footer>
</body>
</html>
'''
    fp = os.path.join(OUT, path, 'index.html') if not path.endswith('.html') else os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, 'w', encoding='utf-8').write(doc)


def titre(h1, sous='', fil=None):
    f = ''
    if fil:
        f = '<div class="fil">' + ' › '.join(f'<a href="{{r}}{p}">{n}</a>' for n, p in fil) + '</div>'
    return f'<div class="titre-page"><div class="wrap">{f}<h1>{h1}</h1>{f"<p>{sous}</p>" if sous else ""}</div></div>'


def mrc_bloc(court=False):
    c = MRC_PREV
    lignes = [f'<dt>Responsable</dt><dd>{c["nom"]}, {c["titre"].lower()}</dd>', f'<dt>Organisme</dt><dd>{c["org"]}</dd>']
    if c.get('adresse'):
        lignes.append(f'<dt>Adresse</dt><dd>{c["adresse"]}</dd>')
    if c['courriel']:
        lignes.append(f'<dt>Courriel</dt><dd><a href="mailto:{c["courriel"]}">{c["courriel"]}</a></dd>')
    if c['tel']:
        lignes.append(f'<dt>Téléphone</dt><dd><a href="tel:{c["tel_href"]}">{c["tel"]}</a></dd>')
    if c.get('site'):
        lignes.append(f'<dt>Site web</dt><dd><a href="{c["site"]}" rel="noopener">cotedegaspe.ca</a></dd>')
    txt = ('La prévention des incendies relève désormais de la MRC de La Côte-de-Gaspé pour l’ensemble des municipalités '
           'du territoire : inspections, visites de prévention, sensibilisation et questions sur la réglementation en prévention.')
    return f'<div class="carte"><p class="kicker">Prévention incendie</p><h3>{c["org"]}</h3><p>{txt}</p><dl class="coord">{"".join(lignes)}</dl></div>'


# =====================================================================
# DONNÉES — CASERNES (Ville de Gaspé)
# =====================================================================
REPARTITION = ('<p>Les membres du Service répondent aux urgences sur le territoire de la Ville de Gaspé, entre L’Anse-à-Valleau et Fort-Prével, '
               'à la suite d’un appel reçu du centre 9-1-1 (CAUREQ, basé à Rimouski) ou d’un ordre interne de la Ville. Il arrive aussi qu’un service '
               'd’urgence d’une municipalité voisine demande des renforts ou de l’entraide.</p>'
               '<p>Les casernes, équipes et unités affectées à un appel varient selon la géographie, le niveau de risque, le type d’appel, la sévérité initiale '
               'et la probabilité de propagation. La répartition des appels par le CAUREQ repose sur un schéma qui tient compte de ces variables, entre autres.</p>'
               '<p>Bien que chaque caserne soit associée à un territoire primaire (une « zone »), toutes les casernes peuvent être appelées sur la zone d’une autre, '
               'en opération partagée, en soutien ou en remplacement, selon ce que détermine le poste de commandement (PC) du Service.</p>')

CASERNES = [
    dict(n=45, nom='Saint-Maurice', lieu='Saint-Maurice-de-l’Échouerie', district='nord', chef='Capitaine Serge Minville',
         adr='41, chemin de l’Église, Gaspé (Québec) G4X 4B3', tel='(418) 269-5743',
         membres=['Capitaine Serge Minville, chef de caserne', 'Robert Cloutier, pompier', 'Éric Paquette, pompier', 'Maxime Scott-Maltais, pompier'],
         unites=[('245', 'Autopompe', '')],
         zone=['Grand-Étang', 'Lac à Julien', 'Portage-Saint-Hélier', 'Ruisseau-à-l’Ail', 'L’Anse-à-Valleau', 'Pointe-Jaune', 'Saint-Maurice-de-l’Échouerie', 'Petit-Cap']),
    dict(n=46, nom='Rivière-au-Renard', lieu='Rivière-au-Renard', district='nord', chef='Capitaine Valère Dufresne',
         adr='14, rue de l’Entrepôt, Gaspé (Québec) G4X 5L4', tel='(418) 368-2104, poste 8550', telec='(418) 368-8553',
         membres=['Capitaine Valère Dufresne, chef de caserne', 'Capitaine Marc Savage, officier', 'Capitaine Stéphane Blouin, officier',
                  'Jean-Michel Aspirault, pompier', 'Pierre Bougie, pompier', 'Liane Cotton, pompier', 'Jean-François Dupuis, pompier', 'Alain Fortin, pompier',
                  'Rodrigue Giasson, pompier', 'Guillaume Pelchat, pompier', 'Yves-Marie Samson, pompier', 'Martin Savage, pompier', 'Kaven Tremblay, pompier'],
         unites=[('346', 'Autopompe-citerne', ''), ('646', 'Sauvetage et désincarcération', '')],
         zone=['Petite-Rivière-au-Renard', 'Rivière-au-Renard-Ouest', 'Rivière-au-Renard', 'Val-Renard', 'Rivière-Morris', 'L’Anse-à-Fugère', 'Trait-Carré', 'L’Anse-au-Griffon']),
    dict(n=47, nom='Cap-des-Rosiers', lieu='Cap-des-Rosiers', district='nord', chef='Capitaine Anselme Whitty',
         adr='1248-A, boul. de Cap-des-Rosiers, Gaspé (Québec) G4X 6G5', tel='(418) 892-5737',
         membres=['Capitaine Anselme Whitty, chef de caserne'],
         unites=[('347', 'Autopompe-citerne', '')],
         zone=['Les Trois-Ruisseaux', 'Jersey Cove', 'Cap-des-Rosiers', 'Cap-des-Rosiers-Est', 'Cap-Bon-Ami']),
    dict(n=48, nom='Gaspé (centre-ville)', lieu='Gaspé', district='sud', chef='Capitaine Mitchell Legresley',
         adr='148, boul. de Gaspé, Gaspé (Québec) G4X 1A9', tel='(418) 360-4012', tel_b='(418) 368-2104, poste 8551',
         membres=[],
         unites=[('148', 'Véhicule d’état-major (1er)', ''), ('248', 'Autopompe (1re)', ''), ('2048', 'Autopompe (2e)', ''), ('448', 'Citerne', ''),
                 ('648', 'Unité de désincarcération et de sauvetage', ''), ('1848', 'Embarcation motorisée (bateau)', ''),
                 ('2848', 'Embarcation motorisée (aéroglisseur)', ''), ('3848', 'Embarcation motorisée (chaloupe)', ''), ('1948', 'VTT 6×6', ''),
                 ('2948', 'Motoneige (1re)', ''), ('3948', 'Motoneige (2e)', ''),
                 ('1458', 'Traîneau d’évacuation médicale', 'Traîneau hybride : transport terrestre sur roues ou sur neige avec skis.'),
                 ('1458-R', 'Traîneau d’évacuation médicale', 'Radeau de sauvetage marin pour 25 personnes.'),
                 ('1148', 'Unité d’équipement spécialisé', 'Remorque pour feux de forêt.'), ('2148', 'Unité d’équipement spécialisé', 'Remorque de premiers soins.'),
                 ('3148', 'Unité d’équipement spécialisé', 'Remorque avec génératrice et groupe électrogène.'),
                 ('1758', 'Unité de matières dangereuses', 'Remorque HAZMAT.'),
                 ('1048', 'Véhicule d’état-major', 'Roulotte de poste de commandement pour incidents majeurs et de longue durée.')],
         zone=[]),
    dict(n=49, nom='Douglastown', lieu='Douglastown', district='sud', chef='Capitaine Richard Matte',
         adr='4, avenue Saint-Patrick, Gaspé (Québec) G4X 2Y2', tel='(418) 368-8543', photo='caserne49.jpg',
         membres=['Capitaine Richard Matte, chef de caserne', 'Capitaine Gaétan Girard, officier', 'Capitaine Peter Patterson, officier', 'Capitaine Paul Bois, officier',
                  'Coralie Bernier, pompière', 'Dave Biard Ferguson, pompier', 'Richard Bond, pompier', 'François Charbonneau, pompier', 'Matthew Clark, pompier',
                  'Junior-Aldo Fortin, pompier', 'Charles-Olivier Henry, pompier', 'Capitaine Mitchell Legresley, pompier', 'Daniel Miville-Deschênes, pompier'],
         unites=[('349', 'Autopompe-citerne', 'Maximétal « Maxi » sur châssis Freightliner, 2020 · 1 500 gal US.')],
         galerie=['349-1.jpg', '349-2.jpg', '349-3.jpg'],
         zone=['Fort-Prével', 'Rue Annett', 'Bois-Brûlé', 'L’Anse-à-Brillant', 'Seal Cove', 'Douglastown', 'Rivière-Saint-Jean', 'Haldimand-Ouest', 'Haldimand-Est']),
    dict(n=50, nom='Aéroport', lieu='Aéroport Michel-Pouliot de Gaspé', district='sud', chef='Capitaine Paul Bois',
         adr='60, rue de l’Aéroport, Gaspé (Québec) G4X 2K2', tel='(418) 368-2104, poste 8551', telec='(418) 368-1452',
         membres=['Capitaine Paul Bois, chef de caserne'],
         unites=[('1151', 'Unité d’équipement spécialisé', 'Autopompe pour incidents aériens.')],
         zone=[]),
    dict(n=52, nom='Rosebridge', lieu='Rosebridge', district='sud', chef='Capitaine Richard Fortin',
         adr='588-A, boul. de Forillon, Gaspé (Québec) G4X 6T7', tel='(418) 368-5679', photo='caserne52.jpg', equipe_photo='rosebridge.jpg',
         membres=['Capitaine Richard Fortin, chef de caserne', 'Capitaine Jean-Marc Lemieux, officier', 'Capitaine Roger Cotton, officier', 'Capitaine Marc Dubé, officier',
                  'Capitaine Victor Jr. Cassivi, pompier', 'Capitaine Sophie Fortier, pompière', 'Craig Adams, pompier', 'Megan Adams, pompière', 'Hugo Arbour, pompier',
                  'Simon Bujold, pompier', 'Daniel Côté, pompier', 'Philippe Cyr, pompier', 'Samantha Diotte, pompière', 'Adam Normand, pompier',
                  'Harris Normand, pompier', 'Florence Prud’hommeaux, pompière', 'Marie-Michèle Quirion, pompière'],
         unites=[('352', 'Autopompe-citerne', 'Maximétal « Maxi » sur châssis Freightliner, 2005 · 1 500 gal US.')],
         galerie=['352-1.jpg'],
         zone=['Corte-Réal', 'Fontenelle', 'Saint-Majorique', 'Rosebridge', 'Farewell Cove', 'Penouille', 'Petit-Cap-aux-Os', 'Cap-aux-Os', 'D’Aiguillon', 'Petit-Gaspé', 'Grande-Grève', 'L’Anse-aux-Amérindiens']),
]


def build_gaspe():
    # ---------------- Accueil ----------------
    body = f'''
<div class="heros" style="background-image:url('{{r}}assets/img/banniere-accueil.jpg')"><div class="wrap">
<p class="kicker" style="color:#ffb4ac">Ville de Gaspé</p>
<h1>Service de sécurité incendie de Gaspé</h1>
<p>Une centaine de pompiers, sauveteurs, plongeurs et membres d’équipes spécialisées, répartis dans sept casernes, au service de la population de L’Anse-à-Valleau à Fort-Prével.</p>
<div class="btns"><a class="btn" href="{{r}}service/recrutement/">Devenir pompier</a><a class="btn alt" href="{{r}}service/">Nos casernes</a></div>
</div></div>
<section><div class="wrap">
<h2>Je recherche…</h2>
<div class="grille">
<a class="carte" href="{{r}}service/recrutement/"><p class="kicker">Recrutement</p><h3>Devenir pompier à temps partiel</h3><p>Le métier, les exigences, la formation et le processus d’embauche.</p><span class="lien">En savoir plus →</span></a>
<a class="carte" href="{{r}}service/"><p class="kicker">Casernes</p><h3>Le Service et ses sept casernes</h3><p>Coordonnées, équipes, unités et territoires desservis.</p><span class="lien">Voir les casernes →</span></a>
<a class="carte" href="{{r}}regroupement/"><p class="kicker">Membres</p><h3>Regroupement des pompiers</h3><p>L’association syndicale qui regroupe les pompiers volontaires du Grand Gaspé.</p><span class="lien">Accéder →</span></a>
<a class="carte" href="{{r}}association/"><p class="kicker">L’Association</p><h3>Association des pompiers volontaires</h3><p>Mandat, historique, activités, mérites et hommages.</p><span class="lien">Découvrir →</span></a>
</div></div></section>
<section class="gris"><div class="wrap deux">
<div><h2>Qui sommes-nous?</h2><p>Le Service de sécurité incendie de Gaspé (SSIG) est un service de la Ville de Gaspé. Il compte environ 100 pompiers, sauveteurs, plongeurs et membres d’équipes spécialisées, répartis dans sept casernes. Il offre des services d’intervention et de gestion de plusieurs types d’incidents d’urgence.</p>
<h3>Nos services</h3><p>En collaboration avec les autres services d’urgence, le SSIG est responsable du combat des incendies, de la gestion des incidents d’urgence et des sinistres, de la désincarcération, du sauvetage et des premiers soins lors d’accidents de la route, en milieu isolé, forestier et aquatique, ainsi qu’en espace clos.</p>
<p class="note"><b>Prévention :</b> la prévention des incendies relève désormais de la MRC de La Côte-de-Gaspé. <a href="{{r}}prevention/">Voir la page Prévention</a>.</p></div>
<div><h2>Notre territoire</h2><p>Nos sept casernes couvrent le territoire de la Ville de Gaspé, de L’Anse-à-Valleau à Fort-Prével.</p>
<table><thead><tr><th>District nord</th><th>District sud</th></tr></thead><tbody>
<tr><td><a href="{{r}}service/caserne-45/">45 — Saint-Maurice</a></td><td><a href="{{r}}service/caserne-48/">48 — Gaspé (centre-ville)</a></td></tr>
<tr><td><a href="{{r}}service/caserne-46/">46 — Rivière-au-Renard</a></td><td><a href="{{r}}service/caserne-49/">49 — Douglastown</a></td></tr>
<tr><td><a href="{{r}}service/caserne-47/">47 — Cap-des-Rosiers</a></td><td><a href="{{r}}service/caserne-50/">50 — Aéroport</a></td></tr>
<tr><td></td><td><a href="{{r}}service/caserne-52/">52 — Rosebridge</a></td></tr>
</tbody></table></div>
</div></section>
<section><div class="wrap">
<div class="grille">
<div class="carte"><p class="kicker">Bureau</p><h3>Service de sécurité incendie</h3><p>{SSI['adresse']}</p></div>
<div class="carte"><p class="kicker">Heures d’affaires</p><h3>Lundi au vendredi</h3><p>9 h à 16 h 30<br>Samedi et dimanche : fermé</p></div>
<div class="carte"><p class="kicker">Nous joindre</p><h3><a href="tel:{SSI['tel1_href']}">{SSI['tel1']}</a></h3><p>{SSI['tel2']}<br><a href="mailto:{SSI['courriel']}">{SSI['courriel']}</a></p></div>
</div>
<h2 style="margin-top:34px">Dernières nouvelles</h2>
<a class="carte" href="{{r}}prevention/#conseils"><p class="kicker">2020-04-16</p><h3>Conseils pratiques pour la prévention des incendies</h3><p>Détecteurs de fumée, extincteurs, feux à ciel ouvert, plan d’évacuation, ramonage…</p><span class="lien">Lire →</span></a>
</div></section>'''
    page('', 'SSI Gaspé — Service de sécurité incendie de la Ville de Gaspé', body,
         desc='Service de sécurité incendie de la Ville de Gaspé : casernes, recrutement, outils, Association et Regroupement des pompiers volontaires.', current='accueil')

    # ---------------- Service ----------------
    cards = ''.join(f'<a class="carte" href="{{r}}service/caserne-{c["n"]}/"><p class="kicker">District {c["district"]}</p><h3>Caserne {c["n"]} — {c["nom"]}</h3><p>{c["adr"]}<br>{c["tel"]}</p><span class="lien">Voir la caserne →</span></a>' for c in CASERNES)
    body = titre('Service incendie', 'Sept casernes, deux districts, un seul service.', [('Accueil', '')]) + f'''
<section><div class="wrap">
<p class="intro">Le Service de sécurité incendie de Gaspé est un service de la Ville de Gaspé. Ses membres, à temps partiel, interviennent lors d’incendies, d’accidents, de sauvetages et d’incidents d’urgence sur tout le territoire de la ville.</p>
<div class="grille" style="margin-top:20px">{cards}</div>
</div></section>
<section class="gris"><div class="wrap deux">
<div><h2>Direction et administration</h2><dl class="coord">
<dt>Adresse</dt><dd>{SSI['adresse']}</dd>
<dt>Courriel</dt><dd><a href="mailto:{SSI['courriel']}">{SSI['courriel']}</a></dd>
<dt>Téléphone</dt><dd><a href="tel:{SSI['tel1_href']}">{SSI['tel1']}</a> · {SSI['tel2']}</dd>
<dt>Télécopieur</dt><dd>{SSI['telec']}</dd></dl>
<p style="margin-top:14px"><a href="{{r}}wp-content/uploads/Organigramme-Service-incendie-aout-2024.pdf">Organigramme du Service (août 2024, PDF)</a></p></div>
<div><h2>Répartition des appels</h2>{REPARTITION}</div>
</div></section>
<section><div class="wrap grille">
<a class="carte" href="{{r}}service/recrutement/"><p class="kicker">Carrières</p><h3>Recrutement</h3><p>Pompier, pompier réserviste, sauveteur : découvrez les métiers et le processus d’embauche.</p><span class="lien">En savoir plus →</span></a>
<a class="carte" href="{{r}}outils/"><p class="kicker">Citoyens</p><h3>Boîte à outils</h3><p>Permis de brûlage, restrictions en vigueur, risque de feu en forêt et d’inondation.</p><span class="lien">Ouvrir →</span></a>
{mrc_bloc()}
</div></section>'''
    page('service/', 'Service incendie — SSI Gaspé', body, desc='Les sept casernes du Service de sécurité incendie de Gaspé.', current='service')

    # ---------------- Casernes ----------------
    for c in CASERNES:
        n = c['n']
        email = f'caserne{n}@incendiegaspe.com'
        telec = f'<dt>Télécopieur</dt><dd>{c["telec"]}</dd>' if c.get('telec') else ''
        coord = f'<dl class="coord"><dt>Caserne</dt><dd>{n} — {c["lieu"]}</dd><dt>Chef de caserne</dt><dd>{c["chef"]}</dd><dt>Adresse</dt><dd>{c["adr"]}</dd><dt>Courriel</dt><dd><a href="mailto:{email}">{email}</a></dd><dt>Téléphone</dt><dd>{c["tel"]}{(" · " + c["tel_b"]) if c.get("tel_b") else ""}</dd>{telec}</dl>'
        photo = f'<figure class="photo"><img src="{{r}}assets/img/{c["photo"]}" alt="Caserne {n} — {c["nom"]}" loading="lazy"></figure>' if c.get('photo') else ''
        membres = ('<ul class="liste">' + ''.join(f'<li>{m}</li>' for m in c['membres']) + '</ul>') if c['membres'] else '<p class="note">Liste des membres à venir.</p>'
        eq_photo = f'<figure class="photo" style="margin:10px 0 16px"><img src="{{r}}assets/img/{c["equipe_photo"]}" alt="Équipe de la caserne {n}" loading="lazy"><figcaption>L’équipe de la caserne {n} devant l’unité 352.</figcaption></figure>' if c.get('equipe_photo') else ''
        unites = ''.join(f'<div class="unite"><b>{u} — {t}</b>{d}</div>' for u, t, d in c['unites'])
        gal = ''
        if c.get('galerie'):
            gal = '<div class="galerie large" style="margin-top:14px">' + ''.join(f'<a href="{{r}}assets/img/{g}"><img src="{{r}}assets/img/{g}" alt="Unité {g.split("-")[0]}" loading="lazy"></a>' for g in c['galerie']) + '</div>'
        zone = (f'<h3>Zone {n}</h3><p>La zone {n} comprend les routes, terrains privés et publics, forêts, rivières, lacs et plans d’eau situés dans ou près de :</p><ul class="liste">' + ''.join(f'<li>{z}</li>' for z in c['zone']) + '</ul>') if c['zone'] else ''
        autres = ' · '.join(f'<a href="{{r}}service/caserne-{o["n"]}/">{o["n"]}</a>' for o in CASERNES if o['n'] != n)
        body = titre(f'Caserne {n} — {c["nom"]}', f'District {c["district"]}', [('Accueil', ''), ('Service incendie', 'service/')]) + f'''
<section><div class="wrap">
<ul class="toc"><li><a href="#coordonnees">Coordonnées</a></li><li><a href="#equipe">Équipe</a></li><li><a href="#unites">Unités</a></li><li><a href="#territoire">Territoire</a></li></ul>
<div class="deux" id="coordonnees" style="margin-top:18px"><div><h2>Coordonnées</h2>{coord}</div>{f"<div>{photo}</div>" if photo else ""}</div>
</div></section>
<section class="gris" id="equipe"><div class="wrap"><h2>Équipe</h2>{eq_photo}{membres}</div></section>
<section id="unites"><div class="wrap"><h2>Unités</h2>{unites}{gal}</div></section>
<section class="gris" id="territoire"><div class="wrap"><h2>Territoire</h2><h3>Protocole de répartition</h3>{REPARTITION}{zone}
<p style="margin-top:24px">Autres casernes : {autres}</p></div></section>'''
        page(f'service/caserne-{n}/', f'Caserne {n} — {c["nom"]} — SSI Gaspé', body, desc=f'Caserne {n} ({c["nom"]}) du Service de sécurité incendie de Gaspé.', current='service')

    # ---------------- Recrutement ----------------
    body = titre('Recrutement', 'Des carrières à temps partiel, au service de votre communauté.', [('Accueil', ''), ('Service incendie', 'service/')]) + f'''
<section><div class="wrap">
<ul class="toc"><li><a href="#metiers">Les métiers</a></li><li><a href="#processus">Processus d’embauche</a></li><li><a href="#conditions">Conditions préalables</a></li><li><a href="#postuler">Postuler</a></li></ul>
<p class="intro">Le Service de sécurité incendie de Gaspé offre une diversité de carrières à temps partiel qui permettent de se réaliser pleinement.</p>
<p>La rémunération dépend du type d’appel, de l’équipe affectée et des tâches accomplies. Même si certaines tâches sont rémunérées, tous les membres du Service font aussi du bénévolat : lors d’incidents, de levées de fonds, au sein de l’Association des pompiers et dans la communauté.</p>
<p>Un membre peut être embauché à titre de réserviste, de pompier, de sauveteur ou de partenaire civil, et être affecté à une ou plusieurs équipes ou services spécialisés. Souvent, un membre débute comme réserviste, suit la formation, devient pompier ou sauveteur, puis se spécialise. Chaque parcours est différent, et nous sommes ouverts à tous.</p>
</div></section>
<section class="gris" id="metiers"><div class="wrap"><h2>Les métiers</h2><div class="grille">
<div class="carte"><h3>Pompier ou pompière</h3><ul class="liste"><li>Combattre les incendies;</li><li>prodiguer des soins d’urgence à titre de premier répondant;</li><li>effectuer des sauvetages dans diverses situations;</li><li>participer à l’entretien de la caserne et des équipements;</li><li>soutenir les opérations au sein des équipes de soutien.</li></ul></div>
<div class="carte"><h3>Pompier réserviste</h3><p>La personne qui souhaite commencer sa formation et son entraînement pour devenir pompier peut débuter comme réserviste, dès l’âge de 16 ans.</p><p>Le réserviste suit les entraînements avec l’équipe en place, mais ne se rend pas sur les lieux d’un accident ou d’un incendie.</p></div>
<div class="carte"><h3>Sauveteur ou sauveteuse</h3><ul class="liste"><li>Prodiguer des soins d’urgence à titre de premier répondant;</li><li>effectuer des sauvetages dans diverses situations;</li><li>participer à l’entretien de la caserne et des équipements;</li><li>soutenir les opérations au sein des équipes de soutien.</li></ul></div>
</div>
<h3>Spécialisations</h3><ul class="liste"><li>Premiers soins</li><li>Sauvetage nautique et plongée sous-marine</li><li>Matières dangereuses (HAZMAT)</li><li>Sauvetage en hauteur</li><li>Recherche et sauvetage en milieu isolé</li><li>Alimentation et raccordement en eau</li></ul>
</div></section>
<section id="processus"><div class="wrap"><h2>Processus d’embauche</h2>
<p>Plusieurs étapes mènent à devenir membre du Service. L’évaluation vise à mieux vous connaître afin de déterminer si votre profil correspond à celui que recherche le SSIG. L’ordre et la nature des étapes peuvent changer sans préavis.</p>
<ol><li>Affichage du concours</li><li>Réception des candidatures et analyse de l’admissibilité</li><li>Entrevue d’évaluation des compétences liées à l’emploi</li><li>Entrevue d’évaluation générale (caractère et personnalité)</li>
<li>Vérifications préemploi : antécédents judiciaires, examen médical récent, curriculum vitæ (diplômes, permis et certifications), permis de conduire classe 4A, références</li>
<li>Test d’aptitudes physiques (au besoin)</li><li>Test psychométrique (au besoin)</li><li>Analyse globale</li><li>Acceptation probatoire</li><li>Début de la période de probation de 12 mois</li>
<li>Réussite de la formation d’accueil et des autres formations internes</li><li>Formation Pompier I (s’il y a lieu)</li><li>Évaluation des aptitudes et des comportements en fonction</li><li>Respect des autres exigences de la période probatoire</li><li>Passage de candidat probatoire à membre en règle</li></ol>
</div></section>
<section class="gris" id="conditions"><div class="wrap"><h2>Conditions préalables à l’embauche</h2>
<p>La Ville de Gaspé et le Service de sécurité incendie exigent au minimum de :</p>
<ol><li>être âgé de 18 ans ou plus et avoir terminé une 3<sup>e</sup> secondaire;</li><li>réussir les examens d’aptitudes que peut exiger la Ville;</li><li>être médicalement apte et réussir les tests médicaux ou autres exigés par la direction, selon la liste déposée annuellement au conseil;</li>
<li>n’avoir aucun antécédent criminel;</li><li>détenir un certificat de bonne conduite émis par la Sûreté du Québec;</li><li>résider dans le secteur couvert par la caserne où l’on souhaite s’intégrer;</li>
<li>détenir, ou obtenir dans les 12 mois suivant l’embauche, le permis de conduire requis pour les véhicules d’intervention (pompiers admissibles à la conduite);</li>
<li>réussir les examens théoriques et pratiques ainsi que les entrevues, s’il y a lieu;</li><li>s’engager à suivre la formation Pompier I dans les délais prévus par la loi pour intervenir en combat d’incendie.</li></ol>
</div></section>
<section id="postuler"><div class="wrap deux">
<div><h2>Postuler</h2><p>Faites parvenir votre candidature (lettre et curriculum vitæ) en personne, par la poste ou par courriel.</p>
<dl class="coord"><dt>Destinataire</dt><dd>Direction du Service de sécurité incendie</dd><dt>Adresse</dt><dd>{SSI['adresse']}</dd><dt>Courriel</dt><dd><a href="mailto:{SSI['courriel']}?subject=Candidature%20%E2%80%94%20Service%20de%20s%C3%A9curit%C3%A9%20incendie">{SSI['courriel']}</a></dd><dt>Téléphone</dt><dd><a href="tel:{SSI['tel1_href']}">{SSI['tel1']}</a></dd></dl>
<p style="margin-top:16px"><a class="btn" href="mailto:{SSI['courriel']}?subject=Candidature%20%E2%80%94%20Service%20de%20s%C3%A9curit%C3%A9%20incendie">Envoyer ma candidature</a></p></div>
<div class="carte"><h3>À joindre à votre courriel</h3><ul class="liste"><li>Nom, prénom, téléphone et adresse</li><li>Caserne ou secteur souhaité</li><li>Curriculum vitæ, diplômes, permis et certifications</li><li>Poste visé : réserviste, pompier, sauveteur ou partenaire civil</li></ul></div>
</div></section>'''
    page('service/recrutement/', 'Recrutement — SSI Gaspé', body, desc='Devenir pompier, pompier réserviste ou sauveteur à temps partiel à Gaspé.', current='service')

    # ---------------- Boîte à outils ----------------
    art = [
        ('1', 'Il est interdit à toute personne d’allumer un feu en plein air pour brûler des herbes, des broussailles ou des déchets sans avoir obtenu au préalable un permis émis par le Service de protection contre les incendies.'),
        ('2', 'Le permis est émis gratuitement par le Service de protection contre les incendies.'),
        ('3', 'Le permis est valide pour une période maximale de trois (3) jours.'),
        ('4', 'La présente réglementation ne s’applique pas aux feux allumés dans des foyers spécialement aménagés à cette fin.'),
        ('5', 'Il est interdit de faire un feu à l’extérieur les jours où la vitesse du vent excède 20 kilomètres par heure.'),
        ('6', 'Toute personne désirant obtenir un permis doit être responsable du feu et avoir les capacités de décider des mesures à prendre et des actions pour assurer la sécurité en cas d’incident.'),
        ('7', 'Cette personne doit s’assurer qu’une distance minimale de 30 mètres est respectée entre le feu et la propriété située à proximité.'),
        ('8', 'Il est interdit d’utiliser des substances prohibées telles que feux d’artifice, pétards, dans les rues, chemins ou autres endroits publics sans autorisation.'),
        ('9', 'Le contrevenant à l’une ou l’autre des dispositions du présent règlement commet une infraction et est passible d’une amende.')]
    reg = ''.join(f'<p><b>Article {a}.</b> {t}</p>' for a, t in art)
    body = titre('Boîte à outils', 'Permis de brûlage, restrictions et risques naturels.', [('Accueil', '')]) + f'''
<section><div class="wrap"><ul class="toc"><li><a href="#permis">Permis de brûlage</a></li><li><a href="#restrictions">Restrictions en vigueur</a></li><li><a href="#foret">Risque de feu en forêt</a></li><li><a href="#inondation">Risque d’inondation</a></li></ul></div></section>
<section class="gris" id="permis"><div class="wrap">
<h2>Permis de brûlage</h2>
<p class="intro">Brûlage d’herbes, de broussailles et de déchets, conformément au Règlement n<sup>o</sup> 627-96 de la Ville de Gaspé, adopté par le conseil municipal le 4 mars 1996.</p>
<div class="grille">
<div class="carte"><h3>Période et permis obligatoire</h3><p>Du 1<sup>er</sup> avril au 15 novembre, tout feu en plein air est interdit sans permis de brûlage délivré par le Service de sécurité incendie de Gaspé. Le permis est gratuit et valide pour au plus trois jours.</p></div>
<div class="carte"><h3>Validité du permis</h3><p>La validité d’un permis peut être limitée par des restrictions imposées par d’autres autorités, comme la SOPFEU. Il vous revient de vérifier que votre permis est valide au moment du brûlage.</p></div>
<div class="carte"><h3>Obtenir un permis</h3><p>Communiquez avec le Service au <a href="tel:{SSI['tel1_href']}">{SSI['tel1']}</a> ou par courriel à <a href="mailto:{SSI['courriel']}?subject=Demande%20de%20permis%20de%20br%C3%BBlage">{SSI['courriel']}</a>.</p></div>
</div>
<details><summary>Texte intégral du Règlement n<sup>o</sup> 627-96 — Concernant le brûlage d’herbes, de broussailles et de déchets</summary><div class="reglement">
<p><b>Ville de Gaspé — Règlement n<sup>o</sup> 627-96</b></p>
<p>ATTENDU QUE certains propriétaires de terrains situés sur le territoire de la municipalité sont portés à brûler des herbes, des broussailles ou des déchets sur leurs terrains, et que ces feux peuvent occasionner des dangers pour la sécurité publique;</p>
<p>ATTENDU QUE ces feux, laissés sans surveillance, peuvent causer des dommages aux propriétés avoisinantes;</p>
<p>ATTENDU QUE certaines personnes, dans le but notamment d’éloigner les moustiques ou lors d’un pique-nique ou d’une baignade, se permettent d’allumer un feu en plein air;</p>
<p>ATTENDU QUE les feux d’herbes, de broussailles ou de déchets qui échappent au contrôle constituent un danger pour la population, les habitations et la forêt, et entraînent parfois des pertes de vie humaine;</p>
<p>ATTENDU QU’il est du devoir ordinaire du service de protection contre les incendies de répondre aux appels et de se rendre sur les lieux d’incendie;</p>
<p>ATTENDU QU’un avis de motion de la présentation de ce règlement a régulièrement été donné à la séance ordinaire du Conseil tenue le 4 mars 1996;</p>
<p>EN CONSÉQUENCE, il est proposé par le conseiller Donald Bourgeois et résolu à l’unanimité qu’un règlement de ce Conseil portant le numéro 627-96 soit adopté et qu’il soit statué et décrété ce qui suit :</p>
{reg}
<p class="note">Texte reproduit à titre informatif. Seule la version officielle détenue par la Ville de Gaspé fait foi.</p></div></details>
</div></section>
<section id="restrictions"><div class="wrap">
<h2>Restrictions en vigueur</h2>
<p>Le droit de faire un feu ou de brûler peut être restreint par la Ville de Gaspé ou par le gouvernement du Québec, par l’entremise de la SOPFEU. Même si un permis de brûlage a été accordé, les restrictions municipales et provinciales ont préséance.</p>
<p>La SOPFEU diffuse régulièrement l’état de la situation : danger d’incendie, feux de forêt actifs et ressources déployées. Ses restrictions peuvent viser l’accès à la forêt, les feux et la circulation en forêt, les mesures préventives lors de travaux en forêt, ou la suspension des permis de brûlage industriel.</p>
<p>La Ville de Gaspé, par son conseil municipal, la mairie ou le Service incendie, peut aussi restreindre ou interdire tout brûlage sur son territoire.</p>
<div class="grille" style="margin-top:16px">
<div class="carte"><img src="{{r}}assets/img/sopfeu-logo.png" alt="SOPFEU" width="133" height="101" style="margin-bottom:10px"><p>Restrictions provinciales actuellement en vigueur.</p><a class="btn" href="https://sopfeu.qc.ca/restrictions/" rel="noopener">Site de la SOPFEU</a></div>
<div class="carte"><img src="{{r}}assets/img/ville-gaspe-logo.png" alt="Ville de Gaspé" width="101" height="101" style="margin-bottom:10px"><p>Restrictions municipales actuellement en vigueur.</p><a class="btn" href="https://ville.gaspe.qc.ca/" rel="noopener">Site de la Ville de Gaspé</a></div>
</div></div></section>
<section class="gris" id="foret"><div class="wrap">
<h2>Risque de feu en forêt</h2>
<p>Les données sur les dangers d’incendie, les restrictions, les mesures préventives et les feux de forêt actifs au Québec, y compris à Gaspé, proviennent de la Société de protection des forêts contre le feu (SOPFEU), l’organisme mandaté par le gouvernement du Québec.</p>
<div class="btns"><a class="btn" href="https://sopfeu.qc.ca" rel="noopener">Site de la SOPFEU</a><a class="btn alt" href="https://cartes.sopfeu.qc.ca/?lang=fr#dangers" rel="noopener">Carte des dangers d’incendie</a></div>
</div></section>
<section id="inondation"><div class="wrap">
<h2>Risque d’inondation</h2>
<p>Niveaux et débits en temps réel, fournis par le ministère de la Sécurité publique du Québec.</p>
<div class="grille">
<div class="carte"><h3>Rivière York</h3><p>Station 020404</p><div class="btns"><a class="btn" href="https://geoegl.msp.gouv.qc.ca/libcommunes/MSPwidgets/hydrogramme/index.php?station=020404&amp;type1=niveau" rel="noopener">Niveau</a><a class="btn alt" href="https://geoegl.msp.gouv.qc.ca/libcommunes/MSPwidgets/hydrogramme/index.php?station=020404&amp;type1=debit" rel="noopener">Débit</a></div></div>
<div class="carte"><h3>Rivière Dartmouth</h3><p>Station 020602</p><div class="btns"><a class="btn" href="https://geoegl.msp.gouv.qc.ca/libcommunes/MSPwidgets/hydrogramme/index.php?station=020602&amp;type1=niveau" rel="noopener">Niveau</a><a class="btn alt" href="https://geoegl.msp.gouv.qc.ca/libcommunes/MSPwidgets/hydrogramme/index.php?station=020602&amp;type1=debit" rel="noopener">Débit</a></div></div>
</div></div></section>'''
    page('outils/', 'Boîte à outils — SSI Gaspé', body, desc='Permis de brûlage, restrictions en vigueur, risque de feu en forêt et d’inondation à Gaspé.', current='outils')

    # ---------------- Prévention ----------------
    body = titre('Prévention', 'Assurée par la MRC de La Côte-de-Gaspé.', [('Accueil', '')]) + f'''
<section><div class="wrap deux">
<div><h2>La prévention relève de la MRC</h2><p class="intro">La prévention des incendies est désormais assurée par la MRC de La Côte-de-Gaspé pour l’ensemble des municipalités du territoire, dont Gaspé, Cloridorme, Grande-Vallée et Murdochville.</p>
<p>Pour une visite de prévention, une inspection ou une question sur la réglementation en prévention, communiquez avec le responsable de la prévention à la MRC. Le Service de sécurité incendie de Gaspé demeure responsable des interventions d’urgence.</p></div>
{mrc_bloc()}
</div></section>
<section class="gris" id="conseils"><div class="wrap">
<p class="kicker">Publié le 2020-04-16</p><h2>Conseils pratiques pour la prévention des incendies</h2>
<h3>En bref</h3>
<p>Un incendie n’a rien d’amusant, mais les exercices de sécurité-incendie peuvent l’être. Prévoyez deux sorties pour chaque pièce de la maison et faites des exercices d’évacuation.</p>
<p>Chaque année, des milliers d’incendies sont causés par l’utilisation imprudente d’appareils électroménagers dans la cuisine. Ne laissez jamais des aliments cuire ou de l’huile chauffer sans surveillance.</p>
<p>Chaque année au Canada, près de 1 300 incendies sont causés par des enfants qui jouent avec des allumettes ou des briquets. Gardez-les hors de la vue et de la portée des enfants.</p>
<p>L’alarme d’un avertisseur de fumée signifie qu’il faut quitter les lieux. Un plan d’évacuation pratiqué régulièrement vous permettra de réagir correctement en cas d’incendie. <i>(Source : Prévention des incendies du Canada)</i></p>
<div class="grille" style="margin-top:10px">
<div class="carte"><h3>Avertisseur de fumée</h3><p>Un avertisseur de fumée en bon état peut faire la différence entre la vie et la mort. Il est obligatoire sur le territoire de la Ville de Gaspé et un règlement municipal en régit l’installation. Vérifiez périodiquement les piles des appareils qui ne sont pas raccordés en permanence au circuit électrique.</p></div>
<div class="carte"><h3>Extincteur</h3><p>Choisissez un extincteur portant la mention ABC : sa poudre polyvalente convient à la plupart des incendies — bois, papier et tissu (A), liquides inflammables (B) et appareils électriques (C).</p></div>
<div class="carte"><h3>Feux d’artifice</h3><p>Certaines pièces pyrotechniques grand public (classe 7.2.1) peuvent être utilisées sans permis sur un terrain privé. Sur un terrain public, comme une rue ou un parc, une autorisation est requise. Le site de lancement doit mesurer au moins 30 m², être dégagé de tout arbre, bâtiment, poteau ou obstacle, et il ne faut jamais lancer par grand vent.</p></div>
<div class="carte"><h3>Feux à ciel ouvert</h3><p>Avant d’allumer un feu à ciel ouvert, même de branchages, obtenez le permis requis (voir la <a href="{{r}}outils/#permis">Boîte à outils</a>). Un foyer extérieur doit être installé à au moins 3 m de tout bâtiment ou matériau combustible, et sa cheminée doit être munie d’un pare-étincelles.</p></div>
<div class="carte"><h3>Plan d’évacuation</h3><p>Un plan d’évacuation prévient la panique. Faites régulièrement des exercices avec votre famille et assurez-vous que tous sortent immédiatement lorsque l’avertisseur sonne ou que quelqu’un crie « Au feu! ».</p></div>
<div class="carte"><h3>Ramonage</h3><p>Faites ramoner toute cheminée au moins une fois l’an et nettoyez régulièrement les tuyaux : l’accumulation de créosote cause de nombreux incendies.</p></div>
</div>
<p class="note" style="margin-top:16px">Sources : Prévention des incendies du Canada; Ville de Gaspé.</p>
</div></section>'''
    page('prevention/', 'Prévention — SSI Gaspé', body, desc='La prévention des incendies est assurée par la MRC de La Côte-de-Gaspé. Conseils pratiques.', current='prevention')

    # ---------------- Association ----------------
    pompier = [('2019', 'Marie-Michèle Quirion'), ('2018', 'Nicolas Pruneau'), ('2017', 'Sophie Fortier'), ('2016', 'Victor Jr. Cassivi'), ('2015', 'Harris Normand'),
               ('2014', 'Dennis Sinnett'), ('2013', 'Sylvain Girard'), ('2012', 'Sylvain Girard'), ('2011', 'Johanne Ferguson'), ('2010', 'Emmanuelle Poirier'),
               ('2009', 'Denise Ouellette, Yolaine Arsenault, Sylvie Cotton, Johanne Ferguson'), ('2008', 'Adam Normand'), ('2007', 'Gaétan Girard'),
               ('2006', 'Jérôme Grand’Maison'), ('2005', 'Dennis Sinnett'), ('2004', 'Jean-François Lévesque'), ('2003', 'Tasha Adams'), ('2002', 'Paul Bois'),
               ('2001', 'Roger Cléments, Johanne Ferguson'), ('2000', 'Dwight Sinnett, Ryan Sinnett'), ('1999', 'Lisa Morin'), ('1998', 'Johanne Ferguson'),
               ('1997', 'Roger Cléments'), ('1996', 'Linda Ferguson'), ('1995', 'Léo Kenny'), ('1994', 'Léo Kenny, Linda Ferguson'), ('1993', 'Michel Morin'),
               ('1987', 'Carl Sinnett'), ('1986', 'Carl Sinnett')]
    officier = [('2019', 'Jean-Marc Lemieux'), ('2018', 'Peter Patterson'), ('2017', 'Gaétan Girard'), ('2016', 'Marc Dubé'), ('2015', 'Denise Ouellette'),
                ('2014', 'Ryan Sinnett'), ('2013', 'Linda Ferguson'), ('2012', 'Johanne Ferguson'), ('2011', 'Carl Sinnett')]
    tab = lambda rows: '<div class="tab-scroll"><table><thead><tr><th>Année</th><th>Lauréat(s)</th></tr></thead><tbody>' + ''.join(f'<tr><td>{a}</td><td>{g}</td></tr>' for a, g in rows) + '</tbody></table></div>'
    amis = [('2004', [('Diane Sinnett', 'association_ami_2004_sinnett_diane.jpg')]),
            ('2003', [('Madone Bujold', 'association_ami_2003_bujold_madone.jpg')]),
            ('2002', [('Roger Sinnett', 'association_ami_2002_sinnett_roger.jpg'), ('La famille Déry', 'association_ami_2002_famille_dery.jpg'), ('Hilary McRoberts et FireFit of Canada', 'association_ami_2002_firefit.jpg')]),
            ('2001', [('Denise Ferguson', 'association_ami_2001_feguson_denise.jpg'), ('Pierrette Dorion', 'association_ami_2001_dorion_pierrette.jpg')]),
            ('1999', [('Michel Smith', 'association_ami_1999_smith_michel.jpg'), ('Jeannine Thibault', 'association_ami_1999_thibault_jeannine.jpg'), ('Irene Sinnett', 'association_ami_1999_sinnett_irene.jpg'), ('André Fortin', 'association_ami_1999_fortin_andre.jpg')]),
            ('1998', [('John McConnell', 'association_ami_1998_mcconnell_john.jpg'), ('Gérard Arsenault', 'association_ami_1998_arsenault_gerard.jpg'), ('Légion royale canadienne, filiale 59 Gaspé', 'association_ami_1998_legion.jpg'),
                      ('Chevaliers de Colomb de Saint-Majorique', 'association_ami_1998_chevaliers_stmajorique.jpg'), ('Bernard Morin', 'association_ami_1998_morin_bernard.jpg'),
                      ('Bernard Clements', None), ('Chevaliers de Colomb de Gaspé', None)])]
    amis_html = ''
    for an, lst in amis:
        figs = ''.join((f'<figure><img src="{{r}}assets/img/{f}" alt="{n}" loading="lazy"><figcaption>{n}</figcaption></figure>' if f else f'<figure><div style="aspect-ratio:1/1;border-radius:8px;background:var(--fond-2);display:flex;align-items:center;justify-content:center;color:var(--gris);font-size:13px;text-align:center;padding:8px">Photo à venir</div><figcaption>{n}</figcaption></figure>') for n, f in lst)
        amis_html += f'<h4>{an}</h4><div class="galerie">{figs}</div>'
    im = [('Sophie Bernier', 'im_sophie.jpg'), ('Gérard', 'im_nenou.jpg'), ('Dennis Biard', 'im_dennis.jpg'), ('Yan Jolicoeur', 'im_yan.jpg'), ('Maurice Déry', 'im_maurice.jpg')]
    im_html = '<div class="galerie large">' + ''.join(f'<figure><a href="{{r}}assets/img/{f}"><img src="{{r}}assets/img/{f}" alt="In memoriam — {n}" loading="lazy"></a><figcaption>{n}</figcaption></figure>' for n, f in im) + '</div>'
    equip = ['Véhicule de sauvetage Ford 1972', 'Motoneige Bombardier Nordic 50', 'Mannequins de réanimation cardiorespiratoire', 'Compresseur', 'Échelle pliante de sauvetage',
             'Vidéos (2)', 'Radios CB', 'Équipement de recherche', 'Escaladeurs', 'Mâchoires de vie', 'Téléavertisseurs de sauvetage (10)', 'Trois séries de vestes',
             'Trousse de premiers soins', 'Un aéroglisseur', 'Tente 10 × 15', 'Bateau Zodiac, vestes, avirons et remorque', 'VTT 6 × 6 Polaris avec treuil et casques', 'Treuil',
             '2 traîneaux de transport de personnes', '4 traîneaux pour motoneige', 'Téléviseurs (2)', 'Raccords pour bouteilles de plongée', 'Équipement pour matières dangereuses',
             'Cordes de 300 pi', 'Lampes de poche Maglite pour pompiers', 'Chemises de sauvetage (1984)', 'Insignes de pompier en métal', 'Un camion de pompier',
             'Un bateau Zodiac à coque rigide', 'Poste de commandement mobile']
    pres = ['Richard Sinnett', 'Bernard Morin', 'Léo Kenny', 'Marco Dubé', 'Linda Ferguson', 'Michel Morin (par intérim)', 'Mark Sinnett', 'Ryan Sinnett',
            'Jean-François Lévesque', 'Michel Morin', 'Sylvain Leblanc (par intérim)', 'François Charbonneau']
    body = titre('L’Association des pompiers volontaires de Gaspé', 'Fondée en 1977 · Volet social et communautaire', [('Accueil', '')]) + f'''
<section><div class="wrap">
<ul class="toc"><li><a href="#mandat">Mandat et historique</a></li><li><a href="#activites">Activités</a></li><li><a href="#merites">Mérites et prix</a></li><li><a href="#amis">Amis des pompiers</a></li><li><a href="#memoriam">In memoriam</a></li><li><a href="#ca">Conseil d’administration</a></li></ul>
<div class="deux" id="mandat" style="margin-top:20px">
<div><h2>Mandat et historique</h2>
<p>L’Association des pompiers volontaires de Gaspé a été fondée en 1977 par un groupe de pompiers, soit Ricky Sinnett, Carl Sinnett et Pierre Larivière. Ses buts sont de :</p>
<ul class="liste"><li>regrouper les personnes qui se dévouent comme pompiers volontaires ou sauveteurs dans la ville de Gaspé;</li><li>étudier, promouvoir, protéger et développer de toutes manières les intérêts matériels, culturels et sociaux de ses membres;</li>
<li>organiser des réunions, des conférences et des échanges, et établir un secrétariat qui serve de lien entre les membres;</li><li>établir et diriger un club social pour la récréation et la détente de ses membres et de leurs invités;</li>
<li>acquérir, posséder et exploiter les biens meubles et immeubles nécessaires à ces fins, et offrir à ses membres et à leurs invités des services liés aux buts de la corporation.</li></ul>
<p>À sa fondation, l’Association regroupait des membres de Gaspé et de Rivière-au-Renard. L’équipe de sauvetage s’y est jointe en 1983, les pompiers de Rosebridge en 1991 et ceux de Douglastown en 1992. Depuis 1986, Gaspé et Rivière-au-Renard ont chacune leur association.</p></div>
<div><img src="{{r}}assets/img/apvg-logo.png" alt="Logo historique du Service des incendies de la Ville de Gaspé" width="260" height="260" style="max-width:260px;margin:0 auto"></div></div>
<p>Depuis ses débuts, l’Association réalise des projets et amasse des fonds pour acquérir de l’équipement au profit du Service incendie. La valeur des équipements remis à la Ville dépasse 300 000 $.</p>
<details><summary>Équipements acquis par l’Association</summary><ul class="liste">{''.join(f"<li>{x}</li>" for x in equip)}</ul></details>
<p>Pour amasser ces fonds, les pompiers ont organisé de nombreuses activités-bénéfice : soupers spaghetti et smoked meat, bingos, déjeuners, brunchs, ventes de hot-dogs. Ils ont aussi joué le rôle de victimes lors d’exercices de la Régie régionale et assuré la sécurité lors d’événements d’envergure.</p>
<p>Le bénévolat est au cœur de leur engagement. Au fil des ans, ils ont repeint trois camions, aménagé l’intérieur de deux véhicules d’urgence et installé une pompe PTO sur le camion-citerne. Lors des Jeux du Québec de 1993, ils ont cumulé 4 000 heures de garde (24 h sur 24) dans les écoles et arrosé, pendant six semaines, les pelouses des sites de compétition. Ils sont présents lors des grands événements pour assurer la sécurité de la population : Mirage sur la banquise, Triathlon du bout de la terre, spectacles, collectes de sang, Régates de Gaspé, Tour de la Baie à vélo et autres.</p>
<p>En 1999, l’Association a célébré les 70 ans du Service incendie et invité les anciens pompiers à se joindre à elle. En 2007, elle comptait plus de 80 membres : pompiers, sauveteurs et anciens pompiers.</p>
<p>Jusqu’en 1999, l’Association veillait aussi aux conditions de travail des pompiers. Ce mandat a changé lorsque les pompiers ont adhéré à un syndicat en 1999. Depuis 2004, à la suite de la dissolution de ce syndicat, l’Association continue de suivre les conditions de travail, mais c’est un regroupement de tous les pompiers de la Ville de Gaspé — aujourd’hui le <a href="{{r}}regroupement/">Regroupement des pompiers volontaires du Grand Gaspé</a> — qui négocie l’entente de travail avec la Ville. La Ville a signé une première entente de travail avec les pompiers en avril 2006.</p>
<h3>Présidences successives</h3><ul class="liste">{''.join(f"<li>{p}</li>" for p in pres)}</ul>
</div></section>
<section class="gris" id="activites"><div class="wrap"><h2>Activités</h2>
<p>L’Association organise régulièrement des activités récréatives et familiales pour ses membres, et coordonne ou appuie chaque année :</p>
<ul class="liste"><li>des déjeuners-bénéfice pour des causes communautaires et humanitaires et pour le financement d’équipements;</li><li>la sécurité et les premiers soins lors d’événements communautaires (concerts, marathons et autres);</li><li>les défilés de l’Halloween, de Noël et autres;</li><li>un 5 à 7 pendant la Semaine de l’action bénévole;</li><li>le souper de homard;</li><li>le Noël des enfants;</li><li>le souper de Noël.</li></ul></div></section>
<section id="merites"><div class="wrap"><h2>Mérites et prix</h2>
<div class="deux"><div><h3>Pompier de l’année</h3><p>Chaque année, une plaque est remise au pompier qui, selon la direction du Service, s’est démarqué au cours de l’année. Cette plaque a été offerte au Service incendie par Romuald Ste-Croix et est présentée au lauréat par la direction du Service.</p>
<img src="{{r}}assets/img/association_prix.png" alt="Plaque du Pompier de l’année" width="242" height="198" style="margin:10px 0">{tab(pompier)}</div>
<div><h3>Officier de l’année</h3><p>Ce prix rend hommage au lieutenant Dennis Biard, officier du SSIG décédé dans l’exercice de ses fonctions lors d’un entraînement. Leader et entraîneur reconnu, il se distinguait par la qualité de son travail, l’excellence de son service et son dévouement remarquable.</p>
<p>Remis depuis 2011 à un officier ayant fait preuve, au cours de l’année, de leadership, d’engagement et d’un sens du devoir exemplaires, ce prix est un don de la conjointe et du fils de Dennis, Linda Ferguson et Dave Ferguson Biard. La première année, ils ont remis la plaque au directeur, Carl Sinnett, un collègue très apprécié de Dennis; depuis, la direction du Service la remet à l’officier qu’elle juge digne.</p>
<img src="{{r}}assets/img/association_prix_officier.png" alt="Plaque de l’Officier de l’année" width="191" height="147" style="margin:10px 0">{tab(officier)}</div></div>
</div></section>
<section class="gris" id="amis"><div class="wrap"><h2>Club « Amis des pompiers »</h2>
<p>La plaque « Ami des pompiers » est remise par le chef du district sud à une personne ou à un organisme qui a contribué à l’avancement et au développement de notre service incendie. Un ami des pompiers, c’est une personne exceptionnelle qui, par son dévouement, son appui et son aide, a fait progresser notre service. Un ami des pompiers, c’est pour la vie.</p>
{amis_html}</div></section>
<section id="memoriam"><div class="wrap"><h2>In memoriam</h2><p>Montages réalisés par Johanne Ferguson, membre du Service incendie, à la mémoire de nos membres décédés.</p>{im_html}</div></section>
<section class="gris" id="ca"><div class="wrap deux">
<div><h2>Conseil d’administration</h2><ul class="sans">
<li><b>Bruno Lévesque</b>, président — <a href="mailto:bruno.levesque@incendiegaspe.com">bruno.levesque@incendiegaspe.com</a> · (418) 361-2359</li>
<li><b>Simon Bujold</b>, secrétaire — <a href="mailto:simon.bujold@incendiegaspe.com">simon.bujold@incendiegaspe.com</a></li>
<li><b>Gaétan Girard</b>, trésorier — <a href="mailto:gaetan.girard@incendiegaspe.com">gaetan.girard@incendiegaspe.com</a> · (418) 361-5911</li></ul>
<p style="margin-top:10px">146, boul. de Gaspé, Gaspé (Québec) G4X 1A9</p></div>
<div class="carte"><h3>Devenir membre du Service</h3><p>Vous souhaitez vous joindre au Service de sécurité incendie de Gaspé?</p><a class="btn" href="{{r}}service/recrutement/">Recrutement</a></div>
</div></section>'''
    page('association/', 'L’Association des pompiers volontaires de Gaspé', body, desc='Association des pompiers volontaires de Gaspé : mandat, historique, activités, mérites et hommages.', current='association')

    # ---------------- Regroupement ----------------
    hub = 'https://regroupement.incendiegaspe.com/hubfs/'
    docs_rpgg = [
        ('Règlement n<sup>o</sup> 1 du Regroupement', hub + 'R%C3%A9glement%20No.%201.docx.pdf', ''),
        ('Règlement n<sup>o</sup> 2 du Regroupement', '', 'Document à venir'),
        ('Entente de travail 2023-01-01 au 2029-12-31 (en vigueur depuis le 2025-12-15, avec rétroactivité)', '', 'Document à venir'),
        ('Salaires des pompiers 2025, incluant la rétroactivité', '', 'Document à venir'),
        ('2026-01-25 — Assurance vie : augmentation de la prestation', hub + '2026%20-%20Assurance.pdf', ''),
        ('Politique de confidentialité et de protection des renseignements personnels', hub + 'RPGG%20-%20Politique%20de%20confidentialit%C3%A9%20et%20de%20protection%20des%20renseignements%20personnels%20(signe).pdf', ''),
        ('2024-11-06 — Procès-verbal de l’assemblée générale annuelle', hub + 'RPGG%20-%20AGA%202024%20-%202024-11-06%20-%20Proc%C3%A8s%20verbal.pdf', ''),
        ('2024-11-06 — Procès-verbal de l’assemblée extraordinaire des membres', hub + 'RPGG%20-%20AGE%202024%20-%202024-11-06%20-%20Proc%C3%A8s%20verbal.pdf', ''),
        ('2024-11-17 — Procès-verbal du conseil d’administration (CMEX-24A)', hub + '2024-11-17%20-%20CMEX%20-%20Proc%C3%A8s%20verbal%20du%20CMEX-A%20(2).pdf', ''),
        ('2024-11-19 — Procès-verbal du conseil élargi (CMEL-24B)', hub + '2024-11-19%20-%20CMEL-24B%20-%20Proc%C3%A8s%20verbal%20de%20lAssembl%C3%A9%20CMEL-24B.pdf', ''),
        ('2024-11-24 — Procès-verbal du conseil élargi (CMEL-24C)', hub + '2024-11-24%20-%20CMEL-24C%20-%20Proc%C3%A8s%20verbal%20de%20lAssembl%C3%A9%20CMEL-24C.pdf', ''),
    ]
    docs_emp = [
        ('Entente de travail 2016-01-01 au 2022-12-31 (remplacée par l’entente 2023-2029)', '{r}wp-content/uploads/Entente-de-travail-pompiers-2016-2022-version-finale-signee.pdf', 'PDF · 4,8 Mo'),
        ('2024-09-27 — Modification mineure à l’entente 2016 : ajout de la Journée nationale de la vérité et de la réconciliation', hub + 'rpgg_jv.pdf', ''),
        ('Salaires des pompiers 2024, incluant la rétroactivité (indexation de la convention générale de la Ville)', '{r}wp-content/uploads/Salaires-pompiers-annee-2024.pdf', 'PDF · 67 ko'),
        ('SSQ Groupe financier — Brochure du régime d’assurance collective des pompiers de la Ville de Gaspé (2018-04-01)', '{r}wp-content/uploads/Brochure-SSQ-pompiers-volontaires-2018-04-01.pdf', 'PDF · 819 ko'),
        ('SSQ Groupe financier — Résumé de l’assurance collective (2018-04-01)', '{r}wp-content/uploads/Resume-SSQ-pompiers-volontaires-2018-04-01.pdf', 'PDF · 739 ko'),
        ('AXA — Assurance vie 100 000 $', hub + 'rpgg_axa.pdf', ''),
        ('Organigramme du SSI Gaspé — août 2024', '{r}wp-content/uploads/Organigramme-Service-incendie-aout-2024.pdf', 'PDF · 392 ko'),
        ('Description de fonction — Pompier à temps partiel', hub + 'rpgg_jd_pompier.pdf', ''),
        ('Description de fonction — Lieutenant à temps partiel', hub + 'rpgg_jd_officier.pdf', ''),
        ('Programme de prévention — Service de protection contre les incendies (2024-10-30)', hub + 'Programme%20de%20pr%C3%A9vention%20Service%20protection%20contre%20les%20incendies%2030%20oct%202024%20.pdf', ''),
        ('Guide d’entretien de l’habit de combat (RH de la Ville, 2024-10-30)', hub + 'Annexe%20C%20Guide%20entretien%20habit%20de%20combats%20oct%202024.pdf', ''),
        ('Formulaire d’accusé de réception et d’engagement (RH de la Ville, 2024-10-30)', hub + 'Engagement%20du%20travailleur%20%C3%A0%20signer.pdf', ''),
        ('PON-001 — Sorties des unités (2015-06-01)', hub + 'PON-001%20-%20Sorties%20des%20unit%C3%A9s%20(V2015-06-01).pdf', ''),
        ('PON-002 — Personnel à bord des unités (2015-06-01)', hub + 'PON-002%20-%20Personnel%20%C3%A0%20bord%20des%20unit%C3%A9s%20(V2015-06-01).pdf', ''),
        ('PON-003 — Véhicule d’état-major (2015-06-01)', hub + 'PON-003%20-%20V%C3%A9hicule%20d%C3%A9tat%20major%20(V2015-06-01).pdf', ''),
        ('PON-004 — Prise des présences (2015-06-01)', hub + 'PON-004%20-%20Prise%20de%20pr%C3%A9snces%20(V2015-06-01).pdf', ''),
        ('PON-005 — Programme d’entraînement des pompiers (2018-01-01)', hub + 'PON-005%20-%20Programme%20d%E2%80%99entra%C3%AEnement%20des%20pompiers%20(V2018-01-01).pdf', ''),
        ('PON-006 — Dénombrement des pompiers (2020-11-01)', hub + 'PON-006%20-%20D%C3%A9nombrement%20des%20pompiers%20(V2020-11-01).pdf', ''),
    ]
    dl = lambda L: '<ul class="sans docs">' + ''.join((f'<li><a href="{u}">{t}</a> <span class="meta">{m}</span></li>' if u else f'<li>{t} <span class="meta">— {m}</span></li>') for t, u, m in L) + '</ul>'
    body = titre('Regroupement des pompiers volontaires du Grand Gaspé', 'Volet syndical · Restez informés, restez unis', [('Accueil', '')]) + f'''
<section><div class="wrap deux">
<div><p class="intro">Le Regroupement représente l’ensemble des pompiers à temps partiel de la Ville de Gaspé et négocie avec la Ville l’entente de travail qui encadre leurs conditions.</p>
<p>Les nouvelles, avis de convocation et le calendrier des assemblées sont publiés sur le portail des membres.</p>
<div class="btns"><a class="btn" href="https://regroupement.incendiegaspe.com/fr-ca/" rel="noopener">Portail des membres</a><a class="btn alt" href="#contact">Nous joindre</a></div></div>
<div class="carte"><h3>Vos communications</h3><p>Conformément à la Loi 25, le Regroupement applique sa <a href="{hub}RPGG%20-%20Politique%20de%20confidentialit%C3%A9%20et%20de%20protection%20des%20renseignements%20personnels%20(signe).pdf">Politique de confidentialité et de protection des renseignements personnels</a>, qui encadre aussi ses communications avec les membres.</p>
<p>Vérifiez votre dossier de courrier indésirable. Pour changer d’adresse courriel ou vous désabonner, écrivez-nous.</p></div>
</div></section>
<section class="gris"><div class="wrap deux">
<div><h2>Documents du Regroupement</h2>{dl(docs_rpgg)}</div>
<div><h2>Documents de l’employeur</h2>{dl(docs_emp)}</div>
</div></section>
<section id="gouvernance"><div class="wrap">
<h2>Gouvernance</h2><p class="note">Le mandat des membres du conseil d’administration et des personnes dirigeantes est de trois ans, ou jusqu’à l’élection de leurs successeurs.</p>
<div class="grille" style="margin-top:14px">
<div class="carte"><h3>Conseil d’administration</h3><ul class="sans"><li><b>Président :</b> Adam Normand</li><li><b>Secrétaire (intérim) :</b> Louis-Philippe Laurin</li><li><b>Trésorier :</b> Bruno Lévesque</li></ul><p class="note" style="margin-top:10px">En fonction depuis le 2024-11-07. Julie Samson, secrétaire, a démissionné le 2024-11-18; intérim assuré depuis le 2024-11-20.</p></div>
<div class="carte"><h3>Conseil élargi</h3><ul class="sans"><li>Membres du conseil d’administration</li><li><b>Délégués nord :</b> Jonathan Leblanc, Julien Tissier (un poste vacant depuis le 2024-12-04)</li><li><b>Délégués sud :</b> Marco Dubé, Mitchell Legresley</li></ul></div>
<div class="carte"><h3>Protection des renseignements personnels</h3><p>Personne responsable (Loi 25), depuis le 2024-11-05 : <b>Adam Normand</b>.</p></div>
</div>
<h3>Comités de négociation</h3>
<p>Le <b>comité de négociation</b> compte au moins un membre du conseil d’administration et peut inclure des membres du conseil élargi ou d’autres membres, dans la limite prévue par le Règlement n<sup>o</sup> 1. Le <b>comité central de négociation</b> réunit le conseil élargi et le comité de négociation.</p>
</div></section>
<section class="gris" id="contact"><div class="wrap"><h2>Nous joindre</h2>
<dl class="coord"><dt>Adresse</dt><dd>148, boul. de Gaspé, Gaspé (Québec) G4X 1A9</dd><dt>Courriel</dt><dd><a href="mailto:regroupement@incendiegaspe.com">regroupement@incendiegaspe.com</a></dd><dt>Téléphone</dt><dd><a href="tel:+15142223064">+1 514 222-3064</a></dd></dl>
</div></section>'''
    page('regroupement/', 'Regroupement des pompiers volontaires du Grand Gaspé', body, desc='Regroupement des pompiers volontaires du Grand Gaspé : documents, gouvernance et contact.', current='regroupement')

    # ---------------- Coordonnées ----------------
    rows = ''.join(f'<tr><td><a href="{{r}}service/caserne-{c["n"]}/">{c["n"]} — {c["nom"]}</a></td><td>{c["chef"]}</td><td>{c["adr"]}</td><td><a href="mailto:caserne{c["n"]}@incendiegaspe.com">caserne{c["n"]}@incendiegaspe.com</a><br>{c["tel"]}</td></tr>' for c in CASERNES)
    body = titre('Coordonnées', '', [('Accueil', '')]) + f'''
<section><div class="wrap">
<div class="alerte"><b>En cas d’urgence, composez le 9-1-1.</b></div>
<div class="grille">
<div class="carte"><p class="kicker">Ville de Gaspé</p><h3>Service de sécurité incendie</h3><dl class="coord"><dt>Adresse</dt><dd>{SSI['adresse']}</dd><dt>Courriel</dt><dd><a href="mailto:{SSI['courriel']}">{SSI['courriel']}</a></dd><dt>Téléphone</dt><dd><a href="tel:{SSI['tel1_href']}">{SSI['tel1']}</a><br>{SSI['tel2']}</dd><dt>Télécopieur</dt><dd>{SSI['telec']}</dd><dt>Heures</dt><dd>{SSI['heures']}</dd></dl></div>
{mrc_bloc()}
<div class="carte"><p class="kicker">Formation</p><h3>Bureau de l’instruction</h3><dl class="coord"><dt>Courriel</dt><dd><a href="mailto:fmc@incendiegaspe.com">fmc@incendiegaspe.com</a></dd><dt>Téléphone</dt><dd>{SSI['tel1']}</dd></dl></div>
</div></div></section>
<section class="gris"><div class="wrap"><h2>Casernes</h2><div class="tab-scroll"><table><thead><tr><th>Caserne</th><th>Chef de caserne</th><th>Adresse</th><th>Contact</th></tr></thead><tbody>{rows}</tbody></table></div></div></section>
<section><div class="wrap"><h2>Organismes</h2><div class="grille">
<div class="carte"><h3>Association des pompiers volontaires de Gaspé</h3><p>Bruno Lévesque, président<br><a href="mailto:bruno.levesque@incendiegaspe.com">bruno.levesque@incendiegaspe.com</a><br>(418) 361-2359</p><a href="{{r}}association/#ca">Conseil d’administration →</a></div>
<div class="carte"><h3>Regroupement des pompiers volontaires du Grand Gaspé</h3><p>Adam Normand, président<br><a href="mailto:regroupement@incendiegaspe.com">regroupement@incendiegaspe.com</a><br>+1 514 222-3064</p><a href="{{r}}regroupement/#gouvernance">Gouvernance →</a></div>
<div class="carte"><h3>Centre de services partagés aux organisations des premiers répondants de Gaspé</h3><p>Adam Normand · Marie-Michèle Quirion<br>146, boul. de Gaspé, Gaspé (Québec) G4X 1A9<br>(418) 368-1452</p></div>
</div></div></section>'''
    page('coordonnees/', 'Coordonnées — SSI Gaspé', body, desc='Coordonnées du Service de sécurité incendie de Gaspé, des casernes et des organismes.', current='coordonnees')

    # ---------------- 404 ----------------
    body = titre('Page introuvable', 'La page demandée n’existe pas ou a été déplacée.') + '''
<section><div class="wrap"><p>Le site a été renouvelé. Voici les principales sections :</p><ul class="liste"><li><a href="/">Accueil — SSI Gaspé</a></li><li><a href="/service/">Service incendie et casernes</a></li><li><a href="/outils/">Boîte à outils (permis de brûlage)</a></li><li><a href="/association/">L’Association</a></li><li><a href="/regroupement/">Le Regroupement</a></li><li><a href="/cloridorme/">Cloridorme</a> · <a href="/grande-vallee/">Grande-Vallée</a> · <a href="/murdochville/">Murdochville</a></li></ul></div></section>'''
    page('404.html', 'Page introuvable — Réseau incendie', body, root='/')


MUNIS = [
    dict(k='cloridorme', nom='Cloridorme', type='Municipalité de Cloridorme', site=''),
    dict(k='grande-vallee', nom='Grande-Vallée', type='Municipalité de Grande-Vallée', site=''),
    dict(k='murdochville', nom='Murdochville', type='Ville de Murdochville', site='https://murdochville.com/'),
]


def build_munis():
    for m in MUNIS:
        k = m['k']
        nav = [('accueil', 'Accueil', f'{k}/'), ('urgence', 'Urgence', f'{k}/#urgence'), ('prevention', 'Prévention', f'{k}/#prevention'), ('brulage', 'Brûlage', f'{k}/#brulage')]
        lien = f'<a class="btn alt" href="{m["site"]}" rel="noopener">Site de la {m["type"].split(" de ")[0].lower()}</a>' if m['site'] else ''
        body = f'''
<div class="titre-page"><div class="wrap"><p class="kicker" style="color:#ffb4ac">{m["type"]}</p><h1>Sécurité incendie — {m["nom"]}</h1><p>Urgence, prévention et brûlage pour les citoyens de {m["nom"]}.</p></div></div>
<section id="urgence"><div class="wrap deux">
<div><h2>En cas d’urgence</h2><div class="alerte"><b>Incendie, accident, personne en danger : composez le 9-1-1.</b></div>
<p>Le centre 9-1-1 répartit l’appel vers le service de sécurité incendie qui dessert {m["nom"]}. Donnez l’adresse exacte et restez en ligne jusqu’à ce que le répartiteur vous indique de raccrocher.</p></div>
<div class="carte"><h3>Service de sécurité incendie de {m["nom"]}</h3><p>Pour toute question non urgente sur le service incendie, communiquez avec la {m["type"].replace("Municipalité", "municipalité").replace("Ville", "ville")}.</p><div class="btns">{lien}</div></div>
</div></section>
<section class="gris" id="prevention"><div class="wrap deux">
<div><h2>Prévention</h2><p class="intro">La prévention des incendies relève désormais de la MRC de La Côte-de-Gaspé pour l’ensemble des municipalités de son territoire, dont {m["nom"]}.</p>
<p>Visites de prévention, inspections, avertisseurs de fumée, ramonage, questions de réglementation : adressez-vous au responsable de la prévention de la MRC.</p>
<p><a href="{{r}}prevention/#conseils">Conseils pratiques pour la prévention des incendies →</a></p></div>
{mrc_bloc()}
</div></section>
<section id="brulage"><div class="wrap">
<h2>Feux à ciel ouvert et brûlage</h2>
<p>Avant tout brûlage, vérifiez les restrictions provinciales de la SOPFEU et la réglementation municipale de {m["nom"]}. Les restrictions provinciales ont préséance sur tout permis municipal.</p>
<div class="btns"><a class="btn" href="https://sopfeu.qc.ca/restrictions/" rel="noopener">Restrictions SOPFEU</a><a class="btn alt" href="https://cartes.sopfeu.qc.ca/?lang=fr#dangers" rel="noopener">Carte des dangers d’incendie</a></div>
</div></section>
<section class="gris"><div class="wrap"><h2>Réseau incendie de La Côte-de-Gaspé</h2><div class="grille">
{''.join(f'<a class="carte" href="{{r}}{p}"><h3>{n}</h3><span class="lien">{d} →</span></a>' for kk, n, p, d in RESEAU if kk != k)}
</div></div></section>'''
        page(f'{k}/', f'Sécurité incendie — {m["nom"]}', body, site=k, nav=nav, current='accueil', municipalite=m['nom'],
             desc=f'Sécurité incendie à {m["nom"]} : urgence 9-1-1, prévention (MRC de La Côte-de-Gaspé) et brûlage.')


if __name__ == '__main__':
    build_gaspe()
    build_munis()
    open(os.path.join(OUT, 'CNAME'), 'w').write('incendiegaspe.com\n')
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: https://incendiegaspe.com/sitemap.xml\n')
    urls = []
    for root, _, files in os.walk(OUT):
        for f in files:
            if f == 'index.html':
                rel = os.path.relpath(root, OUT).replace('\\', '/')
                urls.append('https://incendiegaspe.com/' + ('' if rel == '.' else rel + '/'))
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{u}</loc><lastmod>{MAJ}</lastmod></url>\n' for u in sorted(urls)) + '</urlset>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
    print(len(urls), 'pages')


REDIRECTS = {
    'caserne45': 'service/caserne-45/', 'caserne46': 'service/caserne-46/', 'caserne47': 'service/caserne-47/', 'caserne48': 'service/caserne-48/',
    'caserne49': 'service/caserne-49/', 'caserne50': 'service/caserne-50/', 'caserne52': 'service/caserne-52/',
    'interactif': 'outils/', 'interactif/permis': 'outils/#permis', 'interactif/restrictions': 'outils/#restrictions',
    'interactif/foret': 'outils/#foret', 'interactif/inondation': 'outils/#inondation', 'outils/permis': 'outils/#permis',
    'ssi/recrutement': 'service/recrutement/', 'service/personnel/recrutement': 'service/recrutement/', 'service/recrutement/application': 'service/recrutement/#postuler',
    'conseils-pratiques-pour-la-prevention-des-incendies': 'prevention/#conseils', 'contact': 'coordonnees/', 'coordonnees/formulaire': 'coordonnees/',
    'legal': '', 'feeds': 'prevention/#conseils',
}


def build_redirects():
    for old, new in REDIRECTS.items():
        r = '../' * (old.count('/') + 1)
        tgt = r + new
        d = os.path.join(OUT, old); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(
            f'<!doctype html><html lang="fr-CA"><head><meta charset="utf-8"><title>Page déplacée</title>'
            f'<meta http-equiv="refresh" content="0; url={tgt}"><link rel="canonical" href="https://incendiegaspe.com/{new}"><meta name="robots" content="noindex"></head>'
            f'<body><p>Cette page a été déplacée : <a href="{tgt}">continuer</a>.</p></body></html>\n')


build_redirects()

