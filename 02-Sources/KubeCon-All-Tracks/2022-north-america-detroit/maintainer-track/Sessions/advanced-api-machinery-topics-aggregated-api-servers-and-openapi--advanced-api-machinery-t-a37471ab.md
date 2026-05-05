---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["David Eads", "Red Hat", "Jeffrey Ying", "Google", "Federico Bongiovanni", "Google"]
sched_url: https://kccncna2022.sched.com/event/182Mo/advanced-api-machinery-topics-aggregated-api-servers-and-openapi-v3-david-eads-red-hat-jeffrey-ying-google-federico-bongiovanni-google
youtube_search_url: https://www.youtube.com/results?search_query=Advanced+API+Machinery+Topics%3A+Aggregated+API+Servers+and+OpenAPI+v3+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Advanced API Machinery Topics: Aggregated API Servers and OpenAPI v3 - David Eads, Red Hat; Jeffrey Ying, Google; Federico Bongiovanni, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: David Eads, Red Hat, Jeffrey Ying, Google, Federico Bongiovanni, Google
- Schedule: https://kccncna2022.sched.com/event/182Mo/advanced-api-machinery-topics-aggregated-api-servers-and-openapi-v3-david-eads-red-hat-jeffrey-ying-google-federico-bongiovanni-google
- Busca YouTube: https://www.youtube.com/results?search_query=Advanced+API+Machinery+Topics%3A+Aggregated+API+Servers+and+OpenAPI+v3+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Advanced API Machinery Topics: Aggregated API Servers and OpenAPI v3.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Mo/advanced-api-machinery-topics-aggregated-api-servers-and-openapi-v3-david-eads-red-hat-jeffrey-ying-google-federico-bongiovanni-google
- YouTube search: https://www.youtube.com/results?search_query=Advanced+API+Machinery+Topics%3A+Aggregated+API+Servers+and+OpenAPI+v3+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oLbzn_hYd5E
- YouTube title: Advanced API Machinery Topics: Aggregated API... - David Eads, Jeffrey Ying, Federico Bongiovanni
- Match score: 0.759
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/advanced-api-machinery-topics-aggregated-api-servers-and-openapi-v3/oLbzn_hYd5E.txt
- Transcript chars: 23089
- Keywords: server, request, aggregated, client, cluster, schema, servers, version, namespace, actually, clients, additional, versions, external, allows, number, running, storage

### Resumo baseado na transcript

hi everyone welcome to ckba Machinery Advanced topics our maintainers track for cubicle North America 2022 my name is Federico van Giovanni I'm co-chair of ckpa Machinery in open source kubernetes two very special guests join me today to provide two great presentations David eats from Red Hat who is also my co-chair and Tech lead in Capa machinery and Jeffrey Ying who is one of our top contributors in clpa machinery and other areas of kubernetes the two topics we are going to talk about today are the power

### Excerpt da transcript

hi everyone welcome to ckba Machinery Advanced topics our maintainers track for cubicle North America 2022 my name is Federico van Giovanni I'm co-chair of ckpa Machinery in open source kubernetes two very special guests join me today to provide two great presentations David eats from Red Hat who is also my co-chair and Tech lead in Capa machinery and Jeffrey Ying who is one of our top contributors in clpa machinery and other areas of kubernetes the two topics we are going to talk about today are the power and the danger of aggregated API servers an open Avi V3 which recently graduated to Beta And is making its way to ga so I will leave you with David and with Jeffrey and I will uh give you some information at the end of the thoughts see you later hi my name is Jeffrey and I'm a software engineer at Google and contributor to API machinery today I'll be talking about open API V3 open API V3 is a feature that has gone beta and kubernetes version 124. to give a quick introduction well the open API is a language agnostic interface in the format that is both human and machine readable to describe the capabilities for a service the service in our case being kubernetes uh the open API is provided in both a Json and protobot format and some of the consumers within kubernetes include queue control explain autocompletion for uis and we also use it for generating documentation the official kubernetes documentation is generated from the open API and also clients this talk is about open API V3 but let's just briefly go over some of the differences between V2 and V3 open API V3 is a restructure of V2 and allows reuse of API components and also provides some new features the most notable of these features is the extended Json schema support the open API V3 uses a newer version of Json schema that supports four additional pretty important Fields these are one of any of default and nullable for those of you already familiar with custom resource stack Nations you might know the open API V3 is already supported in the structural schema I like to highlight one key difference between a schema and a specification a schema represents the definition for a particular type or muscle definitions while specification refers to the entire open API document and includes the schema but also includes additional things like pass and Etc so one thing to note is that without this open API need to be feature we wouldn't be publishing the open API V3 specification and that means that would sti
