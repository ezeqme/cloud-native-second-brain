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
speakers: ["Verena Traub", "b'nerd GmbH"]
sched_url: https://kccnceu2026.sched.com/event/2CVzU/operators-in-action-making-kubernetes-work-for-you-verena-traub-bnerd-gmbh
youtube_search_url: https://www.youtube.com/results?search_query=Operators+in+Action%3A+Making+Kubernetes+Work+for+You+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Operators in Action: Making Kubernetes Work for You - Verena Traub, b'nerd GmbH

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Verena Traub, b'nerd GmbH
- Schedule: https://kccnceu2026.sched.com/event/2CVzU/operators-in-action-making-kubernetes-work-for-you-verena-traub-bnerd-gmbh
- Busca YouTube: https://www.youtube.com/results?search_query=Operators+in+Action%3A+Making+Kubernetes+Work+for+You+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Operators in Action: Making Kubernetes Work for You.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzU/operators-in-action-making-kubernetes-work-for-you-verena-traub-bnerd-gmbh
- YouTube search: https://www.youtube.com/results?search_query=Operators+in+Action%3A+Making+Kubernetes+Work+for+You+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=V8fTE-SeVmg
- YouTube title: Operators in Action: Making Kubernetes Work for You - Verena Traub, b'nerd GmbH
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/operators-in-action-making-kubernetes-work-for-you/V8fTE-SeVmg.txt
- Transcript chars: 27265
- Keywords: operator, cluster, actually, within, resource, custom, instance, basically, client, premium, pretty, please, instances, resources, operators, definition, application, course

### Resumo baseado na transcript

Uh in my talk today I will talk about um Kubernetus operators and how they can help us. And what I brought is actually a case from um my company, a very recent one. um and he wants to get them on Kubernetes because he actually counts with a lot of users right we are not talking about one or two instances per day but rather hundred maybe so a lot right that was his idea and the let's Hello and welcome um to the land of Kubernetes operator operators and as this slide says I mean that's basically what we found out pretty fast that's for us the the easiest solution to just get this project started um and as the slide also says I mean basically operators are a way to um extend the Kubernetes API right so we can extend it and we can build in our very domain specific weird appsp specific let's say knowledge into it, right? what kind of enables us um this kind of little snippet is that we can interact with our new resources like we would do with the classic Kubernetes resources right we get pots we can get our hello world apps Right, that's just basically the

### Excerpt da transcript

So it's exactly quarter 3. I think we can start. There are still some people coming. There is some spots here and there. I mean you will find one. And first of all thank you so much for being here. I I mean that's what I would guess is a packed room. Thank you so much all for your interest. Uh in my talk today I will talk about um Kubernetus operators and how they can help us. And what I brought is actually a case from um my company, a very recent one. So actually it's just I mean just released but it was released pretty recent um to production and you are actually the very very first people hearing about this. Um so I hope this makes you kind of feeling honored. Let's say I mean faces don't show but okay. Um last um but before really digging into first things first maybe who am I? Uh I'm Vina. I'm a former tech and recruiting manager turned web developer turned AWS consultant turned cloud consultant working now at Berd and we at Berd it might surprise you but we love Kubernetes and we basically we are a managed uh service provider so we um work on clusters every day and we deploy a lot of stuff to it uh also some apps and also one very specific app I won't call the name but let's say It's the basis of today's um case and it's a very let's call it special application.

Um meaning it's not really built for Kubernetes to be really honest. You can run uh it on Kubernetes but it's not exactly built. It has some very weird specifics uh when it comes to um operating it. So well it might not be the ideal application where I would say like okay cool now let's go for Kubernetes with it. Uh still we have a client and that client came to us um and he wanted to uh build a startup, build a new company and act as a reseller for this one application. Meaning he would like to offer to his clients um different packages of the app. Uh meaning there's a basic package having some sub applications within there is a premium and an ultimate one. um and he wants to get them on Kubernetes because he actually counts with a lot of users right we are not talking about one or two instances per day but rather hundred maybe so a lot right that was his idea and the let's say the starting point was basically okay we have an app the client is building which is actually there for onboarding clients so uh users so a user can sign up and choose okay I want to have package premium them I will pay for it and then off we go some magic happens and instances spin up right and the client wasn't rea
