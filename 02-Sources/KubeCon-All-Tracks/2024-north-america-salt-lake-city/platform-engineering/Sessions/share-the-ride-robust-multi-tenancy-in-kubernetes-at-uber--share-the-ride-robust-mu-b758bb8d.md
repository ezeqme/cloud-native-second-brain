---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Sashank Appireddy", "Apoorva Jindal", "Uber"]
sched_url: https://kccncna2024.sched.com/event/1i7qJ/share-the-ride-robust-multi-tenancy-in-kubernetes-at-uber-sashank-appireddy-apoorva-jindal-uber
youtube_search_url: https://www.youtube.com/results?search_query=Share+the+Ride%3A+Robust+Multi-Tenancy+in+Kubernetes+at+Uber+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Share the Ride: Robust Multi-Tenancy in Kubernetes at Uber - Sashank Appireddy & Apoorva Jindal, Uber

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Sashank Appireddy, Apoorva Jindal, Uber
- Schedule: https://kccncna2024.sched.com/event/1i7qJ/share-the-ride-robust-multi-tenancy-in-kubernetes-at-uber-sashank-appireddy-apoorva-jindal-uber
- Busca YouTube: https://www.youtube.com/results?search_query=Share+the+Ride%3A+Robust+Multi-Tenancy+in+Kubernetes+at+Uber+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Share the Ride: Robust Multi-Tenancy in Kubernetes at Uber.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qJ/share-the-ride-robust-multi-tenancy-in-kubernetes-at-uber-sashank-appireddy-apoorva-jindal-uber
- YouTube search: https://www.youtube.com/results?search_query=Share+the+Ride%3A+Robust+Multi-Tenancy+in+Kubernetes+at+Uber+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ka5oMGh2EiU
- YouTube title: Share the Ride: Robust Multi-Tenancy in Kubernetes at Uber - Sashank Appireddy & Apoorva Jindal
- Match score: 0.856
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/share-the-ride-robust-multi-tenancy-in-kubernetes-at-uber/ka5oMGh2EiU.txt
- Transcript chars: 30558
- Keywords: tenant, cluster, tenants, capacity, isolation, solution, control, namespace, components, clusters, workloads, scheduling, number, challenges, resource, running, latency, question

### Resumo baseado na transcript

hello everyone I am Aur and this is Shashank and we appreciate you taking the time to be here today we are going to talk about our implementation of multi-tenancy in kubernetes at Uber this is a brief agenda for the talk first we will introduce the compute platform at Uber then we discuss what multi-tenancy means at Uber then we discuss a simple solution and present the challenges we faced with it and then we introduce a multi-tenant single cluster solution discuss its design and finally talk about the

### Excerpt da transcript

hello everyone I am Aur and this is Shashank and we appreciate you taking the time to be here today we are going to talk about our implementation of multi-tenancy in kubernetes at Uber this is a brief agenda for the talk first we will introduce the compute platform at Uber then we discuss what multi-tenancy means at Uber then we discuss a simple solution and present the challenges we faced with it and then we introduce a multi-tenant single cluster solution discuss its design and finally talk about the challenges we faced while implementing it first let me introduce a compute platform at Uber Uber operates its own private data centers but it's in the process of replicating them away in favor of oci and gcp on top of the physical machines and VMS we have a layer which we refer to as crane which essentially implements host as a service and is responsible for providing an abstraction to hide away all the underlying providers from the platforms on top of crane we have a container orchestration platform layer which is based on kubernetes it is our own distribution of kubernetes fed from open source with the uh the basic components being exactly the same as open source on top top of kubernetes we have user facing um platforms for example we have up which is what developers use to manage all the stateless microservices we have Michelangelo which uses R to manage machine learning workflows data Sciences workbench to run jobs spark and so on here is a brief summary of the scale of the kubernetes installation at Uber it manages more than 4 and a half ion cores with more than 4,000 microservices being deployed more than 100,000 times every day and across stateless and batch we have more than million and a half containers being launched every day on the platform next let me introduce what multi-tenancy means for Uber note that Uber is a consumer company and not a SAS Enterprise company so we have no requirement or no concerns around having to run untrust third party software in our clusters so the definition of multi-tenancy will be slightly different from what we traditionally see in a SAS company so Uber's definition of multitenancy can be captured as the following three requirements the first requirement is data play and isolation which essentially states that workloads belonging to different tenants cannot be collocated on the same machine of course workloads belonging to the same same machine to the same tenant can run on the same host but they cannot be collocat
