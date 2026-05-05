---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Keith Mattix II", "Microsoft", "John Howard", "Google"]
sched_url: https://kccncna2022.sched.com/event/182KL/one-api-to-rule-them-all-what-the-gateway-api-means-for-service-meshes-keith-mattix-ii-microsoft-john-howard-google
youtube_search_url: https://www.youtube.com/results?search_query=One+API+To+Rule+Them+All%3F+What+the+Gateway+API+Means+For+Service+Meshes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# One API To Rule Them All? What the Gateway API Means For Service Meshes - Keith Mattix II, Microsoft & John Howard, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: United States / Detroit
- Speakers: Keith Mattix II, Microsoft, John Howard, Google
- Schedule: https://kccncna2022.sched.com/event/182KL/one-api-to-rule-them-all-what-the-gateway-api-means-for-service-meshes-keith-mattix-ii-microsoft-john-howard-google
- Busca YouTube: https://www.youtube.com/results?search_query=One+API+To+Rule+Them+All%3F+What+the+Gateway+API+Means+For+Service+Meshes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre One API To Rule Them All? What the Gateway API Means For Service Meshes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182KL/one-api-to-rule-them-all-what-the-gateway-api-means-for-service-meshes-keith-mattix-ii-microsoft-john-howard-google
- YouTube search: https://www.youtube.com/results?search_query=One+API+To+Rule+Them+All%3F+What+the+Gateway+API+Means+For+Service+Meshes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vYGP5XdP2TA
- YouTube title: One API To Rule Them All? What the Gateway API Means For Service Meshes - Keith Mattix & John Howard
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/one-api-to-rule-them-all-what-the-gateway-api-means-for-service-meshes/vYGP5XdP2TA.txt
- Transcript chars: 30478
- Keywords: mesh, gateway, traffic, actually, resources, ingress, trying, policy, meshes, started, resource, implementations, ecosystem, around, functionality, canary, meeting, routing

### Resumo baseado na transcript

uh we're gonna go ahead and get started uh thank you all for coming on a Friday I really appreciate everyone coming out for our talk um our the title of our talk is one API to rule them all uh I'm Keith Maddox I'm a senior engineering lead uh for the open service math project at Microsoft I'm also a uh co-lead of the gamma initiative which we'll talk about uh soon I'm John Howard I'm a software engineer at Google working on the Easter project I'm also a

### Excerpt da transcript

uh we're gonna go ahead and get started uh thank you all for coming on a Friday I really appreciate everyone coming out for our talk um our the title of our talk is one API to rule them all uh I'm Keith Maddox I'm a senior engineering lead uh for the open service math project at Microsoft I'm also a uh co-lead of the gamma initiative which we'll talk about uh soon I'm John Howard I'm a software engineer at Google working on the Easter project I'm also a co-leader on the gamer project which we'll learn about excuse me oop wrong way all right uh before we get into it I just want to give a very very brief I promise uh history of like where we're coming from to give some more context on where we're going um so in the beginning you know kubernetes was launched it gave us a conference to go to and talk about things uh it had some service mesh features that you know it has like Service as a resource gives you some amount of functionality there but not all the rich functionality that we want out of a service mesh today so pretty shortly after new service mesh products were starting to pop up Linker D2 and East Joe were some of the first ones bringing things like HTTP and grbc load balancing and routing mtls Telemetry and tracing it what and much much more over the years a lot of other products started popping up as well giving more and more service mesh implementations each one kind of offering their own feature set and custom API so the custom API part is really what we're going to be focusing on today so if you look at you know a service mesh maybe you want to do a canary deployment right and that's what your your adopting service mesh for or some other traffic routing mechanism if in the landscape today if you want to do that you need to decide do I want to do with a virtual service a traffic Route a service router a service profile a virtual router or many many other ones right so these are all real apis to configure the same thing from different service mesh offerings and so while they all do the same thing or roughly the same thing they all have different communities they all have different documentation testing ecosystems built around them slightly different semantics right so it becomes a bit of a mess to figure out what you want to do for something that's actually fairly quite standard and simple to do like a canary rollout right yeah and so this landscape uh I'll go back a slide just to really hone in on this this landscape is a bit is a lot to work with
