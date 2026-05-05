---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Megan Yahya", "Google LLC"]
sched_url: https://kccnceu2021.sched.com/event/iE8o/xds-in-grpc-for-service-mesh-megan-yahya-google-llc
youtube_search_url: https://www.youtube.com/results?search_query=xDS+in+gRPC+for+Service+Mesh+CNCF+KubeCon+2021
slides: []
status: parsed
---

# xDS in gRPC for Service Mesh - Megan Yahya, Google LLC

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Megan Yahya, Google LLC
- Schedule: https://kccnceu2021.sched.com/event/iE8o/xds-in-grpc-for-service-mesh-megan-yahya-google-llc
- Busca YouTube: https://www.youtube.com/results?search_query=xDS+in+gRPC+for+Service+Mesh+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre xDS in gRPC for Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE8o/xds-in-grpc-for-service-mesh-megan-yahya-google-llc
- YouTube search: https://www.youtube.com/results?search_query=xDS+in+gRPC+for+Service+Mesh+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cGJXkZ7jiDk
- YouTube title: xDS in gRPC for Service Mesh - Megan Yahya, Google LLC
- Match score: 0.789
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/xds-in-grpc-for-service-mesh/cGJXkZ7jiDk.txt
- Transcript chars: 11876
- Keywords: mesh, control, features, application, envoy, course, sidecar, traffic, languages, proxies, talking, provide, basically, support, binaries, launched, product, microservices

### Resumo baseado na transcript

hi everyone my name is megan yahya i am product manager for grpc at google today i'm happy to be talking to you about service meshes with grpc and xds protocol so let's first talk about grpc and microservices so i i'm assuming a lot of you are familiar with grpc but um let's let's talk about why uh grpc is the appropriate way of communication between microservices in a service mesh so grpc is a very high performant and efficient protocol so if you know already uh it's based

### Excerpt da transcript

hi everyone my name is megan yahya i am product manager for grpc at google today i'm happy to be talking to you about service meshes with grpc and xds protocol so let's first talk about grpc and microservices so i i'm assuming a lot of you are familiar with grpc but um let's let's talk about why uh grpc is the appropriate way of communication between microservices in a service mesh so grpc is a very high performant and efficient protocol so if you know already uh it's based on http 2 and is very compatible with protobufs and that is super important in microservices because when we are talking about microservices we are talking about a great amount of east-west traffic uh versus the north-south traffic so the the magnitude of east west traffic is much much bigger than the north-south traffic and that makes it a lot important to make sure that these communications are as performant as possible the other value that a lot of customers are seeking when they adopt grpc is the fact that grpc is supported in a lot of languages in 13 languages at the moment and why it matters is because when you break down your monolith or when you start writing like cloud native application it it's usually because you want to leverage the value that different languages bring to the table right so you might have python you might have uh java you might have c plus plus you might have a lot of different languages as part of the same organization and and it's important for these languages to call each other right so so the fact that grpc supports all these languages makes it easy and reduces a lot of code that your developers would otherwise have to write by just auto generating this code for for the clients and services grpc as i mentioned is compatible with protobufs and of course uh there are several values of protobufs like if you're familiar with it you basically have to write the service definition first and um that that that creates a single source of truth for your service and that it makes the api documentation generation easier and it makes getting into agreement with different teams easier so there are a lot of different values for it protobufs and of course with grpc there are additional features like deadlines cancellation and inter support for interceptors so so grpc already has high industry adoption for the reasons that i mentioned in the previous slide but let's talk about grpc applications inside the service mesh right so today they're like if i assume you you want t
