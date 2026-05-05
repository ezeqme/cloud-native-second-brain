---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Victor Varza", "Aneci Adrian", "Adobe Inc"]
sched_url: https://kccncna2023.sched.com/event/1R2tq/beyond-the-cluster-harnessing-the-power-of-kubernetes-namespaces-victor-varza-aneci-adrian-adobe-inc
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+the+Cluster%3A+Harnessing+the+Power+of+Kubernetes+Namespaces+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Beyond the Cluster: Harnessing the Power of Kubernetes Namespaces - Victor Varza & Aneci Adrian, Adobe Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Victor Varza, Aneci Adrian, Adobe Inc
- Schedule: https://kccncna2023.sched.com/event/1R2tq/beyond-the-cluster-harnessing-the-power-of-kubernetes-namespaces-victor-varza-aneci-adrian-adobe-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+the+Cluster%3A+Harnessing+the+Power+of+Kubernetes+Namespaces+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Beyond the Cluster: Harnessing the Power of Kubernetes Namespaces.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tq/beyond-the-cluster-harnessing-the-power-of-kubernetes-namespaces-victor-varza-aneci-adrian-adobe-inc
- YouTube search: https://www.youtube.com/results?search_query=Beyond+the+Cluster%3A+Harnessing+the+Power+of+Kubernetes+Namespaces+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=33n8zw-n63E
- YouTube title: Beyond the Cluster: Harnessing the Power of Kubernetes Namespaces - Victor Varza & Aneci Adrian
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/beyond-the-cluster-harnessing-the-power-of-kubernetes-namespaces/33n8zw-n63E.txt
- Transcript chars: 27965
- Keywords: cluster, running, platform, clusters, worker, spaces, policies, application, process, resource, argo, upgrade, request, pretty, namespace, policy, shredder, inside

### Resumo baseado na transcript

hello everyone my name is Adrien and together with Victor we are going to present you our five-e journey of how we leverage name spaces in a multi-talent fashion in order to scale the adoption of kubernetes at Adobe and also how we build a foundation for the Adobes developer platform few words about me I'm currently Elite CL softer engineer at Adobe and I'm part of the EOS team which is the team that powers the kubernetes platform at Adobe I'm also a member of the kubernetes GitHub organization

### Excerpt da transcript

hello everyone my name is Adrien and together with Victor we are going to present you our five-e journey of how we leverage name spaces in a multi-talent fashion in order to scale the adoption of kubernetes at Adobe and also how we build a foundation for the Adobes developer platform few words about me I'm currently Elite CL softer engineer at Adobe and I'm part of the EOS team which is the team that powers the kubernetes platform at Adobe I'm also a member of the kubernetes GitHub organization and currently I'm focusing on contributing as much as I can to the cluster API ecosystem and when I'm not not breaking clusters I like seeking for big bikes as you can see on the slide Victor do you want to introduce yourself and kick off the presentation yeah sure uh thank you Adrian hello everyone uh my name is Victor V I'm technical lead Adobe um I'm also passionate about open source contributions I am one of the organizers of kues community days or kcd in Romania which will be the first kcd event in the southeast of Europe and it will be organized next year in April together with Adrian we are the authors of adobe SK Shredder and Costa registry two open source projects that we successfully integrated to our platform and about each we are going to talk today in the first part of the presentation I'm going to talk about project Tios kubernetes name spaces and capacity management and Adrian will continue with uh governance policies multi tenacy at scale and non-disruptive kubernetes upgrades plus a live demo so stay tuned before we dive in I would like to share with you a nice quote by uh Martin Kean which I found in his recent book title inspired he says it doesn't matter how good your engineering team is if they are not giv something worldwide to build in other words it is important what your engineering teams are building but also the target audience at Adobe our kubernetes platform called EOS it's used by amazing internal engineering teams which are working at Adobe products such as Adobe Photoshop Adobe analytics Adobe Firefly Adobe experience manager Adobe sign and so on Project itos it's a cross cloud multi-tenant kubernetes based platform built through the collaboration between the Adobe infrastructure teams and product development teams the initial version of ethos has its roots in 20 2015 and it was built with Docker and dco and it was first in production in 2016 it was a good decision at that moment to start with dcos because we gain experience with cont
