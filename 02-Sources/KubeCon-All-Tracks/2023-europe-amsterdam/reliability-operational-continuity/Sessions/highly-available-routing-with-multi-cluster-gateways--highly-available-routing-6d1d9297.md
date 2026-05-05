---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["AI ML", "Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Rob Scott", "Google", "Liwen Wu", "AWS"]
sched_url: https://kccnceu2023.sched.com/event/1HyZO/highly-available-routing-with-multi-cluster-gateways-rob-scott-google-liwen-wu-aws
youtube_search_url: https://www.youtube.com/results?search_query=Highly+Available+Routing+with+Multi+Cluster+Gateways+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Highly Available Routing with Multi Cluster Gateways - Rob Scott, Google & Liwen Wu, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Rob Scott, Google, Liwen Wu, AWS
- Schedule: https://kccnceu2023.sched.com/event/1HyZO/highly-available-routing-with-multi-cluster-gateways-rob-scott-google-liwen-wu-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Highly+Available+Routing+with+Multi+Cluster+Gateways+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Highly Available Routing with Multi Cluster Gateways.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyZO/highly-available-routing-with-multi-cluster-gateways-rob-scott-google-liwen-wu-aws
- YouTube search: https://www.youtube.com/results?search_query=Highly+Available+Routing+with+Multi+Cluster+Gateways+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jd66OMad6TU
- YouTube title: Highly Available Routing with Multi Cluster Gateways - Rob Scott, Google & Liwen Wu, AWS
- Match score: 0.856
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/highly-available-routing-with-multi-cluster-gateways/jd66OMad6TU.txt
- Transcript chars: 26899
- Keywords: cluster, gateway, clusters, lattice, multi-cluster, version, network, controller, inventory, traffic, config, endpoints, little, mapped, configuration, actually, export, object

### Resumo baseado na transcript

time welcome everyone it's great to have you all here you may notice there are two speakers on the slides up front and there's only one of me unfortunately Lee win could not join us in person today don't worry she was able to pre-record all her slides she's got a great portion of the presentation today and we have some of our colleagues here who can help answer questions at the end so thank you everyone for putting up with this hybrid presentation but I'll get started first I'm here are a few reasons one reason is the inventory service owner want to upgrade to use new version of kubernetes for example you want to use new feature in kubernetes 1.24 but other services in cluster 1 say example F1 app2 they are now ready to upgrade the new kubernetes version yet that's one of the reasons the inventory service owner I'm going to try some of my part workload in new kubernetes service new kubernetes clusters another reason is [Music] um the the inventory service owner want to double the workload and and as you know the custom one is already at its full capacity for example it has reached the maximum number of parts in the cluster one so instead of scale up and try out your scalability during the production we

### Excerpt da transcript

time welcome everyone it's great to have you all here you may notice there are two speakers on the slides up front and there's only one of me unfortunately Lee win could not join us in person today don't worry she was able to pre-record all her slides she's got a great portion of the presentation today and we have some of our colleagues here who can help answer questions at the end so thank you everyone for putting up with this hybrid presentation but I'll get started first I'm Rob Scott and I'll hand it right over to leewen to introduce herself hello my name is Lee Wan Wu I am a software engineer at AWS focusing on AWS bpc networking for kubernetes my first major kubernetes contribution was designed and the development of AWS PC cni plugin for kubernetes networking over AWS VPC I am a active member of Gateway API community here I'm going to show you how we implemented Gateway API on top of AWS VPC lattice I'm sorry I couldn't meet you in person hopefully I will see you in person in future cool uh it's so sad that Lewin couldn't be here but uh we'll have a great presentation uh she's got some great content throughout this uh presentation today my name is Rob Scott I'm a software engineer at Google uh you can find me all over the place uh definitely happy to connect and talk about any of these topics at any point uh let's talk get right into it let's talk about the apis here now I may have skipped over at the beginning but we're talking about two apis here we're talking about multi-cluster services and Gateway API so before we go any further how many people have used multi-cluster services okay a handful that's that's impressive actually how many people have used Gateway API okay a few more that's great uh I I'm very biased I'm one of the maintainers of Gateway API along with Nick Shane and some great people over there so we're very interested in both Gateway API and how it could interact with multi-cluster service because these are both brand new kubernetes apis that have kind of evolved together and we're talking about how they can work in parallel so first there's Gateway API and there's a lot of talks at kubecon about Gateway API so I'm not going to go into lots of details here but understand that a Gateway in this case when we're talking about Cloud providers which we are today largely represents a cloud load balancer uh then routing would be your routing configuration so we have HP route and a bunch of other protocols represented with different route
