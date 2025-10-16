presentation_projet = """
# Présentation du Projet

## 1. Contexte et origine du projet
> Expliquer la genèse du projet : pourquoi il a été lancé, quels besoins ou difficultés il devait résoudre.

Exemples :
- Le projet est né de la volonté de moderniser les outils internes de gestion du temps et des activités (GTA).
- L’ancien système ne répondait plus aux exigences de flexibilité, de performance et de conformité réglementaire.
- L’objectif principal était de simplifier les processus RH et d’offrir une meilleure visibilité sur les plannings.

---

## 2. Objectifs du projet
> Lister les objectifs concrets à atteindre, à la fois techniques et fonctionnels.

| Objectif | Description |
|-----------|--------------|
| Modernisation technologique | Migrer vers une architecture web moderne (Symfony / NextJS) pour assurer scalabilité et maintenabilité. |
| Optimisation des processus métier | Automatiser les validations et calculs complexes liés aux absences et congés. |
| Amélioration de l’expérience utilisateur | Fournir une interface intuitive, réactive et accessible à tous les collaborateurs. |
| Sécurisation et conformité | Garantir la conformité RGPD et la fiabilité des données RH. |

---

## 3. Enjeux et importance pour le client
> Mettre en avant les bénéfices concrets pour le client et son organisation.

- **Gain de temps** : réduction du temps de saisie et de validation des demandes.
- **Fiabilité accrue** : suppression des erreurs manuelles et meilleure traçabilité des actions.
- **Cohérence RH** : harmonisation des pratiques entre services et sites.
- **Pilotage optimisé** : indicateurs et rapports dynamiques pour le management.
- **Satisfaction des collaborateurs** : plus d’autonomie et de clarté sur leurs droits et plannings.

---

## 4. Périmètre fonctionnel
> Décrire les grandes fonctionnalités couvertes par le projet.

### Principales fonctionnalités
- Saisie et gestion des absences, congés, maladies et événements spécifiques  
- Gestion des workflows de validation multi-niveaux  
- Gestion des droits et profils utilisateurs  
- Reporting RH et statistiques d’absentéisme  
- Visualisation des plannings (jour/semaine/mois/année)  
- Export vers paie et intégration avec les systèmes tiers  

---

## 5. Périmètre technique
> Décrire l’architecture et les grandes orientations techniques.

| Composant | Description |
|------------|-------------|
| **Front-end** | Next.js + React Query + AgGrid + TailwindCSS (UI moderne et performante) |
| **Back-end** | Symfony 7 + PostgreSQL (API REST et logique métier centralisée) |
| **Infrastructure** | Nginx (reverse proxy), Docker / PM2, Debian 12 |
| **Supervision / Workers** | FrankenPHP pour la gestion des scripts et processus asynchrones |
| **Sécurité** | Authentification JWT, gestion des rôles et permissions, RGPD conforme |

---

## 6. Bénéfices attendus et mesurables
> Identifier des indicateurs de succès ou des KPI.

| Indicateur | Situation initiale | Objectif visé |
|-------------|-------------------|----------------|
| Temps moyen de validation d’un congé | 48h | < 12h |
| Taux d’erreur sur les soldes | 5 % | < 1 % |
| Satisfaction utilisateur (enquête interne) | 65 % | > 85 % |
| Temps de traitement serveur | 2s | < 500ms |

---

## 7. Vision à long terme
> Expliquer la place du projet dans la stratégie du client.

- Intégration future avec d’autres systèmes RH (paie, SIRH, gestion des compétences)  
- Évolutivité vers un **SaaS complet de GTA** pour d’autres entités du groupe  
- Exploitation des données pour le **pilotage prédictif RH** (IA, recommandations automatiques)  
- Renforcement de la **culture numérique interne** grâce à un outil moderne et adaptable  

---

## 8. Gouvernance et pilotage
> Préciser comment le projet est géré et suivi.

| Rôle | Responsable | Fréquence / Mode de suivi |
|------|--------------|----------------------------|
| Pilotage global | Chef de projet client & chef de projet technique | Réunion hebdomadaire |
| Comité projet | Équipe technique + équipe métier | Mensuel |
| Suivi opérationnel | Kanban / outil de ticketing | Continu |
| Documentation | Wiki interne | Mise à jour en continu |

---

## 9. Chronologie synthétique
> Retracer les grandes étapes du projet.

| Étape | Période | Commentaire |
|--------|----------|-------------|
| Cadrage et expression du besoin | Q1 2024 | Recueil des besoins RH |
| Conception et développement | Q2–Q3 2024 | Implémentation et tests internes |
| Phase pilote | Q4 2024 | Déploiement sur un périmètre restreint |
| Déploiement global | Q1 2025 | Mise en production et accompagnement |
| Évolutions prévues | 2025–2026 | Intégration d’IA et module analytique |

---

## 10. Conclusion
> Résumer en quelques lignes l’essence du projet et sa portée.

Ce projet s’inscrit dans une démarche de **modernisation, d’efficacité et d’innovation**.  
Il symbolise la volonté du client d’outiller ses équipes avec des solutions **pérennes, évolutives et respectueuses des pratiques RH existantes**, tout en s’ouvrant aux usages de demain.

---

Souhaites-tu que je t’en fasse une **version adaptée à ton projet de Gestion des Temps et Activités**, avec les éléments que tu m’as déjà décrits (tech stack, workflows, moteur de règles, intégration IA, etc.) ?  
Cela te donnerait une version prête à publier sur ton Wiki.
"""

equipes_contacts = """
# Équipe du Projet

## 1. Équipe Technique

### 1.1. Responsables techniques
| Nom | Rôle | Société | Contact |
|------|------|----------|----------|
| Jean Dupont | Chef de projet technique | Société X | 📧 jean.dupont@societex.com / 💬 Teams / ☎️ +33 6 12 34 56 78 |
| Marie Lefebvre | Architecte applicatif | Société X | 📧 marie.lefebvre@societex.com |

### 1.2. Développeurs & Intégrateurs
| Nom | Spécialité | Stack principale | Contact |
|------|-------------|------------------|----------|
| Paul Martin | Front-end | React / Next.js / TypeScript | 📧 paul.martin@societex.com |
| Claire Bernard | Back-end | Symfony / PHP / PostgreSQL | 📧 claire.bernard@societex.com |
| Julien Robert | DevOps | Docker / Nginx / Debian / CI-CD | 📧 julien.robert@societex.com |

### 1.3. Support & maintenance
| Nom | Rôle | Contact |
|------|------|----------|
| Sophie André | Support applicatif | 📧 support@societex.com |
| — | Hotline | ☎️ +33 1 23 45 67 89 |

---

## 2. Équipe Métier / Fonctionnelle (Client)

### 2.1. Référents principaux
| Nom | Fonction | Service / Direction | Contact |
|------|-----------|---------------------|----------|
| Nathalie Leroy | Cheffe de projet métier | Direction RH | 📧 nathalie.leroy@client.com |
| Pierre Garnier | Référent process GTA | Service Paie | 📧 pierre.garnier@client.com |

### 2.2. Utilisateurs clés
| Nom | Fonction | Périmètre | Contact |
|------|-----------|-----------|----------|
| Laura Moreau | Responsable d’équipe | Site de Lyon | 📧 laura.moreau@client.com |
| Karim Bensaïd | Gestionnaire RH | Siège | 📧 karim.bensaid@client.com |

---

## 3. Canaux de communication

| Outil / Canal | Usage principal | Accès / Lien |
|----------------|----------------|---------------|
| Microsoft Teams | Réunions, échanges quotidiens | [Lien vers le canal Teams](#) |
| Email | Échanges formels et validation | — |
| Outil de ticketing | Suivi des anomalies et demandes | [Lien vers la plateforme](#) |
| Wiki | Documentation et historique du projet | [Lien vers le Wiki du projet](#) |

---

## 4. Historique des interlocuteurs

> *Ce tableau permet de garder une trace des changements d’équipes ou de référents côté client ou prestataire.*

| Période | Nom | Rôle | Remplacé par | Commentaire |
|----------|------|------|--------------|--------------|
| 2023-01 → 2024-03 | Antoine Dubois | Chef de projet client | Nathalie Leroy | Départ de l’entreprise |
| 2024-05 → Aujourd’hui | Claire Bernard | Lead back-end | — | — |

---

### 📝 Notes complémentaires
- Toute modification dans les équipes doit être reportée ici.
- Les coordonnées personnelles (numéros directs, mobiles, etc.) doivent être partagées uniquement dans le respect des politiques de confidentialité internes.
- Les adresses de contact génériques sont à privilégier pour les demandes d’assistance.

---

Souhaites-tu que je t’en fasse une **version pré-remplie** avec des exemples de ton **projet GTA (Symfony + NextJS)** et de ton **organisation actuelle** (ex : toi en lead dev, équipe technique, client RH) ?  
Cela te donnerait une base directement exploitable.
"""