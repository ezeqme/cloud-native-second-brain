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
themes: ["Observability", "Kubernetes Core"]
speakers: ["Feynman Zhou", "QingCloud"]
sched_url: https://kccnceu2022.sched.com/event/ytt3/build-a-cloud-native-logging-pipeline-on-the-edge-with-fluentbit-operator-feynman-zhou-qingcloud
youtube_search_url: https://www.youtube.com/results?search_query=Build+a+Cloud+Native+Logging+Pipeline+on+the+Edge+with+Fluentbit+Operator+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Build a Cloud Native Logging Pipeline on the Edge with Fluentbit Operator - Feynman Zhou, QingCloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Feynman Zhou, QingCloud
- Schedule: https://kccnceu2022.sched.com/event/ytt3/build-a-cloud-native-logging-pipeline-on-the-edge-with-fluentbit-operator-feynman-zhou-qingcloud
- Busca YouTube: https://www.youtube.com/results?search_query=Build+a+Cloud+Native+Logging+Pipeline+on+the+Edge+with+Fluentbit+Operator+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Build a Cloud Native Logging Pipeline on the Edge with Fluentbit Operator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytt3/build-a-cloud-native-logging-pipeline-on-the-edge-with-fluentbit-operator-feynman-zhou-qingcloud
- YouTube search: https://www.youtube.com/results?search_query=Build+a+Cloud+Native+Logging+Pipeline+on+the+Edge+with+Fluentbit+Operator+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=D_nyUhO8Y7Q
- YouTube title: Build a Cloud Native Logging Pipeline on the Edge with Fluentbit Operator - Feynman Zhou, QingCloud
- Match score: 0.944
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/build-a-cloud-native-logging-pipeline-on-the-edge-with-fluentbit-opera/D_nyUhO8Y7Q.txt
- Transcript chars: 19841
- Keywords: logs, operator, configuration, elasticsearch, fluent, fluently, output, plugins, cluster, destinations, filter, defined, config, define, allows, deploy, status, collect

### Resumo baseado na transcript

hello everyone this is feyman from beijing china it's so glad to be here it's my second time to attend kubecon eu and i was looking forward to attending this meeting in prison since we have a couple of friends and partners in spain but unfortunately due to the pandemic we can only give this speech at the front of screen so i hope everything could be recovered soon and we can meet everyone and have a cup of coffee in person so before we get started with this presentation information from different data sources password which is used to convert from unstructured data to structured data filter is used to match exclude or enrich logs with some specific metadata and output is used to define the destinations for the data for example remote services

### Excerpt da transcript

hello everyone this is feyman from beijing china it's so glad to be here it's my second time to attend kubecon eu and i was looking forward to attending this meeting in prison since we have a couple of friends and partners in spain but unfortunately due to the pandemic we can only give this speech at the front of screen so i hope everything could be recovered soon and we can meet everyone and have a cup of coffee in person so before we get started with this presentation let me briefly introduce myself so my name is feyman joe i'm from cube sphere team i'm a senior community manager and qing cloud cube sphere and i'm also cncf ambassador cdf ambassador and fluent member my skills include but not limited to kubernetes linux flambeat frontie devops and servlets and i'm really enjoying technical writing advocacy and outreach and host events alright in this talk i will demonstrate how to build a cloud native login pipeline on the edge with fluent operator so in this presentation i will walk you through the challenges of logging in kubernetes especially in the enterprise environment and next i will introduce two popular login solutions you might have ever used or heard about it the fluent bait and friendly and next i will introduce and demonstrate how fluent operator empowers fluent bit and fluently and then i will give a little bit deep dive into fluent operator and talk about this architecture and workflow and finally i will give a live demo and talk about this use case in cubesphere all right when it comes to the challenges of logging kubernetes we always receive some demands and complaints from different teams for security and compliance reasons for example our developers said that hey we have a huge amount of logs produced every day they come from different data sources and data formats our administrators said that hey you have to make sure to troubleshoot your logs in a lightweight and secure solution you also need to keep everything traceable and our security teams requested that hey could you ship the logs and data to multiple destinations and outputs to audit and visualize them oh man all of these things are in accounts right so in the real enterprise environment we actually have some logs come from different places such as parameter servers or virtual machines they can also come from embedded devices edge container port tcp or udp and all of those data are in different data formats such as json logs apache logs ngx logs or container locks and in some t
