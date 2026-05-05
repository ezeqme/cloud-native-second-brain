---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["Kubernetes Core"]
speakers: ["Masaki Kimura", "Takafumi Takahashi", "Hitachi"]
sched_url: https://kccnceu2023.sched.com/event/1HyVT/across-kubernetes-namespace-boundaries-your-volumes-can-be-shared-now-masaki-kimura-takafumi-takahashi-hitachi
youtube_search_url: https://www.youtube.com/results?search_query=Across+Kubernetes+Namespace+Boundaries%3A+Your+Volumes+Can+Be+Shared+Now%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Across Kubernetes Namespace Boundaries: Your Volumes Can Be Shared Now! - Masaki Kimura & Takafumi Takahashi, Hitachi

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Masaki Kimura, Takafumi Takahashi, Hitachi
- Schedule: https://kccnceu2023.sched.com/event/1HyVT/across-kubernetes-namespace-boundaries-your-volumes-can-be-shared-now-masaki-kimura-takafumi-takahashi-hitachi
- Busca YouTube: https://www.youtube.com/results?search_query=Across+Kubernetes+Namespace+Boundaries%3A+Your+Volumes+Can+Be+Shared+Now%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Across Kubernetes Namespace Boundaries: Your Volumes Can Be Shared Now!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyVT/across-kubernetes-namespace-boundaries-your-volumes-can-be-shared-now-masaki-kimura-takafumi-takahashi-hitachi
- YouTube search: https://www.youtube.com/results?search_query=Across+Kubernetes+Namespace+Boundaries%3A+Your+Volumes+Can+Be+Shared+Now%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FlcwiHRQIjw
- YouTube title: Across Kubernetes Namespace Boundaries: Your Volumes Can Be Shared Now! - M Kimura & T Takahashi
- Match score: 0.948
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/across-kubernetes-namespace-boundaries-your-volumes-can-be-shared-now/FlcwiHRQIjw.txt
- Transcript chars: 20570
- Keywords: namespace, volume, source, snapshot, feature, reference, created, access, create, resource, wordpress, namespaces, persistent, provisional, resources, second, special, deployed

### Resumo baseado na transcript

hello everyone thank you for coming today we are pleased to have the opportunity to make this presentation our topic for today is across kubernetes namespace boundaries your volume can be seen enough okay let's begin let me introduce my first my name is I have been contributing to the kubernetes community by implementing prohibition volume from close namespace snapshot my name is masaki Kimura I work for statue I have been contributing kubernetes Community to make grab Rock bottling feature and CSI feature GA and I designed and propose

### Excerpt da transcript

hello everyone thank you for coming today we are pleased to have the opportunity to make this presentation our topic for today is across kubernetes namespace boundaries your volume can be seen enough okay let's begin let me introduce my first my name is I have been contributing to the kubernetes community by implementing prohibition volume from close namespace snapshot my name is masaki Kimura I work for statue I have been contributing kubernetes Community to make grab Rock bottling feature and CSI feature GA and I designed and propose a cap that takahumi is implementing today we'll talk about the feature in the cap in detail just a disclaimer before we go any further this session is explained the specifications designs and implementations which are under discussion and development depending on the discussion they are subject to change our talk is divided into six parts first I will explain the existing kubernetes Concepts and features related to the issue that we are trying to solve then I will share the issue use cases and discussions around this feature after that takafumi will take over explain the current design and implementation show demos and then conclude okay let's begin with the existing concept and features related to the issue the first concept is namespace in kubernetes namespaces provide a mechanism for isolating groups of resources within a single cluster namespaces separate a cluster virtually for multiple users to share resources without the interference for example as described in the diagram Resources with the same name like part one can be created by multiple users if the namespaces are different like ns1 and ns2 and if their artwork is set properly we can make that only user run can access to the port one in the ns1 to prevent other users like user 2 from accessing to the pod the point here is that namespace is used as a security boundary to prevent Mauritius users from accessing to the resource in a namespace there is one more point that I must refer to not every resource is namespaced kubernetes resource consists of namespace resource and crosstalk resource namespace resource are usually consumed by normal users examples are Port deployment service and so on on the other hand Crest scope resource are usually managed by admins so normal users won't have permission to modify such resources examples node Street crust persistent volume and so on then I will explain storage related features from our namespace viewpoint let's begin with P
