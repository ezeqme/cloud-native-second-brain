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
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["David Jumani", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyK/project-lightning-talk-get-to-where-youre-going-with-kgateway-david-jumani-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Get+To+Where+You%27re+Going+With+Kgateway+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Get To Where You're Going With Kgateway - David Jumani, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: David Jumani, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyK/project-lightning-talk-get-to-where-youre-going-with-kgateway-david-jumani-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Get+To+Where+You%27re+Going+With+Kgateway+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Get To Where You're Going With Kgateway.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyK/project-lightning-talk-get-to-where-youre-going-with-kgateway-david-jumani-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Get+To+Where+You%27re+Going+With+Kgateway+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BjB-AIFiGqA
- YouTube title: Project Lightning Talk: Get To Where You're Going With Kgateway - David Jumani, Maintainer
- Match score: 0.916
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-get-to-where-youre-going-with-kgateway/BjB-AIFiGqA.txt
- Transcript chars: 5972
- Keywords: gateway, ingress, configurations, deployment, regular, overlays, common, ability, listener, moving, config, decided, integrations, migrate, updates, envoy, implementation, integrates

### Resumo baseado na transcript

So we're going to talk to you about the major updates that have come into K gateway, general use cases and how you can use it and how you can use it to get to get to production. So K gateway is an envoy based Kubernetes gateway API and it it implements the gateway API and not just in not just a regular implementation but it also integrates with your service mesh it can it can integrate with your hyperscalers so it provides So again, we're not just a regular gateway API implementation, but we integrate with your hyperscalers as well. So what we've additionally done is we've looked at the majority of use cases and we've identified 70 to 80% of the common the common annotations like session affinity rate limiting cost and we are contributing up to to ingress to gateway and we also

### Excerpt da transcript

Hi guys, I'm David. I'm an engineer at Solo and I'm a maintainer of the K Gateway project. So the talk today is get to where you're going with K gateway. So we're going to talk to you about the major updates that have come into K gateway, general use cases and how you can use it and how you can use it to get to get to production. All right. So first off, what is K gateway? So K gateway is an envoy based Kubernetes gateway API and it it implements the gateway API and not just in not just a regular implementation but it also integrates with your service mesh it can it can integrate with your hyperscalers so it provides hybrid connectivity as well and it looks like the start ah so you can see the start history so you can see that we're growing at a very healthy rate and within the and within last month we had over 170,000 downloads of our of our product. All right, moving on to the major updates. So, the first update we had was overlays. So, think of a scenario where in your you're trying to use an open source project and it and it exposes a lot of configurations via Helm, but there might be some niche configurations that you might be interested in like let's say your DNS config or topology constraint, but those might not be the those might not have been exposed, right?

And rather than and rather than waiting for users to raise issues and then coming up exposing those configurations which are pretty simple and and waiting for the next release what we decided to do is we decided to go with with what we call overlays. So all our first our common configurations are first class. So they can be like our images, our service type, all of that. the less the less the less common ones those are some things we decided hey you know what why don't we give the users the ability to override configs so what we did is we came up with overlays so they allow you to customize all the Kubernetes resources that are deployed via K gateway so that's your gateway deployment that's your that's your Kubernetes deployment sorry your K gateway deployment and your proxy deployment and the way it works is it works via strategic per strategic merge patch so you have your regular configurations which you can see here is our K gateway patch parameter. So that will allow you to define how your deployment sorry how your proxy is deployed but it might not expose something like your DNS config.

So what we have is we have an overlay so that will be p patched on top of your existing configuration
