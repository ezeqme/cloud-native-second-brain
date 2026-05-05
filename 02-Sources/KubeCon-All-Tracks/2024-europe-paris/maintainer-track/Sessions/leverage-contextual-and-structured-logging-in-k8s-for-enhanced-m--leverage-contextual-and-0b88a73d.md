---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Patrick Ohly", "Intel GmbH", "Shivanshu Raj Shrivastava", "Independent", "Mengjiao Liu", "DaoCloud"]
sched_url: https://kccnceu2024.sched.com/event/1YhhM/leverage-contextual-and-structured-logging-in-k8s-for-enhanced-monitoring-patrick-ohly-intel-gmbh-shivanshu-raj-shrivastava-independent-mengjiao-liu-daocloud
youtube_search_url: https://www.youtube.com/results?search_query=Leverage+Contextual+and+Structured+Logging+in+K8s+for+Enhanced+Monitoring+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Leverage Contextual and Structured Logging in K8s for Enhanced Monitoring - Patrick Ohly, Intel GmbH; Shivanshu Raj Shrivastava, Independent; Mengjiao Liu, DaoCloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Patrick Ohly, Intel GmbH, Shivanshu Raj Shrivastava, Independent, Mengjiao Liu, DaoCloud
- Schedule: https://kccnceu2024.sched.com/event/1YhhM/leverage-contextual-and-structured-logging-in-k8s-for-enhanced-monitoring-patrick-ohly-intel-gmbh-shivanshu-raj-shrivastava-independent-mengjiao-liu-daocloud
- Busca YouTube: https://www.youtube.com/results?search_query=Leverage+Contextual+and+Structured+Logging+in+K8s+for+Enhanced+Monitoring+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Leverage Contextual and Structured Logging in K8s for Enhanced Monitoring.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhhM/leverage-contextual-and-structured-logging-in-k8s-for-enhanced-monitoring-patrick-ohly-intel-gmbh-shivanshu-raj-shrivastava-independent-mengjiao-liu-daocloud
- YouTube search: https://www.youtube.com/results?search_query=Leverage+Contextual+and+Structured+Logging+in+K8s+for+Enhanced+Monitoring+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qdZA_TpIK68
- YouTube title: Leverage Contextual and Structured Logging in K8s for Enhanced Monitoring
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/leverage-contextual-and-structured-logging-in-k8s-for-enhanced-monitor/qdZA_TpIK68.txt
- Transcript chars: 10616
- Keywords: logging, communities, logs, contextual, structured, format, collector, context, components, logger, running, information, default, package, leverage, monitoring, change, collect

### Resumo baseado na transcript

hello everyone um welcome to uh cuties maintenance track uh we are going to we are structured doging working group and we'll be going through the things that we have done in cuties to make uh logging in kuties more contextual and structured and how uh you can leverage that to better monitor your communities clusters I'm shivanu and I'm accompanied by uh mangio and uh yep let's get started so who are we we are part of s instrumentation uh which takes care of instrumenting all the communities components log R slog is a new cented library package which is comparable to log r as the design was partly derived from it uh but it's not a full replacement uh since there is no logger in context and no log helpers in s log

### Excerpt da transcript

hello everyone um welcome to uh cuties maintenance track uh we are going to we are structured doging working group and we'll be going through the things that we have done in cuties to make uh logging in kuties more contextual and structured and how uh you can leverage that to better monitor your communities clusters I'm shivanu and I'm accompanied by uh mangio and uh yep let's get started so who are we we are part of s instrumentation uh which takes care of instrumenting all the communities components be it API server or any other communities component um s instrumentation takes care of uh instrumenting the like providing the traces Matrix and uh events logs and WG structured logging takes care of uh developing and maintaining all the lities that are needed to have a structured and contal logging in uh commun in communities so the target audience for today's talk is uh people and the public Cloud providers who are managing communities teams who are managing communities um like on on on Prem developers who are building uh OSS or uh SAS solutions for monitoring agents and they want to build something to monitor cubes and the contributors who are contributing who are contributing to cubes itself so the agenda includes uh going through some introduction around what structured and contextual logging in communities is some recent development and a demo to understand how you can uh leverage the changes and uh set up a monitoring of communities so uh to start with structured logging there are are a couple of things that we had to do to make login communities stable starting with designing the log schema um so it's it's basically a message with a key value pairs in communities that we have uh developed and the kog library that is used in communities uh depends and models on the log R so here's uh an example of the changes uh that k has on top of log R so that anybody who is writing or or contributing code to kuun can use some methods so that they can just have uh some details around that pod or any cuber object um we also have introduced uh logging format in communities so instead of just a text uh logging format with like you can configure in your communities cluster and all your communities components so that each cuetes component is logging in a Json format here's the sample Json format example for Json we use zapar and uh the other like for structured we use we still use K log uh let's take a look at how contextual logging in kubernetes is so effectively um the
