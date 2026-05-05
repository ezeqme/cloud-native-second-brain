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
themes: ["Kubernetes Core"]
speakers: ["Leigh Capili", "Tanja Ulianova", "Flox"]
sched_url: https://kccnceu2025.sched.com/event/1tx6z/tutorial-workshop-developing-as-a-team-for-kubernetes-with-nix-and-flox-leigh-capili-tanja-ulianova-flox
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Workshop%3A+Developing+as+a+Team+for+Kubernetes+With+Nix+and+Flox+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Tutorial: Workshop: Developing as a Team for Kubernetes With Nix and Flox - Leigh Capili & Tanja Ulianova, Flox

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Tutorials]]
- Temas: [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Leigh Capili, Tanja Ulianova, Flox
- Schedule: https://kccnceu2025.sched.com/event/1tx6z/tutorial-workshop-developing-as-a-team-for-kubernetes-with-nix-and-flox-leigh-capili-tanja-ulianova-flox
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Workshop%3A+Developing+as+a+Team+for+Kubernetes+With+Nix+and+Flox+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Tutorial: Workshop: Developing as a Team for Kubernetes With Nix and Flox.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx6z/tutorial-workshop-developing-as-a-team-for-kubernetes-with-nix-and-flox-leigh-capili-tanja-ulianova-flox
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Workshop%3A+Developing+as+a+Team+for+Kubernetes+With+Nix+and+Flox+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NnYtnUeJi7U
- YouTube title: Tutorial: Workshop: Developing as a Team for Kubernetes With Nix an... Leigh Capili & Tanja Ulianova
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/tutorial-workshop-developing-as-a-team-for-kubernetes-with-nix-and-flo/NnYtnUeJi7U.txt
- Transcript chars: 58297
- Keywords: environment, flux, container, actually, docker, application, little, folder, postgress, inside, dependencies, database, version, package, packages, scrapbook, probably, flocks

### Resumo baseado na transcript

Today we are talking a little bit about something that you may have or you may have not heard about. Uh and then we're going to be fusing that with an idea that you probably have heard about. this is uh going to run a Kubernetes cluster uh and so it's nice to have a little bit of headroom uh that will use your core seconds uh on your GitHub account faster. uh providing you your Kubernetes command line tools, providing kind the Kubernetes cluster itself as well as a bunch of developer tools uh and getting everything set up uh in the dev container and then using Microsoft's init RC and hooks and stuff to start the Kubernetes cluster for you as well as the Nyx statement. Uh but uh there is another repository that has other folders with other micro demos that we can play with. You need to click that and you need to add scale nyx githops to the workspace.

### Excerpt da transcript

Hi friends. How's everyone doing? Yeah. Uh my name is Lee. Um thanks for so much for coming to the tutorial today. Today we are talking a little bit about something that you may have or you may have not heard about. Uh and then we're going to be fusing that with an idea that you probably have heard about. Uh we're going to be talking a little bit about Nyx. Um we had any Nyx users in the room? Oh, wow. All right. So, we're in good company. Now, there's like a half of the room that raised their hand. Uh, and then there's probably another half of the room that has maybe even not heard of Nyx or never touched it or used it before. Uh, and then I want to sort of paint a little bit of the visions and the possibilities. So, I'm going to be real with y'all. I am in the lab right now. Like, I am doing a lot of R&D. Uh, and I wouldn't say that I'm maybe as experienced of a Nyx user as some of the other folks in this room. Uh, but we are all in good company and we're going to run some experiments, uh, learn some principles and try to hack some stuff together.

Uh, does that feel like a good vibe for today? We've got 75 minutes to, uh, get our hands on the keyboard and mess around. All right, the other thing that I am much much more authoritative in is GitOps, right? So we have Nyx which is a completely um kind of separate idea from lots of cloudnative stuff but there where there's a lot of overlap. Nyx is this sort of functional package manager that lets you build reproducible software in a hermetic way. Uh and then you have a bunch of addressed blobs that you can get from caches and you can assemble your programs with graphs of dependencies. Uh so Nyx is all about building software and doing it in a programmatic and a declarative way. Um GitOps is about declaring your infrastructure in a way that is collaborative and sharable. And so uh we're going to be looking at Nyx. Uh we're going to be you using a um easeofuse layer on top of Nyx uh developed by the fine and talented folks at Flocks. Um I did used to work with them so I'm a little bit biased. Uh but I I still use their software every day.

It's very good. Um great way to share Nyx with your team. Uh and then I work at Control Plane. Again, my name is Lee. Uh I think there's two control planes. I'll just get this out of the way. Control plane IO. Um, and I control plane employs me to help maintain the Flux project. I know that I I just mentioned Flux earlier. Um, and now I am telling you that I have I work on a
