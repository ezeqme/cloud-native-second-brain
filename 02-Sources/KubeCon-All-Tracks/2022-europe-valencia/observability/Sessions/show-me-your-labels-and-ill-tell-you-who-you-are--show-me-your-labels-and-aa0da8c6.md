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
speakers: ["Sandor Guba", "Cisco"]
sched_url: https://kccnceu2022.sched.com/event/ytrz/show-me-your-labels-and-ill-tell-you-who-you-are-sandor-guba-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Show+Me+Your+Labels+and+I%E2%80%99ll+Tell+You+Who+You+Are+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Show Me Your Labels and I’ll Tell You Who You Are - Sandor Guba, Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Spain / Valencia
- Speakers: Sandor Guba, Cisco
- Schedule: https://kccnceu2022.sched.com/event/ytrz/show-me-your-labels-and-ill-tell-you-who-you-are-sandor-guba-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Show+Me+Your+Labels+and+I%E2%80%99ll+Tell+You+Who+You+Are+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Show Me Your Labels and I’ll Tell You Who You Are.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytrz/show-me-your-labels-and-ill-tell-you-who-you-are-sandor-guba-cisco
- YouTube search: https://www.youtube.com/results?search_query=Show+Me+Your+Labels+and+I%E2%80%99ll+Tell+You+Who+You+Are+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TWf1ho0XMyM
- YouTube title: Show Me Your Labels and I’ll Tell You Who You Are - Sandor Guba, Cisco
- Match score: 0.922
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/show-me-your-labels-and-ill-tell-you-who-you-are/TWf1ho0XMyM.txt
- Transcript chars: 20640
- Keywords: logs, logging, cluster, actually, output, operator, access, create, labels, outputs, configuration, filter, specify, matrix, fluency, already, applied, created

### Resumo baseado na transcript

so i think it's about time to start uh hello everyone thank you for joining me today i know this is the last day of the conference and it's nearly lunch time but i will try to make this half hour well worth for you so my name is chandragupta i'm co-founder and developer at bonsai cloud acquired by cisco i'm working for more than five years with kubernetes and the fluent ecosystem i'm a huge observability fund and the title is show me your label i will tell you

### Excerpt da transcript

so i think it's about time to start uh hello everyone thank you for joining me today i know this is the last day of the conference and it's nearly lunch time but i will try to make this half hour well worth for you so my name is chandragupta i'm co-founder and developer at bonsai cloud acquired by cisco i'm working for more than five years with kubernetes and the fluent ecosystem i'm a huge observability fund and the title is show me your label i will tell you who you are which may sound the catchphrase but actually i will show you how to exploit labels for your logging subsystem let's start with the basics kubernetes logging is not that difficult the content around time puts the container's std out into the host file system and the kubelet service access to these logs and provide it to the users through the kubernetes api it's that simple it's nothing much you can configure about what's the problem with this uh the problem is uh that these logs are only stored on the host file system and eventually they will get rotated or fill the node file system and the other part is that cube city logs is not always the best way to consume your logs so what you can do you want to collect these logs and transport to your log analyzation system but there are other problems with this as well you need privileged access to access the host file system and there is no separation of logs on the host file system so all kind of pods logs in different name spaces are just stored on the same folder but let's see how this uh system would look like on kubernetes and uh you need the collector to collect the log files uh from the systems and push them out to an output eventually you will need an aggregator that will collect the locks from these agents and push it them to forward to another log analyzation system or whatever destination you want and basically this was the reason behind logging operator that it was born because if you are doing such kind of system you will end up creating tons of configuration files with hundreds of lines of configuration code and the logging operator for this architecture under the whose use is fluent bit as the daemon set we collect all the logs uh from the node level and we transport it to a fluid and the stateful set the heart of the logging operator is a labor router plugin developed at bonsai cloud which helps you to distinguish logs based on kubernetes metadata so you can create different log flows and if you identify the low flow it's really ea
