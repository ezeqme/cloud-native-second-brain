---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Performance"
themes: ["Observability", "SRE Reliability"]
speakers: ["Eduardo Silva", "Calyptia"]
sched_url: https://kccnceu2021.sched.com/event/iE4D/high-throughput-with-low-resource-usage-a-logging-journey-eduardo-silva-calyptia
youtube_search_url: https://www.youtube.com/results?search_query=High+Throughput+with+Low+Resource+Usage%3A+A+Logging+Journey+CNCF+KubeCon+2021
slides: []
status: parsed
---

# High Throughput with Low Resource Usage: A Logging Journey - Eduardo Silva, Calyptia

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Performance]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Eduardo Silva, Calyptia
- Schedule: https://kccnceu2021.sched.com/event/iE4D/high-throughput-with-low-resource-usage-a-logging-journey-eduardo-silva-calyptia
- Busca YouTube: https://www.youtube.com/results?search_query=High+Throughput+with+Low+Resource+Usage%3A+A+Logging+Journey+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre High Throughput with Low Resource Usage: A Logging Journey.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4D/high-throughput-with-low-resource-usage-a-logging-journey-eduardo-silva-calyptia
- YouTube search: https://www.youtube.com/results?search_query=High+Throughput+with+Low+Resource+Usage%3A+A+Logging+Journey+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jaTRWxrcUl8
- YouTube title: High Throughput with Low Resource Usage: A Logging Journey - Eduardo Silva, Calyptia
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/high-throughput-with-low-resource-usage-a-logging-journey/jaTRWxrcUl8.txt
- Transcript chars: 29607
- Keywords: memory, message, information, messages, actually, format, chunks, everything, records, engine, binary, performance, process, fluent, pipeline, processing, sometimes, configuration

### Resumo baseado na transcript

hello everyone my name is eduardo silva and welcome to this session called high throughput plus love resource usage and login journey as you can see my email is it's on the first slide so feel free to reach out anytime for questions or any kind of follow-up that you wanted to do as i say my name is eduardo i'm mostly on twitter and github and the main ether and as the founder of kalitia which is a company which provides full support and products on top of the

### Excerpt da transcript

hello everyone my name is eduardo silva and welcome to this session called high throughput plus love resource usage and login journey as you can see my email is it's on the first slide so feel free to reach out anytime for questions or any kind of follow-up that you wanted to do as i say my name is eduardo i'm mostly on twitter and github and the main ether and as the founder of kalitia which is a company which provides full support and products on top of the fluency and fluid bit ecosystem feel free to reach out through the website too and also the creator and maintainer of fluid project which is part of the cncf fluency project so in general everybody wants performance right if you want to see high throughput then you think about performance but everything has a little cost right so and when people say performance is sometimes think about what's my the number of records or events that i can process by a unit of time right and after that you start realizing that maybe the setup that you have or the strategy that your tool is using might not be conformant or maybe it's not following the best practices from a configuration perspective if you think about hey i want to consume low cpu or i don't want to exceed this amount of memory and that is it's really hard to come up with a with the ideal solution but i can talk about how do we solve this problem in in fluent bed and where are we going with this so our journey started a years ago we had this project called a fluentd and fluency is really good for service it's really good to aggregate information we have a huge ecosystem right where with people and companies has contributed more than a thousand of plugins and it's really great so i'm saying this because i'm maybe i would say that eighty percent of you may be familiar with fluently which is a graduated cncf project but also here we're going to explain and talk about the journey of the sub project of it which is part of the ecosystem and when talking about login um there's a couple of things that we need to clarify right logging by itself is not cheap and we need to understand that logging in the past used to be pretty simple right an application just ship a message this message message got stored in the file system or maybe it uses ziploc or syslog or any or systemd or any kind of service to handle the message for it right and most of these messages are text-based but if you think about what is the end of this message is that it allows you to perform some d
