---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Experience"
themes: ["Community Governance"]
speakers: ["Kashif Khan", "Ericsson", "Dmitry Tantsur", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2CW7E/metal3ios-path-to-cncf-incubation-governance-processes-and-community-kashif-khan-ericsson-dmitry-tantsur-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Metal3.io%E2%80%99s+Path+to+CNCF+Incubation%3A+Governance%2C+Processes%2C+and+Community+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Metal3.io’s Path to CNCF Incubation: Governance, Processes, and Community - Kashif Khan, Ericsson & Dmitry Tantsur, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Kashif Khan, Ericsson, Dmitry Tantsur, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2CW7E/metal3ios-path-to-cncf-incubation-governance-processes-and-community-kashif-khan-ericsson-dmitry-tantsur-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Metal3.io%E2%80%99s+Path+to+CNCF+Incubation%3A+Governance%2C+Processes%2C+and+Community+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Metal3.io’s Path to CNCF Incubation: Governance, Processes, and Community.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7E/metal3ios-path-to-cncf-incubation-governance-processes-and-community-kashif-khan-ericsson-dmitry-tantsur-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Metal3.io%E2%80%99s+Path+to+CNCF+Incubation%3A+Governance%2C+Processes%2C+and+Community+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fqlARu6-NEQ
- YouTube title: Metal3.io’s Path To CNCF Incubation: Governance, Processes, and Community - Kashif Khan, Ericsson
- Match score: 0.948
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/metal3-ios-path-to-cncf-incubation-governance-processes-and-community/fqlARu6-NEQ.txt
- Transcript chars: 29806
- Keywords: actually, process, security, governance, incubation, working, projects, defined, important, itself, making, getting, processes, review, inside, reviewer, release, specifically

### Resumo baseado na transcript

So uh my plan is to talk about metal cubes path to incubation but specifically the parts uh that are usually underestimated the the governance the security and the process itself. Uh most projects focus heavily on the code which also makes sense uh early on but then once your uh adoption uh or you want specifically adoption across companies and communities uh the code is actually not the bottleneck as we know anymore but uh So you have a bunch of servers on the right and you want to u like uh install Kubernetes on top of it and you want to also treat your uh servers as uh as Kubernetes resources but uh and that's the problem that we which doesn't scale well as we know and it's hard to integrate with cloud native workflows. So we actually represent the bare metal servers inside Kubernetes using our favorite YAML and then we have operators which are actually reconciling this YAML and giving back those states that we desire on on this YAML. The idea was just to build and show that this is possible the the that that I mean that something like provisioning and maintaining the life cycle in the kubernetes space is possible.

### Excerpt da transcript

Thanks a lot for joining this talk. So uh my plan is to talk about metal cubes path to incubation but specifically the parts uh that are usually underestimated the the governance the security and the process itself. Uh most projects focus heavily on the code which also makes sense uh early on but then once your uh adoption uh or you want specifically adoption across companies and communities uh the code is actually not the bottleneck as we know anymore but uh usually trust is and and trust comes uh from how your project is actually structured um also um how it behaves um over the time. So what I'm going to walk you through is how how we turned our project uh metal cubed into uh from a working system into um something that could actually pass the CNCF incubation process. I'm going to talk uh or repeat a few words like governance processes community security. The idea is not to bore you to death but uh so that you you leave with with these important terms when when you are at the end of this presentation.

So please bear with me. So um what we ran uh into was a pretty pretty common situation. Uh we had a working system uh real users, multiple uh companies uh contributing but then from uh outside things were looking really uh healthy and and things were working. But internally um a lot of this was actually uh implicit. implicit in a sense that the problem was if someone new is coming into the project and wanting to contribute or or adopt the project or even for CNCF TOC to review it uh they can't actually verify anything in a sense that um um and if they can't verify they can trust for example so the work was for us eventually turning into u like what we have as I said implicit process or tribal knowledge or um informal ownership to something like uh structured and and reviewable um um artifacts. That's that's the really the core of this journey. So before I jump into the actual thing uh like just I want to introduce myself I am one of the pro uh maintainers of this project metalcube.io and besides I wear a couple of other hats.

I'm co-chairing the uh technical advisory group for infrastructure uh together with Dylan who is also sitting here and I'm also an open source architect at the Ericson software technology. So quick context to so that everything else makes sense what this project usually does why is it existing in the CNCF ecosystem. So it provides this Kubernetes native bare metal uh provisioning. So you have a bunch of servers on the right and you w
