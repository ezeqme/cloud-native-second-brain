---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Security", "Runtime Containers", "Community Governance"]
speakers: ["Justin Cormack", "Docker", "Steve Lasker", "Microsoft"]
sched_url: https://kccnceu2021.sched.com/event/iE8H/notary-v2-supply-chain-security-for-containers-justin-cormack-docker-steve-lasker-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Notary+v2%3A+Supply+Chain+Security+for+Containers+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Notary v2: Supply Chain Security for Containers - Justin Cormack, Docker & Steve Lasker, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Justin Cormack, Docker, Steve Lasker, Microsoft
- Schedule: https://kccnceu2021.sched.com/event/iE8H/notary-v2-supply-chain-security-for-containers-justin-cormack-docker-steve-lasker-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Notary+v2%3A+Supply+Chain+Security+for+Containers+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Notary v2: Supply Chain Security for Containers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE8H/notary-v2-supply-chain-security-for-containers-justin-cormack-docker-steve-lasker-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Notary+v2%3A+Supply+Chain+Security+for+Containers+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SZMbuirEQVU
- YouTube title: Notary v2: Supply Chain Security for Containers - Justin Cormack, Docker & Steve Lasker, Microsoft
- Match score: 0.752
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/notary-v2-supply-chain-security-for-containers/SZMbuirEQVU.txt
- Transcript chars: 26941
- Keywords: signature, containers, docker, container, registry, artifact, registries, content, notary, security, environment, software, actually, important, reference, around, artifacts, signatures

### Resumo baseado na transcript

hello and welcome to kubecon um today we're going to talk about nature v2 supply chain security for containers i'm justin cormack i'm the cto at docker i'm a maintainer on notary and a member of cncf technical oversight committee i work a lot with six security and i'm really i've been working on supply chain stuff for quite some time and this is steve hi i'm steve lasker i'm a pm architect in azure work on container registries including acr and mcr um and as part of that you

### Excerpt da transcript

hello and welcome to kubecon um today we're going to talk about nature v2 supply chain security for containers i'm justin cormack i'm the cto at docker i'm a maintainer on notary and a member of cncf technical oversight committee i work a lot with six security and i'm really i've been working on supply chain stuff for quite some time and this is steve hi i'm steve lasker i'm a pm architect in azure work on container registries including acr and mcr um and as part of that you know with registries we're sitting at the middle of all of the services in azure that use containers from production services the devtools so we see quite a lot of different scenarios we talked to a lot of customers around the various scenarios and of course one of them has been around how do i sign my content so that as i consume upstream content from the community and bring it into my environment how do i know what's that and how do i promote it within my environment even though it still has the same integrity so notary's been a key focus for us and it kind of builds on the stuff we did with oci artifacts i'm a tob member for oci and a maintainer for oci artifacts which is how we leverage registries to store all kinds of content and we'd like to be able to sign all kinds of content uh so that there's uh integrity around it so with that so what why are we doing this so until last year really when you i used to have a much longer piece in here about why i suppose your insecurity but sailor wins last year really um kind of uh help people understand what was what was going on that someone could attack some software attack your supplier and insert some you know insert malicious code into their software you would bring it on prem and it would start attacking you this is kind of not what you want to happen um and it's really brought this into a sort of public view and it's like something that uh people are much more aware of now um the solarwinds one was interesting because it was this attack um well where the attack happened was interesting like they they had to figure that out it wasn't based on containers it was an old different technology but the binaries were assigned so they were able to realize that this wasn't some kind of production deployment environment hack it was it actually came from the build system and having that signed content that was deployed gave them the forensics to be able to go back and figure out where the the breach happened and that's something we need to be able
