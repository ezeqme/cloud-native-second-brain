---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Operations"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Megan O'Keefe", "Shabir Mohamed Abdul Samadh", "Google"]
sched_url: https://kccncna2021.sched.com/event/m4sT/yaml-your-cloud-managing-your-hosted-resources-with-kubernetes-megan-okeefe-shabir-mohamed-abdul-samadh-google
youtube_search_url: https://www.youtube.com/results?search_query=YAML+Your+Cloud%21+Managing+Your+Hosted+Resources+With+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# YAML Your Cloud! Managing Your Hosted Resources With Kubernetes - Megan O'Keefe & Shabir Mohamed Abdul Samadh, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Operations]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Megan O'Keefe, Shabir Mohamed Abdul Samadh, Google
- Schedule: https://kccncna2021.sched.com/event/m4sT/yaml-your-cloud-managing-your-hosted-resources-with-kubernetes-megan-okeefe-shabir-mohamed-abdul-samadh-google
- Busca YouTube: https://www.youtube.com/results?search_query=YAML+Your+Cloud%21+Managing+Your+Hosted+Resources+With+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre YAML Your Cloud! Managing Your Hosted Resources With Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/m4sT/yaml-your-cloud-managing-your-hosted-resources-with-kubernetes-megan-okeefe-shabir-mohamed-abdul-samadh-google
- YouTube search: https://www.youtube.com/results?search_query=YAML+Your+Cloud%21+Managing+Your+Hosted+Resources+With+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gmRC7gNDxB0
- YouTube title: YAML Your Cloud! Managing Your Hosted Resources With Kubernetes - Megan O'Keefe & Abdul Samadh
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/yaml-your-cloud-managing-your-hosted-resources-with-kubernetes/gmRC7gNDxB0.txt
- Transcript chars: 28552
- Keywords: resources, resource, cluster, manage, config, controller, running, inside, created, google, bucket, actually, connector, provider, policy, controllers, called, create

### Resumo baseado na transcript

hello everyone welcome to this talk on yaml your cloud managing cloud resources from kubernetes to kick off things let us introduce ourselves megan you want to go first yeah hi everyone my name is megan o'keefe i'm a developer relations engineer at google cloud and yeah i've been working with kubernetes and cloud stuff for the last five years or so so i'm really excited to be here thank you very much uh yeah i'm shabir abdul samad i'm a developer relations engineer as well at google cloud i've

### Excerpt da transcript

hello everyone welcome to this talk on yaml your cloud managing cloud resources from kubernetes to kick off things let us introduce ourselves megan you want to go first yeah hi everyone my name is megan o'keefe i'm a developer relations engineer at google cloud and yeah i've been working with kubernetes and cloud stuff for the last five years or so so i'm really excited to be here thank you very much uh yeah i'm shabir abdul samad i'm a developer relations engineer as well at google cloud i've been working on kubernetes and cloud for the last three to four years so looking forward to this talk let's get started uh so to start off let me brief on what's on the deck we are going to discuss about what is the kubernetes resource model just to give a brief introduction why we would want to manage cloud resources using kubernetes and then finally go over some of the ways in which we can manage cloud-hosted resources using kubernetes so to start the discussion we would like to speak uh we would like to speak about two main areas the api server in kubernetes and the declarative model that kubernetes has so most of the introduction the next slide can be something that you're already familiar with so all of kubernetes component centers around the api server it's what the control plane uses as the source of truth for external tools clients and other internal components so it's how the nodes know what containers they need to run it's how any outside actor like a ci cd system interacts with the cluster and the api server exposes an http api that the user external clients and also the internal components in the control plane can connect to so through this we can query and manipulate any of the resources that is understood by the cluster and some examples of these kubernetes detect lines are the cube control cli tool client libraries like client go or in any other languages and also the kubernetes dashboard it could be on a standalone cooperative deployment or if one of the manage manage kubernetes provider dashboards so the second thing we want to cover before we get to krm is the declarative model adopted by the api server of kubernetes so instead of telling how to achieve what you want what the declarative model says is what you want and how kubernetes knows how to get to that part is using the concept of controllers so every resource or an object in kubernetes has a controller attached to it and controllers are trying to continuously drive from the observed state to
