---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Networking + Edge + Telco"
themes: ["Networking", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Liz Rice", "Isovalent"]
sched_url: https://kccnceu2024.sched.com/event/1YeQn/simplifying-multi-cluster-and-multi-cloud-deployments-with-cilium-liz-rice-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Simplifying+Multi-Cluster+and+Multi-Cloud+Deployments+with+Cilium+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Simplifying Multi-Cluster and Multi-Cloud Deployments with Cilium - Liz Rice, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Liz Rice, Isovalent
- Schedule: https://kccnceu2024.sched.com/event/1YeQn/simplifying-multi-cluster-and-multi-cloud-deployments-with-cilium-liz-rice-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Simplifying+Multi-Cluster+and+Multi-Cloud+Deployments+with+Cilium+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Simplifying Multi-Cluster and Multi-Cloud Deployments with Cilium.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQn/simplifying-multi-cluster-and-multi-cloud-deployments-with-cilium-liz-rice-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Simplifying+Multi-Cluster+and+Multi-Cloud+Deployments+with+Cilium+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qbB3TEiOb24
- YouTube title: Simplifying Multi-Cluster and Multi-Cloud Deployments with Cilium - Liz Rice, Isovalent
- Match score: 0.952
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/simplifying-multi-cluster-and-multi-cloud-deployments-with-cilium/qbB3TEiOb24.txt
- Transcript chars: 22026
- Keywords: cluster, remote, mesh, clusters, running, google, addresses, traffic, policy, address, locally, prefer, actually, connection, connected, global, x-wing, sometimes

### Resumo baseado na transcript

thank you so much everyone for coming it's lovely to see such a full room so I really appreciate you uh spending time here to learn about psyllium and how you can use psyllium cluster mesh to really make it very very easy to deploy your services across multicloud and multicluster I'm going to try and get these out of the way they're a bit I don't think they make any difference because I'm using this so okay great uh I work with ISO veent who are the company that I also want to be able to accept traffic from this remote cluster and we don't have have time or inclination and it's really nothing to do with psyllium but you need to know to set up the farall rules of the security groups or

### Excerpt da transcript

thank you so much everyone for coming it's lovely to see such a full room so I really appreciate you uh spending time here to learn about psyllium and how you can use psyllium cluster mesh to really make it very very easy to deploy your services across multicloud and multicluster I'm going to try and get these out of the way they're a bit I don't think they make any difference because I'm using this so okay great uh I work with ISO veent who are the company that originally created syum so I have the uh pleasure and privilege of working with some incredibly talented Engineers there I've also been very involved in the cncf over the years uh with the technical oversight committee and now the governing board I also work with the open UK board as well soyum uh cluster mesh is not really a new thing so really what I'm going to be talking about today there's no new launch but this is really about diving a little bit more into what cluster mesh is how it works how easy it is to use and I wanted to also just talk a little bit about my experiences of uh connecting clusters in multiple clouds I'm going to do something ever so slightly Reckless which is that I do actually have uh a cluster running in eks so I'm going to be trying to use the wifi uh and I have another cluster running in Google Cloud so let's hope that I will be able to continue talking to those clusters for the next half hour or so is that big enough for everyone to see y great good so cluster mesh really enables us to distribute the functionality that you get in cium across multiple clusters whether those clusters are running kind of collocated in the same Cloud perhaps they're in multiple different regions perhaps they are as I'm going to do today running in different public clouds and there are all sorts of reasons why you might want to do that so the first thing you need to do is actually connect those two different clusters and this isn't really anything to do with pllum this is about how you set up a connection in my case I have connected my VPC in Google and my VPC in AWS with a VPN connection so one thing you have to do is learn the terminology of what these things are called in AWS and what they're called in Google or what they're called in Azure the the terminology might be slightly different in different places the interfaces might look slightly different in different places but you are essentially trying to set up something that's symmetrical so I I've got yeah a VPC essentially I've got on
