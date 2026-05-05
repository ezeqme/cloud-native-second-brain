---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Customizing + Extending Kubernetes"
themes: ["AI ML", "Runtime Containers", "Kubernetes Core"]
speakers: ["Mulugeta Ayalew Tamiru", "University of Rennes 1 / Elastisys AB"]
sched_url: https://kccncna2021.sched.com/event/lV0w/mck8s-container-orchestration-in-kubernetes-multi-clusters-mulugeta-ayalew-tamiru-university-of-rennes-1-elastisys-ab
youtube_search_url: https://www.youtube.com/results?search_query=McK8s%3A+Container+Orchestration+in+Kubernetes+Multi-Clusters+CNCF+KubeCon+2021
slides: []
status: parsed
---

# McK8s: Container Orchestration in Kubernetes Multi-Clusters - Mulugeta Ayalew Tamiru, University of Rennes 1 / Elastisys AB

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Mulugeta Ayalew Tamiru, University of Rennes 1 / Elastisys AB
- Schedule: https://kccncna2021.sched.com/event/lV0w/mck8s-container-orchestration-in-kubernetes-multi-clusters-mulugeta-ayalew-tamiru-university-of-rennes-1-elastisys-ab
- Busca YouTube: https://www.youtube.com/results?search_query=McK8s%3A+Container+Orchestration+in+Kubernetes+Multi-Clusters+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre McK8s: Container Orchestration in Kubernetes Multi-Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0w/mck8s-container-orchestration-in-kubernetes-multi-clusters-mulugeta-ayalew-tamiru-university-of-rennes-1-elastisys-ab
- YouTube search: https://www.youtube.com/results?search_query=McK8s%3A+Container+Orchestration+in+Kubernetes+Multi-Clusters+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=U1iHBZhEWUA
- YouTube title: McK8s: Container Orchestration in Kubernetes Multi-Clusters - Mulugeta Ayalew Tamiru
- Match score: 0.915
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/mck8s-container-orchestration-in-kubernetes-multi-clusters/U1iHBZhEWUA.txt
- Transcript chars: 26013
- Keywords: cluster, clusters, multi-cluster, deploy, deployment, resources, replicas, created, scheduler, applications, federation, status, deployments, network, deployed, placement, resource, application

### Resumo baseado na transcript

hello kubecon and cloudnativecon welcome to my talk mckay it is a container orchestration platform for geo-distributed multi-clusters environments my name is mulugeta and i'm a phd candidate at the focus project at the university of rainwan in france and cloud native engineer fatima stasis ab so today i would like to talk about the evolution of cloud deployments in the past few years and some of the challenges in multi-clusters management in terms of resource management and application deployment and then i'll briefly discuss kubernetes federation which is the provisioner will create the kubernetes cluster on openstack so let's go to openstack and check if the machines have been created so now first masternode for our new clusters is created so it will take a couple of minutes until the cluster is up and

### Excerpt da transcript

hello kubecon and cloudnativecon welcome to my talk mckay it is a container orchestration platform for geo-distributed multi-clusters environments my name is mulugeta and i'm a phd candidate at the focus project at the university of rainwan in france and cloud native engineer fatima stasis ab so today i would like to talk about the evolution of cloud deployments in the past few years and some of the challenges in multi-clusters management in terms of resource management and application deployment and then i'll briefly discuss kubernetes federation which is the foundation of our work and then i will briefly discuss the architecture and controllers of our platform this and lastly show you a demonstration of our platform in action so in the last few years we have seen uh an increasingly geographically distributed cloud deployments the major cloud providers now have data centers in many regions of the world we can identify three main geography deployments namely hybrid cloud multi-cloud and fog computing in hybrid cloud we deploy applications on data centers from private and public cloud providers in the multi-cloud case we deploy applications on multiple public clouds or data centers from multiple regions of the same a public cloud provider the last one for computing is an emerging geo-distributed computing paradigm where we have resources from private public as well as micro data centers that are distributed in vast geographical areas in the aims to be closer to end users much of this evolution is driven by the increasing demands of modern applications some of the non-functional requirements are low latency the desire to provide fast services to end users by placing our applications in regions where most of our users are located high bandwidths and reliable connectivity in the case of iot and video analytics for example would like to have high bandwidth and reliable connectivity so that we can upload a vast amount of data to the analytics framework we have other requirements also such as high availability disaster recovery scalability security and compliance so managing this duration environment is not easy there are a lot of challenges we are talking in terms of hundreds and thousands of clusters which become almost impossible to manage manually so we need to have automated ways of deploying applications and managing resources this means solving many challenges some of which are resilience in terms of hardware and network failures providing various placemen
