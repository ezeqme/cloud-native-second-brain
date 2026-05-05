---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Carlos Sanchez", "Alexandra Stoica", "Adobe"]
sched_url: https://kccnceu2025.sched.com/event/1txEO/debugging-envoy-tunnels-a-deep-dive-carlos-sanchez-alexandra-stoica-adobe
youtube_search_url: https://www.youtube.com/results?search_query=Debugging+Envoy+Tunnels%3A+A+Deep+Dive+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Debugging Envoy Tunnels: A Deep Dive - Carlos Sanchez & Alexandra Stoica, Adobe

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United Kingdom / London
- Speakers: Carlos Sanchez, Alexandra Stoica, Adobe
- Schedule: https://kccnceu2025.sched.com/event/1txEO/debugging-envoy-tunnels-a-deep-dive-carlos-sanchez-alexandra-stoica-adobe
- Busca YouTube: https://www.youtube.com/results?search_query=Debugging+Envoy+Tunnels%3A+A+Deep+Dive+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Debugging Envoy Tunnels: A Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEO/debugging-envoy-tunnels-a-deep-dive-carlos-sanchez-alexandra-stoica-adobe
- YouTube search: https://www.youtube.com/results?search_query=Debugging+Envoy+Tunnels%3A+A+Deep+Dive+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vrG5tBDsdd0
- YouTube title: Debugging Envoy Tunnels: A Deep Dive - Carlos Sanchez & Alexandra Stoica, Adobe
- Match score: 0.728
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/debugging-envoy-tunnels-a-deep-dive/vrG5tBDsdd0.txt
- Transcript chars: 17398
- Keywords: envoy, upstream, downstream, certificate, certificates, increase, connections, docker, compose, getting, scenarios, logs, logging, scenario, errors, content, running, debugging

### Resumo baseado na transcript

So whether you're using Envoy directly or you're using it through some service mesh, we're going to show you what things could go wrong and how to debug them and fix them. Hopefully something that you will find useful for your day-to-day work. It is a CMS, a content management system that helps enterprises build, manage and deliver content at scale. Um, customers can create multiple environments whenever they want and we have a huge bunch of those over 31 uh,000 environments, more than 200,000 Kubernetes deployment objects and over 20,000 namespaces across our clusters. We also uh it is an open-source edge and service proxy designed for cloud native applications. So the beauty of a is that it simplifies complex network problem problems.

### Excerpt da transcript

Hello, thanks for coming. Uh we're going to talk today about debugging envoy tunnels. So whether you're using Envoy directly or you're using it through some service mesh, we're going to show you what things could go wrong and how to debug them and fix them. Hopefully something that you will find useful for your day-to-day work. Okay. I'm Alexandra Stoka. I'm a site reliability engineer at Adobe. I want to say that this is my first CubeCon and first time as a speaker at a conference ever. So I'm very happy for that. I spend my days managing cloud infrastructure, automating everything inside and making sure mostly Kubernetes behaves. I like to say that for me is like coaching a team of unpredictable gymnasts because I used to be a gymnast myself. So, turns out balancing on a beam was great training for balancing performance, cost, and scalability in the cloud. The only difference when things go wrong in tech. At least I don't land on my face. And I'm Carlos. I'm a principal scientist at Adobe and I've been working with open source for a long time.

You probably heard about the Jenkeis Kubernetes plug-in that is been now over 10 years and I I started that and we're both working at Adobe Experience Manager Cloud Service. Okay, before we dive in, I want to tell you about what Adobe Experience Manager actually is. Short is AM. It is a CMS, a content management system that helps enterprises build, manage and deliver content at scale. You create your content, hit publish, and boom, it's out there for the world to see. Technically speaking, AM is a distributed Java OSJ application. Is it is it a it is a bunch of uh open source components from the Apache software foundation and one of the one of the coolest thing uh things about AM is its huge market of extension developers. That means people write code and then we run it on AM for them. customers used to uh run AM on premise or in other cloud setups, but a while ago we launch Adobe Experience Manager as a cloud service. Uh that means we run we handle everything for our customers, deployment, scaling, upgrades and all of that is running on Azure.

Right now we have over 60 clusters worldwide and since this is a content management system, people wanted to run uh their content as close as possible to their users. So we deploy them in almost any region we can get our hands on. What about our scale that we're operate operating at? Think of an AM environment as a fully stacked kitchen. You have everything you need to ser
