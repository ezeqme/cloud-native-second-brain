---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Security", "Platform Engineering", "Kubernetes Core"]
speakers: ["Joaquin Rodriguez", "Microsoft"]
sched_url: https://kccnceu2024.sched.com/event/1YeN8/the-art-of-kubernetes-add-on-validation-secure-strategies-for-the-modern-developer-platform-joaquin-rodriguez-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=The+Art+of+Kubernetes+Add-on+Validation%3A+Secure+Strategies+for+the+Modern+Developer+Platform+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Art of Kubernetes Add-on Validation: Secure Strategies for the Modern Developer Platform - Joaquin Rodriguez, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Security]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Joaquin Rodriguez, Microsoft
- Schedule: https://kccnceu2024.sched.com/event/1YeN8/the-art-of-kubernetes-add-on-validation-secure-strategies-for-the-modern-developer-platform-joaquin-rodriguez-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=The+Art+of+Kubernetes+Add-on+Validation%3A+Secure+Strategies+for+the+Modern+Developer+Platform+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Art of Kubernetes Add-on Validation: Secure Strategies for the Modern Developer Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeN8/the-art-of-kubernetes-add-on-validation-secure-strategies-for-the-modern-developer-platform-joaquin-rodriguez-microsoft
- YouTube search: https://www.youtube.com/results?search_query=The+Art+of+Kubernetes+Add-on+Validation%3A+Secure+Strategies+for+the+Modern+Developer+Platform+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=odnZTPltaQc
- YouTube title: The Art of Kubernetes Add-on Validation: Secure Strategies for the Modern Developer Platform
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-art-of-kubernetes-add-on-validation-secure-strategies-for-the-mode/odnZTPltaQc.txt
- Transcript chars: 21927
- Keywords: cluster, basically, clusters, add-ons, validation, version, production, running, prometheus, deploy, argo, environment, add-on, pretty, validate, policy, instance, working

### Resumo baseado na transcript

well let's get started uh so welcome uh this is the art of kubernetes add-on validation uh secure strategies for the modern uh developer platform my name is hen Rodriguez I'm a software engineer at Microsoft I'm based in Austin Texas welcome so for today's agenda uh we're going to be talking about cluster add-ons uh I'll be introducing what they are in case you're not familiar with them uh why validation is important uh some of the validation strategies that you can take um and and Implement also I'll

### Excerpt da transcript

well let's get started uh so welcome uh this is the art of kubernetes add-on validation uh secure strategies for the modern uh developer platform my name is hen Rodriguez I'm a software engineer at Microsoft I'm based in Austin Texas welcome so for today's agenda uh we're going to be talking about cluster add-ons uh I'll be introducing what they are in case you're not familiar with them uh why validation is important uh some of the validation strategies that you can take um and and Implement also I'll be talking about secure rollouts and I will conclude uh today's presentation with a demo so closer add-ons why what are they and what do why do we care so closer add-ons are tools they're applications or services that enhance the functionality of a kubernetes cluster uh they provide essential capabilities that're not included in the core kubernetes components so if you think about kubernetes we know kubernetes is great and if you implement the vanilla cluster it can just do so much you need to enhance it you need to expand it so that's what cluster adoms are here for uh customization just like I was saying um they allow you to customize your kubernetes cluster according to the specific requirement uh of that cluster so no all cluster is the same some clusters might have different requirements so it just really depends on what is that you're trying to do uh Resource Management so add-ons help us manage resources uh to make sure that everything is running smoothly and and you know as as you're expecting it to be and also you're making sure that your resources are not uh being wasted um so basically also you have an add-on ecosystem so these add-ons are meant to interact well in some cases they are meant to inter act with one another so when we're validating we need to check that that when you're having these Integrations between um add-ons you know they they're working as as they're expected so uh these are some examples of cluster add-ons uh you can group them in different categories such as monitoring and logging networking and communication security and authorization and storage um I'm kind of curious by show of hands who has used any of these yeah pretty much everybody uh so that's great so okay then why do we need to validate these add-ons so the first thing is compat uh we want them to be compatible right so when you deploy these uh add-ons uh you need to make sure that they're compatible with for example the kubernetes version uh as kubernetes progresses
