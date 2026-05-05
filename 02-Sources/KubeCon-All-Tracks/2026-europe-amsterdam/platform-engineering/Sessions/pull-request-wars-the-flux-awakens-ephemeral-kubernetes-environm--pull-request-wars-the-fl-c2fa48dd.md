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
themes: ["Platform Engineering", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Matteo Bianchi", "GitHub", "Stefan Prodan", "ControlPlane"]
sched_url: https://kccnceu2026.sched.com/event/2CW37/pull-request-wars-the-flux-awakens-ephemeral-kubernetes-environments-strike-back-matteo-bianchi-github-stefan-prodan-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Pull+Request+Wars%3A+The+Flux+Awakens+-+Ephemeral+Kubernetes+Environments+Strike+Back+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Pull Request Wars: The Flux Awakens - Ephemeral Kubernetes Environments Strike Back - Matteo Bianchi, GitHub & Stefan Prodan, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Matteo Bianchi, GitHub, Stefan Prodan, ControlPlane
- Schedule: https://kccnceu2026.sched.com/event/2CW37/pull-request-wars-the-flux-awakens-ephemeral-kubernetes-environments-strike-back-matteo-bianchi-github-stefan-prodan-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Pull+Request+Wars%3A+The+Flux+Awakens+-+Ephemeral+Kubernetes+Environments+Strike+Back+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Pull Request Wars: The Flux Awakens - Ephemeral Kubernetes Environments Strike Back.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW37/pull-request-wars-the-flux-awakens-ephemeral-kubernetes-environments-strike-back-matteo-bianchi-github-stefan-prodan-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Pull+Request+Wars%3A+The+Flux+Awakens+-+Ephemeral+Kubernetes+Environments+Strike+Back+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uGhHeYZ4zGg
- YouTube title: Pull Request Wars: The Flux Awakens - Ephemeral Kubernetes Environ... Matteo Bianchi & Stefan Prodan
- Match score: 0.906
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/pull-request-wars-the-flux-awakens-ephemeral-kubernetes-environments-s/uGhHeYZ4zGg.txt
- Transcript chars: 21953
- Keywords: request, flux, github, actually, release, platform, cluster, course, little, operator, anything, copilot, everything, create, deploy, branch, commit, engine

### Resumo baseado na transcript

Welcome to Por Request Wars, the Flux Awakens Ephemeral Environment Strike Back. open source contributor in Kubernetes and former release me release team member of Kubernetes upstream and today with me Stefan Stefan Prodan principal engineer at control plane creator of flagger how many of you know flagger or use flagger yes po amazing uh core maintainer The idea that that what what we want to showcase is that without having you know any kind of uh Kubernetes configuration in my app repo I can instruct flux to deploy it on a cluster as an FML environment and uh why is FML Of course, here you should run your, you know, llinters, uh, unit tests, end to end tests if you have that kind of thing with Kubernetes kind. But no matter how much testing you are embedding here in CI, it will never cover uh you know what actually happens with the application once it runs in Kubernetes. So you can avoid like Kubernetes costs in case you're not using your local host of course.

### Excerpt da transcript

Welcome to Por Request Wars, the Flux Awakens Ephemeral Environment Strike Back. So, this talk is about Star Wars. No, I'm kidding. It was just uh there to uh for cloud, you know, for getting accepted. It worked. So, my name is Mat Bankei. I'm a solutions engineer at GitHub, CNCF ambassador. I'm a former startup CTO and a semi-retired Devril. I've been speaking too much lately. open source contributor in Kubernetes and former release me release team member of Kubernetes upstream and today with me Stefan Stefan Prodan principal engineer at control plane creator of flagger how many of you know flagger or use flagger yes po amazing uh core maintainer of flux uh and you know 20 plus years in software engineering and also the mind behind the flux operator and also the flux UI. Tomorrow he has another talk about that. So if you wanna you want to join him, it's really cool. Platform teams in the AI era. How many platform engineers we have in the room? Okay. Almost half of the room is a platform engineer. Amazing.

>> How many are sales? >> Yeah. So the more you tighten your grip in CI/CD pipelines, the more developers experience slips through your fingers. This is a quote from probably OB1 if he was a platform engineer. Uh the challenges today are various pipelines are hard to maintain a lot and inconsistent across teams. It's very difficult to have everyone using the same tooling and so we need something to standardize our workflows. Share staging environments a nightmare. a lot of maintenance, a lot of downtime as well. Uh long review cycles because of course you need to fix bugs. It needs to be quick and you need a quick feedback loop and that's not always possible. App teams want a lot of self-service because of course I'm a developer. I'm lazy. I don't want to do anything with infrastructure. I just want to get stuff for free. Good. That's amazing. But platform teams need governance. They need everything centralized. They need control. They need observability. they need to know their things you know and then AI and agentic coding which is great it helps in a in a lot of ways but it also creates a lot of slop uh and so we need to actually test in a real environment what we're doing and the answer to this and this is what we're going to talk about today it's a declarative prdriven githops native preview environments owned by platform teams but made for developers that can self serve by applying ing a single label on a GitHub pull request.

We have three repos
