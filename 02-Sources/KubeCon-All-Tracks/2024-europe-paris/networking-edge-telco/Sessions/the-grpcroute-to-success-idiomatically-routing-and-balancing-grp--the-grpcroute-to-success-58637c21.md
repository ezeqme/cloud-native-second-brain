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
themes: ["Networking"]
speakers: ["Richard Belleville", "Google LLC", "Arko Dasgupta", "Tetrate"]
sched_url: https://kccnceu2024.sched.com/event/1YeRZ/the-grpcroute-to-success-idiomatically-routing-and-balancing-grpc-traffic-with-the-gateway-apis-richard-belleville-google-llc-arko-dasgupta-tetrate
youtube_search_url: https://www.youtube.com/results?search_query=The+gRPCRoute+to+Success%3A+Idiomatically+Routing+and+Balancing+GRPC+Traffic+with+the+Gateway+APIs+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The gRPCRoute to Success: Idiomatically Routing and Balancing GRPC Traffic with the Gateway APIs - Richard Belleville, Google LLC & Arko Dasgupta, Tetrate

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]]
- País/cidade: France / Paris
- Speakers: Richard Belleville, Google LLC, Arko Dasgupta, Tetrate
- Schedule: https://kccnceu2024.sched.com/event/1YeRZ/the-grpcroute-to-success-idiomatically-routing-and-balancing-grpc-traffic-with-the-gateway-apis-richard-belleville-google-llc-arko-dasgupta-tetrate
- Busca YouTube: https://www.youtube.com/results?search_query=The+gRPCRoute+to+Success%3A+Idiomatically+Routing+and+Balancing+GRPC+Traffic+with+the+Gateway+APIs+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The gRPCRoute to Success: Idiomatically Routing and Balancing GRPC Traffic with the Gateway APIs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRZ/the-grpcroute-to-success-idiomatically-routing-and-balancing-grpc-traffic-with-the-gateway-apis-richard-belleville-google-llc-arko-dasgupta-tetrate
- YouTube search: https://www.youtube.com/results?search_query=The+gRPCRoute+to+Success%3A+Idiomatically+Routing+and+Balancing+GRPC+Traffic+with+the+Gateway+APIs+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8cXm-TtkGd0
- YouTube title: The gRPCRoute to Success: Idiomatically Routing and Balancing...- Richard Belleville & Arko Dasgupta
- Match score: 0.825
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-grpcroute-to-success-idiomatically-routing-and-balancing-grpc-traf/8cXm-TtkGd0.txt
- Transcript chars: 22939
- Keywords: gateway, traffic, routing, request, client, mesh, connection, server, method, cluster, configure, implementations, reflection, protocol, support, mentioned, little, clients

### Resumo baseado na transcript

the grpc route to success my name is aroas Gupta I'm a software engineer at tet trade and a maintainer on the envoy Gateway project and I'm Richard Belleville from the grpc team at Google this talk is about the new grpc route resource part of the Gateway apis this presentation is a special milestone for GPC route because after two years it is finally heading to V1 so we are excited for it to make its way into the hands of a bunch of people in the near future

### Excerpt da transcript

the grpc route to success my name is aroas Gupta I'm a software engineer at tet trade and a maintainer on the envoy Gateway project and I'm Richard Belleville from the grpc team at Google this talk is about the new grpc route resource part of the Gateway apis this presentation is a special milestone for GPC route because after two years it is finally heading to V1 so we are excited for it to make its way into the hands of a bunch of people in the near future hopefully some of you uh in this talk we'll be covering the basics of grpc and the Gateway API for people who are unfamiliar we'll lay out a few great reasons to start using grpc route today and then we'll tease you with a look at where grpc route may be heading in the future before we jump into that though uh I have one thing to plug uh normally this is where we like to show you all of the great related talks uh at cucon this year but as you know we are very close to the end of things so we only have one talk to plug right now which is what's new in GR RPC this is a maintainer talk run by the grpc team covering everything that's happened with grpc recently including a brief mention of the subject of this talk grpc route and that is happening immediately after this talk so if you want to follow me down the hall I'd love for some of you to join me there all right let's Dive Right In I think most of you are probably familiar with grpc I saw from the show of hands but for those of you who are new to it and curious let's start with a brief recap so grp C is a high performance remote procedure call or RPC framework uh you write what are basically function signatures in a language called protuff and we will generate code for you that will efficiently serialize requests send them over the wire deserialize them on the other end and then hand them off to a server that you have written grpc has a special place in the kubernetes ecosystem because it's the basis for many of kubernetes own apis for example the container storage interface the networking interface and the upcoming kni or kubernetes networking reimagined interface uh beyond the kubernetes control plane grpc is used by thousands and thousands of engineering organizations to get their bites where they're going and then make sense of them on the other end uh for those of you coming from the rest or Json over HTTP world let's call out a few key differences between grpc and HTTP the first big difference is that grpc is schema that means that you write your
