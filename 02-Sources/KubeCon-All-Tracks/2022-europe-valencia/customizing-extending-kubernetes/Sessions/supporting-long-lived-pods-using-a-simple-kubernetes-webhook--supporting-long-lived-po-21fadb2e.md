---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Clément Labbe", "Slack"]
sched_url: https://kccnceu2022.sched.com/event/ytmo/supporting-long-lived-pods-using-a-simple-kubernetes-webhook-clement-labbe-slack
youtube_search_url: https://www.youtube.com/results?search_query=Supporting+Long-Lived+Pods+Using+a+Simple+Kubernetes+Webhook+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Supporting Long-Lived Pods Using a Simple Kubernetes Webhook - Clément Labbe, Slack

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Clément Labbe, Slack
- Schedule: https://kccnceu2022.sched.com/event/ytmo/supporting-long-lived-pods-using-a-simple-kubernetes-webhook-clement-labbe-slack
- Busca YouTube: https://www.youtube.com/results?search_query=Supporting+Long-Lived+Pods+Using+a+Simple+Kubernetes+Webhook+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Supporting Long-Lived Pods Using a Simple Kubernetes Webhook.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytmo/supporting-long-lived-pods-using-a-simple-kubernetes-webhook-clement-labbe-slack
- YouTube search: https://www.youtube.com/results?search_query=Supporting+Long-Lived+Pods+Using+a+Simple+Kubernetes+Webhook+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ISuV0-8x2uA
- YouTube title: Supporting Long-Lived Pods Using a Simple Kubernetes Webhook - Clément Labbe, Slack
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/supporting-long-lived-pods-using-a-simple-kubernetes-webhook/ISuV0-8x2uA.txt
- Transcript chars: 23756
- Keywords: killed, lifespan, cluster, admission, applications, feature, getting, request, simple, webhook, running, resources, instances, anything, actually, pretty, tolerations, slides

### Resumo baseado na transcript

hi i'm clem and my pronouns are he he and him and i work at slack as an engineer thanks for joining this session today where i'm going to talk about how it's lag we support long live pods using a simple kubernetes web hook and other bits and pieces so today after quickly introducing my team i'm going to describe what our so-called long lift pods and why we need to support them and then we're going to dive into what the solution that we came up with looks just want to mutate request on the flight on the right hand side i've got the architecture concept diagram from the cube builder documentation and this is probably too small to read but i just wanted to put this up to illustrate to show all

### Excerpt da transcript

hi i'm clem and my pronouns are he he and him and i work at slack as an engineer thanks for joining this session today where i'm going to talk about how it's lag we support long live pods using a simple kubernetes web hook and other bits and pieces so today after quickly introducing my team i'm going to describe what our so-called long lift pods and why we need to support them and then we're going to dive into what the solution that we came up with looks like and the different parts that it's made of finally we'll wrap up with a few of the limitations and possible future improvements so i work in a cloud compute team that's like and i'm based in melbourne we have about half the team in australia and the other half in the united states so let's look at some numbers to give you some context about like what we are dealing with on a good day at slack we get about 16 million concurrent users that load is spread onto some 45 000 ec2 instances so we are on aws we manage about 162 kubernetes clusters onto which some 316 services are deployed and we have just above a thousand engineers we also manage 235 chef roles and although my talk today is focused on our kubernetes compute platform we still have important applications running on our original compute stack which is chef on ec2 okay so let's look at what the problem is well the problem is that some pods want a long lifespan but the nodes that they're running on are getting killed so first let's look at why some pods want a long lifespan and then we look at what actually is killing our nodes okay so in an ideal world applications are 12-factor they're stateless they boot instantly they scale out infinitely without any drain on infrastructure they're fun to work with but unfortunately we don't live in an ideal world instead we live in a growth-obsessed capitalist society and we have to deal with applications that are stateful that can be slow to warm up that can be intensive on infrastructure when they do scale out maybe they don't like to get terminated early or maybe they hold on to some long-lived web sockets or sticky sessions or things we don't want to lose so while at slack we do have some ideal applications those were the first ones to migrate from our original chef compute platform to our kubernetes platform and so today we are left with a long tail of unruly ducks which are applications that are hard to move from one platform to another so this is peach apricot and plum my ducks and they are very cute fri
