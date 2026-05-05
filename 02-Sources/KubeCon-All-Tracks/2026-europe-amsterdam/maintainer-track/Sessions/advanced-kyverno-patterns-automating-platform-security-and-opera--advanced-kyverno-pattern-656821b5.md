---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Platform Engineering", "Community Governance"]
speakers: ["Frank Jogeleit", "Nirmata", "Johannes Sonner", "Deutsche Telekom"]
sched_url: https://kccnceu2026.sched.com/event/2EF49/advanced-kyverno-patterns-automating-platform-security-and-operations-frank-jogeleit-nirmata-johannes-sonner-deutsche-telekom
youtube_search_url: https://www.youtube.com/results?search_query=Advanced+Kyverno+Patterns+%3A+Automating+Platform+Security+and+Operations+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Advanced Kyverno Patterns : Automating Platform Security and Operations - Frank Jogeleit, Nirmata; Johannes Sonner, Deutsche Telekom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Frank Jogeleit, Nirmata, Johannes Sonner, Deutsche Telekom
- Schedule: https://kccnceu2026.sched.com/event/2EF49/advanced-kyverno-patterns-automating-platform-security-and-operations-frank-jogeleit-nirmata-johannes-sonner-deutsche-telekom
- Busca YouTube: https://www.youtube.com/results?search_query=Advanced+Kyverno+Patterns+%3A+Automating+Platform+Security+and+Operations+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Advanced Kyverno Patterns : Automating Platform Security and Operations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF49/advanced-kyverno-patterns-automating-platform-security-and-operations-frank-jogeleit-nirmata-johannes-sonner-deutsche-telekom
- YouTube search: https://www.youtube.com/results?search_query=Advanced+Kyverno+Patterns+%3A+Automating+Platform+Security+and+Operations+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7YuMvcW5wRA
- YouTube title: Advanced Kyverno Patterns : Automating Platform Security and Ope... Frank Jogeleit & Johannes Sonner
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/advanced-kyverno-patterns-automating-platform-security-and-operations/7YuMvcW5wRA.txt
- Transcript chars: 25548
- Keywords: policy, policies, already, cluster, certificate, platform, resources, reporting, possible, create, everything, namespace, pretty, admission, resource, kivero, second, basically

### Resumo baseado na transcript

very welcome to our Kyono maintainer track today about advanced Kyono uh patterns automating platform security and operations. I'm also the creator of the sub project policy reporter if someone of you using it. Uh it allows you to configure it as an envoy plug-in and also uh validate your envoy requests with the same or very similar uh API uh like the Kyerno Kubernetes validating policies. As I mentioned it's really easy to learn for people who know Kubernetes already. Um I have a little bit more or a few more demographics questions about the audience before we go into the use cases. Who is using Kyerno already for anything that is not at all related to security?

### Excerpt da transcript

very welcome to our Kyono maintainer track today about advanced Kyono uh patterns automating platform security and operations. Um my name is Frank. I'm a Kyuno maintainer for I think almost two years now. I'm also the creator of the sub project policy reporter if someone of you using it. And >> yeah, I'm Johannes. I work for Deutsche Telecom and I'm a platform engineering lead there. So let's take a a short look on our agenda today. So at first I do a short introduction what Kyono is, what it does and what makes it different from alternatives. So who of you knows Kyono or using it? Yeah, really quite a lot. That's >> who who uses uses it in production. >> Okay, >> really great. So then I keep the introduction short. So most of you know Kyerno as an admission controller means it's registering inside your um Kubernetes cluster as an validating um web hook as well as an mutating uh web hook. So it intercepts your admission requests and is able to operate on your admission reviews. So you can validate resources and you can mutate resources.

Um it's also possible to generate uh resources and the background controller enables also background work. So it's also able to operate on already existing workloads if you want to apply policies on your already running applications in your already existing clusters. So, but you may know that Kubernetes already has some built-in policies which are called validating admission policies and mutating admission policies. So, why won't you choose Kyerno over it? So, there are some key features Kyerno brings you on top of this already existing solutions. At one, we have a really uh good reporting system which makes it possible to validate as I mentioned already existing workloads. So you can see if you have an application running for months, how it applies to your new policy. And if you want to um make your already existing workloads compliant over time, you are able to do so because you can use the reporting system to show what needs to be changed to comply against your uh policies. We also as mentioned supporting generation which means you can for example autogenerate um limits and request quotas for new created namespaces.

You can synchronize a central image pull request secret across other namespaces you want to using it as well without the need of copying manually from one name space to another. And we are providing cleanup policies to remove no longer needed resources based on a label or add expressions. We also have some
