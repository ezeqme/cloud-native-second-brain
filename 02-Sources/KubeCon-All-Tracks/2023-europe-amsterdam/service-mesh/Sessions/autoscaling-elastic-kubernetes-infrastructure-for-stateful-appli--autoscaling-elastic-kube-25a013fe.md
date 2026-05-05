---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Service Mesh"
themes: ["Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Sanjay Pujare", "Costin Manolache", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HyXz/autoscaling-elastic-kubernetes-infrastructure-for-stateful-applications-using-proxyless-grpc-and-istio-sanjay-pujare-costin-manolache-google
youtube_search_url: https://www.youtube.com/results?search_query=Autoscaling+Elastic+Kubernetes+Infrastructure+for+Stateful+Applications+Using+Proxyless+gRPC+and+Istio+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Autoscaling Elastic Kubernetes Infrastructure for Stateful Applications Using Proxyless gRPC and Istio - Sanjay Pujare & Costin Manolache, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Sanjay Pujare, Costin Manolache, Google
- Schedule: https://kccnceu2023.sched.com/event/1HyXz/autoscaling-elastic-kubernetes-infrastructure-for-stateful-applications-using-proxyless-grpc-and-istio-sanjay-pujare-costin-manolache-google
- Busca YouTube: https://www.youtube.com/results?search_query=Autoscaling+Elastic+Kubernetes+Infrastructure+for+Stateful+Applications+Using+Proxyless+gRPC+and+Istio+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Autoscaling Elastic Kubernetes Infrastructure for Stateful Applications Using Proxyless gRPC and Istio.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyXz/autoscaling-elastic-kubernetes-infrastructure-for-stateful-applications-using-proxyless-grpc-and-istio-sanjay-pujare-costin-manolache-google
- YouTube search: https://www.youtube.com/results?search_query=Autoscaling+Elastic+Kubernetes+Infrastructure+for+Stateful+Applications+Using+Proxyless+gRPC+and+Istio+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3cJIDvePywk
- YouTube title: Autoscaling Elastic Kubernetes Infrastructure for Stateful... - Sanjay Pujare & Costin Manolache
- Match score: 0.803
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/autoscaling-elastic-kubernetes-infrastructure-for-stateful-application/3cJIDvePywk.txt
- Transcript chars: 22873
- Keywords: session, cookie, balancer, traffic, sessions, affinity, feature, istio, cluster, stateful, application, support, request, client, backend, gateway, balancing, server

### Resumo baseado na transcript

uh hi uh the stock is about Auto scaling elastic kubernetes infrastructure in the presence of stateful applications that use proxilious grpc and istio my name is Sanjay pujari and I am an engineer in Google Cloud question also at Google so how many of you attended the grpc maintenance talk yesterday a show offense okay um so we'll start off with a description of kubernetes elastic and auto scalable infrastructure I'll then talk about the problems faced by stateful applications in such an environment we'll look at implementing a their data so this is hard to scale and is expensive so we use a cookie to maintain that state the load balancer issues a cookie after routing the first RPC in a session and the cookie is returned by the client in all these

### Excerpt da transcript

uh hi uh the stock is about Auto scaling elastic kubernetes infrastructure in the presence of stateful applications that use proxilious grpc and istio my name is Sanjay pujari and I am an engineer in Google Cloud question also at Google so how many of you attended the grpc maintenance talk yesterday a show offense okay um so we'll start off with a description of kubernetes elastic and auto scalable infrastructure I'll then talk about the problems faced by stateful applications in such an environment we'll look at implementing a stateful session Affinity that's needed for stateful applications I'll discuss an approach that's based on cookies infinity and how it is implemented in the proxilious grpc library uh session training and Canary deployment are important aspects of this discussion because they affect a stateful session Affinity uh so we'll touch upon those we will then move on to a real-life use case from broadcom who are going to be using this feature in their WSS software costin will talk about how to use this feature using the new Gateway API and the status of our implementation and hopefully we'll have a few minutes towards the end for uh q a okay um it's Friday I suspect you already heard about kubernetes Auto scaling and you know how awesome it is um Auto scaling allows kubernetes to scale up your boards to start New Ports when traffic increases it reduces number of PODS when traffic goes down it's wonderful but it has some some dark Corners there are some some small issues for example you know probably that when support starts up you need to wait for um for it to warm up before Readiness probe is passing so you don't have high latency or errors at startup similarly when when the Pod goes down there are some some things you need to be careful about and and we'll talk about this in a bit in in more details um in in this example we are showing that uh you know when when we were focusing on the scale down and we are showing that um boards will eventually be killed and then nodes will be freed up and your application can can um you know optimize the costs and and um and and support better characteristics uh let's go into the details here okay so when doubt scaling happens there are two things happening uh traffic to existing back-ends can get shifted uh even when ring hash load balancing is used and backends with assigned sessions might be removed as part of downscaling uh in this diagram the load balancer which is shown in the yellow rectangles uh
