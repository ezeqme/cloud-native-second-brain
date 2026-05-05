---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Security", "Networking", "Community Governance"]
speakers: ["Sanjay M Pujare", "Google"]
sched_url: https://kccncna2021.sched.com/event/lV7i/grpc-proxyless-service-mesh-with-security-sanjay-m-pujare-google
youtube_search_url: https://www.youtube.com/results?search_query=gRPC+Proxyless+Service+Mesh+with+Security+CNCF+KubeCon+2021
slides: []
status: parsed
---

# gRPC Proxyless Service Mesh with Security - Sanjay M Pujare, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Sanjay M Pujare, Google
- Schedule: https://kccncna2021.sched.com/event/lV7i/grpc-proxyless-service-mesh-with-security-sanjay-m-pujare-google
- Busca YouTube: https://www.youtube.com/results?search_query=gRPC+Proxyless+Service+Mesh+with+Security+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre gRPC Proxyless Service Mesh with Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV7i/grpc-proxyless-service-mesh-with-security-sanjay-m-pujare-google
- YouTube search: https://www.youtube.com/results?search_query=gRPC+Proxyless+Service+Mesh+with+Security+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cSxHGt7tc88
- YouTube title: gRPC Proxyless Service Mesh with Security - Sanjay M Pujare, Google
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/grpc-proxyless-service-mesh-with-security/cSxHGt7tc88.txt
- Transcript chars: 23477
- Keywords: mesh, security, certificate, server, certificates, control, google, traffic, configuration, client, provider, channel, credential, implementation, plugin, called, authorization, framework

### Resumo baseado na transcript

uh hi everyone uh i'm sanjay pujari a staff software engineer in google cloud and part of the grpc team i lead the psm security offering a psm being proxima service mesh uh in this talk uh i'm going to cover a grpc proxima service mesh intro and summary uh i'll also talk about why we need security in the service mesh and why is it so painful today i'll talk about how we added security to the grpc proxima service mesh and how it works i'll i'll do a

### Excerpt da transcript

uh hi everyone uh i'm sanjay pujari a staff software engineer in google cloud and part of the grpc team i lead the psm security offering a psm being proxima service mesh uh in this talk uh i'm going to cover a grpc proxima service mesh intro and summary uh i'll also talk about why we need security in the service mesh and why is it so painful today i'll talk about how we added security to the grpc proxima service mesh and how it works i'll i'll do a technical drill down with a deployment diagram uh then i'll talk about what changes we made to the grpc library specifically the grpc programming api for using this feature and later on i'll i'll basically uh describe a psm security deployment what it looks like in google cloud as an example uh towards the end i'll cover the future roadmap and i also have a slide that has some links to resources for psm in case you're interested and towards the end you know we'll have a few minutes for a q a now i'll give a brief intro to service mesh so uh service mesh with proxies was the initial model uh this is how the service mesh started uh in this uh transparent proxies in red boxes allow existing applications to be in a service mesh the applications shown in blue boxes are not aware of the service mesh the proxies implement these uh is it me okay cool uh so where was i okay so the service mesh includes uh features like service discovery routing load balancing security and observability uh now grpc is a popular framework for service to service communication as randy just mentioned and so we were thinking can we add service mesh features or awareness of the service mesh to grpc so in this use case applications would still be uh gen somewhat unaware of the service mesh around them but the service mesh policies would be transparently applied uh to the grpc traffic by the grpc library now let me talk about xts because xdf frequently mentioned in the context of uh service meshes uh xds is a protocol for control plane uh to talk to data plane entities uh hence it's called a data plane api uh xts where x stands for something like an unknown quantity uh in uh equations and ds is discovery service so like discovery of clusters routes and listeners etc xts was developed for envoy but it is a pretty open and extensible for any kind of service mesh so grpc adopted it and extended it for the proximity service mesh so when the pandemic was reaching we were enhancing the proximal service mesh with grpc our first release last year in jun
