---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Ľuboslav Pivarč", "Red Hat", "Alay Patel", "NVIDIA"]
sched_url: https://kccnceu2025.sched.com/event/1td18/how-we-tackle-kubevirts-growth-and-scalability-luboslav-pivarc-red-hat-alay-patel-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Tackle+KubeVirt%E2%80%99s+Growth+and+Scalability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How We Tackle KubeVirt’s Growth and Scalability - Ľuboslav Pivarč, Red Hat & Alay Patel, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Ľuboslav Pivarč, Red Hat, Alay Patel, NVIDIA
- Schedule: https://kccnceu2025.sched.com/event/1td18/how-we-tackle-kubevirts-growth-and-scalability-luboslav-pivarc-red-hat-alay-patel-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Tackle+KubeVirt%E2%80%99s+Growth+and+Scalability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How We Tackle KubeVirt’s Growth and Scalability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td18/how-we-tackle-kubevirts-growth-and-scalability-luboslav-pivarc-red-hat-alay-patel-nvidia
- YouTube search: https://www.youtube.com/results?search_query=How+We+Tackle+KubeVirt%E2%80%99s+Growth+and+Scalability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xwGDxqI_3Nk
- YouTube title: How We Tackle KubeVirt’s Growth and Scalability - Ľuboslav Pivarč, Red Hat & Alay Patel, NVIDIA
- Match score: 0.777
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-we-tackle-kubevirts-growth-and-scalability/xwGDxqI_3Nk.txt
- Transcript chars: 20557
- Keywords: cubeword, running, actually, change, simulation, process, controller, design, metrics, object, looking, wanted, called, release, started, cublet, control, upstream

### Resumo baseado na transcript

Um, welcome to the talk um, how to tackle cubits growth and scalability. Yeah, it's a quite an interesting project I think but I'm biased obviously. But basically um we still have those root approvers um that uh do uh take a look at um at special things but yeah this helps us to scale uh more into um uh yeah um spreading the load over everyone. So uh what we did next was we wanted to have like a um special process to look at designs that would be introduced. We had initially we had like the evolution of like a like a design proposal process inside the community repository. Um but that didn't scale as good because um this was inside the community repository.

### Excerpt da transcript

Hello everyone. Um, welcome to the talk um, how to tackle cubits growth and scalability. Um, I am not lubis pir. I'm filling in for him. My name is Danny Hill. I'm from uh, Red Hat. Um, this is Ryan. Um, sorry Ali, sorry for that. Do you want to introduce yourself? Hi everyone. I am Alai Patel. I'm from um, Nvidia. Um, we run cubeird at scale. So I'm going to be talking about it um after Daniel. Yeah. And I'm part of the open virtualization team. Um my main concern is the Cubert upstream CI system. So um how many people uh in this room are already using Cubert? Okay. A couple. How many have heard of that? That's nice. Great. Yeah, it's a quite an interesting project I think but I'm biased obviously. So um yeah, let me start um to talk a bit about the community evolution that we have seen and that we have um uh so where we have tried to improve things so that it works better for the community. Um so first of all in uh 2024 we had the situation where we only had like root approvers who could um were responsible for everything to go in somehow.

Uh this obviously didn't scale because there were very few approvers. So basically you know um you most of you are probably familiar with the system like LGTM and a proof um from the Kubernetes ecosystem right or do I have to explain that okay seems to be okay um so um as I said uh basically we only had root approvers and this didn't scale so we were looking at how we can improve that situation so we were going with the idea from the upstream so from the kubernetes as the ecosystem to uh ecosystem to look into uh SIGs and we basically came up with um like uh how many six do we have? Five or six I think. So like compute um network storage um also scaling um and observability. Did I forget anything? No. Yeah. Okay. Um these are like the uh the sigs that look at the special aspects that are relevant for that SIG. But we have also like the uh concept of SIG chairs which actually need to interact with other SIGs and to coordinate with them. But basically um we still have those root approvers um that uh do uh take a look at um at special things but yeah this helps us to scale uh more into um uh yeah um spreading the load over everyone.

So uh what we did next was we wanted to have like a um special process to look at designs that would be introduced. We had initially we had like the evolution of like a like a design proposal process inside the community repository. Um but that didn't scale as good because um this was inside
