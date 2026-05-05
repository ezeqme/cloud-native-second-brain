---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Kubernetes Core"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQhV/kubernetes-style-apis-for-saas-like-control-planes-with-kcp-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes-style+APIs+for+SaaS-like+Control+Planes+with+kcp+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes-style APIs for SaaS-like Control Planes with kcp | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQhV/kubernetes-style-apis-for-saas-like-control-planes-with-kcp-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes-style+APIs+for+SaaS-like+Control+Planes+with+kcp+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes-style APIs for SaaS-like Control Planes with kcp | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQhV/kubernetes-style-apis-for-saas-like-control-planes-with-kcp-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes-style+APIs+for+SaaS-like+Control+Planes+with+kcp+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-P1kUo5zZR4
- YouTube title: Kubernetes-style APIs for SaaS-like Control Planes with kcp | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-style-apis-for-saas-like-control-planes-with-kcp-project-li/-P1kUo5zZR4.txt
- Transcript chars: 4835
- Keywords: provide, platform, clusters, logical, control, workload, orchestrator, certain, mongodb, containers, status, resources, crossplane, container, reason, sandbox, called, workspace

### Resumo baseado na transcript

hello everyone um we're very happy to be here this is MJ my name is Marvin we are two of the maintainers for kcp and today we would like to talk about building a kubernetes style API um well using kubernetes stle apis for building a Zas like control plane um first of all kubernetes is first and foremost uh a workload orchestrator for containers um but kubernetes through Cs and operators has become a fantastic way to provide additional apis to developers um the kubernetes API is declarative it

### Excerpt da transcript

hello everyone um we're very happy to be here this is MJ my name is Marvin we are two of the maintainers for kcp and today we would like to talk about building a kubernetes style API um well using kubernetes stle apis for building a Zas like control plane um first of all kubernetes is first and foremost uh a workload orchestrator for containers um but kubernetes through Cs and operators has become a fantastic way to provide additional apis to developers um the kubernetes API is declarative it is very easy to understand it is clear about inputs and outputs it has a lot of good patterns like the status sub resources and it makes it very easy and consistent to interact with the cuberes API because of that we as a community have long moved past just orchestrating containers with it just look at all the great cncf projects that are on stage today um we have crossplane coming up uh as an example um a lot of amazing tools have been built on top of an API that was meant to be a service sorry a container workload orchestrator because of all this greatness in the API um the reason for kcp or that was the reason for starting kcp um kcp was established as an open source project in 2021 so we have a couple of years under our belts uh in 2023 it transitioned to a community governance model and was later accepted into the scene of sandbox so late into last year um therefore this is our first cubec con um we're very excited to be here as CCF sandbox project um and because well it's our first one we didn't want to give a status update we wanted to show you why kcp might be interesting to you the question at the beginning of kcp was uh what if the kubernetes API moved past just the role as a container workload orchestrator um what if it became a platform for building um generic apis and serve them at scale and we want to show you what kcp as a control plan for that has to offer so first thing um kcp implements something that is called logical clusters so logical clusters are a way to provide kubernetes apis as a commodity um and they are implemented to something called workspaces each workspace has it is own kubernetes API um they are organized in a tree structure and you can basically easily navigate them with a cube CTL plugin we have written and each of them has its own API types resources and airbu and now MJ will tell you about how to manage apis in these logical clusters cool so kcp has way more features than this but this is just one example of use case how you can d
