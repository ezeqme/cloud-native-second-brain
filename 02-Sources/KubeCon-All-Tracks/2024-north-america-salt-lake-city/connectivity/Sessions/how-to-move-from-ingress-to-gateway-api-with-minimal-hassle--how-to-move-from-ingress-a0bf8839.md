---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Keith Mattix", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1i7ng/how-to-move-from-ingress-to-gateway-api-with-minimal-hassle-keith-mattix-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Move+from+Ingress+to+Gateway+API+with+Minimal+Hassle+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How to Move from Ingress to Gateway API with Minimal Hassle - Keith Mattix, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: Keith Mattix, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1i7ng/how-to-move-from-ingress-to-gateway-api-with-minimal-hassle-keith-mattix-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Move+from+Ingress+to+Gateway+API+with+Minimal+Hassle+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How to Move from Ingress to Gateway API with Minimal Hassle.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ng/how-to-move-from-ingress-to-gateway-api-with-minimal-hassle-keith-mattix-microsoft
- YouTube search: https://www.youtube.com/results?search_query=How+to+Move+from+Ingress+to+Gateway+API+with+Minimal+Hassle+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dyye6L6aKkA
- YouTube title: How to Move from Ingress to Gateway API with Minimal Hassle - Keith Mattix, Microsoft
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-to-move-from-ingress-to-gateway-api-with-minimal-hassle/dyye6L6aKkA.txt
- Transcript chars: 33067
- Keywords: gateway, ingress, resources, traffic, migration, balancer, cluster, resource, figure, specific, actually, organization, process, provider, engine, controller, platform, address

### Resumo baseado na transcript

so I'm going to go ahead and get things uh kicked off here about a minute early um and again if uh as people come in if you could just raise your hand uh if you've got an empty spot next to you we'll try to get as many people seated here as possible uh so my name is Keith Maddox uh I'm a senior engineering lead at Microsoft I work on lots of Open Source projects um in the networking space such as uh ISO Envoy proxy and of

### Excerpt da transcript

so I'm going to go ahead and get things uh kicked off here about a minute early um and again if uh as people come in if you could just raise your hand uh if you've got an empty spot next to you we'll try to get as many people seated here as possible uh so my name is Keith Maddox uh I'm a senior engineering lead at Microsoft I work on lots of Open Source projects um in the networking space such as uh ISO Envoy proxy and of course Gateway API uh a couple of years ago I was uh one of the original Gateway API mesh maintainers and uh still to this day contributes a good bit to the project to to keep things moving forward so really excited to talk to you about how to move from Ingress to Gateway API with minimal hassle so as you've probably heard by now and I'm guessing based on the number of you here uh you've heard about the fact that Gateway API uh is in and Ingress is out for lack of a better term uh Gateway API is a new standard for layer 7 traffic Management in kubernetes um that does doesn't mean that the Ingress API is going away um many of you again if you're here for this talk you're probably using Ingress somewhere in your kubernetes clusters in fact raise your hand if you're still using the Ingress API in your clusters today lots and lots of you yeah so never fear um nothing's going to break Ingress API is a V1 API in kubernetes it's not going away anytime soon however if you look at the uh at the g at the uh kubernetes documentation uh it's been mentioned that the Ingress API has been frozen so no new features um your Ingress API implementations should still be doing uh cve patches and things of that nature uh but all new development and new features um and new energy is being moved towards the Gateway API uh and in this talk I'm not going to actually go through all the different features and uh the setup of Gateway API there are lots of amazing speakers throughout this conference that have already spoken about Gateway API that are going to continue to speak about Gateway API uh lots of previous talks at uh at previous conferences uh so that's not what I'm going to do today I'm going to leave let those other speakers uh take care of you there what I want to talk to you about is how to get to Gateway API if you're already using Ingress now when you saw the title for this talk um and you made a decision to come here and listen to it you probably thought about something like this that there is going to be um this Keith guy is going to give me this one
