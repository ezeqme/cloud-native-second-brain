---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Keynote Sessions"
themes: ["Kubernetes Core"]
speakers: ["Clayton Coleman", "Architect for Kubernetes and OpenShift", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/id08/sponsored-keynote-kubernetes-as-the-control-plane-for-the-hybrid-cloud-clayton-coleman-architect-for-kubernetes-and-openshift-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Kubernetes+as+the+Control+Plane+for+the+Hybrid+Cloud+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Keynote: Kubernetes as the Control Plane for the Hybrid Cloud - Clayton Coleman, Architect for Kubernetes and OpenShift, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Clayton Coleman, Architect for Kubernetes and OpenShift, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/id08/sponsored-keynote-kubernetes-as-the-control-plane-for-the-hybrid-cloud-clayton-coleman-architect-for-kubernetes-and-openshift-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Kubernetes+as+the+Control+Plane+for+the+Hybrid+Cloud+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Kubernetes as the Control Plane for the Hybrid Cloud.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/id08/sponsored-keynote-kubernetes-as-the-control-plane-for-the-hybrid-cloud-clayton-coleman-architect-for-kubernetes-and-openshift-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Kubernetes+as+the+Control+Plane+for+the+Hybrid+Cloud+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Xd0uzgZqYgk
- YouTube title: Sponsored Keynote: Kubernetes as the Control Plane for the Hybrid Cloud - Clayton Coleman
- Match score: 0.977
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-keynote-kubernetes-as-the-control-plane-for-the-hybrid-cloud/Xd0uzgZqYgk.txt
- Transcript chars: 6331
- Keywords: cluster, control, clusters, application, declarative, applications, details, pretty, simple, without, prototype, within, config, integration, deployment, kubecon, needed, excite

### Resumo baseado na transcript

my previous kubecon talks focused on how boring kubernetes needed to be after a pretty crazy year feel this is the perfect time to talk about the ideas that really excite me ideas that have evolved within and alongside our community that i think can help application authors and operation teams alike seven years ago we began this project around a really simple idea orchestration of containers with a declarative api model designed to capture intent our machines would realize we heard clearly from early adopters make that model easily

### Excerpt da transcript

my previous kubecon talks focused on how boring kubernetes needed to be after a pretty crazy year feel this is the perfect time to talk about the ideas that really excite me ideas that have evolved within and alongside our community that i think can help application authors and operation teams alike seven years ago we began this project around a really simple idea orchestration of containers with a declarative api model designed to capture intent our machines would realize we heard clearly from early adopters make that model easily extensible to new concepts which has helped us standardize how teams build and run all types of applications but we can't rest on our laurels what do we need to do to improve security make new application abstractions possible and continue to improve resiliency and operational flexibility and help simplify what's still pretty complicated today to many here kubernetes the container orchestrator and kubernetes declarative api engine may seem inextricably linked but what if we reverse direction what if we could let kubernetes the api take the lead what would kubernetes look like without pods what would be the basic tools in our podlust toolbox these are some pretty powerful tools namespaces can subdivide our work rbac can protect it secrets and config maps can accept generic config and crds can allow us to define all the new apis we need so what you're seeing is a really simple prototype of how a cube-like control plane might behave kubernetes api without pods containers or nodes but all the extensibility client support and tooling needed to integrate declarative apis describing a much more integrated world so what would we do with this lightweight control plane uh well we can do quite a lot not knowing about pods the crds i'm installing today are just some examples of existing integrations to cube that program things off clusters programming cloud resources external dns or load balancing that coordinates across clusters or even provisioning databases to connect back to apps on the cluster and a key challenge for all these integrations today is they require you to know who owns the integration a less opinionated control plane could actually be a central spot that helps centralize these tools and provides new avenues for coordination after all they'd just be declarative kubernetes compatible apis um obviously as we put more and more stuff together things get more complicated if we just put everything together in a higher level contr
