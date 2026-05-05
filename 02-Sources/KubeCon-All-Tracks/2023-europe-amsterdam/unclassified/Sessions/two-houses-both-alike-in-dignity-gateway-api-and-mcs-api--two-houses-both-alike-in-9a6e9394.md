---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["Networking"]
speakers: ["Laura Lorenz", "Rob Scott", "Google", "Stephen Kitt", "Red Hat", "Mike Morris", "HashiCorp"]
sched_url: https://kccnceu2023.sched.com/event/1Hydh/two-houses-both-alike-in-dignity-gateway-api-and-mcs-api-laura-lorenz-rob-scott-google-stephen-kitt-red-hat-mike-morris-hashicorp
youtube_search_url: https://www.youtube.com/results?search_query=Two+Houses%2C+Both+Alike+in+Dignity%3A+Gateway+API+and+MCS+API+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Two Houses, Both Alike in Dignity: Gateway API and MCS API - Laura Lorenz & Rob Scott, Google; Stephen Kitt, Red Hat; Mike Morris, HashiCorp

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Laura Lorenz, Rob Scott, Google, Stephen Kitt, Red Hat, Mike Morris, HashiCorp
- Schedule: https://kccnceu2023.sched.com/event/1Hydh/two-houses-both-alike-in-dignity-gateway-api-and-mcs-api-laura-lorenz-rob-scott-google-stephen-kitt-red-hat-mike-morris-hashicorp
- Busca YouTube: https://www.youtube.com/results?search_query=Two+Houses%2C+Both+Alike+in+Dignity%3A+Gateway+API+and+MCS+API+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Two Houses, Both Alike in Dignity: Gateway API and MCS API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hydh/two-houses-both-alike-in-dignity-gateway-api-and-mcs-api-laura-lorenz-rob-scott-google-stephen-kitt-red-hat-mike-morris-hashicorp
- YouTube search: https://www.youtube.com/results?search_query=Two+Houses%2C+Both+Alike+in+Dignity%3A+Gateway+API+and+MCS+API+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ekDgGDPb1xU
- YouTube title: Two Houses, Both Alike in Dignity: Gateway... - Laura Lorenz & Rob Scott, Stephen Kitt, Mike Morris
- Match score: 0.733
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/two-houses-both-alike-in-dignity-gateway-api-and-mcs-api/ekDgGDPb1xU.txt
- Transcript chars: 30640
- Keywords: gateway, multi-cluster, clusters, meshes, cluster, together, import, across, implementations, juliet, traffic, version, upstream, instead, projects, little, implementation, started

### Resumo baseado na transcript

hello great yep excellent yeah so welcome everyone to this panel uh two houses both Atlantic I like and dignity Gateway API and MCS API I'm Stephen Kitt I work for red hat on the submarena project I'm Rob Scott I work for Google on kubernetes networking and I'm a Gateway API maintainer and I'm Mike Morris and I work for hashicor on console and I am one of the co-loads of the gamma uh initiative and you may notice that unfortunately Laura could not be here in person but

### Excerpt da transcript

hello great yep excellent yeah so welcome everyone to this panel uh two houses both Atlantic I like and dignity Gateway API and MCS API I'm Stephen Kitt I work for red hat on the submarena project I'm Rob Scott I work for Google on kubernetes networking and I'm a Gateway API maintainer and I'm Mike Morris and I work for hashicor on console and I am one of the co-loads of the gamma uh initiative and you may notice that unfortunately Laura could not be here in person but she was able to pre-record what I think is a very creative intro okay hi all this is Laura coming at you from the past as I was not able to travel to kubecon EU this year instead I have the privilege of sending my digital form to you to give a quick intro to our panel topics for two houses both alike in dignity Gateway API and MCS API so what we want to talk about today is these three General projects MCS API Gateway API and service meshes and where they overlap and how they are coming together we've been thinking a lot about these little overlapping joints in here in the Venn diagram so all of these projects in the center here all of them bundle some back ends together so some higher level of abstraction like a service to bundle some endpoints together MCS and service meshes are both very concerned with providing ways to discover a service especially across cluster boundaries the Gateway API and service meshes both do traffic shaping with different levels of expressibility and sophistication and meanwhile all the service meshes usually have a whole other Suite of things that they are able to independently do like securing traffic for example so since all these projects are still a little bit in flux it's informative to know at least a little bit about their history but the most important part is that these efforts have been evolving all along the same time in the face of shared problems that were really clarified in 2019 that users needed more sophisticated Traffic Solutions than were available in kubernetes at the time but that the solution space which was pioneered by all these different projects collectively known as service meshes was too fragmented so a few of those projects connected on their own attempt to converge called the service mesh interface or SMI spec and at the same time Sig multi-cluster and Sig Network respectively approached individual pieces of the problem in the form of the MCS and Gateway apis so the MCS and Gateway apis went through a very exploratory period in 2020
