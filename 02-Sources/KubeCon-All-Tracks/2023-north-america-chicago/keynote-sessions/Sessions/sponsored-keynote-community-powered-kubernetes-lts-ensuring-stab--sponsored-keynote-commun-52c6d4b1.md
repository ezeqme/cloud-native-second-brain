---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Keynote Sessions"
themes: ["Kubernetes Core", "Community Governance"]
speakers: ["Jeremy Rickard", "Principal Software Engineer", "Microsoft Azure"]
sched_url: https://kccncna2023.sched.com/event/1R4cZ/sponsored-keynote-community-powered-kubernetes-lts-ensuring-stability-and-compatibility-while-driving-innovation-jeremy-rickard-principal-software-engineer-microsoft-azure
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Community-Powered+Kubernetes+LTS%3A+Ensuring+Stability+and+Compatibility+While+Driving+Innovation+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Sponsored Keynote: Community-Powered Kubernetes LTS: Ensuring Stability and Compatibility While Driving Innovation - Jeremy Rickard, Principal Software Engineer, Microsoft Azure

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Jeremy Rickard, Principal Software Engineer, Microsoft Azure
- Schedule: https://kccncna2023.sched.com/event/1R4cZ/sponsored-keynote-community-powered-kubernetes-lts-ensuring-stability-and-compatibility-while-driving-innovation-jeremy-rickard-principal-software-engineer-microsoft-azure
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Community-Powered+Kubernetes+LTS%3A+Ensuring+Stability+and+Compatibility+While+Driving+Innovation+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Community-Powered Kubernetes LTS: Ensuring Stability and Compatibility While Driving Innovation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R4cZ/sponsored-keynote-community-powered-kubernetes-lts-ensuring-stability-and-compatibility-while-driving-innovation-jeremy-rickard-principal-software-engineer-microsoft-azure
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Community-Powered+Kubernetes+LTS%3A+Ensuring+Stability+and+Compatibility+While+Driving+Innovation+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-7TXEsDZR_k
- YouTube title: Sponsored Keynote: Community-Powered Kubernetes LTS: Ensuring Stability and... - Jeremy Rickard
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/sponsored-keynote-community-powered-kubernetes-lts-ensuring-stability/-7TXEsDZR_k.txt
- Transcript chars: 5268
- Keywords: working, upgrade, support, cluster, upgrades, pretty, create, operational, clusters, across, change, having, survey, long-term, making, easier, plugin, upgrading

### Resumo baseado na transcript

hey everyone today I want to talk to you about kubernetes the community and long-term support but first let's talk about how AI tools are making it easier to deal with complexity like this open AI ql plugin that my co-worker ctOS made large language models are helping us create uh new things we can create yaml to deploy applications uh for example we could say Cube CI create an engine X deployment with two replicas and then we get the AML these tools are going to make all of

### Excerpt da transcript

hey everyone today I want to talk to you about kubernetes the community and long-term support but first let's talk about how AI tools are making it easier to deal with complexity like this open AI ql plugin that my co-worker ctOS made large language models are helping us create uh new things we can create yaml to deploy applications uh for example we could say Cube CI create an engine X deployment with two replicas and then we get the AML these tools are going to make all of our operational headaches go away cluster upgrades are going to be super easy right let's use that plugin again and try to upgrade a cluster oh well that's kind of a bummer upgrading is a complicated process and we can't just generate some yaml to do it okay so then how do we upgrade well open AI says we should consult the kubernetes docs um shout out to Sig docs the docs are pretty good but I'm not ready to give up on AI assistance just yet so let's ask Bing how we upgrade a cluster okay so there's some steps there it seems like a lot but I think it's pretty straightforward we should be able to apply these to all of our clusters across our whole Fleet and upgrade things uh edit some some yams and we'll be good to go right we'll do this pretty quickly but the reality is that even in 2023 cluster upgrades can be pretty complicated and timec consuming and operational concerns like maybe you're running uh bare metal servers and you can't get new uh capacity you're in regulated environments that maybe have lockdowns or Tight Windows when you can do things uh might make it difficult to upgrade each version and suddenly you're upgrading it across four versions or more sadly this isn't really a new problem so let's take a trip back to 2018 kubernetes 112 is just released it's the very first release I got to work on it seems like so long ago uh and there's a discussion in the community about the frequency of releases are we doing it too quickly too slowly maybe we should do more how long should things be supported for what about LTS from those discussions comes a proposal to start up a new working group inside of kubernetes called the long-term support working group there were a lot of questions to answer and a lot of people were involved and over the next two years a lot of data was gathered a lot of discussions happened and at the end of 2020 a new kubernetes enhancement proposal or kep was submitted to change the support period from 9 months to a year to better line with business cadences g
