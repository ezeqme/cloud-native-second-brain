---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Chip Zoller", "Dolis Sharma", "Nirmata"]
sched_url: https://kccncna2022.sched.com/event/182Nj/kyverno-introduction-and-overview-chip-zoller-dolis-sharma-nirmata
youtube_search_url: https://www.youtube.com/results?search_query=Kyverno+Introduction+And+Overview+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kyverno Introduction And Overview - Chip Zoller & Dolis Sharma, Nirmata

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Chip Zoller, Dolis Sharma, Nirmata
- Schedule: https://kccncna2022.sched.com/event/182Nj/kyverno-introduction-and-overview-chip-zoller-dolis-sharma-nirmata
- Busca YouTube: https://www.youtube.com/results?search_query=Kyverno+Introduction+And+Overview+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kyverno Introduction And Overview.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Nj/kyverno-introduction-and-overview-chip-zoller-dolis-sharma-nirmata
- YouTube search: https://www.youtube.com/results?search_query=Kyverno+Introduction+And+Overview+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YHkQWN5kC-I
- YouTube title: Kyverno: An Introduction and Deep Dive - Panel
- Match score: 0.817
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kyverno-introduction-and-overview/YHkQWN5kC-I.txt
- Transcript chars: 32596
- Keywords: policy, policies, actually, cluster, engine, resources, certain, called, write, admission, validating, create, network, images, another, security, configurations, created

### Resumo baseado na transcript

awesome thank you everyone so hi again welcome I am Anushka mital and uh I work with chainu guard as a software engineer there I have been a main uh I have been a contributor to kerno for quite some time I think almost four years now I am a maintainer to one of its projects and today we have a really cool panel in front of you and we're going to talk about all things kerno so kerno of course uh I'll let everyone introduced themselves you know as support these validating admission policies also right so you can actually use Kono C for validating all sear use cases and even there is a quick demo which you can uh use in the kuo playground to play around to play with the validating admission

### Excerpt da transcript

awesome thank you everyone so hi again welcome I am Anushka mital and uh I work with chainu guard as a software engineer there I have been a main uh I have been a contributor to kerno for quite some time I think almost four years now I am a maintainer to one of its projects and today we have a really cool panel in front of you and we're going to talk about all things kerno so kerno of course uh I'll let everyone introduced themselves you know as in when we take the mic so that was for me kerno is a kubernetes native policy engine but let's stop right there and understand what a policy engine is first right so a policy engine to understand very easily is kind of like a traffic cop a traffic cop would sort of make sure that are some you know traffic rules and regulations and people follow it and they'll make sure there are no wrong entries no people not wearing seat belts people are you know abiding by rules so similarly a policy engine will play the same role for your workloads for your clusters a policy engine will make sure uh whatever rules you've you know defined in the beginning your workload complies with it a policy engine will sit on top of your workload make sure nothing wrong goes in makes sure everything is as you would expect it no surprises no heart attack tax all of a sudden so that's a policy engine and now what is cerno right so cerno like I said is a kuber kuber's native policy engine it is a cncf incubating project which offers you multiple capabilities it lets you handle validation Dynamic validation so it makes sure that whatever is going inside your cluster is uh abiding by rules that you've set so if you don't want something with a label XY Z that that resource does not go inside your workload apart from validation it also offers you mutation generation it will help you clean up your workloads and also verify images that are already inside or that are going inside your clusters now that's really cool and that's actually one of the reasons why you should you would want to use kerno so that's our next slide why would you want to use kerno now anyone familiar with kubernetes would know what a deployment yaml looks like right because kerno is kubernetes native your policies that you're supposed to write and make sure they're present in your cluster they look very similar to your regular yaml so it's very easy to use it's very easy to understand and get started with it KERO offers a kerno CLI as well how that helps you is um by you know let
