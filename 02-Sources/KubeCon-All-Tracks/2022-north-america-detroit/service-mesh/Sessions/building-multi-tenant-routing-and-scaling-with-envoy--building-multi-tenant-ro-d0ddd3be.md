---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Service Mesh"
themes: ["Networking", "SRE Reliability"]
speakers: ["Yiming Peng", "Amazon Web Services", "Inc."]
sched_url: https://kccncna2022.sched.com/event/182KU/building-multi-tenant-routing-and-scaling-with-envoy-yiming-peng-amazon-web-services-inc
youtube_search_url: https://www.youtube.com/results?search_query=Building+Multi-Tenant+Routing+And+Scaling+With+Envoy+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Building Multi-Tenant Routing And Scaling With Envoy - Yiming Peng, Amazon Web Services, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Yiming Peng, Amazon Web Services, Inc.
- Schedule: https://kccncna2022.sched.com/event/182KU/building-multi-tenant-routing-and-scaling-with-envoy-yiming-peng-amazon-web-services-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Multi-Tenant+Routing+And+Scaling+With+Envoy+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Building Multi-Tenant Routing And Scaling With Envoy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182KU/building-multi-tenant-routing-and-scaling-with-envoy-yiming-peng-amazon-web-services-inc
- YouTube search: https://www.youtube.com/results?search_query=Building+Multi-Tenant+Routing+And+Scaling+With+Envoy+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6-akjOASvxc
- YouTube title: Building Multi-Tenant Routing And Scaling With Envoy - Yiming Peng, Amazon Web Services, Inc.
- Match score: 0.823
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/building-multi-tenant-routing-and-scaling-with-envoy/6-akjOASvxc.txt
- Transcript chars: 15679
- Keywords: request, traffic, upstream, endpoints, application, cluster, routing, product, source, support, provides, balancing, discovery, router, architecture, runtime, scaling, little

### Resumo baseado na transcript

hello everyone welcome to the session today today's topic it is building multi-talent routing and scaling with Android I'm the speaker I mean pen I'm from the Amazon web service happy to be here to talk about the topic with you guys today so a little bit self-introduction about myself I'm the senior engineer from AWS based in Seattle I'm the family engineer of the AWS app Runner I participated in building the sales mode products from zero to one and which it in the 2021.

### Excerpt da transcript

hello everyone welcome to the session today today's topic it is building multi-talent routing and scaling with Android I'm the speaker I mean pen I'm from the Amazon web service happy to be here to talk about the topic with you guys today so a little bit self-introduction about myself I'm the senior engineer from AWS based in Seattle I'm the family engineer of the AWS app Runner I participated in building the sales mode products from zero to one and which it in the 2021. the product I'm working activities closely in the AWS is the including app rounder the Amazon ECS elastic container service the AWS Market which is focused on the serverless containers compute and elastic beam stock so my expertise I will focus on the cloud native containers and sublease compute and open source so I'm also pretty passionate in the open source Community I'm the founder and the maintainer of the cloud native and service Meetup community you can find me in the GitHub and Twitter I'm pretty active there so I want to show a little bit the motivation to have this talk today I want to share the journey from the end user point of view by using Envoy I want to also give back to the community to share the lessons learned and experience by using Amway as a builder and hope it brings value to the community and help the products growth and I also want to use this opportunity to sense and appreciate all the support from the Amway community no matter it is internal or external by the way um Amazon has uh internal interest group for the Amway proxy with like around 160 people I'm the founder and maintainer of lead Channel I also want to send to the platform and I want to use this platform for the future discussion and communication I'm the fan of kubecon for years I'm really happy and excited YouTube here to talk with you guys for the topic a little bit introduction for apron as I mentioned before so AWS App Partners G8 in the 2021 is a fully managed service that makes it easy for computers to quickly deploy container web service and APS at a scale with less and zero infrastructure experience required here is our official website feel free to check it out so from the user point of view that problem provides managed experience for customers app hosting request the routing load balancing and auto scaling networking the Ingress egress both observability cicd deployment and safe deployment and more so customer just need to have their GitHub source code or the ECR image private or public and d
