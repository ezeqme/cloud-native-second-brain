---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Rob Scott", "Google", "James Strong", "Isovalent at Cisco"]
sched_url: https://kccnceu2025.sched.com/event/1txAl/making-the-leap-what-gateway-api-needs-to-support-ingress-nginx-users-rob-scott-google-james-strong-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Making+the+Leap%3A+What+Gateway+API+Needs+To+Support+Ingress-NGINX+Users+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Making the Leap: What Gateway API Needs To Support Ingress-NGINX Users - Rob Scott, Google & James Strong, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United Kingdom / London
- Speakers: Rob Scott, Google, James Strong, Isovalent at Cisco
- Schedule: https://kccnceu2025.sched.com/event/1txAl/making-the-leap-what-gateway-api-needs-to-support-ingress-nginx-users-rob-scott-google-james-strong-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Making+the+Leap%3A+What+Gateway+API+Needs+To+Support+Ingress-NGINX+Users+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Making the Leap: What Gateway API Needs To Support Ingress-NGINX Users.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAl/making-the-leap-what-gateway-api-needs-to-support-ingress-nginx-users-rob-scott-google-james-strong-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=Making+the+Leap%3A+What+Gateway+API+Needs+To+Support+Ingress-NGINX+Users+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EeegJKZ_4g0
- YouTube title: Making the Leap: What Gateway API Needs To Support Ingress-NGINX Users - Rob Scott & James Strong
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/making-the-leap-what-gateway-api-needs-to-support-ingress-nginx-users/EeegJKZ_4g0.txt
- Transcript chars: 27660
- Keywords: gateway, ingress, engineext, features, cuddle, engine, support, continue, conversation, functionality, experience, feature, around, maintainers, trying, migration, working, implement

### Resumo baseado na transcript

I know this has been an incredibly long day, so thank you for sticking around for the very last session of day one. Uh what gateway API needs to do to move to support ingress engine X users as hopefully they migrate to gateway API. Um it's you know design documentation having conversations testing um we do need those folks as contri non-code contributors as well but there's a big question of are we ready for this is gateway API ready for this is ingress engineext ready for this and Um it it is concerning from that perspective but we do have you know 43 dependencies across four architectures for three Helm versions. I was like, well, we're not going to do mod security because we're not going to do WFT. So whether you want to match based on headers, query params, methods, uh whether you want to modify request or response headers, make some cross namespace references.

### Excerpt da transcript

Hey everyone, happy day one of KubeCon. Thank you all for making it. I know this has been an incredibly long day, so thank you for sticking around for the very last session of day one. Uh we're going to be talking today about making the the leap. Uh what gateway API needs to do to move to support ingress engine X users as hopefully they migrate to gateway API. Uh my name is Rob Scott. I work at Google on Kubernetes networking. I'm also a gateway API maintainer and I also have used ingress engine X very heavily in production uh dozens of clusters and I am very grateful for ingress engine X being amazing. Uh but with that I'll hand it off to James. Hi everyone, my name is James Strong. I'm a solutions architect at Isovalent now at Cisco. I help folks implement Kubernetes networking with Selium and secure their clusters with Tetreon. So let's dive into a little bit of context. What are we talking about and why are we talking about both ingress engineext and gateway API? Because obviously ingress engineext in the name is an ingress implementation.

What does that have to do with gateway API? Well, let's back up a little bit. Uh how many people are familiar with gateway API? Okay, that's great. That's good. Um so gateway API graduated to GA in 2023. And one of the things I really like to highlight about this API is it's been in my opinion I think uh there's there's good data behind this is the most collaborative API in Kubernetes history. Uh we've had hundreds of contributors that have helped make it the API it is today. Uh it's a featurerich API that is a supererset of the ingress API and today we h have more than 30 implementations of the API already with more on the way. So it's been great to work with this community. It's really exciting to see kind of the next generation. Uh and really this was initially called ingress v2. So that should give you an idea of what the goal was. This was the next generation API for ingress. Uh and that's gateway. So with ingress engine X uh how many people are using ingress engine X? A lot. How many people had to patch their clusters last week?

There should be more hands up. Uh it is a SIG network sub project. Um I I didn't write this slide but it does say one of the most popular ingress controllers. Uh 40% of clusters according to whiz. Uh thanks whiz for that information. It has a lot a unique set of extensions for the ingress API via annotations and then config map. It has 118. That number I will continue to repeat throug
