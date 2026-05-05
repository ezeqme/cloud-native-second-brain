---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Derek Cavanaugh", "Sara Moore", "Recursion Pharma"]
sched_url: https://kccnceu2023.sched.com/event/1Hyd4/hazardous-defaults-managing-cardinality-and-performance-for-your-logging-stack-derek-cavanaugh-sara-moore-recursion-pharma
youtube_search_url: https://www.youtube.com/results?search_query=Hazardous+Defaults%3A+Managing+Cardinality+and+Performance+for+Your+Logging+Stack+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Hazardous Defaults: Managing Cardinality and Performance for Your Logging Stack - Derek Cavanaugh & Sara Moore, Recursion Pharma

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Derek Cavanaugh, Sara Moore, Recursion Pharma
- Schedule: https://kccnceu2023.sched.com/event/1Hyd4/hazardous-defaults-managing-cardinality-and-performance-for-your-logging-stack-derek-cavanaugh-sara-moore-recursion-pharma
- Busca YouTube: https://www.youtube.com/results?search_query=Hazardous+Defaults%3A+Managing+Cardinality+and+Performance+for+Your+Logging+Stack+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Hazardous Defaults: Managing Cardinality and Performance for Your Logging Stack.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyd4/hazardous-defaults-managing-cardinality-and-performance-for-your-logging-stack-derek-cavanaugh-sara-moore-recursion-pharma
- YouTube search: https://www.youtube.com/results?search_query=Hazardous+Defaults%3A+Managing+Cardinality+and+Performance+for+Your+Logging+Stack+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=A1YgG0yz68Q
- YouTube title: Hazardous Defaults: Managing Cardinality and Performance for Your Lo... Derek Cavanaugh & Sara Moore
- Match score: 0.906
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/hazardous-defaults-managing-cardinality-and-performance-for-your-loggi/A1YgG0yz68Q.txt
- Transcript chars: 24836
- Keywords: logs, labels, active, streams, cardinality, chunks, number, promptel, configuration, grafana, indexes, looking, stream, performance, little, cluster, queries, metrics

### Resumo baseado na transcript

uh we're gonna go ahead and get started so I'm Sarah Moore and I'm Derek Kavanaugh uh this is our first talk at kubecon so we're super excited to be here and today we are going to take you with us on a journey about default configuration in your log in stack and how shipping the defaults could cause unforeseen challenges so let's start with a little story the date was November 9th we received a message from a fellow engineer saying um I can't seem to find my logs like 40 times faster and 97 percent less data being fetched so to close out the case of the missing logs we reduce the cardinality of our log labels and in turn Loki was able to ingest logs again this not only closed the case of the missing logs but as you could see by the previous numbers it increased our performance and efficiency as well so here are some of our key takeaways first off every cluster is unique what worked for us might not necessarily work for you

### Excerpt da transcript

uh we're gonna go ahead and get started so I'm Sarah Moore and I'm Derek Kavanaugh uh this is our first talk at kubecon so we're super excited to be here and today we are going to take you with us on a journey about default configuration in your log in stack and how shipping the defaults could cause unforeseen challenges so let's start with a little story the date was November 9th we received a message from a fellow engineer saying um I can't seem to find my logs in grafana huh that's not good so we start poking around a little bit and we confirmed the problem the logs have gone missing today we're going to walk you through the case of the missing logs and how we solved it before we get too far into the details of solving this problem let's go through an overview of the plg stack so the plg stat consists of three main components promtel for shipping logs Loki for aggregating and storing logs and grafana for interfacing with logs promtel runs as a Daemon set in any cluster you pull logs from by default promptel will pull pod logs that are logging to standard out or standard error and ship them to Loki Loki is the log aggregation component Loki exposes an API for prompt till the push logs to it will ship both the raw logs and an index to a storage back end and that's typically a storage bucket we'll talk more about indexes in a little bit grafana is the UI interfacing with Loki so we can create a Loki data store our data source in grafana in order to run queries against the logs this gives us the ability to interact with the logs in a number of ways from simple Auto queries to complex dashboards with integrated alerting all right so back to the case of the missing logs so at this point what we've done is confirm the problem the logs are indeed missing so what's next well Derek you're a good SRE what would you do in this situation well Sarah I would probably query Loki to look at the logs for Loki yeah did we mention we work at a company called recursion so looking at the Pod logs for Loki we see a few errors that look like this maximum active stream limit exceeded reduce the number of active streams or contact your Loki administrator to see if the limit can be increased hey Derek do you know who the Loki administrators are I thought that was you wait I thought that was you I guess it's us so as talented Loki administrators we decide to start by Rolling the Loki pods I mean let's just see if these errors resolve themselves you can guess how that went when we
