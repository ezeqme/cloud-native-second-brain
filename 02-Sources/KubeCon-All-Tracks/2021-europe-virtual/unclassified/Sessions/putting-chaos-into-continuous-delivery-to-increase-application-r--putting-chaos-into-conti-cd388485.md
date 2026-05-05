---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Unclassified"
themes: ["Storage Data", "GitOps Delivery", "SRE Reliability"]
speakers: ["Juergen Etzlstorfer", "Dynatrace", "Karthik Satchitanand", "Mayadata"]
sched_url: https://kccnceu2021.sched.com/event/iEn7/putting-chaos-into-continuous-delivery-to-increase-application-resiliency-juergen-etzlstorfer-dynatrace-karthik-satchitanand-mayadata
youtube_search_url: https://www.youtube.com/results?search_query=Putting+Chaos+Into+Continuous+Delivery+to+Increase+Application+Resiliency+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Putting Chaos Into Continuous Delivery to Increase Application Resiliency - Juergen Etzlstorfer, Dynatrace & Karthik Satchitanand, Mayadata

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Unclassified]]
- Temas: [[Storage Data]], [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Juergen Etzlstorfer, Dynatrace, Karthik Satchitanand, Mayadata
- Schedule: https://kccnceu2021.sched.com/event/iEn7/putting-chaos-into-continuous-delivery-to-increase-application-resiliency-juergen-etzlstorfer-dynatrace-karthik-satchitanand-mayadata
- Busca YouTube: https://www.youtube.com/results?search_query=Putting+Chaos+Into+Continuous+Delivery+to+Increase+Application+Resiliency+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Putting Chaos Into Continuous Delivery to Increase Application Resiliency.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iEn7/putting-chaos-into-continuous-delivery-to-increase-application-resiliency-juergen-etzlstorfer-dynatrace-karthik-satchitanand-mayadata
- YouTube search: https://www.youtube.com/results?search_query=Putting+Chaos+Into+Continuous+Delivery+to+Increase+Application+Resiliency+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_DgCc4-BLW8
- YouTube title: Putting Chaos Into Continuous Delivery to Increase App... Juergen Etzlstorfer & Karthik Satchitanand
- Match score: 0.806
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/putting-chaos-into-continuous-delivery-to-increase-application-resilie/_DgCc4-BLW8.txt
- Transcript chars: 24092
- Keywords: captain, application, evaluation, litmus, actually, important, deployment, production, already, applications, everything, experiment, finished, quality, criteria, resilience, delivery, performance

### Resumo baseado na transcript

hi everyone and welcome to our presentation on putting chaos into continuous delivery to increase application resiliency my name is jorgen essendorfer i'm a maintainer of the captain project and i work for dynatrace and together i'm here with kartik hello kartik hi jurgen hi everyone so this is karthik i am the maintenance chaos project and workforce native absolutely thrilled to speak at cubecon so let's dive into the topic because we have a really exciting topic prepared for today so let's start with the typical cd process in

### Excerpt da transcript

hi everyone and welcome to our presentation on putting chaos into continuous delivery to increase application resiliency my name is jorgen essendorfer i'm a maintainer of the captain project and i work for dynatrace and together i'm here with kartik hello kartik hi jurgen hi everyone so this is karthik i am the maintenance chaos project and workforce native absolutely thrilled to speak at cubecon so let's dive into the topic because we have a really exciting topic prepared for today so let's start with the typical cd process in a multi-stage delivery pipeline you have your death your any kind of pre production environments and finally your production environment and what you already might use are some kind of quality gates that evaluate based on performance and load testing the quality of your applications and only if those tests pass you're allowed to move and move them to the next stage this is totally fine but in production there is always something happening that you can maybe not foresee or you cannot really test so there is one trend that goes into testing in production and basically uh trying to break production and then getting insights into what has to be improved but today we really want to advocate for taking this idea and moving it to pre-production environments and not adding to your performance in your load test adding also chaos tests and evaluating them not only on performance criteria but actually on obsidian's criteria and with moving and shifting left the chaos into pre-production environments to keep production let's say a safe place and keep the green lights on in your production environments that's the main idea of today's presentation and i'm handing over here to kartik to explain a little bit how we can evaluate resiliency uh and uh to take it from there thanks you again thanks for setting the context now that we've already spoken about chaos and the need for us to test it before deploying in production let's look at why keras engineering is important and what are some practices we can follow to improve the resiliency of our application infrastructure load tests are great functional tests are great but they need to be augmented with failure scenarios especially so in a cloud native world where everything is in the form of a micro service everything is loosely coupled there is so much points of failure the surface attack surface area for attacks or failures rather more and it is important for us to test what's happening when the comp
