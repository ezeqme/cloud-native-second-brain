---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Hristo Hristov", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFxh/project-lightning-talk-namespace-multi-tenancy-but-all-the-problems-related-to-it-hristo-hristov-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Namespace+Multi-Tenancy%2C+But+All+The+Problems+Related+To+It+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Namespace Multi-Tenancy, But All The Problems Related To It - Hristo Hristov, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Hristo Hristov, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFxh/project-lightning-talk-namespace-multi-tenancy-but-all-the-problems-related-to-it-hristo-hristov-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Namespace+Multi-Tenancy%2C+But+All+The+Problems+Related+To+It+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Namespace Multi-Tenancy, But All The Problems Related To It.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxh/project-lightning-talk-namespace-multi-tenancy-but-all-the-problems-related-to-it-hristo-hristov-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Namespace+Multi-Tenancy%2C+But+All+The+Problems+Related+To+It+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-imwG5MP2aw
- YouTube title: Project Lightning Talk: Namespace Multi-Tenancy, But All The Problems Related To It - Hristo Hristov
- Match score: 0.995
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-namespace-multi-tenancy-but-all-the-problems-re/-imwG5MP2aw.txt
- Transcript chars: 5372
- Keywords: multi-tenancy, developers, namespaces, tenant, around, cluster, capsule, absolutely, namespace, course, resources, everything, consume, policies, integrate, related, sandbox, launched

### Resumo baseado na transcript

So, my name's Christopher and I'm a project maintainer for a project capsule, which is a CNCF sandbox project. So, we launched around 4 years ago as a CNCF sandbox project and we're going to talk a little bit more about multi-tenancy, specifically namespace multi-tenancy. And you know that's absolutely bad, like you have to do something because the cost has been all over the place. And you take you take a stop at the challenges like resource pools where the developers need set of resources, you give them per tenant, and it's up to them to how they going to consume them. And in the end what you achieve is like a very, very good level of multi-tenancy where the developers can self-serve them, like it's absolutely what a cheap cost, so it's if you have a look now like how the architecture like for a very high overview looks like, you can see we started very simple, like we use mostly Kubernetes primitives.

### Excerpt da transcript

All right, thank you. So, my name's Christopher and I'm a project maintainer for a project capsule, which is a CNCF sandbox project. Like we launched I think around 4 years ago. Closer microphone, okay. So, we launched around 4 years ago as a CNCF sandbox project and we're going to talk a little bit more about multi-tenancy, specifically namespace multi-tenancy. So, for people who dealt with the platform engineering or with Kubernetes and developers overall, like they've probably been in this situation or close to this situation where you have start small, like you have few namespaces maybe for dev, staging, and production. But suddenly your company starts to scale up and you eventually reach to a point where you have around probably 200-300 microservices, a lot of developers, and so the doing kubectl get namespaces sometimes takes so long that you have enough time to make a coffee, come back, and still not have an output. And also like your air back is absolutely all over the place, like it's very hard to keep track what is deployed, what is it.

And the developers, of course, very smart people, they get around your limitations in your Kubernetes cluster by getting more namespaces and more namespaces so they can get more resources. And you start to think about the multi-tenancy now. And the next native thing that comes to your mind in Kubernetes, that's a cluster. So, you start to do in multi-tenancy in a cluster where you provision maybe one cluster per your data, per your teams. But this also quickly turns into a nightmare. So, you have now multiple clusters, you have to patch them, you have to secure them, you have to like the developers also do funky stuff inside them and they start to break. And generally it's a big, big nightmare. And but at this point it works, so you have a multi-tenancy now, like you're multi-tenant. Then you see okay, job is done. And eventually you get a thank you letter, but that thank you letter is not from your management. Oh, no. It's from your cloud provider and they thank you for meeting your their next quarter revenue target.

And you know that's absolutely bad, like you have to do something because the cost has been all over the place. And that's where we come in. It's a project capsule. It's where one namespace is absolutely not enough, but entire cluster is just way too much for you. And what we do is we introduce the the the concept called the tenant, which wraps around multiple namespaces. The idea is like the devel
