---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Observability"
themes: ["Observability"]
speakers: ["Colin Douch", "Cloudflare"]
sched_url: https://kccnceu2022.sched.com/event/yto1/operating-prometheus-in-a-serverless-world-colin-douch-cloudflare
youtube_search_url: https://www.youtube.com/results?search_query=Operating+Prometheus+in+a+Serverless+World+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Operating Prometheus in a Serverless World - Colin Douch, Cloudflare

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Spain / Valencia
- Speakers: Colin Douch, Cloudflare
- Schedule: https://kccnceu2022.sched.com/event/yto1/operating-prometheus-in-a-serverless-world-colin-douch-cloudflare
- Busca YouTube: https://www.youtube.com/results?search_query=Operating+Prometheus+in+a+Serverless+World+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Operating Prometheus in a Serverless World.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yto1/operating-prometheus-in-a-serverless-world-colin-douch-cloudflare
- YouTube search: https://www.youtube.com/results?search_query=Operating+Prometheus+in+a+Serverless+World+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Zln_Kvv7hxY
- YouTube title: Operating Prometheus in a Serverless World - Colin Douch, Cloudflare
- Match score: 0.865
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/operating-prometheus-in-a-serverless-world/Zln_Kvv7hxY.txt
- Transcript chars: 25168
- Keywords: gateway, metrics, serverless, prometheus, interesting, functions, aggregation, request, counters, cloudflare, wanted, gauges, standard, metric, applications, solutions, client, another

### Resumo baseado na transcript

right uh should we get started sound good uh all right i just want to start by saying how tremendously excited i am to be back speaking at in person conferences again it's great to see all of your smiling faces hopefully under masks please but today we're gonna have a bit of fun talking about the strange scary world of monitoring serverless applications is that going to let me change slide oh no technology yeah yeah it works uh for a bit of a quick introduction uh for those

### Excerpt da transcript

right uh should we get started sound good uh all right i just want to start by saying how tremendously excited i am to be back speaking at in person conferences again it's great to see all of your smiling faces hopefully under masks please but today we're gonna have a bit of fun talking about the strange scary world of monitoring serverless applications is that going to let me change slide oh no technology yeah yeah it works uh for a bit of a quick introduction uh for those of you who haven't met me yet my name is khan douche i have been doing this observability thing for arguably far too long uh i started out in like physical control systems before realizing that spoiler physics kind of sucks and the less you have to deal with that the better but i now tech lead our amazing observability platform team at cloudflare we build the tools that cloudflare engineers use to monitor and debug cloudflare and today i'm going to take you on a bit of a journey through cloudflare's evolution into the serverless space because it's kind of interesting right over the last 10 years or so we've seen this like slow transition into serverless applications and at least from an open source observability standpoint it really feels like we haven't been able to keep up i don't know whether that's the vendor lock-in that's inherent with serverless platforms or what but i'll be honest i'm getting old part of me just wants to you know shake my fist in the sky and say hey let the young folk deal with it but i mean the more i'm forced to deal with serverless functions the more i've learned to love them because you know i have been forced to use them as i'd imagine at least some of you have and they're great they solve quite a few issues that our standard servered applications have they get things like scaling for free they get things like uh sort of microservice architectures really really easily so what we really need to do is update our operational models to deal with them right and that brings me to cloudflare workers uh this isn't a sales pitch i just want to give a bit of flavor to our experience but back in 2017 or so cloudflare invented its own serverless platform you know as you do and the annoying thing happened because when you invent something the absolute worst thing that can possibly happen to you is that people start using it and as an observability team we blinked and you know in that blink we had a bit of a problem because we had this weird cambrian explosion of serverl
