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
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Alex Collins", "Intuit", "Jason Hall", "Red Hat"]
sched_url: https://kccncna2021.sched.com/event/lV3h/argo-and-tekton-pushing-the-boundaries-of-the-possible-on-kubernetes-alex-collins-intuit-jason-hall-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Argo+and+Tekton%3A+Pushing+the+Boundaries+of+the+Possible+on+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Argo and Tekton: Pushing the Boundaries of the Possible on Kubernetes - Alex Collins, Intuit & Jason Hall, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Operations]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Alex Collins, Intuit, Jason Hall, Red Hat
- Schedule: https://kccncna2021.sched.com/event/lV3h/argo-and-tekton-pushing-the-boundaries-of-the-possible-on-kubernetes-alex-collins-intuit-jason-hall-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Argo+and+Tekton%3A+Pushing+the+Boundaries+of+the+Possible+on+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Argo and Tekton: Pushing the Boundaries of the Possible on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV3h/argo-and-tekton-pushing-the-boundaries-of-the-possible-on-kubernetes-alex-collins-intuit-jason-hall-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Argo+and+Tekton%3A+Pushing+the+Boundaries+of+the+Possible+on+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iPRw_n_JV4o
- YouTube title: Argo and Tekton: Pushing the Boundaries of the Possible on Kubernetes - Alex Collins & Jason Hall
- Match score: 0.93
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/argo-and-tekton-pushing-the-boundaries-of-the-possible-on-kubernetes/iPRw_n_JV4o.txt
- Transcript chars: 35317
- Keywords: container, containers, argo, actually, pretty, write, process, resources, another, resource, server, workflows, tecton, custom, termination, directory, status, shared

### Resumo baseado na transcript

hi we're here from argo and techton to talk about pushing the boundaries of what's possible on kubernetes so who are he well i'm alex i work at intuit i specialize in kubernetes and kind of oltp stuff and the lead engineer on argo workflows argo events and argo labs dataflow and i like coffee and cycling ideally a bike ride to a nice coffee shop is my kind of ideal sunday yeah and i'm jason hall i work at red hat i've been in involved with various developer tools

### Excerpt da transcript

hi we're here from argo and techton to talk about pushing the boundaries of what's possible on kubernetes so who are he well i'm alex i work at intuit i specialize in kubernetes and kind of oltp stuff and the lead engineer on argo workflows argo events and argo labs dataflow and i like coffee and cycling ideally a bike ride to a nice coffee shop is my kind of ideal sunday yeah and i'm jason hall i work at red hat i've been in involved with various developer tools for nyon eight years now i helped co-found the tecton project and i like pizza and sitting and ideally sitting while eating pizza um and what do we do um like alex said he works on argo workflows argo workflows is a general purpose workflow execution engine uh steps in argo runs sequentially and tasks in argo run uh in a dag or a directed acyclic graph uh it's built on kubernetes and it has a cute logo techton is also a continuous delivery focused workflow engine steps run sequentially tasks run in a dag it's built on kubernetes and we also have a cute logo they're friends why did we decide to build on kubernetes um when building a workflow service there are two well there are a lot of problems uh two of the biggest ones are node management just managing the resources uh to that will be doing the work and another is workload scheduling so when a user's request comes in i want to do this work putting that on one of those nodes to do the work well uh if you are at kubecon and know anything about kubernetes kubernetes is very good at these and so we by building on kubernetes we don't ever have to well we do have to deal with it sometimes but mainly we just get to offload that and make it kubernetes problem kubernetes also has a great a great resource in custom resources this lets us build flexible extensible apis inside the kubernetes api server and ecosystem and we basically get our back for free our back is another huge source of work if you don't have one already built for you and kubernetes built that for us so we love it and then there is the long tail of just community stuff that's all of you that's everyone outside that's everyone watching uh watching all of this later there's a huge community around kubernetes that provide people to look out for the security of the platform and the performance of the platform and observing the platform and portability across different architectures and platforms um client tooling for all of these things and multi-tenancy concerns and policy enforcement and to
