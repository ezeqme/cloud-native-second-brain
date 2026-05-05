---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Mark Lavi", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcvx/project-lightning-talk-empowering-data-protection-for-stateful-applications-on-kubernetes-with-kanister-mark-lavi-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Empowering+Data+Protection+for+Stateful+Applications+on+Kubernetes+with+Kanister+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Empowering Data Protection for Stateful Applications on Kubernetes with Kanister - Mark Lavi, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Mark Lavi, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcvx/project-lightning-talk-empowering-data-protection-for-stateful-applications-on-kubernetes-with-kanister-mark-lavi-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Empowering+Data+Protection+for+Stateful+Applications+on+Kubernetes+with+Kanister+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Empowering Data Protection for Stateful Applications on Kubernetes with Kanister.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvx/project-lightning-talk-empowering-data-protection-for-stateful-applications-on-kubernetes-with-kanister-mark-lavi-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Empowering+Data+Protection+for+Stateful+Applications+on+Kubernetes+with+Kanister+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6CXsWNOqYSw
- YouTube title: Project Lightning Talk: Empowering Data Protection for Stateful Applications on Kuberne... Mark Lavi
- Match score: 0.964
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-empowering-data-protection-for-stateful-applica/6CXsWNOqYSw.txt
- Transcript chars: 5935
- Keywords: cluster, application, backup, framework, distributed, applications, blueprints, action, protection, canister, thursday, inside, backups, blueprint, stateful, sandbox, elastic, search

### Resumo baseado na transcript

I'm Mark Lavy and today we're going to talk about storage track data protection canister. But we're going to tell you the problem that we solve, how we solve it better, and why you should join up. So persistence on the cluster, data services on the cluster is something that people are trying to go from step one to step two to step three maybe or going from step three back to step two because they hit a performance bottleneck or they're scaling their cluster in a different way or they need to manage their applications in a completely different way for operational performance and other security needs. So we have helped design a framework called canister to help orchestrate and take care of all these different situations and even help you change them because it is a framework for helping orchestrate data protection on a cluster with on and off cluster concerns. Once you get your application onto Kubernetes and get your data onto Kubernetes or adjacent to Kubernetes, there are a million different domains you need to span.

### Excerpt da transcript

All right. Hi everybody. I'm Mark Lavy and today we're going to talk about storage track data protection canister. Uh canister is one of those brand new 130 sandbox projects. But we're going to tell you the problem that we solve, how we solve it better, and why you should join up. Uh you can reach me lobby through all the different places. Uh, I will be manning our project pavilion booth kiosk 208 all day Thursday. Come find me if you have any other questions. I'm one of the maintainers of the project. So, it's no secret that Kubernetes explosion exploding uh usage is now incredibly stateful. Distributed applications like Elastic Search and so on are putting state on the cluster. There's no more GitOps your way out of this anymore. Right? This is what we're seeing with all of our customers. Uh, and so it doesn't even have to be Elastic Search or other distributed app apps like our new vector databases, but any database. And so as soon as you have state on the cluster, you need to talk about backup and recovery.

Let's not even talk about disaster recovery because this is the first step. And even with the first step, there's three steps. And with the three steps, we're even to 32 0 something like that now because we extend this to cloud and multicloud backup scenarios. I won't read the slides to you because you're all smarter than me. So let's keep going. But that's how we do things. And so now the question is where are the data services? Are they off the cluster? That's on the left. Are they on the cluster but not in the application? That's in the middle. Or are they actually distributed inside the pods with the application? Right? We're seeing all of these scenarios happening. So persistence on the cluster, data services on the cluster is something that people are trying to go from step one to step two to step three maybe or going from step three back to step two because they hit a performance bottleneck or they're scaling their cluster in a different way or they need to manage their applications in a completely different way for operational performance and other security needs.

So we have helped design a framework called canister to help orchestrate and take care of all these different situations and even help you change them because it is a framework for helping orchestrate data protection on a cluster with on and off cluster concerns. So that is because it is such a complex world out there. Once you get your application onto Kubernetes and get your da
