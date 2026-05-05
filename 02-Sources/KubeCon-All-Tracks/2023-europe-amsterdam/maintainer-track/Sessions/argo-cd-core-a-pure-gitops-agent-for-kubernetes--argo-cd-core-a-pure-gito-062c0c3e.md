---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "Kubernetes Core", "Community Governance"]
speakers: ["Alexander Matyushentsev", "Akuity", "Leonardo Luz Almeida", "Intuit"]
sched_url: https://kccnceu2023.sched.com/event/1HySi/argo-cd-core-a-pure-gitops-agent-for-kubernetes-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Argo+CD+Core+-+A+Pure+GitOps+Agent+for+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Argo CD Core - A Pure GitOps Agent for Kubernetes - Alexander Matyushentsev, Akuity & Leonardo Luz Almeida, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alexander Matyushentsev, Akuity, Leonardo Luz Almeida, Intuit
- Schedule: https://kccnceu2023.sched.com/event/1HySi/argo-cd-core-a-pure-gitops-agent-for-kubernetes-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Argo+CD+Core+-+A+Pure+GitOps+Agent+for+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Argo CD Core - A Pure GitOps Agent for Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HySi/argo-cd-core-a-pure-gitops-agent-for-kubernetes-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit
- YouTube search: https://www.youtube.com/results?search_query=Argo+CD+Core+-+A+Pure+GitOps+Agent+for+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nXEb1yZ580E
- YouTube title: Argo CD Core - A Pure GitOps Agent for Kubernetes - Alexander Matyushentsev & Leonardo Luz Almeida
- Match score: 0.756
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/argo-cd-core-a-pure-gitops-agent-for-kubernetes/nXEb1yZ580E.txt
- Transcript chars: 28304
- Keywords: argo, application, cluster, clusters, applications, server, components, component, traffic, basically, itself, access, manage, little, repository, presentation, installation, administrators

### Resumo baseado na transcript

all right so let's begin my name is Alexander I'm really happy to see you all here and happy to welcome you to our presentation we're going to talk about using cargo City core as a pure pure github's agent for kubernetes so I'm a long time maintainer of Fargo project and currently a Chief Architect at Acuity company that tries to move Argo to the next level we have two speakers today I will let Michael speaker introduce himself hi everyone my name is Leonardo I usually go by

### Excerpt da transcript

all right so let's begin my name is Alexander I'm really happy to see you all here and happy to welcome you to our presentation we're going to talk about using cargo City core as a pure pure github's agent for kubernetes so I'm a long time maintainer of Fargo project and currently a Chief Architect at Acuity company that tries to move Argo to the next level we have two speakers today I will let Michael speaker introduce himself hi everyone my name is Leonardo I usually go by Leo I'm one of the maintainers of Argo City and Argo rollouts projects I work as a staff software developer at Intuit um okay let me start by presenting the agenda for today I will start by providing you the problem statement providing a list of use cases that Argo City core aims to address okay but before jumping into what Argo City core is I want to provide you a quick overview on agrocity component architecture I believe with this small piece of knowledge things are going to be less magical and more logical honestly I prefer this way maybe you do too um okay then I'm going to present you uh give a brief introduction into Argo City core and that's the moment where Alex will join the the presentation showing you um the use cases that I listed in the in the in the problem statement uh slide and also providing you a demo one quick note uh think that uh in one of those future slides Alex is going to provide you a QR code with the links to the GitHub repo that he's going to be using during his demo so if you want to have access to that repo for future reference maybe it's a good idea to keep your cell phone prepared to scan that QR code cool all right so let's get started and um yeah in our in the project we like to to hear constructive uh criticism uh and actually this talk was based on a list of those uh okay and it usually goes by um Argo City is great but feature X doesn't fit our use case to the point that for for those users they will consider alternatives which is not a problem per se but uh let's see what are those feature X that some users are complaining okay so um first one is a multi-tenancy so there are some use cases where for example you have cluster admin who wants to um manage their old cluster and they have no intention in sharing that cluster with other teams they don't need isolation so multi-tenancy is not something that for this type of use case is going to make a lot of sense then next common complaint that we hear is the proprietary or back model right so if you kn
