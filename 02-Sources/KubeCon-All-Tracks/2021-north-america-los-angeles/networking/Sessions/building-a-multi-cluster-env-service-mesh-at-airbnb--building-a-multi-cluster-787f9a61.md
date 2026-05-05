---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Networking"
themes: ["AI ML", "Networking", "Kubernetes Core"]
speakers: ["Weibo He", "Stephen Chan", "Airbnb"]
sched_url: https://kccncna2021.sched.com/event/lV0D/building-a-multi-clusterenv-service-mesh-at-airbnb-weibo-he-stephen-chan-airbnb
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Multi+Cluster%2FEnv+Service+Mesh+at+Airbnb+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Building a Multi Cluster/Env Service Mesh at Airbnb - Weibo He & Stephen Chan, Airbnb

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Networking]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Weibo He, Stephen Chan, Airbnb
- Schedule: https://kccncna2021.sched.com/event/lV0D/building-a-multi-clusterenv-service-mesh-at-airbnb-weibo-he-stephen-chan-airbnb
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Multi+Cluster%2FEnv+Service+Mesh+at+Airbnb+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Building a Multi Cluster/Env Service Mesh at Airbnb.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0D/building-a-multi-clusterenv-service-mesh-at-airbnb-weibo-he-stephen-chan-airbnb
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Multi+Cluster%2FEnv+Service+Mesh+at+Airbnb+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1D8lg36ZNHs
- YouTube title: Building a Multi Cluster/Env Service Mesh at Airbnb - Weibo He & Stephen Chan, Airbnb
- Match score: 0.859
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/building-a-multi-cluster-env-service-mesh-at-airbnb/1D8lg36ZNHs.txt
- Transcript chars: 28286
- Keywords: mesh, istio, cluster, clusters, external, workloads, control, airbnb, version, workload, network, production, envoy, health, finally, endpoints, multi-cluster, running

### Resumo baseado na transcript

so welcome everyone to this session building a multi-cluster environment service mesh at airbnb and we have the presenters weibo he and stephen chan my name is henrik blixt and i'm the moderator so just a few couple of notes before we get started so we'll do questions at the end i'm gonna be running around with the microphone so once we get to the q a raise your hand i'll run over as quick as i can with the microphone if there are questions we don't have time to

### Excerpt da transcript

hi everyone i think it's uh time to get started it's 5 25. so welcome everyone to this session building a multi-cluster environment service mesh at airbnb and we have the presenters weibo he and stephen chan my name is henrik blixt and i'm the moderator so just a few couple of notes before we get started so we'll do questions at the end i'm gonna be running around with the microphone so once we get to the q a raise your hand i'll run over as quick as i can with the microphone if there are questions we don't have time to cover please do that out in the hallway with the presenters so we can clear the room and also lastly don't forget to rate the session in this get scheduled app when we're done so just quick intros and then we'll we'll get get going so stephen is passionate about large-scale distributed systems open source technical leadership and engine excellence and he's currently focused on solving scaling challenges of infrastructure high-growth companies like airbnb weibo works on building performance scalable and resilient distributed systems in the cloud and he's currently focused on building the next generation service mesh at airbnb and will that with that i'll leave the floor to the presenters thank you thank you welcome everyone my name is weibo and this is stefan we are both engineers from the cloud foundation team at airbnb today we are very excited to walk you through our experience of building a multi-cluster multi-environment service mesh on top of istio on airbnb here's the agenda for today we will start by introducing where we are at in our service mesh journey then we're going to talk about why we need a multi-cluster service mesh and how we deploy istio to enable that after that we will cover multi-environment support including multiple tier mesh expansion and external services and finally we're going to end with key takeaways in the past few years airbnb like many of our p companies have transitioned from the monolith architecture to soa at the same time we also migrated the majority of our workloads from kubernetes from ec2 to kubernetes as we underwent such fundamental infra changes our legacy in-house service mesh no longer meets our needs in 2019 we started the search of modern service mesh and landed on istio as the foundation for more information about this choice feel free to check out our ecocom talk earlier this year linked on the slide last year we evaluated different deployment models and deployed issue in production we start
