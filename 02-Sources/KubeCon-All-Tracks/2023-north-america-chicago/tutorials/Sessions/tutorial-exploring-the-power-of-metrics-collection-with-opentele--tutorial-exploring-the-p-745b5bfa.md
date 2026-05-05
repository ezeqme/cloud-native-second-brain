---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Tutorials"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Pavol Loffay", "Benedikt Bongartz", "Red Hat", "Anthony Mirabella", "AWS", "Matej Gera", "Coralogix", "Anusha Reddy Narapureddy", "Apple"]
sched_url: https://kccncna2023.sched.com/event/1R2pr/tutorial-exploring-the-power-of-metrics-collection-with-opentelemetry-on-kubernetes-pavol-loffay-benedikt-bongartz-red-hat-anthony-mirabella-aws-matej-gera-coralogix-anusha-reddy-narapureddy-apple
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Exploring+the+Power+of+Metrics+Collection+with+OpenTelemetry+on+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: Exploring the Power of Metrics Collection with OpenTelemetry on Kubernetes - Pavol Loffay & Benedikt Bongartz, Red Hat; Anthony Mirabella, AWS; Matej Gera, Coralogix; Anusha Reddy Narapureddy, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Pavol Loffay, Benedikt Bongartz, Red Hat, Anthony Mirabella, AWS, Matej Gera, Coralogix, Anusha Reddy Narapureddy, Apple
- Schedule: https://kccncna2023.sched.com/event/1R2pr/tutorial-exploring-the-power-of-metrics-collection-with-opentelemetry-on-kubernetes-pavol-loffay-benedikt-bongartz-red-hat-anthony-mirabella-aws-matej-gera-coralogix-anusha-reddy-narapureddy-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Exploring+the+Power+of+Metrics+Collection+with+OpenTelemetry+on+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: Exploring the Power of Metrics Collection with OpenTelemetry on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pr/tutorial-exploring-the-power-of-metrics-collection-with-opentelemetry-on-kubernetes-pavol-loffay-benedikt-bongartz-red-hat-anthony-mirabella-aws-matej-gera-coralogix-anusha-reddy-narapureddy-apple
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Exploring+the+Power+of+Metrics+Collection+with+OpenTelemetry+on+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hsI7mCJ0JSE
- YouTube title: Tutorial: Exploring the Power of Metrics Collection with OpenTelemetry on Kubernetes...
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-exploring-the-power-of-metrics-collection-with-opentelemetry/hsI7mCJ0JSE.txt
- Transcript chars: 59757
- Keywords: collector, metrics, prometheus, target, exporter, scrape, instrumentation, application, allocator, metric, section, receiver, operator, configuration, instrument, running, console, targets

### Resumo baseado na transcript

so hello everyone if you will if you would like to follow us with the on the tutorial and do the coding with us please you can start um um getting ready uh if you go to my GitHub account there is the cubec con EU 2023 open tetri kues tutorial or you can just scan this QR code uh there is read me with with the setup and so I would advise you to to start looking at this and maybe create a kubernetes cluster and deploy the observability your environment dynamically as we will see on kubernetes so I'm running here uh a container which is has Java installed because the machine doesn't um so it may be an option for you and what we see next is more or less like we

### Excerpt da transcript

so hello everyone if you will if you would like to follow us with the on the tutorial and do the coding with us please you can start um um getting ready uh if you go to my GitHub account there is the cubec con EU 2023 open tetri kues tutorial or you can just scan this QR code uh there is read me with with the setup and so I would advise you to to start looking at this and maybe create a kubernetes cluster and deploy the observability backend that we'll be using the QR code is as well on the slides that are uploaded to shut okay so hello everyone and welcome to the tutorial for exploring uh open Telemetry metrics on kubernetes and this is essentially continuation from the last cubec Con in Amsterdam where we did a tutorial for kind of exploring all the open Telemetry signals on U how to collect them on kubernetes and today we're going to just focus on the metrics um so my name is uh Pell I'm principal engineer at redhead I uh maintain open Telemetry operator and as well contribute the to the open open Telemetry project um as well maintainer of the Jager project and um grafana Tempo operator uh and with me today is amazing group of people uh would you like to start the introductions I can do yeah hi my name is bin I work uh I contribute to the open tary project and I also work at rard together with Pavo and hi I'm Anthony Mirella uh I'm a senior engineer at AWS and I work on open slet tree um mostly The Collector and the go uh client Library Aries uh hey hi I'm Anusha I'm a software engineer at Apple I'm I'm also an open source uh contributor I work on open elimary metrics and traces hello everyone my name is matate I work as a software engineer at cor Logics and I'm also open source contributor uh I'm coming mostly from the promes ecosystem recently I've been working more with open Telemetry with the collector and operator so that's my area of focus okay thank you very much so as you can see we are all kind of you know contributing to the ecosystem uh and it's it's a tutorial and all the content is hosted on GitHub uh so if you would like to follow what we do live on stage please scan this QR code or go to uh this URL or to my GitHub account and the repository is pinned um on the on the index page if you will have any issues during the tutorial you can just raise your hand and we will come and help you to to resolve issues if you will know obviously uh and with that I will jump to the to GitHub and so what we prepared today is is essentially you know couple
