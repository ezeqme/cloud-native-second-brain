---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["AI ML", "GitOps Delivery"]
speakers: ["Savin Goyal", "Outerbounds", "Yuan Tang", "Akuity"]
sched_url: https://kccncna2023.sched.com/event/1R2u4/beyond-prototypes-production-ready-ml-systems-with-metaflow-and-argo-project-savin-goyal-outerbounds-yuan-tang-akuity
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+Prototypes%3A+Production-Ready+ML+Systems+with+Metaflow+and+Argo+Project+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Beyond Prototypes: Production-Ready ML Systems with Metaflow and Argo Project - Savin Goyal, Outerbounds & Yuan Tang, Akuity

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[GitOps Delivery]]
- País/cidade: United States / Chicago
- Speakers: Savin Goyal, Outerbounds, Yuan Tang, Akuity
- Schedule: https://kccncna2023.sched.com/event/1R2u4/beyond-prototypes-production-ready-ml-systems-with-metaflow-and-argo-project-savin-goyal-outerbounds-yuan-tang-akuity
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+Prototypes%3A+Production-Ready+ML+Systems+with+Metaflow+and+Argo+Project+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Beyond Prototypes: Production-Ready ML Systems with Metaflow and Argo Project.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2u4/beyond-prototypes-production-ready-ml-systems-with-metaflow-and-argo-project-savin-goyal-outerbounds-yuan-tang-akuity
- YouTube search: https://www.youtube.com/results?search_query=Beyond+Prototypes%3A+Production-Ready+ML+Systems+with+Metaflow+and+Argo+Project+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mupRo7TX_H8
- YouTube title: Beyond Prototypes: Production-Ready ML Systems with Metaflow and Argo Pro... Savin Goyal & Yuan Tang
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/beyond-prototypes-production-ready-ml-systems-with-metaflow-and-argo-p/mupRo7TX_H8.txt
- Transcript chars: 32837
- Keywords: workflows, workflow, machine, learning, metaflow, argo, organization, engineering, access, models, compute, native, scientist, provide, training, orchestrator, events, systems

### Resumo baseado na transcript

welcome to today's session around bing machine Learning Systems um my name is sain I'm the co-founder CTO of out of bounds where we are building machine learning platforms so that all organizations can build ml systems in a more straightforward manner before starting out of bounds I was at Netflix for close to six years helping build out their machine learning platforms so for those of you in the crowd who like Netflix's recommendations um much of my work went into that and if you not like Netflix's recommendations the same sort of like criteria and the same principles apply across all clouds and as I mentioned previously right like most data access patterns uh for machine learning are high throughput data access patterns where maybe you're responsible for pulling data for all partitions

### Excerpt da transcript

welcome to today's session around bing machine Learning Systems um my name is sain I'm the co-founder CTO of out of bounds where we are building machine learning platforms so that all organizations can build ml systems in a more straightforward manner before starting out of bounds I was at Netflix for close to six years helping build out their machine learning platforms so for those of you in the crowd who like Netflix's recommendations um much of my work went into that and if you not like Netflix's recommendations I left Netflix a couple of years ago I don't have much to do anymore with that but Jokes Aside it's like the today's agenda you know especially in light of all the excitement that we see around llms and geni is how do you actually go about building principled ml systems especially for organizations who might be new to machine learning what is the right mindset to think about it and what are the right tooling Investments that need to be done and of course I mean you know like we at Netflix and many other places that I have worked at there was a point in time when we were also new to ml adoption now one mechanism of thinking about investing in machine learning is to think of it as no different than software engineering where you sort of like plan out ahead you think about every single step in great amount of detail you have your project plans you have your quarterly yearlong commitments to your leadership and then you sort of like get to work and you start building it in Cathedral style imagine you know like if let's say in early 2010s if you were building a recommendation system it's very likely that you would sort of like you know think about it that way that okay where am I getting all the data that I need to train my recommendation model how do I think about that specific model and you would build a platform that would be very specific to that single use case that works beautifully well uh as long as you are willing to make that investment make that commitment uh which often times can be non-trivial uh but it also comes with certain specific downsides right I mean Cathedrals are expensive to build that also then limits the number of areas where you can invest in from an ml point of view uh they're also very static very rigid if your requirements change if there are new Innovations in machine learning as it so often happens then uh you might be left behind or at least there is a risk for this and then on the other end of the spectrum you can go
