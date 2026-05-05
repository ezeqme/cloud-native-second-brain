---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Michael McCune", "Red Hat", "Joseph Anttila Hall", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2oN/improving-kubernetes-security-with-the-konnectivity-proxy-michael-mccune-red-hat-joseph-anttila-hall-google
youtube_search_url: https://www.youtube.com/results?search_query=Improving+Kubernetes+Security+with+the+Konnectivity+Proxy+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Improving Kubernetes Security with the Konnectivity Proxy - Michael McCune, Red Hat & Joseph Anttila Hall, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Michael McCune, Red Hat, Joseph Anttila Hall, Google
- Schedule: https://kccncna2023.sched.com/event/1R2oN/improving-kubernetes-security-with-the-konnectivity-proxy-michael-mccune-red-hat-joseph-anttila-hall-google
- Busca YouTube: https://www.youtube.com/results?search_query=Improving+Kubernetes+Security+with+the+Konnectivity+Proxy+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Improving Kubernetes Security with the Konnectivity Proxy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2oN/improving-kubernetes-security-with-the-konnectivity-proxy-michael-mccune-red-hat-joseph-anttila-hall-google
- YouTube search: https://www.youtube.com/results?search_query=Improving+Kubernetes+Security+with+the+Konnectivity+Proxy+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wTRezbXnlj8
- YouTube title: Improving Kubernetes Security with the Konnectivity Proxy - Michael McCune & Joseph Anttila Hall
- Match score: 0.845
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/improving-kubernetes-security-with-the-konnectivity-proxy/wTRezbXnlj8.txt
- Transcript chars: 21097
- Keywords: connectivity, server, cluster, control, connection, network, clusters, worker, running, number, implementation, connect, scalability, traffic, default, resources, interesting, configuration

### Resumo baseado na transcript

okay I think we have Quorum and we can start I got the thumbs up in the back great so um before we get very far along I have to give you an update my co-speaker uh Michael mun uh couldn't make it at the very last minute to be honest he got covid and is doing the responsible thing and staying home um his topic as the co-speaker was going to be more about the security posture of running connectivity proxy in a kuber cluster and my material is

### Excerpt da transcript

okay I think we have Quorum and we can start I got the thumbs up in the back great so um before we get very far along I have to give you an update my co-speaker uh Michael mun uh couldn't make it at the very last minute to be honest he got covid and is doing the responsible thing and staying home um his topic as the co-speaker was going to be more about the security posture of running connectivity proxy in a kuber cluster and my material is um was going to be more about the experience I had in gke running connectivity at that scale so we've sort of tweaked the slides around to essentially Focus mainly on my content so if anybody feels strongly bait and switched I apologize so getting started um here's the structure of this talk uh I'm going to start with a generic overview of the problems Sol by connectivity proxy and how it works and then I'll go into as a main as a maintainer and this is a maintainer track uh talk I'll go into my personal experience in gke using the proxy okay so um just make sure so just for starters um connectivity is a TCP proxy for cube API server running in the control plane to talk to Cluster uh resources on worker nodes uh this extension is um associated with the API machinery and cloud provider sigs uh it utilizes a server and agent topology it's a it's a forward proxy uh you'll see that later and it's um it's a specific to API server um solution it's not meant to be a generic proxy um also Al I want to mention this presentation will attempt to avoid covering too much repeat information with some previous cubec con talks in 2019 some of the designers and implementers of connectivity gave a nice presentation of uh more of the inner workings and implementation details so I won't get too into the depth here uh and then just last year a couple of presenters talked about some interesting um Rich use cases that they had found for connectivity um yeah they had a nice talk where they talked about remote control plans was the term they used uh so I won't talk too much about the variety of use cases um so getting started the diagram you see uh illustrates the the typical divide of a kubernetes cluster on the left you've got the control plane components um and on the right you've got there's usually one or more worker nodes uh running cluster resources most control plane traffic is client-based and destined to the API server even most control plane components like the scheduler controller manager Etc are API server clients uh etcd is the pr
