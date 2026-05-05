---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Mangirdas Judeikis", "Cast AI", "Nabarun Pal", "Independent"]
sched_url: https://kccnceu2025.sched.com/event/1txAB/extending-kubernetes-resource-model-krm-beyond-kubernetes-workloads-mangirdas-judeikis-cast-ai-nabarun-pal-independent
youtube_search_url: https://www.youtube.com/results?search_query=Extending+Kubernetes+Resource+Model+%28KRM%29+Beyond+Kubernetes+Workloads+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Extending Kubernetes Resource Model (KRM) Beyond Kubernetes Workloads - Mangirdas Judeikis, Cast AI & Nabarun Pal, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Mangirdas Judeikis, Cast AI, Nabarun Pal, Independent
- Schedule: https://kccnceu2025.sched.com/event/1txAB/extending-kubernetes-resource-model-krm-beyond-kubernetes-workloads-mangirdas-judeikis-cast-ai-nabarun-pal-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Extending+Kubernetes+Resource+Model+%28KRM%29+Beyond+Kubernetes+Workloads+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Extending Kubernetes Resource Model (KRM) Beyond Kubernetes Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAB/extending-kubernetes-resource-model-krm-beyond-kubernetes-workloads-mangirdas-judeikis-cast-ai-nabarun-pal-independent
- YouTube search: https://www.youtube.com/results?search_query=Extending+Kubernetes+Resource+Model+%28KRM%29+Beyond+Kubernetes+Workloads+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=y0JgZ-hQ-Bo
- YouTube title: Extending Kubernetes Resource Model (KRM) Beyond Kubernetes Work... Mangirdas Judeikis & Nabarun Pal
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/extending-kubernetes-resource-model-krm-beyond-kubernetes-workloads/y0JgZ-hQ-Bo.txt
- Transcript chars: 22962
- Keywords: cluster, create, basically, clusters, database, compute, status, resource, control, resources, ideally, creating, pattern, storage, object, writing, already, virtual

### Resumo baseado na transcript

Uh where we talk about how do you extend KRM beyond Kubernetes workloads and reach to a state like KRM++. I do some Kubernetes maintenance and I also contribute to KCP on the side and you can find me on these socials. But then should we as a tech company who knows what their business goals are, what their business metrics are, you should ideally do what you know the best. Now all of this is known to us right it's sounds very trivial now and when you try to create any object in the Kubernetes control plane you essentially um have this specific format no matter what you are dealing with um other than probably So these three things make the Kubernetes resource model really powerful for your use cases. like do can you just start writing some go types use kubernetes code generator and then create crds um does sound easy but then you can do really u weird things with it so there are some pitfalls there are some gotchas that you have

### Excerpt da transcript

Good morning. Um feels great to see um a lot of you here in this talk. Uh where we talk about how do you extend KRM beyond Kubernetes workloads and reach to a state like KRM++. Um so so I'm MJ. I'm one of the maintainers at KCP. I work for Casti. We basically do funky things with Kubernetes. I am Navarun. I do some Kubernetes maintenance and I also contribute to KCP on the side and you can find me on these socials. So let's get started with the talk. So we're going to see three things in this talk. In part one, we're going to see um what is scarm if you are not really familiar with it or um don't know the gotchas or nitty-g gritties of it and we will come to know like why it got such success. Then we will explore how does KCP add to it and how uh the KCP project is pushing for the next evolution of KRM. And later on uh we will try to show you a demo of how do you create custom APIs without using CDs but still the Kubernetes API machinery through KCP. So let's get into a problem like why are we here and why are APIs so hard to do.

So imagine you are a tech company running a hybrid cloud setup and you want to create infra resources like compute or some networking stuff or some storage things. So you'd be interacting with a lot of different cloud providers if you are on multiple clouds. The problem that comes is consistency across providers. Every provider has their own different APIs. interoperability between them and then the whole ecosystem. How do you build things? When you try to integrate all of it, it surely becomes a little overwhelming and at that point you might ask yourself a lot of questions. What are we even doing? And often why we do that is we really like reinventing things. We like to build our own new standards. But then should we as a tech company who knows what their business goals are, what their business metrics are, you should ideally do what you know the best. You know your area of business. You know where is your value proposition and you should start to stop inventing outside those areas and you need to start seeing something which is more like a standard and used by a lot of people.

So we do really have an answer that we should do not try to reinvent if there are existing patterns that you can use. And there comes the Kubernetes resource model. You all have been using it through the Kubernetes API. It's basically the API surface of Kubernetes and how things are done. What are the key properties of those? First declariveness. So you
