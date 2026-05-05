---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Runtime Containers", "Community Governance"]
speakers: ["Justin Cormack", "Docker", "Toddy Mladenov", "Microsoft"]
sched_url: https://kccnceu2023.sched.com/event/1HyUS/securing-the-container-supply-chain-with-notary-justin-cormack-docker-toddy-mladenov-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Securing+the+Container+Supply+Chain+with+Notary+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Securing the Container Supply Chain with Notary - Justin Cormack, Docker & Toddy Mladenov, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Justin Cormack, Docker, Toddy Mladenov, Microsoft
- Schedule: https://kccnceu2023.sched.com/event/1HyUS/securing-the-container-supply-chain-with-notary-justin-cormack-docker-toddy-mladenov-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+the+Container+Supply+Chain+with+Notary+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Securing the Container Supply Chain with Notary.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyUS/securing-the-container-supply-chain-with-notary-justin-cormack-docker-toddy-mladenov-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Securing+the+Container+Supply+Chain+with+Notary+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7RvFj_RWE7c
- YouTube title: Secure Container Supply Chain with Notation, ORAS, and Ratify
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/securing-the-container-supply-chain-with-notary/7RvFj_RWE7c.txt
- Transcript chars: 13986
- Keywords: artifacts, supply, notation, registry, container, verify, secure, ratify, attached, github, security, registries, software, attach, signature, signed, sample, deploy

### Resumo baseado na transcript

hello everyone this is famous I come from Beijing China I'm working at Microsoft and also a cncf ambassador and Microsoft product manager you can find my Twitter and GitHub profile at Fame and Joe so in today's webinar I would like to discuss our daily security concerns and problems and then I will share how to secure container supply chain with Note 3 oras and ratify foreign specifically I will first introduce what is software supply chain security and next I will talk about the challenges and concerns from

### Excerpt da transcript

hello everyone this is famous I come from Beijing China I'm working at Microsoft and also a cncf ambassador and Microsoft product manager you can find my Twitter and GitHub profile at Fame and Joe so in today's webinar I would like to discuss our daily security concerns and problems and then I will share how to secure container supply chain with Note 3 oras and ratify foreign specifically I will first introduce what is software supply chain security and next I will talk about the challenges and concerns from the industries and our end users next I will walk you through the sense of Open Source projects in this area such as Note 3 V2 auras and ratify for example we can leverage Note 3 V2 to sign and verify artifacts and we can use auras to promote artifacts across registries and if you are running applications on kubernetes gratify enables kubernetes clusters to verify artifacts security prior to deployment so if you want to automate and build a secure supply chain in CSD Pipeline with GitHub actions we will also provide provide our practice with these projects let's start from the real concerns we hear from our end users and I guess you might also struggling with these problems in your software delivery process not only security engineers most developers are also concerned about their security in their delivery process for example how to sign and verify your container image before you deploy it how to promote supply chain artifacts from development to production how to attach spawn file and signatures to contain the image to ensure consistency and integrity we also hear people want to make sure their deployment is secure and view their artifact references in Secure supply chain the most popular problem we hear is that how can we set up a secure supply chain in CSD workflow so in today's webinar I hope I can resolve all of those questions and concerns first of all I'd like to briefly introduce the software supply chain actually it starts from creation of content such as the building of content like binaries packages and images after after you created that you might need to this distribute all of those contents to different environments such as you need to Distributing the content to your end users and customers you might also need to distribute and promote across different environments and Registries and finally the consumption of those content so you might need to deploy all of those artifacts and apps to the environment foreign that you will find securing
