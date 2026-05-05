---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Ahmet Alp Balkan", "LinkedIn"]
sched_url: https://kccncna2025.sched.com/event/27Fdd/evicted-all-the-ways-kubernetes-kills-your-pods-and-how-to-avoid-them-ahmet-alp-balkan-linkedin
youtube_search_url: https://www.youtube.com/results?search_query=Evicted%21+All+the+Ways+Kubernetes+Kills+Your+Pods+%28and+How+To+Avoid+Them%29+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Evicted! All the Ways Kubernetes Kills Your Pods (and How To Avoid Them) - Ahmet Alp Balkan, LinkedIn

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Ahmet Alp Balkan, LinkedIn
- Schedule: https://kccncna2025.sched.com/event/27Fdd/evicted-all-the-ways-kubernetes-kills-your-pods-and-how-to-avoid-them-ahmet-alp-balkan-linkedin
- Busca YouTube: https://www.youtube.com/results?search_query=Evicted%21+All+the+Ways+Kubernetes+Kills+Your+Pods+%28and+How+To+Avoid+Them%29+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Evicted! All the Ways Kubernetes Kills Your Pods (and How To Avoid Them).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fdd/evicted-all-the-ways-kubernetes-kills-your-pods-and-how-to-avoid-them-ahmet-alp-balkan-linkedin
- YouTube search: https://www.youtube.com/results?search_query=Evicted%21+All+the+Ways+Kubernetes+Kills+Your+Pods+%28and+How+To+Avoid+Them%29+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jVwXcuNEDYE
- YouTube title: Evicted! All the Ways Kubernetes Kills Your Pods (and How To Avoid Them) - Ahmet Alp Balkan
- Match score: 0.97
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/evicted-all-the-ways-kubernetes-kills-your-pods-and-how-to-avoid-them/jVwXcuNEDYE.txt
- Transcript chars: 31753
- Keywords: cublet, eviction, actually, running, controller, happens, stateful, control, application, memory, terminate, delete, deleted, basically, enough, coming, evictions, whatever

### Resumo baseado na transcript

In the next 30 minutes, uh we're going to explore internals of Kubernetes to better understand how each Kubernetes component is coming after your pods and how they potentially pose a risk to your availability. Um a lot of what you're going to hear today is either hard lessons from operating Kubernetes or we proactively surveyed the codebase to enumerate all the different ways Koreans can evict your pods. And I think this makes LinkedIn uh one of the largest Kubernetes installations in terms of compute footprint. Um how we actually use Kubernetes, how we uh deploy Kubernetes itself and how we build a platform on top of it and offer it to thousands of engineers at LinkedIn. And year before we were at Salt Lake City and we talked about how we treat Kubernetes uh how we treat stateful systems on Kubernetes as a first class citizen and how we run stateful systems with local discs. So we're pretty invested in Kubernetes at this point and we deeply care about the reliability of our compute stack.

### Excerpt da transcript

Hello everyone. Thanks for joining me in the last day of CubeCon. In the next 30 minutes, uh we're going to explore internals of Kubernetes to better understand how each Kubernetes component is coming after your pods and how they potentially pose a risk to your availability. Um a lot of what you're going to hear today is either hard lessons from operating Kubernetes or we proactively surveyed the codebase to enumerate all the different ways Koreans can evict your pods. A little bit about myself. My name is Amad Al Palkin. I've been operating in Korean's open source space and container space since the early days of Docker. Um I contributed to Docker in its early um versions and nowadays I'm leading the Korean infrastructure at LinkedIn. But probably if you know me at all, it's probably because of QCTX or Cuban or something like that. Can we get a quick show of hands actually who uses QCTX QS? Good stuff. Okay. Um yes, this is my sixth time presenting CubeCon. So I want to talk about my employer and how I got into this rabbit hole.

Uh so at LinkedIn we use Kubernetes to run our mission critical services. Uh we serve the LinkedIn website that you all see and use and we run thousands of microservices and largecale databases on top of Kubernetes. And our fleet is pretty large. We have half a million servers in our bare metal data centers. And a significant portion of this is already on Kubernetes. And the rest is soon going to be all on Kubernetes as well. And I think this makes LinkedIn uh one of the largest Kubernetes installations in terms of compute footprint. And this is not our first CubeCon. We presented at CubeCon before. Six months ago we were at London. We presented our Kubernetes-based compute platform. Um how we actually use Kubernetes, how we uh deploy Kubernetes itself and how we build a platform on top of it and offer it to thousands of engineers at LinkedIn. And year before we were at Salt Lake City and we talked about how we treat Kubernetes uh how we treat stateful systems on Kubernetes as a first class citizen and how we run stateful systems with local discs.

So we're pretty invested in Kubernetes at this point and we deeply care about the reliability of our compute stack. Okay, coming back to the topic. Um so a harsh reality that we came to realize over time is that Kubernetes is your enemy if you care about your pod availability and evictions. Um every single component in Kubernetes is trying to kill your pods maybe except for HCD actuall
