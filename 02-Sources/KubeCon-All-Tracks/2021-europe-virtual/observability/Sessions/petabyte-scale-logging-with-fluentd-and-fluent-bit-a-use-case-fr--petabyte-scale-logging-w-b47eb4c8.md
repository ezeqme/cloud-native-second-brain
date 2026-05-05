---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Hanzel Jesheen", "Intuit", "Anurag Gupta", "Calyptia"]
sched_url: https://kccnceu2021.sched.com/event/iE1k/petabyte-scale-logging-with-fluentd-and-fluent-bit-a-use-case-from-intuit-hanzel-jesheen-intuit-anurag-gupta-calyptia
youtube_search_url: https://www.youtube.com/results?search_query=Petabyte+Scale+Logging+with+Fluentd+and+Fluent+Bit%3A+A+Use+Case+From+Intuit+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Petabyte Scale Logging with Fluentd and Fluent Bit: A Use Case From Intuit - Hanzel Jesheen, Intuit & Anurag Gupta, Calyptia

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Hanzel Jesheen, Intuit, Anurag Gupta, Calyptia
- Schedule: https://kccnceu2021.sched.com/event/iE1k/petabyte-scale-logging-with-fluentd-and-fluent-bit-a-use-case-from-intuit-hanzel-jesheen-intuit-anurag-gupta-calyptia
- Busca YouTube: https://www.youtube.com/results?search_query=Petabyte+Scale+Logging+with+Fluentd+and+Fluent+Bit%3A+A+Use+Case+From+Intuit+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Petabyte Scale Logging with Fluentd and Fluent Bit: A Use Case From Intuit.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE1k/petabyte-scale-logging-with-fluentd-and-fluent-bit-a-use-case-from-intuit-hanzel-jesheen-intuit-anurag-gupta-calyptia
- YouTube search: https://www.youtube.com/results?search_query=Petabyte+Scale+Logging+with+Fluentd+and+Fluent+Bit%3A+A+Use+Case+From+Intuit+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OuKm2SiwnGM
- YouTube title: Petabyte Scale Logging with Fluentd and Fluent Bit: A Use Case From... Hanzel Jesheen & Anurag Gupta
- Match score: 0.906
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/petabyte-scale-logging-with-fluentd-and-fluent-bit-a-use-case-from-int/OuKm2SiwnGM.txt
- Transcript chars: 20614
- Keywords: pipeline, events, metadata, logs, cluster, logging, second, container, fluent, object, latency, within, cost, deployment, running, transport, transfer, fluency

### Resumo baseado na transcript

hi everyone welcome to petabyte scale logging with fluency influent bit a use case from intuit my name is onorock i'm part of the company calyptia and i help run product there so who are we so today it's going to be myself and hansel who's joining me from intuit who's on the cloud observability team there as a senior software engineer and for myself i'm part of the oss group that is a maintainer for the fluent bit project and i help drive product for both flipped and flinty

### Excerpt da transcript

hi everyone welcome to petabyte scale logging with fluency influent bit a use case from intuit my name is onorock i'm part of the company calyptia and i help run product there so who are we so today it's going to be myself and hansel who's joining me from intuit who's on the cloud observability team there as a senior software engineer and for myself i'm part of the oss group that is a maintainer for the fluent bit project and i help drive product for both flipped and flinty so for those who are unfamiliar with what is fluenty and what what is fluent bit they are cloud native computing foundation projects they are part of the graduated projects alongside kubernetes prometheus and others they started 10 years ago and the primary problem they solve is how do you take data from point a and send it to point b and if we look at this problem over the last 10 years where you see that data sources continually evolve we have more things like mobile applications system logs kubernetes microservices containers app metrics and we have additional destinations that just keep compounding you might have things like uh amazon s3 you might have splunk elasticsearch loki azure gcp kafka and those destinations just continue to evolve and expand you might need to send data to multiple you might need to send data to all of them you might need to send data to a single one but in any case fluent d and fluent bid are really vendor neutral solutions to saying let's collect data once and send it to as many destinations as you require now when we look at challenges for logging at scale we have to look at this and perspective of a broad overview one is high scale can really equal very high costs you can have things like reliability and buffering uh how do you make sure that logs get sent where they're supposed to and you don't want to open up a request every single time that you have a new message think about that when you're sending 10 000 to 100 000 messages per second networking always an issue here with things like ephemeral workloads and kubernetes or you're in the cloud you might have air gapped environments how do you make sure networking doesn't hurt you when you're doing logging at scale event throughput you might need to maximize how many messages per second you're sending you might have latency requirements you might have to get messages so that they your developers your operations folks can go and start to debug and diagnose all that information security so again in a large
