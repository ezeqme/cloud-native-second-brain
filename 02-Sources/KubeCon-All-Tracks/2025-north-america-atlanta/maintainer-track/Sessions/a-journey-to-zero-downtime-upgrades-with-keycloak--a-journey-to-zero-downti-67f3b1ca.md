---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Martin Bartoš", "Ryan Emerson", "IBM"]
sched_url: https://kccncna2025.sched.com/event/27NoF/a-journey-to-zero-downtime-upgrades-with-keycloak-martin-bartos-ryan-emerson-ibm
youtube_search_url: https://www.youtube.com/results?search_query=A+Journey+To+Zero-Downtime+Upgrades+With+Keycloak+CNCF+KubeCon+2025
slides: []
status: parsed
---

# A Journey To Zero-Downtime Upgrades With Keycloak - Martin Bartoš, Ryan Emerson, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Martin Bartoš, Ryan Emerson, IBM
- Schedule: https://kccncna2025.sched.com/event/27NoF/a-journey-to-zero-downtime-upgrades-with-keycloak-martin-bartos-ryan-emerson-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=A+Journey+To+Zero-Downtime+Upgrades+With+Keycloak+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre A Journey To Zero-Downtime Upgrades With Keycloak.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NoF/a-journey-to-zero-downtime-upgrades-with-keycloak-martin-bartos-ryan-emerson-ibm
- YouTube search: https://www.youtube.com/results?search_query=A+Journey+To+Zero-Downtime+Upgrades+With+Keycloak+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=x3e1wqWTbUs
- YouTube title: A Journey To Zero-Downtime Upgrades With Keycloak - Martin Bartoš, Ryan Emerson, IBM
- Match score: 0.846
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/a-journey-to-zero-downtime-upgrades-with-keycloak/x3e1wqWTbUs.txt
- Transcript chars: 26097
- Keywords: keycloak, rolling, database, update, question, solution, downtime, version, configuration, metadata, upgrades, operator, cluster, compatibility, command, changes, versions, change

### Resumo baseado na transcript

That's uh that's the uh that's the talk that we are going to cover this uh this time. Key is used by hundreds or thousands of organizations uh managing identity and access. uh but then there are some requirements about token standardization about uh user federation about uh security edge cases security CVS even multiffactor authentication and so on uh but kiklo takes care of everything like that so uh you can focus on your business needs Glo run and scale in cloud and non-cloud non-cloud environments and we offer kubernetes operator and high availability setups. uh with the recent uh with the recent release we provide passwordless authentication so uh you don't need passwords anymore so you can use security keys uh or biometrics for example face ID and so on it would be nice to mention something about keylo authentication there's the support for financial grade API version two uh there's the uh depot support as demonstrating proof of position and preview support for federated client authentication like SPIFFY.

### Excerpt da transcript

Okay. Hello everyone. We can start and let's start with a question. How do you upgrade a critical system without anyone noticing? That's uh that's the uh that's the talk that we are going to cover this uh this time. It is a journey to zero downtime upgrades with keylo. Key is used by hundreds or thousands of organizations uh managing identity and access. If such a service um managing the identity and access is down uh the downtime is not just annoying it's just critical for your business. In this talk we will talk about uh how we are moving forward uh towards the zero downtime upgrades in keylog uh and we will see uh what's new inside there uh what's next and what works. Uh before we go deep inside uh it would be nice to introduce ourselves right. Uh so I'm Martin Bartto and I'm senior software engineer at IBM and I'm part of Kiklo cloud native team. >> Hi everyone. I'm Ryan Emerson. I'm a principal software engineer at IBM and I'm part of the S sur team. >> Yeah. So before we go down into the zero downtime upgrades and so on, it would be nice to say some words about Glo itself.

So what is actually keycloak? Keycloak is identity and access management solution or am for short. It authenticates and authoriz authorize users for services token hand uh I mean keylo handles login token issuance and even request validation for your applications and APIs. There's the question do you really need an IM in your deployment? Uh the answer is simple. Yes, you do. Sometimes um sometimes uh there are some companies that or organizations they want to uh do the authentication and IM on their own but sooner or later uh they find out it's a rabbit hole. You know you can you can cover the basic basic stuff like login or sessions. uh but then there are some requirements about token standardization about uh user federation about uh security edge cases security CVS even multiffactor authentication and so on uh but kiklo takes care of everything like that so uh you can focus on your business needs so kiko authenticate and authorize users and services plus uh offers the single sign on capability uh which means means that your users can only log in once across your organization.

Uh keylo provides the bridge to existing infrastructure. So you can connect it with the active directory, ldup even with uh your own database of users. uh also connect it with any other OIDC s or keros provider and um your users can login also via social providers like github Facebook and so on. Glo run an
