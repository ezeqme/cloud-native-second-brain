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
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Marco Ebert", "Giant Swarm", "James Strong", "Isovalent at Cisco"]
sched_url: https://kccnceu2025.sched.com/event/1tcyc/how-to-gateway-with-ingress-140-days-ingate-marco-ebert-giant-swarm-james-strong-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=How+To+Gateway+With+Ingress+-+140+Days+InGate+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How To Gateway With Ingress - 140 Days InGate - Marco Ebert, Giant Swarm & James Strong, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Marco Ebert, Giant Swarm, James Strong, Isovalent at Cisco
- Schedule: https://kccnceu2025.sched.com/event/1tcyc/how-to-gateway-with-ingress-140-days-ingate-marco-ebert-giant-swarm-james-strong-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=How+To+Gateway+With+Ingress+-+140+Days+InGate+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How To Gateway With Ingress - 140 Days InGate.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcyc/how-to-gateway-with-ingress-140-days-ingate-marco-ebert-giant-swarm-james-strong-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=How+To+Gateway+With+Ingress+-+140+Days+InGate+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zTLbnstVjHc
- YouTube title: How To Gateway With Ingress - 140 Days InGate - Marco Ebert & James Strong
- Match score: 0.855
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-to-gateway-with-ingress-140-days-ingate/zTLbnstVjHc.txt
- Transcript chars: 23525
- Keywords: gateway, ingress, engine, actually, ingate, working, features, release, controller, change, engineext, continue, version, talking, already, configuration, trying, releases

### Resumo baseado na transcript

Hello everybody and welcome to our talk how to gate away with ingress uh 40 days in gate. Uh you might wonder why we crossed the one actually um back then in Salt Lake City Cube Conna last year we came up with the idea yeah let's do that talk will be somewhere in the project at that time it turned out nope Um we were aware of this but at this point also decided okay security is more important for now and hopefully somewhere in the future find a possibility to reenable this check but for now and in this patched version it's disabled by default and also there's no way around this. And last but not least, because the Google container registry got deprecated or at least we for Kubernetes project should not no longer use it. So as of now, we'd like to still provide a as stable as possible solution and therefore we will definitely continue updating Alpine, Golang, Kubernetes, third party dependencies. Um apart from that we still will support new Kubernetes releases in the future because as of now what we do is just spinning up a kind cluster in a specific Kubernetes version and then we run our whole E2E test suit against this.

### Excerpt da transcript

Hello everybody and welcome to our talk how to gate away with ingress uh 40 days in gate. Uh you might wonder why we crossed the one actually um back then in Salt Lake City Cube Conna last year we came up with the idea yeah let's do that talk will be somewhere in the project at that time it turned out nope plans are not working as they do and so uh we just had our first community meeting about ingate 40 days ago this is why I allowed myself to slightly change the title a bit about me uh my name My name is Marco Ibad. I'm a site reliability engineer at Giant Swarm. Um already more than 10 years in open source working with Kubernetes since 2016 and proudly a maintainer of Ingress EngineX since November 2023. Besides that, I'm interested in climbing and mountain biking. And with that, handing over to James. Hello everyone. My name is James Strong. I'm a solutions architect at Isurvalent now with Cisco. Um I've been a maintainer of the Kubernetes ingress engineext project for a long enough time now that I don't remember how long it's been.

Uh I am also the author of the Orali book networking Kubernetes a cluru instructor um on basically the same thing that was the basis of the book and um I you know I can't really travel with the axe. I would love to um but I don't think he would like that or you know you know the United States government but I am a Gimly cosplay enthusiast. So uh what are we going going to talk about today? First of all something about the state of status of Ingress engineext. There have been some little CVEs recently. Yeah I don't know um some other topics uh that we were faced with and then before we hand over to James again about the ingate status I'd like to talk about how we get out of ingress engine X into a maintenance mode and what we are going to provide there. Uh we're going to talk a little bit about how we're going to do that transition with uh I I'm going to continue to say the word approximate because like uh the title of our talk, we thought we'd be 140 days in to Ingate. Um so it's going to be an approximate timeline for that migration path and we're going to talk about what that gateway API support for ingress engineext features are.

Um I don't know I we have a lot of features. We've talked about a lot of those features all the time. So we're going to talk about what that looks like from a gateway API migration. uh what the current status is of Endgate and um how you all can um contribute to it. So let's start with this lit
