---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Steven Wong", "Michael Gasch", "VMware"]
sched_url: https://kccnceu2022.sched.com/event/yttR/optimize-kubernetes-on-vsphere-with-event-driven-automation-steven-wong-michael-gasch-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Optimize+Kubernetes+on+vSphere+with+Event-Driven+Automation+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Optimize Kubernetes on vSphere with Event-Driven Automation - Steven Wong & Michael Gasch, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Steven Wong, Michael Gasch, VMware
- Schedule: https://kccnceu2022.sched.com/event/yttR/optimize-kubernetes-on-vsphere-with-event-driven-automation-steven-wong-michael-gasch-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Optimize+Kubernetes+on+vSphere+with+Event-Driven+Automation+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Optimize Kubernetes on vSphere with Event-Driven Automation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yttR/optimize-kubernetes-on-vsphere-with-event-driven-automation-steven-wong-michael-gasch-vmware
- YouTube search: https://www.youtube.com/results?search_query=Optimize+Kubernetes+on+vSphere+with+Event-Driven+Automation+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NJYBwJemdoY
- YouTube title: Optimize Kubernetes on vSphere with Event-Driven Automation - Steven Wong & Michael Gasch, VMware
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/optimize-kubernetes-on-vsphere-with-event-driven-automation/NJYBwJemdoY.txt
- Transcript chars: 41686
- Keywords: events, vsphere, vcenter, function, virtual, running, information, little, environment, actually, vmware, question, integration, machine, happens, basically, already, whatever

### Resumo baseado na transcript

okay we're going to get started um hi welcome to the kubecon 2022 event in valencia i'm steve wong and i'm joined by michael gash you're about to learn about some cool new tech that lets you enable better integration of kubernetes workloads with vsphere and this is brought to you by the vmware user group a word about this user group we're inclusive of all users running all kubernetes on vmware infrastructure so i don't want you to be mistaken thinking thinking that since the two of us happen

### Excerpt da transcript

okay we're going to get started um hi welcome to the kubecon 2022 event in valencia i'm steve wong and i'm joined by michael gash you're about to learn about some cool new tech that lets you enable better integration of kubernetes workloads with vsphere and this is brought to you by the vmware user group a word about this user group we're inclusive of all users running all kubernetes on vmware infrastructure so i don't want you to be mistaken thinking thinking that since the two of us happen to be with vmware that we're only talking vmware kubernetes distributions if you're running red hat open shift or rancher or whatever what we're going to talk about here still applies this is completely generic it should work with any compliant kubernetes running on the vsphere hypervisor and this group itself if you elect to join the community all the stuff we cover is like that it's completely neutral as to the type of kubernetes you're running um we're going to start with a little background explaining why a tool that monitors activities spanning multiple layers of your stack from infrastructure up to kubernetes might be useful or even essential and then we're going to explain the tool mostly through demonstrations uh a strong reason to retain your own on-prem infrastructure is a sovereign sovereign cloud requirement where you can ensure data locality and local governance you know kubernetes can run either on on-prem things like vsphere or in a public cloud with kubernetes and with hypervisor infrastructure the goal is to maintain a working illusion so that operations run consistently across locations and across variations over time so these abstraction layers can simplify the job of the components above them but they do need to make some choices as to how to support what runs on top in relation to the layers that are below vsphere is designed to allow vms to opt in to a high availability model that rigorously attempts to defend workloads from going down the kubernetes model is more tuned to an expectation that a workload has an architecture that allows for individual components and individual containers to go down while still maintaining an acceptable level of service there are classes of applications better suited to the vsphere model others better suited to the kubernetes model and if you're running an on-prem installation you likely have both operating and they might need to interoperate a lot of on-prem installations host legacy vm-based services which interact
