---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Networking"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Harry Bagdi", "Kong Inc.", "Rob Scott", "Google"]
sched_url: https://kccnceu2021.sched.com/event/iE39/gateway-api-a-new-set-of-kubernetes-apis-for-advanced-traffic-routing-harry-bagdi-kong-inc-rob-scott-google
youtube_search_url: https://www.youtube.com/results?search_query=Gateway+API%3A+A+New+Set+of+Kubernetes+APIs+for+Advanced+Traffic+Routing+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Gateway API: A New Set of Kubernetes APIs for Advanced Traffic Routing - Harry Bagdi, Kong Inc. & Rob Scott, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Harry Bagdi, Kong Inc., Rob Scott, Google
- Schedule: https://kccnceu2021.sched.com/event/iE39/gateway-api-a-new-set-of-kubernetes-apis-for-advanced-traffic-routing-harry-bagdi-kong-inc-rob-scott-google
- Busca YouTube: https://www.youtube.com/results?search_query=Gateway+API%3A+A+New+Set+of+Kubernetes+APIs+for+Advanced+Traffic+Routing+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Gateway API: A New Set of Kubernetes APIs for Advanced Traffic Routing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE39/gateway-api-a-new-set-of-kubernetes-apis-for-advanced-traffic-routing-harry-bagdi-kong-inc-rob-scott-google
- YouTube search: https://www.youtube.com/results?search_query=Gateway+API%3A+A+New+Set+of+Kubernetes+APIs+for+Advanced+Traffic+Routing+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lCRuzWFJBO0
- YouTube title: Gateway API: A New Set of Kubernetes APIs for Advanced Traffic Routing - Harry Bagdi & Rob Scott
- Match score: 0.943
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/gateway-api-a-new-set-of-kubernetes-apis-for-advanced-traffic-routing/lCRuzWFJBO0.txt
- Transcript chars: 26705
- Keywords: gateway, resource, traffic, ingress, cluster, resources, requests, implementations, simple, clusters, custom, application, little, features, external, gateways, infrastructure, already

### Resumo baseado na transcript

hello everyone welcome to this talk on gateway api a new set of kubernetes apis for advanced routing i'm harry bachty i'm a software engineer at kong and with me today i have rob scott who is a software engineer at google we've been working on this new api for a while and want to take some time today to introduce you to the api and demonstrate some use cases that it enables for the problems that you might be facing before we get started i want to mention that we'll send a quick curl request and you can see that we're getting served responses from the same acme store pods as before we can curl a couple more times and again the same pods are responding all right in our third demo we're going we're going to say any request that has a specific header should go to our canary service and everything else should go to our stable service okay so in that case our gateway looks very similar but for this demo we're using traffic so create was a really cool demo and i love when we can see the kubernetes community working so well together across ziggs we've got sig multi-cluster and sig network apis working really well together and these apis enable a lot more functionality than we can demo so header modification cross name space route selection advanced tls configuration custom route filters traffic mirroring l4 protocols there's just so much more that we can do here and unfortunately i...

### Excerpt da transcript

hello everyone welcome to this talk on gateway api a new set of kubernetes apis for advanced routing i'm harry bachty i'm a software engineer at kong and with me today i have rob scott who is a software engineer at google we've been working on this new api for a while and want to take some time today to introduce you to the api and demonstrate some use cases that it enables for the problems that you might be facing before we get started i want to mention that this api is the result of a community-wide effort within the sig network api group in kubernetes and this wouldn't have been possible without contributions from you know all the members in that group now to set some expectation uh we're going to get a little bit of give a little bit of background and then give some quick examples of the api which should give you a good feel of how this api looks like and as we go through through this examples uh we'll explain some key concepts in how why the api was designed the way it is and then we have some cool demos to show some existing implementations of this api and that and then we we conclude with some road map and future that is for this api please feel free to ask questions during this entire talk so ingress api has been around for a long time it has seen a lot of adoption with over 15 implementations of the api but ingress was really aimed for simple use cases with time users have expressed the need for more complicated and advanced use cases and this has resulted in a wide variety of annotations to extend the ingress resource now all these annotations do get the job done they result in a very poor user experience as you know annotations are free for form strings so users have no validation there is no consistency between features of different implementations and so on at the same time we have the service resource which is seeing almost the similar problems as ingress resource it too is getting a lot of custom annotations and it is now becoming bloated with features which concern different areas of kubernetes one such area is load balancing and it's been getting a lot of load balancing features the resource has become complicated enough that it's now proving to be a little difficult to manage and evolve as we go on so these problems have existed for a while uh um and then at cube consent san diego in 2019 we came together and an idea started floating around on how a new api could be used to solve these problems now with the background we're going to prese
