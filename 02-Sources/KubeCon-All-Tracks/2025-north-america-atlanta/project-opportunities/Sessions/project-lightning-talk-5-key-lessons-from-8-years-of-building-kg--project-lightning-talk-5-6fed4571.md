---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Yuval Kohavi", "Lead Maintainer"]
sched_url: https://kccncna2025.sched.com/event/28yGT/project-lightning-talk-5-key-lessons-from-8-years-of-building-kgateway-yuval-kohavi-lead-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+5+Key+Lessons+From+8+Years+of+Building+Kgateway+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: 5 Key Lessons From 8 Years of Building Kgateway - Yuval Kohavi, Lead Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Yuval Kohavi, Lead Maintainer
- Schedule: https://kccncna2025.sched.com/event/28yGT/project-lightning-talk-5-key-lessons-from-8-years-of-building-kgateway-yuval-kohavi-lead-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+5+Key+Lessons+From+8+Years+of+Building+Kgateway+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: 5 Key Lessons From 8 Years of Building Kgateway.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/28yGT/project-lightning-talk-5-key-lessons-from-8-years-of-building-kgateway-yuval-kohavi-lead-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+5+Key+Lessons+From+8+Years+of+Building+Kgateway+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=G3Iu2ezSkVE
- YouTube title: Project Lightning Talk: 5 Key Lessons From 8 Years of Building Kgateway - Yuval Kohavi
- Match score: 0.995
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-5-key-lessons-from-8-years-of-building-kgateway/G3Iu2ezSkVE.txt
- Transcript chars: 4565
- Keywords: gateway, support, ingress, workloads, lessons, everything, extendability, everybody, learned, developing, kateway, routes, without, talking, initially, donated, notice, events

### Resumo baseado na transcript

I'm here to tell you about five key lessons we learned from eight years of developing K gateway. It's uh essentially what routes the traffic into the cluster into your workloads. We had, you know, Kubernetes support, Nomad support, console support, file support if you for whatever reason want to run it in a VM, NAT support for events. H performance gets impacted because it's hard to optimize when you have to all these abstractions that you have to fulfill. They're not sure if you're if if K gateway solved their problem because now it has not support. Uh you you know glue edge the the previous name of K gateway before we donated to the CNCF scaled up to a point.

### Excerpt da transcript

Hi everybody, welcome back from lunch. I hope it was good. Um, my name is Yuval Kohave. I'm the chief architect at Solo.io and K Gateway maintainer. I'm here to tell you about five key lessons we learned from eight years of developing K gateway. So quick intro about K gateway. Kateway is an API gateway. It's gateway API base the new ingress API. It's uh essentially what routes the traffic into the cluster into your workloads. Kateway works for AI workloads for regular workloads, microservices, lambda functions, and supports multiple data planes, avoid proxy if you're familiar with it, and the new agent gateway which me which is meant for AI workloads. All right. So, uh without further ado, let's start talking about the lessons we learned uh developing it in the almost last decade. So, first thing is uh that open governance accelerated growth. H initially we were very hesitant about donating our project to a foundation. We feared kind of losing control. But u as soon as we donated K gateway to the CNCF last year, last KubeCon North America, we immediately notice uh improved enga engagement in all of our channels.

You know, GitH request um Slack, you know, kind of everything more people notice you more alleviates their fears of, you know, oh what if they change their license? So the only regret we have with that is not doing it sooner. All right. Uh, next thing is to uh focus on the core. So we have initially tried to please many users and add many many edge use cases. We had, you know, Kubernetes support, Nomad support, console support, file support if you for whatever reason want to run it in a VM, NAT support for events. And uh while it has small benefits of having all these features, we thought it'll attract more users. It also has a lot of drawbacks. H performance gets impacted because it's hard to optimize when you have to all these abstractions that you have to fulfill. It overwhelms users. They're not sure if you're if if K gateway solved their problem because now it has not support. Is it for events? Is it for HTTP? What's going on here? And of course, it's maintenance burden for us because every such feature you know it's code tests, integration tests, command line utilities, debugging and maintenance.

So you know everything even a feature that looks small takes a a lot of effort to turn into something that you can run in production. So our new philosophy kind of focus on the 80% of the users and kind of just say no to niche features extendabilit
