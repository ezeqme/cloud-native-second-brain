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
themes: ["Community Governance"]
speakers: ["Jonasz Łasut-Balcerzak", "Contributor"]
sched_url: https://kccnceu2026.sched.com/event/2EFxt/project-lightning-talk-what-can-crossplane-actually-do-a-real-world-field-guide-jonasz-lasut-balcerzak-contributor
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What+Can+Crossplane+Actually+Do%3F+A+Real+World+Field+Guide+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: What Can Crossplane Actually Do? A Real World Field Guide - Jonasz Łasut-Balcerzak, Contributor

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jonasz Łasut-Balcerzak, Contributor
- Schedule: https://kccnceu2026.sched.com/event/2EFxt/project-lightning-talk-what-can-crossplane-actually-do-a-real-world-field-guide-jonasz-lasut-balcerzak-contributor
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What+Can+Crossplane+Actually+Do%3F+A+Real+World+Field+Guide+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: What Can Crossplane Actually Do? A Real World Field Guide.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxt/project-lightning-talk-what-can-crossplane-actually-do-a-real-world-field-guide-jonasz-lasut-balcerzak-contributor
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What+Can+Crossplane+Actually+Do%3F+A+Real+World+Field+Guide+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l1LICWLtXIE
- YouTube title: Project Lightning Talk: What Can Crossplane Actually Do? A Real World Fiel... Jonasz Łasut-Balcerzak
- Match score: 0.947
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-what-can-crossplane-actually-do-a-real-world-fi/l1LICWLtXIE.txt
- Transcript chars: 4579
- Keywords: crossplane, provider, platform, providers, create, application, simple, resources, shared, developers, allows, examples, policies, deployments, complex, requirements, extend, multiple

### Resumo baseado na transcript

So one of the biggest benefits that you get with crossplane is of course that you get Kubernetes control plane and ecosystem together with it. So what you can which parts of Kubernetes ecosystem you can use with crossplane to enhance it is for example policies Kybero opa gatekeeper admission policies you can also reuse the same arbback that you use for your application deployments and then use it for you have security requirements that may change from day to day and crossplane actually allows you to create new composition revisions to just release updates to all cloud resources to be compliant with all those security requirements. For example, you can create a simple abstraction that allows you to deploy application to Kubernetes and then with a simple flag SSO enabled would create everything that is required for of to uh authentication create all resources from the gateway API of your choice So, Kubernetes, gateway API and cloud provider or identity provider and that way developer can just do one really simple resource without any knowledge about the internals and get a safe safely deployed application.

### Excerpt da transcript

So let's talk about what can crossplain do for you. Uh my name is Yonwas Baleshak. I work at Balawas which is Swiss insurance company. And let's just jump straight on the topic. Why should you choose crossplane? Sorry. Why should you choose crossplane for your platform APIs? So one of the biggest benefits that you get with crossplane is of course that you get Kubernetes control plane and ecosystem together with it. You all know and love Kubernetes. I mean we are at CubeCon. So what you can which parts of Kubernetes ecosystem you can use with crossplane to enhance it is for example policies Kybero opa gatekeeper admission policies you can also reuse the same arbback that you use for your application deployments and then use it for your infrastructure deployments that way and that brings me to the point that you get a single pane of glass for both your application and infra deployments which can be pretty useful. You can reuse the same GitHubs flows and promotion flows for both your apps and infra. What you also get is implementation flexibility.

Um you can start really simple with YAML templating using pattern transform. You can also use Go templates which you know if you've used Helm uh but you can also use general purpose programming languages with functions. So you can use Go, TypeScript, Python. uh if you want to do something more complex than just templating and you get vast array of providers so for example provider Azure that I've mentioned and any other big cloud provider so what's the real world problem uh self-service in highly regulated multi-tenant environment is tricky uh you have a lot of resources that have shared usage but no shared responsibility for example w or DNS it's really hard to bring self-service to the developers for those um you also get a compliance which is ever evolving and you have security requirements that may change from day to day and crossplane actually allows you to create new composition revisions to just release updates to all cloud resources to be compliant with all those security requirements.

You can also extend the cloud provider product if you are missing something for compliance and you can build abstraction of a really complex configuration that's span across multiple providers or multiple tenant boundaries. um and I will show you three examples of what we did at Baloas um and what crossplane allowed us to do in such examples. So first example would be shared usage without shared responsibility in that case D
