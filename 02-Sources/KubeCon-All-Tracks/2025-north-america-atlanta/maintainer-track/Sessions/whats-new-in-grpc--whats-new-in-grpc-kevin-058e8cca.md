---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Kevin Nilson", "Google", "Israel Shapiro", "Broadcom"]
sched_url: https://kccncna2025.sched.com/event/27NnZ/whats-new-in-grpc-kevin-nilson-google-israel-shapiro-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+New+in+gRPC+CNCF+KubeCon+2025
slides: []
status: parsed
---

# What's New in gRPC - Kevin Nilson, Google & Israel Shapiro, Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Kevin Nilson, Google, Israel Shapiro, Broadcom
- Schedule: https://kccncna2025.sched.com/event/27NnZ/whats-new-in-grpc-kevin-nilson-google-israel-shapiro-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+New+in+gRPC+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre What's New in gRPC.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NnZ/whats-new-in-grpc-kevin-nilson-google-israel-shapiro-broadcom
- YouTube search: https://www.youtube.com/results?search_query=What%27s+New+in+gRPC+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BakC-RjiaFg
- YouTube title: What's New in gRPC? - Gina Yeh, Google
- Match score: 0.76
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/whats-new-in-grpc/BakC-RjiaFg.txt
- Transcript chars: 14864
- Keywords: server, policy, support, request, observability, metrics, feature, available, custom, application, cookie, recently, balancing, enable, session, information, manage, sending

### Resumo baseado na transcript

um good afternoon everyone welcome to this talk what's new in JPC uh my name is j and I'm a JPC maintainer on the go team and I'm excited to be here to share the latest updates on JPC so the goal of this talk is to give you an overview of the new features that we launch in JPC recently and we have a lot to cover so I'm not getting into too much details on each individual features that we have instead um you'll be seeing short links

### Excerpt da transcript

um good afternoon everyone welcome to this talk what's new in JPC uh my name is j and I'm a JPC maintainer on the go team and I'm excited to be here to share the latest updates on JPC so the goal of this talk is to give you an overview of the new features that we launch in JPC recently and we have a lot to cover so I'm not getting into too much details on each individual features that we have instead um you'll be seeing short links in most of the slides throughout my presentation and that will takes you to our resources and documentation and that you can learn about it after the talk and as always you can certainly talk to us during the day if you have any questions or feedback all right so let's get started so kubernetes kubernetes Gateway API is a new API that provides an extensible way um to manage your traffic routing in Inc clusters it is designed to as a revamp of the Ingress resource and to get rid of the fender specific annotations the special interest group firstly identify the most common use cases of the Ingress resource and bring that over build that into the kubernetes gateway API we introduced JPC route to integrate JPC with the Gateway API so that you can router your JPC track traffic earlier easier um rather than having to do it at the level of HTTP Dr PC route is now currently in the experimental stream and will be promoted to V betan soon and it's currently supported by gcp traffic director and several other controllers the other exciting thing in this phase is GMA um using the gway API to manage not just for Ingress but also for surface Mash use cases um and we are deeply engaged in the design process to ensure that drpc processess service match will have the first class support with the in the apis so stay tuned for the ability um to use the fander agnostic kubernetes gway API to manage your Dr PC processess service mesh and we also have a birds of feather topic around service match um be freid to join reard and myself if you are interested in this topic after this talk we have been working hard to expand our support in low balancing and one of them is custom backend metrix this is a mechanism in the JPC library that allows you to inject your own custom Matrix at the Dr PC server and this metrics can be used with your low balancing policy we follow the open request cost segregation standard that you can report your custom metrics from your back end in two ways the first first option is to sending us the metrix when RPC finishes and the
