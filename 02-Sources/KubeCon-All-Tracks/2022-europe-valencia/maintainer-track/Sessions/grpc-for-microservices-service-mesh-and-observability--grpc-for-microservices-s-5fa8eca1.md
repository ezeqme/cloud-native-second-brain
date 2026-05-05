---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Sanjay Pujare", "Wenbo Zhu‎", "Google"]
sched_url: https://kccnceu2022.sched.com/event/ytlP/grpc-for-microservices-service-mesh-and-observability-sanjay-pujare-wenbo-zhu-google
youtube_search_url: https://www.youtube.com/results?search_query=gRPC+For+Microservices%3A+Service-mesh+and+Observability+CNCF+KubeCon+2022
slides: []
status: parsed
---

# gRPC For Microservices: Service-mesh and Observability - Sanjay Pujare & Wenbo Zhu‎, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Sanjay Pujare, Wenbo Zhu‎, Google
- Schedule: https://kccnceu2022.sched.com/event/ytlP/grpc-for-microservices-service-mesh-and-observability-sanjay-pujare-wenbo-zhu-google
- Busca YouTube: https://www.youtube.com/results?search_query=gRPC+For+Microservices%3A+Service-mesh+and+Observability+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre gRPC For Microservices: Service-mesh and Observability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlP/grpc-for-microservices-service-mesh-and-observability-sanjay-pujare-wenbo-zhu-google
- YouTube search: https://www.youtube.com/results?search_query=gRPC+For+Microservices%3A+Service-mesh+and+Observability+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=y2lKORewzJA
- YouTube title: gRPC For Microservices: Service-mesh and Observability - Sanjay Pujare & Wenbo Zhu‎, Google
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/grpc-for-microservices-service-mesh-and-observability/y2lKORewzJA.txt
- Transcript chars: 20895
- Keywords: mesh, security, observability, server, client, configuration, traffic, application, called, google, credential, proxies, information, presentation, infrastructure, control, metrics, channel

### Resumo baseado na transcript

hello uh my name is uh sanjay pujari i'm in google cloud engineering and i am a lead in the grpc team so in this session i'm going to talk about what grpc is and some history behind it then i'll discuss microservices and service mesh and grpc's role in that evolution one of the main stages in the evolution of service mesh is proxima service mesh and i'll cover that then there are a few slides about main tenets of proximal service mesh traffic management and security i'll mention

### Excerpt da transcript

hello uh my name is uh sanjay pujari i'm in google cloud engineering and i am a lead in the grpc team so in this session i'm going to talk about what grpc is and some history behind it then i'll discuss microservices and service mesh and grpc's role in that evolution one of the main stages in the evolution of service mesh is proxima service mesh and i'll cover that then there are a few slides about main tenets of proximal service mesh traffic management and security i'll mention xds and how traffic management and security works in the proxima service mesh with xds i'll describe how to use proxyres grpc with an example in java then i'll talk about one of the main developments in grpc observability and what's happening there and then we'll end end with questions and answers so what's grpc grpc was created by google based on their experience off and the next version of study study is the internal rpc framework google has been using successfully to operate google scale of microservices one of the numbers i heard mentioned is something like order of 10 to the power of 10 about 10 billion rpcs per second one of the improvements of grpc over stubby is use of http 2 and the benefits we get are binary framing multiplexing streaming and h-back compression for headers i'll also talk about protocol buffers in a later slide protocol buffer is also known as protobuf and that's the term i'll use in the arrest of this presentation uh protobuf is used as the serialization framework with grpc so how does one use grpc at a high level you define your interface using the protobuf idl in a dot profile dot proto is the extension for such files i use the protoc compiler to generate client and server stubs oh by the way protocol buffers is a separate project and the protoc compiler uses a language specific plugin to generate code for a target language so for example there is a java plugin for protoc and that's how protoc generates java code uh so anyway after the code is generated and stuffs are extended or implemented you can use the client stub to simply make a call to the server strictly speaking grpc can be used with another serialization framework protobuf is not strictly speaking mandatory but is the most popular and de facto framework for grpc uh so what's provost protobuf predates grpc since google has been using it with stubby for quite some time uh as you can see its advantages are that it is strongly typed it has a binary format for compactness and is highly extensive i
