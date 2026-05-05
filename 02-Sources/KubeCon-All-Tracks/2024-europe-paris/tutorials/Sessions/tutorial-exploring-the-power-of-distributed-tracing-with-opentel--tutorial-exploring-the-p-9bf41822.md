---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Tutorials"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Pavol Loffay", "Benedikt Bongartz", "Red Hat", "Matej Gera", "Coralogix", "Anthony Mirabella", "AWS", "Anusha Reddy Narapureddy", "Apple"]
sched_url: https://kccnceu2024.sched.com/event/1YePA/tutorial-exploring-the-power-of-distributed-tracing-with-opentelemetry-on-kubernetes-pavol-loffay-benedikt-bongartz-red-hat-matej-gera-coralogix-anthony-mirabella-aws-anusha-reddy-narapureddy-apple
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Exploring+the+Power+of+Distributed+Tracing+with+OpenTelemetry+on+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: Exploring the Power of Distributed Tracing with OpenTelemetry on Kubernetes - Pavol Loffay & Benedikt Bongartz, Red Hat; Matej Gera, Coralogix; Anthony Mirabella, AWS; Anusha Reddy Narapureddy, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Tutorials]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Pavol Loffay, Benedikt Bongartz, Red Hat, Matej Gera, Coralogix, Anthony Mirabella, AWS, Anusha Reddy Narapureddy, Apple
- Schedule: https://kccnceu2024.sched.com/event/1YePA/tutorial-exploring-the-power-of-distributed-tracing-with-opentelemetry-on-kubernetes-pavol-loffay-benedikt-bongartz-red-hat-matej-gera-coralogix-anthony-mirabella-aws-anusha-reddy-narapureddy-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Exploring+the+Power+of+Distributed+Tracing+with+OpenTelemetry+on+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: Exploring the Power of Distributed Tracing with OpenTelemetry on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePA/tutorial-exploring-the-power-of-distributed-tracing-with-opentelemetry-on-kubernetes-pavol-loffay-benedikt-bongartz-red-hat-matej-gera-coralogix-anthony-mirabella-aws-anusha-reddy-narapureddy-apple
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Exploring+the+Power+of+Distributed+Tracing+with+OpenTelemetry+on+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nwy0I6vdtEE
- YouTube title: Tutorial: Exploring the Power of Distributed Tracing with OpenTelemetry on Kubernetes
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-exploring-the-power-of-distributed-tracing-with-opentelemetry/nwy0I6vdtEE.txt
- Transcript chars: 60861
- Keywords: sampling, instrumentation, trace, collector, application, metrics, traces, information, configuration, certain, context, parent, attributes, operation, processor, tracing, section, configure

### Resumo baseado na transcript

hello everyone and welcome to the uh tutorial on open Telemetry using open Telemetry for distributed tracing uh on kubernetes um my name is pav I work at redhead I'm maintainer of the open Telemetry operator project as well contributor maintainer of jger as well um and uh maintainer of the grafana tempo operator and yeah it's been long time I'm contributing to the uh cncf observability projects and with me is U amazing crowd of people hi my name is Bena and I work with pav at redhead and 59 seconds um so the collector is uh or the instrumentation is getting the locks from the standard output of the application and it's enriching the locks with the kubernetes attributes to uh to identify you know from where they are sent it send them to the collector and collector is printing them to the standard output but you can as well configure The Collector to send the logs into your uh open search or other you know U logging systems and these are the logs uh and the metrics are sent to Prometheus so if you pull forward promeo service you will see what are the metrics sent from the from the back end to from the Java as well what we see here is the um the red metrics for Server um so we get the the know the latency the number of calls and number of errors and as well couple of jvm metrics we got this all you know by simply you know uh instrumenting with a with a simple agent um so...

### Excerpt da transcript

hello everyone and welcome to the uh tutorial on open Telemetry using open Telemetry for distributed tracing uh on kubernetes um my name is pav I work at redhead I'm maintainer of the open Telemetry operator project as well contributor maintainer of jger as well um and uh maintainer of the grafana tempo operator and yeah it's been long time I'm contributing to the uh cncf observability projects and with me is U amazing crowd of people hi my name is Bena and I work with pav at redhead and I'm also contributing to the open cic project and Jager hi I'm Anthony Marabella I work at AWS and I'm contributing to open Telemetry uh and our distribution of it oh hi I'm manusha I'm a software engineer at Apple I uh work for the observable team there and I'm an open source contributor I work mostly on metrics and JIS hey everyone I'm mat I work as a software engineer at Coral Logics and I also work in the observability uh in and among other things I work in the Prometheus ecosystem but as well in open Telemetry um okay so the whole tutorial is written on on GitHub so we will continue there if you could please scan the QR code or go to this URL um and if you will have any questions during the tutorial please raise your hand and we will help you um in your um on your laptop you don't have to follow on your laptop if you don't want to everything is uh in the repository you will be able to replicate everything at home after the conference as well so I will go to to the GitHub oops and the repository is as well pinned on my account so you can just jump there and find it as a as a first repository so what we prepared today for you is sort of I would say maybe comprehensive tutorial on how to use open Telemetry for distributed tracing um we will start with setting up the environment then we will do some theory about um you know how tracing is implemented in otel what are the concepts um and then we will do the instrumentation uh we will use the auto instrumentation to instrument Services running on kuber ities um you will you know you will see how the open Telemetry um operator is used on kubernetes then B will continue with the manual instrumentation so we will use the the API and SDK to manually instrument the application or one of the services from the application uh and then we have a bunch of uh topics that are really important in tracing as well uh we will look at sampling how we can reduce cost of um data that we want to collect um then we have metrics uh that are deri
