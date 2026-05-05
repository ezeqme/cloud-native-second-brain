---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Service Mesh"
themes: ["AI ML", "Networking"]
speakers: ["Yizhou Xu", "Intel", "Devan Nair", "Ericsson"]
sched_url: https://kccncna2023.sched.com/event/1R2tX/grpc-tapping-filter-with-hardware-accelerated-in-service-mesh-yizhou-xu-intel-devan-nair-ericsson
youtube_search_url: https://www.youtube.com/results?search_query=gRPC+Tapping+Filter+with+Hardware+Accelerated+in+Service+Mesh+CNCF+KubeCon+2023
slides: []
status: parsed
---

# gRPC Tapping Filter with Hardware Accelerated in Service Mesh - Yizhou Xu, Intel & Devan Nair, Ericsson

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Yizhou Xu, Intel, Devan Nair, Ericsson
- Schedule: https://kccncna2023.sched.com/event/1R2tX/grpc-tapping-filter-with-hardware-accelerated-in-service-mesh-yizhou-xu-intel-devan-nair-ericsson
- Busca YouTube: https://www.youtube.com/results?search_query=gRPC+Tapping+Filter+with+Hardware+Accelerated+in+Service+Mesh+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre gRPC Tapping Filter with Hardware Accelerated in Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tX/grpc-tapping-filter-with-hardware-accelerated-in-service-mesh-yizhou-xu-intel-devan-nair-ericsson
- YouTube search: https://www.youtube.com/results?search_query=gRPC+Tapping+Filter+with+Hardware+Accelerated+in+Service+Mesh+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2qbMEZzbSyY
- YouTube title: gRPC Tapping Filter with Hardware Accelerated in Service Mesh - Yizhou Xu & Devan Nair
- Match score: 0.933
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/grpc-tapping-filter-with-hardware-accelerated-in-service-mesh/2qbMEZzbSyY.txt
- Transcript chars: 21622
- Keywords: tapping, traffic, basically, filter, acceleration, memory, information, hardware, within, tracing, request, connection, trace, envoy, thread, network, response, provides

### Resumo baseado na transcript

um so who are we we are um a small group of envoy developers within Ericson who customize enoy filters for our custom use cases for 5G Telecom applications um uh I did this project along with my colleague Saka at ericon and also Yu from Intel who contributed for the hardware acceleration part of this um Talk uh of uh today's agenda we are going to look at some of the background regarding uh the um the problem statement why we had to go for something like a tapping

### Excerpt da transcript

um so who are we we are um a small group of envoy developers within Ericson who customize enoy filters for our custom use cases for 5G Telecom applications um uh I did this project along with my colleague Saka at ericon and also Yu from Intel who contributed for the hardware acceleration part of this um Talk uh of uh today's agenda we are going to look at some of the background regarding uh the um the problem statement why we had to go for something like a tapping filter and some overview of the existing tapping syns that we had in EN why we had to go for this new grpc tabing sync and some um robustness Machinery that we added for um our tracing mechanism and then finally uh we would uh discuss a bit about the hardware acceleration part that we needed for memory copies for this uh tracing Machinery um so just to give you a brief background of uh what we work on and um uh where this use case exactly fits in so uh the uh latest 5G core uh network uh looks something like this where there are a lot of distributed Network function each having its own life cycle and independent policies and management interfaces uh basically they all communicate to each other via http2 on a service uh on a service bus and uh me and my colleagues basically work on two of these uh Network functions that you see which are called service communication proxy and a security Edge protection proxy basically these two proxies set between the whole traffic that goes through a 5G core Network and S essentially act as the window into what is the traffic within the 5G code domain so uh naturally in a multivendor ecosystem like telecommunications you can expect that um there are multiple of these Network functions each coming from different vendors and the uh diagram that I show over here is basically one of the first problems that we faced wherein um one of the uh Network functions uh coming from one of the vendors was not functioning properly on the Ingress side so how do we isolate that fault how do we um troubleshoot that so that was the basic question and so there are some means that um uh a distributed um uh deployment system like uh NY with kubernetes uh provides use such as uh Matrix and logs however uh however matric can only show limited information about certain failure situations such as labels which cannot be fully comprehensive and hence they cannot give proper header uh query or body parameters regarding the failure and then raising the log levels is also not an option for uh c
