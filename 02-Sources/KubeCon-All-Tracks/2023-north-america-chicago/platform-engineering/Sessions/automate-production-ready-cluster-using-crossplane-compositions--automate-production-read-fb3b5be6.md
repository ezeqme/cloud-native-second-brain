---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Dolis Sharma", "Nirmata"]
sched_url: https://kccncna2023.sched.com/event/1R2wR/automate-production-ready-cluster-using-crossplane-compositions-and-kyverno-dolis-sharma-nirmata
youtube_search_url: https://www.youtube.com/results?search_query=Automate+Production-Ready+Cluster+Using+Crossplane+Compositions+and+Kyverno+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Automate Production-Ready Cluster Using Crossplane Compositions and Kyverno - Dolis Sharma, Nirmata

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Dolis Sharma, Nirmata
- Schedule: https://kccncna2023.sched.com/event/1R2wR/automate-production-ready-cluster-using-crossplane-compositions-and-kyverno-dolis-sharma-nirmata
- Busca YouTube: https://www.youtube.com/results?search_query=Automate+Production-Ready+Cluster+Using+Crossplane+Compositions+and+Kyverno+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Automate Production-Ready Cluster Using Crossplane Compositions and Kyverno.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2wR/automate-production-ready-cluster-using-crossplane-compositions-and-kyverno-dolis-sharma-nirmata
- YouTube search: https://www.youtube.com/results?search_query=Automate+Production-Ready+Cluster+Using+Crossplane+Compositions+and+Kyverno+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_YaCVr5zPfM
- YouTube title: Automate Production-Ready Cluster Using Crossplane Compositions and Kyverno - Dolis Sharma, Nirmata
- Match score: 0.957
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/automate-production-ready-cluster-using-crossplane-compositions-and-ky/_YaCVr5zPfM.txt
- Transcript chars: 26036
- Keywords: cluster, create, policy, production, composition, automate, clusters, resources, developers, talking, everything, entire, instance, crossplane, created, simple, saying, require

### Resumo baseado na transcript

hi everyone my name is dois and I'm working for nirmata we are actually the Creator uh of kerno I'm flying all the way from Halifax which is in NOA Scotia Canada and so far I'm enjoying Chicago so today we're going to talk about how you can automate production ready cluster using crossplane composition and KERO folks we got some space here so you can accommodate okay so let's talk about a little bit of agenda of what this talk is all about we'll talk what is what is

### Excerpt da transcript

hi everyone my name is dois and I'm working for nirmata we are actually the Creator uh of kerno I'm flying all the way from Halifax which is in NOA Scotia Canada and so far I'm enjoying Chicago so today we're going to talk about how you can automate production ready cluster using crossplane composition and KERO folks we got some space here so you can accommodate okay so let's talk about a little bit of agenda of what this talk is all about we'll talk what is what is actually production ready cluster and why do we need to automate production ready cluster and what the workflow looks like with crossbend composition how can Crossman composition looks like and how it can help you to automate all of this stuff I'll give you a quick demo of the entire workflow and then I'm going to talk a little more about what are the challenges in the current workflow and where KERO comes into the picture how you can help in this entire workflow how kerno can be helpful and I'll I'll give the same demo with crosspin composition and kerno together so to start with let's talk about what are production ready cluster so the heading of this talk was automate production ready cluster and the question might be like aren't they similar to normal clusters like what is production ready so when we when we talk about production ready cluster we have some kind of parameters that we always consider we it's just not like spinning any cluster and calling it production ready right when we call a cluster production ready we make sure that we are entirely designing the sizing we are taking care of the entire architecture we are designing the size we are making sure and considering what workloads will be running on these cluster and make it customizable or designing it that way right once they are up and running then we start thinking about what are the add-ons we want to deploy what are the monitoring tools for visibility backup and storage um what else uh it can be like okay backup and storage monitoring for security what are the add-ons we want to do and all these add-ons we decide and we we create clustered add-ons for the production clusters once these clusters are up and running we figure out what does the access management looks like who can access this cluster what does the security looks like what does the configuration of the applications look like what the best practices we try to figure out and consider it so it's just not like normal clusters these are like making sure that these are
