---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Evangelista Tragni", "Devoteam"]
sched_url: https://kccnceu2026.sched.com/event/2CVy5/api-is-the-new-ssh-forging-a-zero-trust-vm-platform-on-kubernetes-evangelista-tragni-devoteam
youtube_search_url: https://www.youtube.com/results?search_query=API+is+the+New+SSH%3A+Forging+a+Zero-Trust+VM+Platform+on+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# API is the New SSH: Forging a Zero-Trust VM Platform on Kubernetes - Evangelista Tragni, Devoteam

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Evangelista Tragni, Devoteam
- Schedule: https://kccnceu2026.sched.com/event/2CVy5/api-is-the-new-ssh-forging-a-zero-trust-vm-platform-on-kubernetes-evangelista-tragni-devoteam
- Busca YouTube: https://www.youtube.com/results?search_query=API+is+the+New+SSH%3A+Forging+a+Zero-Trust+VM+Platform+on+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre API is the New SSH: Forging a Zero-Trust VM Platform on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVy5/api-is-the-new-ssh-forging-a-zero-trust-vm-platform-on-kubernetes-evangelista-tragni-devoteam
- YouTube search: https://www.youtube.com/results?search_query=API+is+the+New+SSH%3A+Forging+a+Zero-Trust+VM+Platform+on+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mVcBnbSfBrs
- YouTube title: API is the New SSH: Forging a Zero-Trust VM Platform on Kubernetes - Evangelista Tragni, Devoteam
- Match score: 0.903
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/api-is-the-new-ssh-forging-a-zero-trust-vm-platform-on-kubernetes/mVcBnbSfBrs.txt
- Transcript chars: 33606
- Keywords: machine, virtual, kubevirt, little, concept, feature, obviously, running, please, cluster, honest, cilium, another, application, network, virtualization, source, networking

### Resumo baseado na transcript

I will I have a little bit of technical information to share okay during this presentation. So my maybe my pacing will be a little bit speedy okay because I want to give time also to ask question and this is our own topic about you know virtual machine and running how to run that. A lot of Kubernetes also cluster run on virtual machine or so this is this means that virtual machine are heavily involved still in our environment and our data center. So what I should say is that obviously we want to we are using Kubernetes. So if we see possibility to move virtual machine also in Kubernetes I think this can be helpful too because we will have the same team with highly skilled in Kubernetes that we will we will manage also the virtual machine. So another thing that I want to add is that um maybe this started I think that the adoption in Kubernetes of virtual machine started with integrating database server with our stateless application.

### Excerpt da transcript

Welcome everyone. Thank you for joining the session. I will I have a little bit of technical information to share okay during this presentation. So my maybe my pacing will be a little bit speedy okay because I want to give time also to ask question and this is our own topic about you know virtual machine and running how to run that. So how to create a VM platform. So I will start soon okay. If someone is joining please feel free to sit everywhere. I see still some empty chairs here so First of all who I am I'm evangelist at Red Hat lead engineer for DevOps okay. I work currently in Luxembourg okay based but I mean not only working there but involved in this different project also in Germany in this case and today our schedule will be we will be talking a little bit about virtual machine. Anyone of us knows that we have a big big technology leader in virtualization like right now and this is obviously VMware. I think it would be hard to find someone that will say that VMware is not a technology leader there.

But anyone want to try maybe different road reduce some lock-in for some vendor or stuff like this so another road that could be opened is a having KubeVirt okay open source project of CNCF running this into Kubernetes. So during our session we will talk about of this shift against the open source world and also core capability of KubeVirt. What are also the limitation of KubeVirt some networking choice that we have there and to be honest I I will add some details that I discovered also yesterday announced by [clears throat] some other project so this will be interesting. So first of all we know a lot of environment have are heavily depending on hypervisor okay and technology that can virtualize our bare metal server. This is why because obviously there are a lot of application this is where we came from. We started with bare metal server and then we applied some virtualization there developed some virtual machine developed microservices and then adopted also microservices in container. >> [snorts] >> But we still have around maybe I will say 60% overall of the workload is still going on virtual machine.

A lot of Kubernetes also cluster run on virtual machine or so this is this means that virtual machine are heavily involved still in our environment and our data center. So what I what we see to be honest is since a few years there is a increasing adoption of open source okay all around the world and different sector also because before we had some som
