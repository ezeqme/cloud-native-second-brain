---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["André Mocke", "Rodrigo Fior Kuntzer", "Miro"]
sched_url: https://kccnceu2025.sched.com/event/1txHO/stateful-connections-in-kubernetes-the-scaling-secrets-nobody-talks-about-andre-mocke-rodrigo-fior-kuntzer-miro
youtube_search_url: https://www.youtube.com/results?search_query=Stateful+Connections+in+Kubernetes%3A+The+Scaling+Secrets+Nobody+Talks+About+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Stateful Connections in Kubernetes: The Scaling Secrets Nobody Talks About - André Mocke & Rodrigo Fior Kuntzer, Miro

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: André Mocke, Rodrigo Fior Kuntzer, Miro
- Schedule: https://kccnceu2025.sched.com/event/1txHO/stateful-connections-in-kubernetes-the-scaling-secrets-nobody-talks-about-andre-mocke-rodrigo-fior-kuntzer-miro
- Busca YouTube: https://www.youtube.com/results?search_query=Stateful+Connections+in+Kubernetes%3A+The+Scaling+Secrets+Nobody+Talks+About+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Stateful Connections in Kubernetes: The Scaling Secrets Nobody Talks About.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txHO/stateful-connections-in-kubernetes-the-scaling-secrets-nobody-talks-about-andre-mocke-rodrigo-fior-kuntzer-miro
- YouTube search: https://www.youtube.com/results?search_query=Stateful+Connections+in+Kubernetes%3A+The+Scaling+Secrets+Nobody+Talks+About+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=h1AyaAIf3HA
- YouTube title: Stateful Connections in Kubernetes: The Scaling Secrets Nobody... André Mocke & Rodrigo Fior Kuntzer
- Match score: 0.839
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/stateful-connections-in-kubernetes-the-scaling-secrets-nobody-talks-ab/h1AyaAIf3HA.txt
- Transcript chars: 25697
- Keywords: connections, scaling, connection, stateful, rodrigo, server, important, websocket, active, gateway, websockets, platform, infrastructure, existing, limits, traffic, little, product

### Resumo baseado na transcript

Good afternoon everybody and thank you so much for joining Rodrigo and myself this late on a Friday. Uh we realize we're one of the last things between you and your weekend. Next, we'll take a look at how we used a platform built on Kubernetes to migrate Miro's websocket manager into Kubernetes from a stateful EC2 service to a stateless service on EKS, reshaping our edge routing for websocket connections, reducing operational cost, all while embracing cloudnative technologies. Uh I would like to kick things off with a little bit of history about Mir's product architecture and infrastructure. At the heart of this engine sits our board server, a stateful service crucial for performance and low latence. The stateful nature of this service or this the stateful nature here introduces a significant routing challenge.

### Excerpt da transcript

Good afternoon everybody and thank you so much for joining Rodrigo and myself this late on a Friday. Uh we realize we're one of the last things between you and your weekend. So we really appreciate that you signed up for our three-hour lecture on websockets. I'm I'm kidding. It's just it's just 30 minutes. First allow me to start with a little intro of the two people that's daring to address you right now. My co-speaker Rodrigo. He's the reason we're here and the visionary behind Miro's evolution into cloudnative technologies. Our Kubernetes platform and CNCF adoption. AWS has published case studies on his work and uh we use them as a cheat as a cheat code at Miro since he's more effective than most LLMs. My myself Andre I'm a newish S sur compared to this titan next to me. Um, I've joined I've I've dared to venture into infrastructure and platforming after a decade of being a product engineer. And I will still write front-end code when in danger. Like any good story, we'd like to offer a little bit of history, set the stage, so to speak.

Rodrigo is going to walk us through a brief history of Mero, our product, our infrastructure, where we came from to where we are today. We'll aim to illuminate why long live stateful connections are so important to our product. Next, we'll take a look at how we used a platform built on Kubernetes to migrate Miro's websocket manager into Kubernetes from a stateful EC2 service to a stateless service on EKS, reshaping our edge routing for websocket connections, reducing operational cost, all while embracing cloudnative technologies. We're going to dive a bit on some of the mistakes we made. the lessons we got so that nobody in this room has to repeat them. And finally, we're going to brag a bit with the results and hopefully do all of this fast enough so that we're out of here before midnight. Just kidding, it's still 30 minutes. Uh thank you, Andrea, for the sweet introduction and thank you all for making this very last CubeCon U 2025 uh talk. Uh I would like to kick things off with a little bit of history about Mir's product architecture and infrastructure.

Uh these diagrams shows a simplified overview of one of our most important parts of the product and this is how Miru was born a few years ago. Uh you can imagine Miro as a gaming engine for enterprise collaboration. Uh currently Andrea and I we are here uh in what we call the mirror board running this presentation. But if we were to invite you all into this boards in
