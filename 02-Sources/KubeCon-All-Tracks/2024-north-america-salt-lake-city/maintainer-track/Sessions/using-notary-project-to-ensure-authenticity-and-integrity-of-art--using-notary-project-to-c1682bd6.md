---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Toddy Mladenov", "Microsoft", "Tjark Rasche", "Mercedes-Benz Tech Innovation GmbH"]
sched_url: https://kccncna2024.sched.com/event/1hovU/using-notary-project-to-ensure-authenticity-and-integrity-of-artifacts-within-the-enterprise-toddy-mladenov-microsoft-tjark-rasche-mercedes-benz-tech-innovation-gmbh
youtube_search_url: https://www.youtube.com/results?search_query=Using+Notary+Project+to+Ensure+Authenticity+and+Integrity+of+Artifacts+Within+the+Enterprise+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Using Notary Project to Ensure Authenticity and Integrity of Artifacts Within the Enterprise - Toddy Mladenov, Microsoft & Tjark Rasche, Mercedes-Benz Tech Innovation GmbH

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Toddy Mladenov, Microsoft, Tjark Rasche, Mercedes-Benz Tech Innovation GmbH
- Schedule: https://kccncna2024.sched.com/event/1hovU/using-notary-project-to-ensure-authenticity-and-integrity-of-artifacts-within-the-enterprise-toddy-mladenov-microsoft-tjark-rasche-mercedes-benz-tech-innovation-gmbh
- Busca YouTube: https://www.youtube.com/results?search_query=Using+Notary+Project+to+Ensure+Authenticity+and+Integrity+of+Artifacts+Within+the+Enterprise+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Using Notary Project to Ensure Authenticity and Integrity of Artifacts Within the Enterprise.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hovU/using-notary-project-to-ensure-authenticity-and-integrity-of-artifacts-within-the-enterprise-toddy-mladenov-microsoft-tjark-rasche-mercedes-benz-tech-innovation-gmbh
- YouTube search: https://www.youtube.com/results?search_query=Using+Notary+Project+to+Ensure+Authenticity+and+Integrity+of+Artifacts+Within+the+Enterprise+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pO3sZsths2s
- YouTube title: Using Notary Project to Ensure Authenticity and Integrity of Artifacts Wit... T. Mladenov, T. Rasche
- Match score: 0.919
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/using-notary-project-to-ensure-authenticity-and-integrity-of-artifacts/pO3sZsths2s.txt
- Transcript chars: 34980
- Keywords: actually, notary, integrity, already, signatures, infrastructure, container, important, images, clusters, support, notation, provide, artifacts, everything, running, signed, cluster

### Resumo baseado na transcript

okay let's get started folks uh welcome to notary project uh uh presentation so this is part of the notary project maintenance track and today we will talk about using notary project to ensure authenticity and integrity in the Enterprise uh I am toy mov one of the maintainers of notary project and I have tar here yeah hi my name is Char gash I work for Mercedes-Benz Tech Innovation where we're currently in the process of rolling out uh Integrity with notary project at a pretty large scale and

### Excerpt da transcript

okay let's get started folks uh welcome to notary project uh uh presentation so this is part of the notary project maintenance track and today we will talk about using notary project to ensure authenticity and integrity in the Enterprise uh I am toy mov one of the maintainers of notary project and I have tar here yeah hi my name is Char gash I work for Mercedes-Benz Tech Innovation where we're currently in the process of rolling out uh Integrity with notary project at a pretty large scale and uh today what we'll talk about is why integrity and authenticity matters uh then we will actually show you how you can get there and tar will go through a a bunch of steps like what they're doing in their Enterprise and at the end we'll finish with some updates from notary project and what's coming up so uh starting with why integrity and authenticity matters uh we Implement uh zero trust everywhere else so we Implement zero trust uh uh for our applications we Implement zero trust for our users so we don't trust them all the time we ask them to go and reauthenticate every time when they need to do some uh new action we do the same also for our networks but we rarely actually implement zero trust for our applications so we go and pick up container image from dockerhub we don't check who published it most of the time we don't have a way to check who published it and we just actually start using it whether it's in our build or whether it's in our um deployment and it goes directly to our production clusters the way we look at uh kind of the supply chain for uh containers or any other software artifact is you go through a bunch of stages so first you acquire an image uh from as I said dockerhub or GCR or GCR and so on uh after that you actually build an internal catalog of thrusted images then you use it for build and then deploy it and then run it at the end between each one of those stages we are looking to actually Implement authentication and check for integrity of uh any software artifact that we have getting and not only the software artifacts but also any additional supply chain artifacts like s bombs like vulnerability reports or attestations so I will hand it over to Tar uh just to go through uh their experience and get some learning uh from their implementation so go ahead okay cool now we've learned we should probably be concerned with uh Integrity in our supply chains and let's first look at a like the dream scenario the what we would have in an Ideal World so
