---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Tim Goodwin", "UC Santa Cruz"]
sched_url: https://kccncna2025.sched.com/event/27FXy/ive-got-99-problems-and-theyre-all-controllers-tim-goodwin-uc-santa-cruz
youtube_search_url: https://www.youtube.com/results?search_query=I%E2%80%99ve+Got+99+Problems+and+They%E2%80%99re+All+Controllers+CNCF+KubeCon+2025
slides: []
status: parsed
---

# I’ve Got 99 Problems and They’re All Controllers - Tim Goodwin, UC Santa Cruz

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Tim Goodwin, UC Santa Cruz
- Schedule: https://kccncna2025.sched.com/event/27FXy/ive-got-99-problems-and-theyre-all-controllers-tim-goodwin-uc-santa-cruz
- Busca YouTube: https://www.youtube.com/results?search_query=I%E2%80%99ve+Got+99+Problems+and+They%E2%80%99re+All+Controllers+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre I’ve Got 99 Problems and They’re All Controllers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXy/ive-got-99-problems-and-theyre-all-controllers-tim-goodwin-uc-santa-cruz
- YouTube search: https://www.youtube.com/results?search_query=I%E2%80%99ve+Got+99+Problems+and+They%E2%80%99re+All+Controllers+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=E1f87Z6mij0
- YouTube title: I’ve Got 99 Problems and They’re All Controllers - Tim Goodwin, UC Santa Cruz
- Match score: 0.86
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/ive-got-99-problems-and-theyre-all-controllers/E1f87Z6mij0.txt
- Transcript chars: 39411
- Keywords: controller, controllers, resource, simulation, deployment, actually, process, cluster, control, testing, reconcile, server, update, reconciles, native, replica, custom, another

### Resumo baseado na transcript

Uh, and today I'm going to be talking about Kubernetes controllers and how we can compose them together to build higher level platform abstractions, the headaches involved with this process, and a new simulation testing tool that I've been developing as part of my research to make this process a lot easier. So, when Kubernetes started off about a decade ago, it was about orchestrating containers. And Kubernetes makes it really easy to apply this model to new use cases through the extensibility of its API. So to add new functionality to the platform, say for example, we want to teach Kubernetes to manage some database that's called like FUDB. Of course with kubernetes we can deploy this using a service a deployment and our foodb custom resource. And this is what enables Kubernetes to function as a platform for building platforms.

### Excerpt da transcript

Hello, my name is Tim Goodwin. Um, I'm a PhD student at UC Santa Cruz. Uh, and today I'm going to be talking about Kubernetes controllers and how we can compose them together to build higher level platform abstractions, the headaches involved with this process, and a new simulation testing tool that I've been developing as part of my research to make this process a lot easier. So, when Kubernetes started off about a decade ago, it was about orchestrating containers. But today we can do way more than that. We can use Kubernetes to manage a whole variety of cloud infrastructure. Um frameworks like crossplane let us use Kubernetes to manage infrastructure that's even external to the cluster itself. Uh so how did we get from you know a better way to run containers to a universal control plane for anything we want? Well, the answer lies in the power and generality of the underlying model that Kubernetes uses in which we describe some desired state of our system in terms of logical resources and then the system is going to continuously reconcile that state with controllers.

So, of course, this model works great for orchestrating containers, but it generalizes far beyond that. Pretty much anything that can be described declaratively and reconciled continuously, we can manage with Kubernetes. And Kubernetes makes it really easy to apply this model to new use cases through the extensibility of its API. So to add new functionality to the platform, say for example, we want to teach Kubernetes to manage some database that's called like FUDB. Well, we can simply define a new resource type or CRD for fu DB and then we're going to implement the behavior of that resource with a custom food DB controller. So resources and controllers give us the building blocks to make custom control plane functionality for whatever we want. And it's very powerful to be able to add a new resource type for something like foodb. But there's even more power in our ability to compose resources together to create higher level abstractions. So say we're in some software organization and we're constantly writing applications that all need to talk or have some network endpoint and they all need to store some data maybe using foodb.

Of course with kubernetes we can deploy this using a service a deployment and our foodb custom resource. But we could also abstract away these architectural details using a higher level composite resource type. So as platform engineers we could add another resource. M
