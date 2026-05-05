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
speakers: ["Lin Sun", "Solo.io", "Ahmed Bebars", "The New York Times"]
sched_url: https://kccnceu2025.sched.com/event/1txEX/journey-at-the-new-york-times-is-sidecar-less-service-mesh-disappearing-into-infrastructure-lin-sun-soloio-ahmed-bebars-the-new-york-times
youtube_search_url: https://www.youtube.com/results?search_query=Journey+at+the+New+York+Times%3A+Is+Sidecar-Less+Service+Mesh+Disappearing+Into+Infrastructure%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Journey at the New York Times: Is Sidecar-Less Service Mesh Disappearing Into Infrastructure? - Lin Sun, Solo.io & Ahmed Bebars, The New York Times

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United Kingdom / London
- Speakers: Lin Sun, Solo.io, Ahmed Bebars, The New York Times
- Schedule: https://kccnceu2025.sched.com/event/1txEX/journey-at-the-new-york-times-is-sidecar-less-service-mesh-disappearing-into-infrastructure-lin-sun-soloio-ahmed-bebars-the-new-york-times
- Busca YouTube: https://www.youtube.com/results?search_query=Journey+at+the+New+York+Times%3A+Is+Sidecar-Less+Service+Mesh+Disappearing+Into+Infrastructure%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Journey at the New York Times: Is Sidecar-Less Service Mesh Disappearing Into Infrastructure?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEX/journey-at-the-new-york-times-is-sidecar-less-service-mesh-disappearing-into-infrastructure-lin-sun-soloio-ahmed-bebars-the-new-york-times
- YouTube search: https://www.youtube.com/results?search_query=Journey+at+the+New+York+Times%3A+Is+Sidecar-Less+Service+Mesh+Disappearing+Into+Infrastructure%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9U3WMez9q74
- YouTube title: Journey at the New York Times: Is Sidecar-Less Service Mesh Disappearing I... Lin Sun & Ahmed Bebars
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/journey-at-the-new-york-times-is-sidecar-less-service-mesh-disappearin/9U3WMez9q74.txt
- Transcript chars: 27376
- Keywords: mesh, ambient, application, traffic, waypoint, running, cluster, tunnel, architecture, question, multicluster, egress, gateway, selium, multiple, policies, started, across

### Resumo baseado na transcript

We are going to be here talk about journey at New York Time is cyclless service mesh ambient mesh disappearing into the infrastructure. Uh I work at Solo and a fun fact about my employer, we are the 10th largest contributor to all of the CNCF project combined. So we started to define the workflows for our engineers when they want to create a service and then they start like code the service and they get like CI/CD pipelines out of the box and we have a shared Kubernetes cluster that we run things on. So why we ask them to like hey expose all of your metrics like do this with your clients. So we start with selium selium seems to be the right fit from that perspective then we have a multicluster architecture so we have some challenges how to do that across multiple VBCs across multiple tenants. of the box but you need to have this decoupled in a way and from here on give it to Lynn so she can walk us through the ambient architecture.

### Excerpt da transcript

Good morning CubeCon. Can you hear us? All right. We are going to be here talk about journey at New York Time is cyclless service mesh ambient mesh disappearing into the infrastructure. Uh my name is Selen. I come from Raleigh, North Carolina, a suburb of Raleigh Kerry. Uh I work at Solo and a fun fact about my employer, we are the 10th largest contributor to all of the CNCF project combined. Now I'm going to pass to my co-speaker. Thank you Lyn. Hello everyone. My name is Ahmed Bors. I'm a principal engineer at the New York Times. I work in infrastructure. I do Kubernetes. I do STO. And this is a specific talk is special. It's my second talk that I have my daughter with me. She's sitting over here. Let's give her a round of applause. So, let's start talk about the New York Times. Our mission is simple. We seek the truth and help people understand the world. And we aim to do that by building the essential subscription for every English speaking person so they can understand the world. One question I get a lot is like what we do like we are very known for our news and journalism but we also do other things like games like I'm sure you heard about Wordle crosswords and other games that we provide.

We also have the cooking apps if you are inspired to do some recipes. Would love to talk to you about what's your favorite recipes. And then we have the wire cutter if you want a product recommendation. Athletic for like all of our sports fans and audio as well if you want to listen to our stories and different articles as well. So let's start by a question. Do we really need a service mesh? Who's in here use a service mesh? Can you raise your hand? Everyone here uses service mesh. That's great. But like sometimes you come to a question when like you start to build your infrastructure and your platform and you ask your team like hey we need a service mesh. Some people would say hm why do we need it for sometimes it's hard to answer this question. So I'm here today to tell you about our journey on why we decided to use a service mesh. So as a platform team we offer multiple things to our end users. When I talk about our end users, I'm talking about our product engineering teams. So our road map is like workflows.

So we started to define the workflows for our engineers when they want to create a service and then they start like code the service and they get like CI/CD pipelines out of the box and we have a shared Kubernetes cluster that we run things on. Then we ro
