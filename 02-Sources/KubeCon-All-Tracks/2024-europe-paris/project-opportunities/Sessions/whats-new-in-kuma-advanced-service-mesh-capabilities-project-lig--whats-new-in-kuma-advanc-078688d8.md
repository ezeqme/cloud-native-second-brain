---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Networking"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQgO/whats-new-in-kuma-advanced-service-mesh-capabilities-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=What%E2%80%99s+New+in+Kuma%3A+Advanced+Service+Mesh+Capabilities+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# What’s New in Kuma: Advanced Service Mesh Capabilities | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Networking]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQgO/whats-new-in-kuma-advanced-service-mesh-capabilities-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=What%E2%80%99s+New+in+Kuma%3A+Advanced+Service+Mesh+Capabilities+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre What’s New in Kuma: Advanced Service Mesh Capabilities | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQgO/whats-new-in-kuma-advanced-service-mesh-capabilities-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=What%E2%80%99s+New+in+Kuma%3A+Advanced+Service+Mesh+Capabilities+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wHIbrOoU5EY
- YouTube title: What’s New in Kuma: Advanced Service Mesh Capabilities | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/whats-new-in-kuma-advanced-service-mesh-capabilities-project-lightning/wHIbrOoU5EY.txt
- Transcript chars: 4410
- Keywords: traffic, mesh, called, workloads, policies, target, source, define, wanted, configuration, policy, balancing, strategy, control, decide, getting, proxies, couple

### Resumo baseado na transcript

okay uh hello everyone my name is Christopher I'm a software engineer at Kong where I work on Open Source service me code Kuma and today I want to talk to you about the latest features that we uh released in Kuma okay but what is Kuma anyway uh Kuma Is An Open Source service mesh that allows you to bring security observability and advanced routing capabilities into your service smash installation um and into your microservices uh as well uh so okay uh it supports both kubernetes and and

### Excerpt da transcript

okay uh hello everyone my name is Christopher I'm a software engineer at Kong where I work on Open Source service me code Kuma and today I want to talk to you about the latest features that we uh released in Kuma okay but what is Kuma anyway uh Kuma Is An Open Source service mesh that allows you to bring security observability and advanced routing capabilities into your service smash installation um and into your microservices uh as well uh so okay uh it supports both kubernetes and and VM workloads uh it can be deployed in multiple clusters and in uh multiple regions and is built on top of envoy okay so let's get into it the first uh feature I want to talk about is called auto reachable services so um when your service MH is really big and you have a lot of envoy configurations going over the network and so on this can get really heavy on the network CPU and memory so up until now you had to manually Define if you wanted to you know mitigate that you had to manually Define which Services your service is consuming and then the service mes would only send over this configuration but right now if you use mesh traffic permissions and auto reachable services this will be automatically figured out and you get the performance benefit pretty much for free the next thing I want to talk about is a new policy that we introduced it's called mesh load balancing strategy it allows fine grain control over how the uh routing is done inside your Zone and across zones so the first part of meas Lo balancing strategy is called uh local Zone and under there you have Affinity TXS and based on those TXS and the weight you assigned you decide how much traffic goes to which workloads with the same value of a particular tag so in this case 99.9% of the traffic will go to the workloads with the same kubernetes that io/ hostname tag and 0.1% will go to topology kubernetes doio szone and the second part of meslo balancing strategy is called cross Zone and here you decide what happens with the traffic uh when the workloads are not available in your local zone so uh in this example if the workload is not available in US-1 Zone uh we will fail over to the uh us-2 and us-3 zones okay uh the next thing I want to talk about is is source and destination policies are getting deprecated and are being replaced by Target rep policies and Target rep policies are way more flexible when it comes to like selecting which proxies configuration are going to be changed and what happens to the incoming
