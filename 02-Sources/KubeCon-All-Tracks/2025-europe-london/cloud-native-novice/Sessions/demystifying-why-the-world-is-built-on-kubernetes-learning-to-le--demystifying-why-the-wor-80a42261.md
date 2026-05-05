---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Cloud Native Novice"
themes: ["Kubernetes Core"]
speakers: ["Abby Bangser", "Syntasso", "Sebastien Blanc", "Port"]
sched_url: https://kccnceu2025.sched.com/event/1txGW/demystifying-why-the-world-is-built-on-kubernetes-learning-to-leverage-bespoke-crds-and-controllers-abby-bangser-syntasso-sebastien-blanc-port
youtube_search_url: https://www.youtube.com/results?search_query=Demystifying+Why+the+World+Is+Built+on+Kubernetes%3A+Learning+To+Leverage+Bespoke+CRDs+and+Controllers+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Demystifying Why the World Is Built on Kubernetes: Learning To Leverage Bespoke CRDs and Controllers - Abby Bangser, Syntasso & Sebastien Blanc, Port

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Abby Bangser, Syntasso, Sebastien Blanc, Port
- Schedule: https://kccnceu2025.sched.com/event/1txGW/demystifying-why-the-world-is-built-on-kubernetes-learning-to-leverage-bespoke-crds-and-controllers-abby-bangser-syntasso-sebastien-blanc-port
- Busca YouTube: https://www.youtube.com/results?search_query=Demystifying+Why+the+World+Is+Built+on+Kubernetes%3A+Learning+To+Leverage+Bespoke+CRDs+and+Controllers+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Demystifying Why the World Is Built on Kubernetes: Learning To Leverage Bespoke CRDs and Controllers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txGW/demystifying-why-the-world-is-built-on-kubernetes-learning-to-leverage-bespoke-crds-and-controllers-abby-bangser-syntasso-sebastien-blanc-port
- YouTube search: https://www.youtube.com/results?search_query=Demystifying+Why+the+World+Is+Built+on+Kubernetes%3A+Learning+To+Leverage+Bespoke+CRDs+and+Controllers+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dVM20108SRc
- YouTube title: Demystifying Why the World Is Built on Kubernetes: Learning To Lev... Abby Bangser & Sebastien Blanc
- Match score: 0.847
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/demystifying-why-the-world-is-built-on-kubernetes-learning-to-leverage/dVM20108SRc.txt
- Transcript chars: 23636
- Keywords: controller, resource, custom, controllers, developer, cluster, create, operator, platform, operators, deployment, resources, database, definition, define, anything, another, talking

### Resumo baseado na transcript

I'm a principal engineer at Centaso, uh, where we're building a framework for building platforms. And a lot of what we're doing is trying to make all of this a little bit more accessible. and they may be setting standards for Kubernetes around things like arbbacks or role-based access control and other things. But what they're looking at in this role as a developer is they're looking at extending Kubernetes to actually do more to not just do what Kubernetes does out of the box, but to bring more value to their organizations and and to their teams. So if I simplify this down even further, a user sees Kubernetes as some infrastructure. And it's part of why Kubernetes is taking over the world is because it does solve all of these problems extremely well.

### Excerpt da transcript

Good morning everyone. How are you doing? Good. Yeah, last day so few hours and then you can crash. Okay. Anyway, thank you so much for attending our talk. We will be talking about CRDS controllers. Let me introduce myself. I'm Sebastian Blonde. You can call me Sebie. I'm a developer advocate for port and developer uh internal portal. And uh Abby, hi. I'm Abby Bangzer. I'm a principal engineer at Centaso, uh, where we're building a framework for building platforms. And a lot of what we're doing is trying to make all of this a little bit more accessible. But today isn't about either of our products. It's about what makes Kubernetes so powerful in so many different contexts. And the thing is is that there are different models, interaction models for Kubernetes. And sometimes when you're talking to someone and you're confused about how they use Kubernetes, it might be because you're talking across these models. So I want to call them out and call attention to them. So the first is the user personality. And this is people who who might use cubectl which is the command line tool to be able to see what's going on in the cluster.

But the big thing here is that what they're focused on is what's what applications are running in the cluster. What are the pods that are running? how do they get logs from the software that's running in the cluster and that kind of thing. The second interaction model is around the administrator and this is people that probably definitely use the CLI tool uh but they're going to be focused around different things that they care about. They're more infrastructure oriented. They're looking at administrating a cluster. So how do they create the nodes? How do they do taints? How do they do upgrades of Kubernetes itself? and they may be setting standards for Kubernetes around things like arbbacks or role-based access control and other things. The third interaction model is the developer model and this is probably the least mo the least spoken about here at CubeCon or just in general. And often these developers have a background as either users or administrators or sometimes both. But what they're looking at in this role as a developer is they're looking at extending Kubernetes to actually do more to not just do what Kubernetes does out of the box, but to bring more value to their organizations and and to their teams.

So if I simplify this down even further, a user sees Kubernetes as some infrastructure. An administrator sees it as a contain
