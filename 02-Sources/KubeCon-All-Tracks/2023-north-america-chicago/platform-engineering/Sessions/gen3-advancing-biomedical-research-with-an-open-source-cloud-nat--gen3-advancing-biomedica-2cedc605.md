---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "Community Governance"]
speakers: ["Jawad Qureshi", "University of Chicago", "Colin Griffin", "Krumware"]
sched_url: https://kccncna2023.sched.com/event/1R2rx/gen3-advancing-biomedical-research-with-an-open-source-cloud-native-platform-jawad-qureshi-university-of-chicago-colin-griffin-krumware
youtube_search_url: https://www.youtube.com/results?search_query=Gen3%3A+Advancing+Biomedical+Research+with+an+Open+Source+Cloud-Native+Platform+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Gen3: Advancing Biomedical Research with an Open Source Cloud-Native Platform - Jawad Qureshi, University of Chicago & Colin Griffin, Krumware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Jawad Qureshi, University of Chicago, Colin Griffin, Krumware
- Schedule: https://kccncna2023.sched.com/event/1R2rx/gen3-advancing-biomedical-research-with-an-open-source-cloud-native-platform-jawad-qureshi-university-of-chicago-colin-griffin-krumware
- Busca YouTube: https://www.youtube.com/results?search_query=Gen3%3A+Advancing+Biomedical+Research+with+an+Open+Source+Cloud-Native+Platform+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Gen3: Advancing Biomedical Research with an Open Source Cloud-Native Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rx/gen3-advancing-biomedical-research-with-an-open-source-cloud-native-platform-jawad-qureshi-university-of-chicago-colin-griffin-krumware
- YouTube search: https://www.youtube.com/results?search_query=Gen3%3A+Advancing+Biomedical+Research+with+an+Open+Source+Cloud-Native+Platform+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iS1ecX4v9oQ
- YouTube title: Gen3: Advancing Biomedical Research with an Open Source Cloud-Nativ... Jawad Qureshi & Colin Griffin
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/gen3-advancing-biomedical-research-with-an-open-source-cloud-native-pl/iS1ecX4v9oQ.txt
- Transcript chars: 34661
- Keywords: research, platform, environment, environments, little, comments, essentially, provide, native, mentioned, infrastructure, support, researchers, automation, argo, workflows, working, access

### Resumo baseado na transcript

all right hello everyone and Welcome to our talk about gen 3 and advancing biomedical research with an open source and Cloud native platform my name is Jad kesi uh I'm the lead platform engineer at ctds auu Chicago and I'm Colin Griffin I'm a founder and chief engineer at kware uh we develop Cloud native Technologies I'm a contributing member of Tag app delivery and the platform's working group all right little bit about the agenda for this presentation uh we'll go quickly uh over an intro where I'll sharing it's data copying and security as well becomes a thing that each individual research institution uh has to take care of and research is essentially done in isolation uh and it's hard to reproduce and we're all familiar with the term works on my machine just apply that to research so the cloud for biomedical research is a great thing like you can get immediate access to large data set mounted in Cloud compute environments you can have elastic compute so you can scale up and down and only chicago.edu to learn about the center for translational data science and if you want to read the platform's white paper you can find it on taga delivery.

### Excerpt da transcript

all right hello everyone and Welcome to our talk about gen 3 and advancing biomedical research with an open source and Cloud native platform my name is Jad kesi uh I'm the lead platform engineer at ctds auu Chicago and I'm Colin Griffin I'm a founder and chief engineer at kware uh we develop Cloud native Technologies I'm a contributing member of Tag app delivery and the platform's working group all right little bit about the agenda for this presentation uh we'll go quickly uh over an intro where I'll introduce ctds and what we do uh we'll talk about bedal research give a little bit of background on especially in the cloud then we go over gen 3 which is the platform that we're building to conduct research in the cloud um and just a little bit of our Cloud native and kubernetes journey uh quick plug for chwar um we're software developers that specialize uh in Cloud native software Solutions uh we are application developers that are actively practicing uh platform engineering practices and we support software vendors and their end users and help build uh shippable software products and ctds which is Center for translational data science so as I mentioned we're the builders and maintainers of gen 3 uh we're part of the biological science division at University of Chicago uh our found founder and director is Dr Robert Grossman and he's a top leader for data sharing and data comment in particular uh yeah the ctds vision is a world which researchers have already access to the data needed and the tools required to make datadriven discoveries and our mission is basically to apply data science in a translational way and apply it to problems in biology medicine healthare and the environment a little bit more about our Center so it's effectively split in half where half of our Center is working on something called the genomic data comments that's a research platform uh developed with National Cancer Institute uh and it's used by about 100,000 research Searchers worldwide it makes 6.7 paby of harmonized data available for about 89,000 patients um J GDC runs exclusively in the U Chicago data centers uh but it is that technology that pioneering technology to build data comments that we standardized and made open source and Cloud native that turned into gen 3 and gen 3 today hosts about two million different total subjects uh we have about 93 million files and that total to about 22 and a half petabyte in total file size and some more impressive stats can be found at stat
