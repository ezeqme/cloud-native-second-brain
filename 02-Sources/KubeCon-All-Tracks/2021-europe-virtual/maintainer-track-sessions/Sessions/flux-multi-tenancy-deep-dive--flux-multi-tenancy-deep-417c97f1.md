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
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Philip Laine", "Xenit"]
sched_url: https://kccnceu2021.sched.com/event/iona/flux-multi-tenancy-deep-dive-philip-laine-xenit
youtube_search_url: https://www.youtube.com/results?search_query=Flux%3A+Multi-tenancy+Deep+Dive+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Flux: Multi-tenancy Deep Dive - Philip Laine, Xenit

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Philip Laine, Xenit
- Schedule: https://kccnceu2021.sched.com/event/iona/flux-multi-tenancy-deep-dive-philip-laine-xenit
- Busca YouTube: https://www.youtube.com/results?search_query=Flux%3A+Multi-tenancy+Deep+Dive+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Flux: Multi-tenancy Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iona/flux-multi-tenancy-deep-dive-philip-laine-xenit
- YouTube search: https://www.youtube.com/results?search_query=Flux%3A+Multi-tenancy+Deep+Dive+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=F7B_TBcIyl8
- YouTube title: Flux: Multi-tenancy Deep Dive - Philip Laine, Xenit
- Match score: 0.827
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/flux-multi-tenancy-deep-dive/F7B_TBcIyl8.txt
- Transcript chars: 20935
- Keywords: cluster, flux, repository, tenant, deployment, around, commit, change, application, running, actually, changes, manifest, pipeline, production, status, configuration, started

### Resumo baseado na transcript

hello and thank you for joining this flex deep dive session my name is philip lane and i work as a devops engineer at senate we are a swedish based company who builds developer-centered experiences around cloud kubernetes and gitops i am also part of the flux maintainer team and that's what i'm here to talk to you about today so what is flux well flux is a tool for keeping kubernetes clusters in sync with sources of configuration what this means is that in basic terms that that you

### Excerpt da transcript

hello and thank you for joining this flex deep dive session my name is philip lane and i work as a devops engineer at senate we are a swedish based company who builds developer-centered experiences around cloud kubernetes and gitops i am also part of the flux maintainer team and that's what i'm here to talk to you about today so what is flux well flux is a tool for keeping kubernetes clusters in sync with sources of configuration what this means is that in basic terms that that you have configuration stored in in some sort of external repository for the most of the time this will be git and then you have flux the tool running inside of your kubernetes cluster that continuously synchronizes with that external repository and applies it into the cluster this has the benefits partially due to auditability when it comes to git because you have a history of changes that you can see who made changes to what configuration but also an observability uh perspective where it is very easy to look inside the git repository and see what is actually being applied inside of the cluster so this is a a quick overview of how it might look like to work with flux so in one end you have your deployment manifest that you are going to commit to a git repository on the other end of this you have flux flex is pulling the git repository constantly looking for changes if a change is detected here it will apply it to the cluster so as you can see here you have your deployment manifest on one end and then your deployment on the other and this also works in the sense that if somebody were to go in and delete this deployment in the cluster flux will eventually detect the drift between what is wanted or expected and what is actually there in cluster and reapply the deployment you have the possibility of really doing this as simple or as complex as possible in this example here it's very simple but you can make you can scale this out to run across multiple teams and and have different types of functionality and automation but there isn't really any requirement to do so so that's kind of the beauty of flux is that it works for smaller teams but also works for large enterprises at the same time quickly before we get started i just want to go through a quick timeline of flux and flagger so currently flex is incubation project it has 14 containers at five companies but it started it's been around for a while now so in 2016 it started developing at weworks uh since then we've had uh the fighter
