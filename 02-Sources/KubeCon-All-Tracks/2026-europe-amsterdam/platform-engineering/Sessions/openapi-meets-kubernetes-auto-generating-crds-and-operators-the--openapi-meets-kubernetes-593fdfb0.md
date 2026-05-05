---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Sergiusz Urbaniak", "Jose Vázquez González", "MongoDB"]
sched_url: https://kccnceu2026.sched.com/event/2CW2y/openapi-meets-kubernetes-auto-generating-crds-and-operators-the-smart-way-sergiusz-urbaniak-jose-vazquez-gonzalez-mongodb
youtube_search_url: https://www.youtube.com/results?search_query=OpenAPI+Meets+Kubernetes%3A+Auto-Generating+CRDs+and+Operators+the+Smart+Way+CNCF+KubeCon+2026
slides: []
status: parsed
---

# OpenAPI Meets Kubernetes: Auto-Generating CRDs and Operators the Smart Way - Sergiusz Urbaniak & Jose Vázquez González, MongoDB

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Sergiusz Urbaniak, Jose Vázquez González, MongoDB
- Schedule: https://kccnceu2026.sched.com/event/2CW2y/openapi-meets-kubernetes-auto-generating-crds-and-operators-the-smart-way-sergiusz-urbaniak-jose-vazquez-gonzalez-mongodb
- Busca YouTube: https://www.youtube.com/results?search_query=OpenAPI+Meets+Kubernetes%3A+Auto-Generating+CRDs+and+Operators+the+Smart+Way+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre OpenAPI Meets Kubernetes: Auto-Generating CRDs and Operators the Smart Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW2y/openapi-meets-kubernetes-auto-generating-crds-and-operators-the-smart-way-sergiusz-urbaniak-jose-vazquez-gonzalez-mongodb
- YouTube search: https://www.youtube.com/results?search_query=OpenAPI+Meets+Kubernetes%3A+Auto-Generating+CRDs+and+Operators+the+Smart+Way+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2_nbkiI_UJU
- YouTube title: OpenAPI Meets Kubernetes: Auto-Generating CRDs and Oper... Sergiusz Urbaniak & Jose Vázquez González
- Match score: 0.799
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/openapi-meets-kubernetes-auto-generating-crds-and-operators-the-smart/2_nbkiI_UJU.txt
- Transcript chars: 30572
- Keywords: operators, obviously, resource, operator, machine, resources, remote, external, mongodb, little, called, another, terraform, status, fields, created, notion, cluster

### Resumo baseado na transcript

Um, welcome to our talk uh autogenerating codds and operators the smart way. And who in this audience is integrating those operators into developer platforms? we're particularly interested in stateful applications so we run MongoDB on your premises um but also obviously machine learning inference workloads on your clusters the other type of operators that we saw over time uh and I see this sort of like of a progression any any deployments on your cluster, but it creates certificates obviously by leveraging cube APIs and CRDs or you have operators that do policy enforcement um or for me for me the um orbback controller inside the controller manager that comes with Kubernetes is also This whole like MongoDB Atlas Kubernetes operator kind of like um makes sense from the naming perspective that lets you provision those clusters. And these are just some examples again like the Atlas Kubernetes operator that we are working on.

### Excerpt da transcript

Yeah. >> Okay. Can you hear me? All right, that looks good. Um, okay. Welcome everybody. Um, I hope you're enjoying CubeCon. Who Who enjoys CubeCon? Hands up. Awesome. Very cool. Um, welcome to our talk uh autogenerating codds and operators the smart way. Uh, my name is Sergio, which is completely unpronouncable. Just call me search, whatever works for you. I'm a software engineer at MongoDB. >> I'm Jose, also a software engineer with service. Cool. Um, so what are we trying to solve? I want to see another hands up. Uh, who in this room is still developing operators? That's very good. Cool. Awesome. And who in this audience is integrating those operators into developer platforms? Also very good. Okay, good news. You're in the right room. Um, so what are we trying to solve? Especially those of you who do operators and who do platform integration? obviously are aware that Kubernetes is not only a workload scheduler anymore, right? I mean that was all the rage when the project was created. Uh but today Kubernetes is obviously also a foundation to build platforms.

Um and more formally uh we see more and more demand and more and more things being done uh to connect Kubernetes to external systems and this is also the stuff that we have been working on for the last two and a half years and obviously the whole notion of the cube resource model and the API centric nature of Kubernetes lets you in a great way um abstract and expose APIs to users in a unified way. Um what we found with the operator that we are implementing that the classic operator pattern doesn't really work well. And what I what do I mean with operator pattern? I mean the pattern as we used to develop operators or still are that are launching workloads on your clusters. They're like a little bit of a different beast and they they work a little bit like in similar way uh in in different ways. So to make things a little bit more concrete what are we talking about when I when I speak about different operator types? Obviously the elephant in the room is the workload operators right like the key idea is to run something inside cube something that occupies CPU GPU nowadays obviously memory network um independent if it's stateful or stateless obviously I mean we are from MongoDB so we're particularly interested in stateful applications so we run MongoDB on your premises um but also obviously machine learning inference workloads on your clusters the other type of operators that we saw over time uh and I s
