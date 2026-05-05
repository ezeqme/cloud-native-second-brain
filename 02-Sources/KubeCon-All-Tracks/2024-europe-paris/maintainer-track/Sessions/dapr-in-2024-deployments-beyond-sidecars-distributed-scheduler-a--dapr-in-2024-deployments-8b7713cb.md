---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Security", "GitOps Delivery", "Kubernetes Core", "Community Governance"]
speakers: ["Yaron Schneider", "Josh van Leeuwen", "Diagrid"]
sched_url: https://kccnceu2024.sched.com/event/1Yhg0/dapr-in-2024-deployments-beyond-sidecars-distributed-scheduler-api-and-app-level-zero-trust-yaron-schneider-josh-van-leeuwen-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Dapr+in+2024%3A+Deployments+Beyond+Sidecars%2C+Distributed+Scheduler+API+and+App-Level+Zero+Trust+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Dapr in 2024: Deployments Beyond Sidecars, Distributed Scheduler API and App-Level Zero Trust - Yaron Schneider & Josh van Leeuwen, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[GitOps Delivery]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Yaron Schneider, Josh van Leeuwen, Diagrid
- Schedule: https://kccnceu2024.sched.com/event/1Yhg0/dapr-in-2024-deployments-beyond-sidecars-distributed-scheduler-api-and-app-level-zero-trust-yaron-schneider-josh-van-leeuwen-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Dapr+in+2024%3A+Deployments+Beyond+Sidecars%2C+Distributed+Scheduler+API+and+App-Level+Zero+Trust+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Dapr in 2024: Deployments Beyond Sidecars, Distributed Scheduler API and App-Level Zero Trust.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhg0/dapr-in-2024-deployments-beyond-sidecars-distributed-scheduler-api-and-app-level-zero-trust-yaron-schneider-josh-van-leeuwen-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Dapr+in+2024%3A+Deployments+Beyond+Sidecars%2C+Distributed+Scheduler+API+and+App-Level+Zero+Trust+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TN4RlsQ32zw
- YouTube title: Dapr in 2024: Deployments Beyond Sidecars, Distributed Scheduler API and App-Level Zero Trust
- Match score: 1.1
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/dapr-in-2024-deployments-beyond-sidecars-distributed-scheduler-api-and/TN4RlsQ32zw.txt
- Transcript chars: 29713
- Keywords: workflows, cluster, application, basically, certificate, actually, important, identity, actors, security, sidecar, reminders, infrastructure, control, message, running, secret, developers

### Resumo baseado na transcript

I am a steering committee member of the Dapr project, also a core maintainer for the runtime. I work at Diagrid, which is a company I started back in January of 2022. Dapr runs really well on top of Kubernetes or just as a binary, a single binary that can run on your machine. So, for each one of these APIs, you will find a set of components that you can use to connect your infrastructure and Dapr will provide additional security and reliability guarantees on top of what you'd normally find. I'm not going to cover all of them, but um the most important thing I think, you know, the first is to give developers uh tools that solve their problems of the day. If there is a new problem that developers, application developers face, Dapr will be set to meet that problem tomorrow, which is why Dapr is continuing to add more and more APIs.

### Excerpt da transcript

Okay, let's get started. Hello, everyone. My name is Yaron Schneider. I am a steering committee member of the Dapr project, also a core maintainer for the runtime. I work at Diagrid, which is a company I started back in January of 2022. And today we're working with lots of major enterprises on their open source Dapr adoption. And here with me today Yeah, hi everyone. I'm Josh. I'm also a core maintainer of the Dapr project. Yeah, I'm also a software engineer at Diagrid. Yeah. All right. It's great to have you all here. Um just so you know, you're really helping out the project simply by attending this talk because the questions you will be asking us afterwards and you know, getting to know all of the latest things that are happening in the project really helps us because then you will open up GitHub issues, right? You'll go on Discord and you'll tell us what you like and what you don't like. And this is what helps the project really the most. So, let's start talking about what Dapr is. And we'll really cover this for people who don't know um Dapr.

So, all the stuff in the middle that you're seeing, all of these different building blocks, those APIs, that's the stuff you don't really have to deal with. Service discovery, invocation, uh pub/sub, creating event-driven systems, connecting to databases, pub/sub, message brokers, configuration stores, coding for resiliency, fault tolerance, observability, monitoring, monitoring the whole thing, right? Um creating resiliency policies, circuit breakers, timeouts, retries, all of that stuff just adds up so much. And so Dapr gives you these building blocks, these developer primitives, these APIs for you to be able to focus on what matters to you the most, which is your business, your IP, your core business. Um and Dapr really takes care of all of the rest. Dapr runs really well on top of Kubernetes or just as a binary, a single binary that can run on your machine. And it'll run pretty much on top of any Kubernetes cluster also. Um if you're running on Kubernetes and OpenShift. And Dapr integrates with your existing stack.

So, Dapr is not a replacement to your infrastructure. It actually makes it better. It makes it more secure. It makes it more reliable by providing sometimes features that you don't find if you're talking to the underlying database or pub/sub or secret store directly. Um Dapr has a vibrant community. We'll talk about that in a second, but we have over 120 of these specific component level integrat
