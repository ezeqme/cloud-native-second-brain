---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Tutorials"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Robert Vasek", "Clyso GmbH", "Nabarun Pal", "Independent", "Varsha Narsing", "Red Hat", "Marko Mudrinic", "Kubermatic GmbH", "Mangirdas Judeikis", "Cast AI"]
sched_url: https://kccnceu2025.sched.com/event/1tx6b/tutorial-exploring-multi-tenant-kubernetes-apis-and-controllers-with-kcp-robert-vasek-clyso-gmbh-nabarun-pal-independent-varsha-narsing-red-hat-marko-mudrinic-kubermatic-gmbh-mangirdas-judeikis-cast-ai
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Exploring+Multi-Tenant+Kubernetes+APIs+and+Controllers+With+Kcp+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Tutorial: Exploring Multi-Tenant Kubernetes APIs and Controllers With Kcp - Robert Vasek, Clyso GmbH; Nabarun Pal, Independent; Varsha Narsing, Red Hat; Marko Mudrinic, Kubermatic GmbH; Mangirdas Judeikis, Cast AI

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Tutorials]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Robert Vasek, Clyso GmbH, Nabarun Pal, Independent, Varsha Narsing, Red Hat, Marko Mudrinic, Kubermatic GmbH, Mangirdas Judeikis, Cast AI
- Schedule: https://kccnceu2025.sched.com/event/1tx6b/tutorial-exploring-multi-tenant-kubernetes-apis-and-controllers-with-kcp-robert-vasek-clyso-gmbh-nabarun-pal-independent-varsha-narsing-red-hat-marko-mudrinic-kubermatic-gmbh-mangirdas-judeikis-cast-ai
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Exploring+Multi-Tenant+Kubernetes+APIs+and+Controllers+With+Kcp+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Tutorial: Exploring Multi-Tenant Kubernetes APIs and Controllers With Kcp.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx6b/tutorial-exploring-multi-tenant-kubernetes-apis-and-controllers-with-kcp-robert-vasek-clyso-gmbh-nabarun-pal-independent-varsha-narsing-red-hat-marko-mudrinic-kubermatic-gmbh-mangirdas-judeikis-cast-ai
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Exploring+Multi-Tenant+Kubernetes+APIs+and+Controllers+With+Kcp+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Fb_3dWJdY9I
- YouTube title: Tutorial: Exploring Multi-Tenant Kubernetes APIs and Controllers With Kcp
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/tutorial-exploring-multi-tenant-kubernetes-apis-and-controllers-with-k/Fb_3dWJdY9I.txt
- Transcript chars: 44425
- Keywords: workspace, create, cluster, created, provider, workspaces, config, export, cowboy, resource, workshop, database, consumer, particular, posgress, resources, terminal, basically

### Resumo baseado na transcript

So we're going to try to keep it very as much informal as we can whereas quite a few of us. So once we end up with our part on the stage, we're gonna start mingling around. Very happy to be with you all here today and to learn a bit more KCP as well. Uh I'm in and around the Kubernetes ecosystem with operators and things and I was a part of the KCP team when it was first introduced in design. So KC in order to not confuse too much uh like KCP with Kubernetes and how Kubernetes works. So if you know how Kubernetes API server starts, it's very similar to what happens when you start Kubernetes API server plus a few additional controllers to make sure u certain things are running well in the control plane.

### Excerpt da transcript

Hello everybody. Please grab a seat. As you might notice in the agenda, that's a workshop tutorial. So if you want really hands-on experience, get your laptops out. So we're going to try to keep it very as much informal as we can whereas quite a few of us. So once we end up with our part on the stage, we're gonna start mingling around. So if you have a question or something is broken, ask a hand. I'm very cautious. There is 500 of you and five of us. This means everybody of us gets a hundred. So please help your table, friends, co-workers, colleagues if you can. So that's and we have few other KCP friends and family. So if you have a question during the like silent time and we catching up there's a microphone in the center. Just grab it, ask it. So let's not wait for the Q&A at the end. There's no microphone actually. That's one center. There is. Yeah, cool. So we're good to start. So welcome to exploring multi-tenant Kubernetes APIs and controllers with KCP. The link will be always in the footnote of the slides.

This is where we be hanging out. But before that, a bit of intro. So prerequisites, we will require four shell terminals, Linux, MacBooks. We strongly recommend using GitHub code spaces. We're going to show how to set it up. Hence, everybody has the same environment and we can debug faster. But if you feel comfortable, use whatever terminal you like. And for the starters, git is basically what we need and we're setting up everything else. A bit of intros. I'm MJ. I'm staff engineer at Castai and KCP maintainer. So been with KCP for the last four, five years. Hello. Uh I'm Robert. I'm working for Clyo, a company that's primarily focused on storage defi uh software defined storage and Kubernetes. uh but recently we started investing time into KCP as well and I've started on the project not too long ago about four five months uh but still learning we are even today learning to together and uh let's see hello everyone I am Mark Mudrinich I am a senior software engineer at cubmatic and as of a recent recently a KCP contributor.

Very happy to be with you all here today and to learn a bit more KCP as well. Hi everyone. Uh I'm Navarun. I have been uh contributing to Kubernetes for the last uh six years. Um I maintain a few areas in the project. Um currently um I'm also a chair of sik contrib and apart from that I contribute uh to KCP and uh try to build products around it and that's all. Hey everyone, I'm Vasha. I work as a software engineer at Red Hat.
