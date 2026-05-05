---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Application + Development + Delivery"
themes: ["GitOps Delivery"]
speakers: ["Anusha Ragunathan", "Kevin Downey", "Intuit Inc"]
sched_url: https://kccncna2022.sched.com/event/182Gi/paradox-of-choice-how-to-pick-an-application-definition-that-works-for-you-anusha-ragunathan-kevin-downey-intuit-inc
youtube_search_url: https://www.youtube.com/results?search_query=Paradox+Of+Choice%3A+How+To+Pick+an+Application+Definition+That+Works+For+You%21+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Paradox Of Choice: How To Pick an Application Definition That Works For You! - Anusha Ragunathan & Kevin Downey, Intuit Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Application + Development + Delivery]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Anusha Ragunathan, Kevin Downey, Intuit Inc
- Schedule: https://kccncna2022.sched.com/event/182Gi/paradox-of-choice-how-to-pick-an-application-definition-that-works-for-you-anusha-ragunathan-kevin-downey-intuit-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Paradox+Of+Choice%3A+How+To+Pick+an+Application+Definition+That+Works+For+You%21+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Paradox Of Choice: How To Pick an Application Definition That Works For You!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Gi/paradox-of-choice-how-to-pick-an-application-definition-that-works-for-you-anusha-ragunathan-kevin-downey-intuit-inc
- YouTube search: https://www.youtube.com/results?search_query=Paradox+Of+Choice%3A+How+To+Pick+an+Application+Definition+That+Works+For+You%21+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2LuIGIr5nXE
- YouTube title: Paradox Of Choice: How To Pick an Application Definition That Wo... Anusha Ragunathan & Kevin Downey
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/paradox-of-choice-how-to-pick-an-application-definition-that-works-for/2LuIGIr5nXE.txt
- Transcript chars: 23218
- Keywords: application, actually, developer, developers, deployment, control, pipeline, customized, argo, platform, solution, infrastructure, specification, resources, definition, wanted, choice, solutions

### Resumo baseado na transcript

Welcome to our talk um today we're going to be talking about a paradox of choice how to pick an application definition that works for you my name is Anisha ragunathan and with me is Kevin Downey and we're software Engineers working at into it today we'll be talking about some of the background of why we're even doing this talk and introduce you to the problems that we faced in our platform infrastructure team supporting the millions of uh customers as well as our thousands of developers that build our existing tool chain so krm plugins are an efficient way to do this in fact we're stay tuned we're going to write a block post about more details on the krm plugin that we implemented and what we demoed today um if you have

### Excerpt da transcript

Welcome to our talk um today we're going to be talking about a paradox of choice how to pick an application definition that works for you my name is Anisha ragunathan and with me is Kevin Downey and we're software Engineers working at into it today we'll be talking about some of the background of why we're even doing this talk and introduce you to the problems that we faced in our platform infrastructure team supporting the millions of uh customers as well as our thousands of developers that build application PL on top of our platform and the meat of the problem the Paradox of choice we will be talking about that and the solutions we came up with when we were faced with this problem we'll finish up with results and takeaways into it and our infrastructure at a glance into it is a Global Financial tech company that provides a vast array of financial products and services built on an AI driven export platform if youve used any of these products Turbo Tax QuickBooks Mint Credit Karma mail Shimp know that they've been running on our kubernetes powered infrastructure we support about 900 plus developer teams consisting of 6,000 application developers and they deliver more than 2,000 Services powered on 2 245 kubernetes cluster running on 16,000 plus name spaces not that these are just average numbers when we have our tax Peak Seasons these numbers go really high and one of the core tenets of our platform infrastructure team is to accelerate the developer velocity of our end developers and we try to reduce friction where and when possible let's take a look at a average developers cicd pipeline an application developer commits code which Trigg build which triggers test typically unit and integration tests and then gets deployed to a particular environment whether it's qal performance staging or praud and eventually gets monitored using an array of monitoring tools about the health of the application now note that the application developer also has to work with a deployment repo for their deployment needs what are the configurations for my applications running on various different environments that's when they are bearing both the dev and the Ops hat let's take a closer look at our deployment pipeline the application developer uses customized based overlay and base configs and overlay configs for their deployment repos this gets picked up by Argo CD which is our primary tool for deploying any of the deployment manifests into our end kubernetes production clusters
