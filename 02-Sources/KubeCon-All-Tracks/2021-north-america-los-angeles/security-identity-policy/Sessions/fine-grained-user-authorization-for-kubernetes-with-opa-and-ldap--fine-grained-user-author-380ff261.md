---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["AI ML", "Security", "Kubernetes Core"]
speakers: ["Cagri Cetin", "Quentin Long", "Yelp Inc."]
sched_url: https://kccncna2021.sched.com/event/lV2F/fine-grained-user-authorization-for-kubernetes-with-opa-and-ldap-cagri-cetin-quentin-long-yelp-inc
youtube_search_url: https://www.youtube.com/results?search_query=Fine-Grained+User+Authorization+for+Kubernetes+with+OPA+and+LDAP+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Fine-Grained User Authorization for Kubernetes with OPA and LDAP - Cagri Cetin & Quentin Long, Yelp Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Cagri Cetin, Quentin Long, Yelp Inc.
- Schedule: https://kccncna2021.sched.com/event/lV2F/fine-grained-user-authorization-for-kubernetes-with-opa-and-ldap-cagri-cetin-quentin-long-yelp-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Fine-Grained+User+Authorization+for+Kubernetes+with+OPA+and+LDAP+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Fine-Grained User Authorization for Kubernetes with OPA and LDAP.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2F/fine-grained-user-authorization-for-kubernetes-with-opa-and-ldap-cagri-cetin-quentin-long-yelp-inc
- YouTube search: https://www.youtube.com/results?search_query=Fine-Grained+User+Authorization+for+Kubernetes+with+OPA+and+LDAP+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VFE6D30Qhx0
- YouTube title: Fine-Grained User Authorization for Kubernetes with OPA and LDAP - Cagri Cetin & Quentin Long
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/fine-grained-user-authorization-for-kubernetes-with-opa-and-ldap/VFE6D30Qhx0.txt
- Transcript chars: 21519
- Keywords: access, authorization, policy, clusters, metadata, request, infrastructure, resources, capability, security, privilege, capabilities, team-based, cluster, control, architecture, workloads, needed

### Resumo baseado na transcript

before we start i would like to thank all of the kubecon organizers for giving us the opportunity to share our story with you all let's get started quentin and i work on the security team at yap today we are going to talk about how we utilize the open policy agent and active directory to provide fine-grained role-based access control to the kubernetes infrastructure at the app and let's start with the motivation for this work if you are not familiar with yelp it's a company that connects people new use cases for us beyond just services and batch workloads and with this came a lot of interest from the uh this came a lot of interest from the other development teams with yelp that wanted to leverage the kubernetes infrastructure support like other types of workloads such as kafka cassandra and various other use cases these developers would need to interact with different namespaces and resources depending on their use case unfortunately the security model that we use in the basis word was carried over to kubernetes world

### Excerpt da transcript

before we start i would like to thank all of the kubecon organizers for giving us the opportunity to share our story with you all let's get started quentin and i work on the security team at yap today we are going to talk about how we utilize the open policy agent and active directory to provide fine-grained role-based access control to the kubernetes infrastructure at the app and let's start with the motivation for this work if you are not familiar with yelp it's a company that connects people with great local businesses as of at the end of 2020 yelpers have contributed to 224 million reviews on our platform approximately 31 million unique devices access yap every month on average and more than half a million business locations spend money on yelp ads every month to promote their businesses and as you can imagine it takes a lot of infrastructure to support an application of that scale today we have more than 1000 geographically distributed software engineers across hundreds of different teams we have a containerized microservice architecture managed by an in-house build open source platform as a service framework called pasta under the hood pasta uses kubernetes as the container orchestration framework to manage thousands of workloads and we have a dozen of kubernetes clusters that we run on ec2 instances with several custom name spaces where we run our web microservices and patch ups and other types of statement workloads like cassandra clusters kafka filling spark and other many various use cases but we weren't always using kubernetes in fact it's a relatively new technology for us at yap as early adapters to the whole containerized work workload system we had been using mesos as their container orchestration framework since 2014.

our mesos infrastructure was primarily used for running services and bench workloads in containers and we didn't really have a strong need for fine-grained access control on the mesa's clusters because only the infrastructure team needed to interact with the mesos directly and they literally use only shared secrets with administrative privileges for that access workload developers use an abstraction layer provided by the infrastructure team and they really didn't need to direct access and to be honest they didn't even need to worry about the underlying technology at all and but over time kubernetes gained a lot of popularity in the community and we eventually decided as a company that we should migrate over to kubernetes for
