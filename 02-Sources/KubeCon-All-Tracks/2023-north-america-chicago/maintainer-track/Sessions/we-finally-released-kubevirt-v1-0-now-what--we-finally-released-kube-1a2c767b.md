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
themes: ["AI ML", "Community Governance"]
speakers: ["Fabian Deutsch", "Red Hat", "Ryan Hallisey", "Nvidia"]
sched_url: https://kccncna2023.sched.com/event/1R2q6/we-finally-released-kubevirt-v10-now-what-fabian-deutsch-red-hat-ryan-hallisey-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=We+Finally+Released+KubeVirt+V1.0.+Now+What%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# We Finally Released KubeVirt V1.0. Now What? - Fabian Deutsch, Red Hat & Ryan Hallisey, Nvidia

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Fabian Deutsch, Red Hat, Ryan Hallisey, Nvidia
- Schedule: https://kccncna2023.sched.com/event/1R2q6/we-finally-released-kubevirt-v10-now-what-fabian-deutsch-red-hat-ryan-hallisey-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=We+Finally+Released+KubeVirt+V1.0.+Now+What%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre We Finally Released KubeVirt V1.0. Now What?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2q6/we-finally-released-kubevirt-v10-now-what-fabian-deutsch-red-hat-ryan-hallisey-nvidia
- YouTube search: https://www.youtube.com/results?search_query=We+Finally+Released+KubeVirt+V1.0.+Now+What%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=33h9hpbtPhI
- YouTube title: We Finally Released KubeVirt V1.0. Now What? - Fabian Deutsch, Red Hat & Ryan Hallisey, Nvidia
- Match score: 0.736
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/we-finally-released-kubevirt-v1-0-now-what/33h9hpbtPhI.txt
- Transcript chars: 33330
- Keywords: cubert, features, release, actually, virtual, virtualization, running, important, interesting, concept, little, native, releases, machines, feature, change, measure, traditional

### Resumo baseado na transcript

okay uh so in uh in preparation for this talk I was actually doing a little bit of research about uh kord's history a little bit about the timeline and um I actually got a little sidetracked I ended up stumbling upon a little bit of history about virtualization in general and I kind of thought this was interesting so I figured I'd share it um virtualization its concept has been around a long time and what I was reading is that virtualization in some form has been around since

### Excerpt da transcript

okay uh so in uh in preparation for this talk I was actually doing a little bit of research about uh kord's history a little bit about the timeline and um I actually got a little sidetracked I ended up stumbling upon a little bit of history about virtualization in general and I kind of thought this was interesting so I figured I'd share it um virtualization its concept has been around a long time and what I was reading is that virtualization in some form has been around since around the 1960s I'll take the internet's word for it so it's been around a long time um as a concept and when you think about the idea of virtualization as as a technology and and you put cubert on the timeline of different use cases and ways to use Virtual virtual machines it's kind of interesting to think about cubert is a uh concept of running virtual machines on top of a cloud native environment running virtual machines on top of kubernetes um so actually running that virtual machine inside a pod so really interesting concept when you when you think about it that way and so kind of going back to um cubert and when when the um you know the project started was around 2016 uh began as a concept and eventually became project and uh over the last seven years or so this this project has spent a lot of time uh and over this long long journey to uh eventually reach V1 uh which is a really exciting Milestone and accomplishment by the community and so that's what we're going to talk about today some of what that means for you as an end user what that means for you as someone in the community what that means for you as a developer uh when we say V1 uh something has been released and then we're going to talk a little bit about what's next um you know now that v1's released what can you expect to to see next from cubert so when we were coming up with this V1 release and cutting the the V1 release we wanted to come up with a theme what were we going to focus on when we release cubert and the theme we came came up with was we wanted to align with kubernetes so what does that mean aligning with kubernetes well it means a lot of different things um and one of the things that uh we we first focused on was uh the release Cadence cubert as a project has been releasing on a monthly Cadence for almost six years and this made a lot of sense for a long period of time if you can imagine cu's got a lot of a lot of features it needs to develop so there's a lot of Maintenance there's a lot of uh feature vel
