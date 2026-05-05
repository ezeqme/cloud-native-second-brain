---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Cloud Native Experience"
themes: ["Networking"]
speakers: ["Alex Leong", "Buoyant"]
sched_url: https://kccnceu2025.sched.com/event/1txHj/museum-of-weird-bugs-our-favorites-from-8-years-of-service-mesh-debugging-alex-leong-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Museum+of+Weird+Bugs%3A+Our+Favorites+From+8+Years+of+Service+Mesh+Debugging+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Museum of Weird Bugs: Our Favorites From 8 Years of Service Mesh Debugging - Alex Leong, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Networking]]
- País/cidade: United Kingdom / London
- Speakers: Alex Leong, Buoyant
- Schedule: https://kccnceu2025.sched.com/event/1txHj/museum-of-weird-bugs-our-favorites-from-8-years-of-service-mesh-debugging-alex-leong-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Museum+of+Weird+Bugs%3A+Our+Favorites+From+8+Years+of+Service+Mesh+Debugging+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Museum of Weird Bugs: Our Favorites From 8 Years of Service Mesh Debugging.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txHj/museum-of-weird-bugs-our-favorites-from-8-years-of-service-mesh-debugging-alex-leong-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Museum+of+Weird+Bugs%3A+Our+Favorites+From+8+Years+of+Service+Mesh+Debugging+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Kcjh0-hXwWw
- YouTube title: Museum of Weird Bugs: Our Favorites From 8 Years of Service Mesh Debugging - Alex Leong, Buoyant
- Match score: 0.965
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/museum-of-weird-bugs-our-favorites-from-8-years-of-service-mesh-debugg/Kcjh0-hXwWw.txt
- Transcript chars: 29371
- Keywords: updates, controller, update, policy, status, resource, destination, information, window, linkerd, gateway, sending, stream, receiver, written, control, memory, proxies

### Resumo baseado na transcript

Uh this is uh our favorites from eight years of service mesh debugging on lingardy. Or you could have alternately titled this each of these took a year off my life. Uh, I don't want to get too much into it, but I want to make sure we have enough shared context and we're on the same page in order to be able to talk about these bugs and how they kind of relate to the link architecture. Uh so just to give some highlevel uh architecture of of how linkerdy works. Now both of those controllers, the destination controller and the policy controller get all the information they need from the Kubernetes API. So they're establishing HTTP watches on the Kubernetes API and listening for updates about pods, about service accounts, about services, about endpoints, and all that information is coming into them.

### Excerpt da transcript

Hi everyone, welcome. Thank you for coming to my talk. Uh this is the museum of weird bugs. Uh this is uh our favorites from eight years of service mesh debugging on lingardy. Or you could have alternately titled this each of these took a year off my life. Um there's some nasty some nasty bugs in here. So I hope you enjoy. Um so my name is Alex Leong. I am a maintainer on the link project. I've been working on linkerd for eight years since the project began. Um, and so I've seen and created a lot of nasty bugs in that time. Even though I've heard it's official link policy that link should have no bugs, you know, here we are. Um, so if you're not familiar with what linkertd is, linkertd is a service mesh. Uh, service mesh was a really really big buzzword a few years ago and I think now has kind of descended into the the realm of being just boring technology, which is great. Um, I love that. Um, it has been in use for for over eight years. Um, and it's been in use by a lot of different people in a lot of different environments at a lot of different scales.

Um, and so that's made uh kind of a ripe environment for a lot of different bugs to be exercised and to occur and to happen in really weird ways that are very difficult to reproduce. Um, and that also makes things very challenging. Um, so I wanted to just start by giving a little bit of background on linkerd and the highle architecture very high level. Uh, I don't want to get too much into it, but I want to make sure we have enough shared context and we're on the same page in order to be able to talk about these bugs and how they kind of relate to the link architecture. Um, and then I've kind of selected a a tasting of of three bugs for us to go through. Uh, each of these is very very delicious. Um I think we probably will only have time to get through two of them. We'll see how it goes. Uh they they each deserve their fair share of time. Uh but we'll see. Uh so just to give some highlevel uh architecture of of how linkerdy works. Um on the right hand side is what we call the data plane. And so that's where your application in Kubernetes is running.

Each of those yellow boxes on the right there is a pod and inside each pod is your applications container and then additionally there is uh the linkd proxy which also runs as a sidecar container in those pods and that sidecar container is written in rust that's the linker microproxy uh that runs alongside and handles all of your network traffic and in order t
