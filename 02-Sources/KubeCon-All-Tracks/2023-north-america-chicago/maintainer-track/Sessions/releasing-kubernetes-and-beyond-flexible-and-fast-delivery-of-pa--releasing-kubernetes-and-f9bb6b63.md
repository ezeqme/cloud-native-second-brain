---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "Kubernetes Core", "Community Governance"]
speakers: ["Grace Nguyen", "University of Waterloo", "Adolfo Garcia Veytia", "Chainguard", "Jim Angel", "Google", "John Anderson", "Ditto"]
sched_url: https://kccncna2023.sched.com/event/1RQeC/releasing-kubernetes-and-beyond-flexible-and-fast-delivery-of-packages-grace-nguyen-university-of-waterloo-adolfo-garcia-veytia-chainguard-jim-angel-google-john-anderson-ditto
youtube_search_url: https://www.youtube.com/results?search_query=Releasing+Kubernetes+and+Beyond%3A+Flexible+and+Fast+Delivery+of+Packages+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Releasing Kubernetes and Beyond: Flexible and Fast Delivery of Packages - Grace Nguyen, University of Waterloo; Adolfo Garcia Veytia, Chainguard; Jim Angel, Google; John Anderson, Ditto

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Grace Nguyen, University of Waterloo, Adolfo Garcia Veytia, Chainguard, Jim Angel, Google, John Anderson, Ditto
- Schedule: https://kccncna2023.sched.com/event/1RQeC/releasing-kubernetes-and-beyond-flexible-and-fast-delivery-of-packages-grace-nguyen-university-of-waterloo-adolfo-garcia-veytia-chainguard-jim-angel-google-john-anderson-ditto
- Busca YouTube: https://www.youtube.com/results?search_query=Releasing+Kubernetes+and+Beyond%3A+Flexible+and+Fast+Delivery+of+Packages+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Releasing Kubernetes and Beyond: Flexible and Fast Delivery of Packages.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1RQeC/releasing-kubernetes-and-beyond-flexible-and-fast-delivery-of-packages-grace-nguyen-university-of-waterloo-adolfo-garcia-veytia-chainguard-jim-angel-google-john-anderson-ditto
- YouTube search: https://www.youtube.com/results?search_query=Releasing+Kubernetes+and+Beyond%3A+Flexible+and+Fast+Delivery+of+Packages+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hor5p8TjjvE
- YouTube title: Releasing Kubernetes and Beyond: Flexible and Fast Delivery of Packages
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/releasing-kubernetes-and-beyond-flexible-and-fast-delivery-of-packages/hor5p8TjjvE.txt
- Transcript chars: 17515
- Keywords: release, packages, process, google, everything, releases, looking, working, engineering, projects, joining, together, tooling, images, package, better, little, helping

### Resumo baseado na transcript

all right we're starting for real this time welcome um thank you for coming to the talk I know it's the last on the last day of the conference we're all from sick release and we'll be sharing stuff about the release team and release engineering so my name is Grace I let the uh 1.28 kuat release that came out in August and I've been on the release team for over two years now hey I'm John Anderson I'm an SRE at a company called ditto and I'm the

### Excerpt da transcript

all right we're starting for real this time welcome um thank you for coming to the talk I know it's the last on the last day of the conference we're all from sick release and we'll be sharing stuff about the release team and release engineering so my name is Grace I let the uh 1.28 kuat release that came out in August and I've been on the release team for over two years now hey I'm John Anderson I'm an SRE at a company called ditto and I'm the newest member of the release team I've been on the last two releases 128 and now 129 and my name is Alo Garcia I'm a an open source engineer with chenard and I am one of the technical leads with kubernetes Sig release and as R said like we're so honored to have you here as in the very very last minute of the conference uh so I guess thank you to all of you and to the thousands looking at us on YouTube so cool so let's begin with what is Sig relase so as some of you may know kubernetes is organized itself in several special interest groups uh you have special interest groups for all sorts of things uh that compose the project we have one for storage which we have one for networking and we happen to be the group that takes care of releasing kubernetes every month um uh we have a clear uh and defined Mission uh which is establish a consumable interos spectable and secure supply chain for kubernetes um and but I I guess the way you can think about this is that we are the SE that groups together all of the contributors that are working on the release tooling and the processes that make uh bring you kubernetes every every month um SE releases SE release has two main sub projects one is the release engineering uh sub project which um I'm one of the uh technical leads together with Carlos here and I'm going to be talking about that and the other one is the release team uh which my colleagu here and going are going to talk about um this is our main entry point into the Sig uh we're going to have links for it at the end so you could say that uh Sig release is sort of two parts one part uh a wonderful group of uh volunteers that rotate constantly with every release and the the Machinery that powers all of the release processes and release engineering is a part that that takes care of that um uh the release engineering team takes care of the tooling that powers the kubernetes releases uh we also uh manage the release managers team uh which are are the group of uh contributors that uh take care of uh executing the tools to releas
